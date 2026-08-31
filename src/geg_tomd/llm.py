import os

from dotenv import load_dotenv
from google import genai
from google.genai import errors
from tenacity import (
    retry,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential,
)

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


class GeminiService:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model = "gemini-3.1-flash-lite"

    # retryable errors
    @staticmethod
    def is_retryable(exception: Exception) -> bool:
        return isinstance(exception, errors.ServerError)

    # tenta gerar conteúdo até 5 vezes com espera exponencial entre as tentativas
    @retry(
        retry=retry_if_exception(is_retryable),
        stop=stop_after_attempt(5),
        wait=wait_exponential(
            multiplier=1,
            min=2,
            max=30,
        ),
    )
    def generate_content(self, prompt: str, contents: list) -> str:
        response = self.client.models.generate_content(
            model=self.model, contents=[prompt] + contents
        )
        return response.text

    # extrai texto de pdf
    def extract_pdf_text(self, file_path: str) -> str:
        pdf = self.client.files.upload(file=file_path)
        prompt = """
            Converta o PDF fornecido para Markdown.

            Transcreva e estruture o documento com fidelidade. Preserve todo o conteúdo relevante e não resuma, omita, parafraseie ou adicione informações.

            Requisitos:
            - Preserve a ordem original do conteúdo.
            - Use níveis apropriados de títulos Markdown para representar a hierarquia do documento.
            - Preserve parágrafos, listas, listas numeradas, tabelas e outras estruturas relevantes.
            - Preserve códigos, fórmulas e notações matemáticas sempre que possível.
            - Mantenha legendas associadas às respectivas imagens ou tabelas.
            - Preserve links quando estiverem presentes e forem identificáveis.
            - Se uma imagem contiver texto relevante, transcreva esse texto.
            - Não descreva imagens, a menos que a descrição seja necessária para representar conteúdo relevante do documento.
            - Não corrija, interprete ou "melhore" o conteúdo original.
            - Se alguma parte do documento estiver ilegível ou não puder ser extraída com segurança, indique `[ilegível]` em vez de tentar adivinhar.
            - Não inclua comentários sobre o processo de conversão.

            Retorne somente o Markdown resultante.
            """

        try:
            return self.generate_content(prompt=prompt, contents=[pdf])
        finally:
            self.client.files.delete(name=pdf.name)

    # resume textos
    def summarize(self, text: str) -> str:
        prompt = """
                Resuma o conteúdo Markdown fornecido.

                Crie um resumo claro, organizado e fiel ao conteúdo original, destacando as informações, conceitos e ideias mais importantes.

                Requisitos:
                - Preserve os conceitos essenciais e informações relevantes.
                - Remova repetições, exemplos excessivamente detalhados e informações secundárias quando possível.
                - Mantenha a hierarquia e a organização do conteúdo usando Markdown.
                - Use títulos, subtítulos, listas e outros elementos Markdown quando ajudarem na organização.
                - Preserve fórmulas, definições, termos técnicos e informações importantes.
                - Não invente, altere ou complemente informações que não estejam no conteúdo original.
                - Não faça comentários sobre o processo de resumo

                Retorne somente o Markdown resultante.
            """

        return self.generate_content(prompt=prompt, contents=[text])

    def complete(self, text: str) -> str:
        prompt = """"
            Você receberá um texto extraído de um PDF.

            Identifique lacunas que prejudiquem sua compreensão, como trechos cortados, referências sem contexto ou conceitos essenciais sem explicação.

            Preste atenção especial a referências como **"ver no livro"**, **"ver no texto"**, **"ver no material de apoio"**, **"ver capítulo"**, **"ver seção"**, **"veja a figura"** ou referências semelhantes. Caso o conteúdo referenciado não esteja presente no texto, tente complementar a informação quando possível.

            Complete apenas o que for possível com segurança e não invente informações.

            Retorne o texto original em Markdown, adicionando **Complemento:** para informações externas necessárias e **Informação ausente:** quando não puder completar.

            Não resuma nem reescreva o conteúdo desnecessariamente. Se não houver alterações a serem feitas, não faça.
        """

        return self.generate_content(prompt=prompt, contents=[text])
