from pathlib import Path

from geg_tomd.converter import convert
from geg_tomd.llm import GeminiService


def convert_to_md(
    file_path_str: str,
    output_path_str: str,
    summarize: bool,
    use_ai: bool,
    complete: bool,
) -> None:
    file_path = Path(file_path_str)

    if output_path_str == None:
        output_path = file_path.with_suffix(".md")
    else:
        output_path = Path(
            output_path_str
        )  # depois proteger contra saida != de markdown

    # se for arquivo
    if file_path.is_file():
        process_file(file_path, output_path, summarize, use_ai, complete)
        return

    # depois criar dataclass pra passar parametros
    if file_path.is_dir():
        if not (output_path.is_dir()):
            print("erro, deve ser dir")
            return
        process_dir(file_path, file_path, output_path, summarize, use_ai, complete)

    return


# processa um arquivo, converte e escreve no output
def process_file(
    file_path: Path, output_path: Path, summarize: bool, use_ai: bool, complete: bool
) -> None:
    # converte o arquivo
    gemini_service = None
    if use_ai or summarize:
        gemini_service = GeminiService()

    md_text = convert(
        file_path=file_path,
        summarize=summarize,
        use_ai=use_ai,
        complete=complete,
        gemini_service=gemini_service,
    )

    # escreve
    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    Path(output_path).write_text(md_text, encoding="utf-8")


# processa um diretorio, recursivamente, convertendo todos os arquivos e escrevendo no output
def process_dir(
    input_root: Path,
    file_path: Path,
    output_path: Path,
    summarize: bool,
    use_ai: bool,
    complete: bool,
) -> None:
    for file in file_path.rglob("*"):
        if file.is_dir():
            process_dir(input_root, file, output_path, summarize, use_ai, complete)
        else:
            relative = file.relative_to(input_root)
            process_file(
                file,
                output_path / relative.with_suffix(".md"),
                summarize,
                use_ai,
                complete,
            )
