import typer
from pathlib import Path

from geg_tomd.converter import convert
from geg_tomd.llm import GeminiService

app = typer.Typer()


@app.command()
def main(
    file_path_str: str,
    output_path_str: str = typer.Option(None, "--output", "-o"),
    summarize: bool = typer.Option(False, "--summarize", "-s"),
    use_ai: bool = typer.Option(False, "--ai")
):
    file_path = Path(file_path_str)

    if output_path_str == None:
        output_path = file_path.with_suffix(".md")
    else:
        output_path = Path(output_path_str) # depois proteger contra saida != de markdown

    # se for arquivo
    if file_path.is_file():
         process_file(file_path, output_path, summarize, use_ai)
         return

    # depois criar dataclass pra passar parametros
    if file_path.is_dir():
        if not (output_path.is_dir()):
            print("erro, deve ser dir")
            return
        process_dir(file_path, file_path, output_path, summarize, use_ai)


def process_file(file_path: Path, output_path: Path, summarize: bool, use_ai: bool) -> None:
    # converte o arquivo
    if use_ai or summarize:
        gemini_service = GeminiService()

    md_text = convert(file_path=file_path, summarize=summarize, use_ai=use_ai, gemini_service=gemini_service)

    # escreve
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    Path(output_path).write_text(md_text, encoding="utf-8")

    return


def process_dir(input_root: Path, file_path: Path, output_path: Path, summarize: bool, use_ai: bool) -> None:
    for file in file_path.rglob("*"):
        if file.is_dir():
            process_dir(input_root, file, output_path, summarize, use_ai)
        else:
            relative = file.relative_to(input_root)
            process_file(file, output_path / relative.with_suffix(".md"), summarize, use_ai)

# fazer ele adicionar no deck da pasta

app()
