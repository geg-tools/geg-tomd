from pathlib import Path

import pymupdf4llm
from geg_core.files import detect_file_extension

from geg_tomd.llm import GeminiService


def convert(
    file_path: Path,
    summarize: bool,
    use_ai: bool,
    complete: bool,
    gemini_service: GeminiService | None,
) -> str:
    file_extension = detect_file_extension(file_path)

    # PDF
    if file_extension in (".pdf"):
        if use_ai:
            md_text = gemini_service.extract_pdf_text(file_path=str(file_path))
        else:
            md_text = pymupdf4llm.to_markdown(str(file_path))
    # TEXT FILES
    elif file_extension in (".txt", ".md"):
        md_text = file_path.read_text(encoding="utf-8")
    else:
        print("erro, extensão de arquivo não suportada")
        return

    print("texto gerado...")

    # COMPLETE
    if complete:
        md_text = gemini_service.complete(text=md_text)
        print("texto preenchido...")

    # RESUME
    if summarize:
        md_text = gemini_service.summarize(text=md_text)
        print("texto resumido...")

    print(f"Resultado escrito em {file_path}")

    return md_text
