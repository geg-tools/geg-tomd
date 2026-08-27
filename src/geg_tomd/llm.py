from dotenv import load_dotenv
import os

from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class GeminiService:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.chat = self.client.chats.create(
            model="gemini-3.5-flash-lite"
        )

    # extrai texto de pdf
    def extract_pdf_text(self, file_path: str) -> str:
        pdf = self.client.files.upload(file=file_path)

        prompt = f""""
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

        response = self.chat.send_message([
            pdf, 
            prompt,
        ])
        
        return response.text

    # resume textos
    def summarize(self, text: str) -> str:
        prompt = f""""
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

                {text}
            """

        response = self.chat.send_message(prompt)
        
        return response.text
