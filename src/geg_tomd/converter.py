from pathlib import Path

from geg_core.files import detect_file_extension
from geg_tomd.llm import GeminiService

def convert(file_path: Path, summarize: bool, use_ai: bool, gemini_service: GeminiService | None) -> str:
    file_extension = detect_file_extension(file_path)

    # deixar gemini service generico e passar prompt e arquivo como parametro
    if file_extension in (".pdf"):
        if use_ai:
            md_text = gemini_service.extract_pdf_text(file_path=str(file_path))
        else:
            md_text = "sem ia"
    elif file_extension in (".txt", ".md"):
        md_text = file_path.read_text(encoding="utf-8")
    else:
        print("erro, extensão de arquivo não suportada")
        return

    print("texto gerado...")

    # resume o texto gerado
    if summarize:
        md_text = gemini_service.summarize(text=md_text)
        print("texto resumido...")

    return md_text