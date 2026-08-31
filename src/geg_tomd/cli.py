import typer

from geg_tomd.processor import convert_to_md

app = typer.Typer()


@app.command()
def main(
    file_path_str: str,
    output_path_str: str = typer.Option(None, "--output", "-o"),
    summarize: bool = typer.Option(False, "--summarize", "-s"),
    complete: bool = typer.Option(False, "--complete", "-c"),
    use_ai: bool = typer.Option(False, "--ai", "-a"),
):

    convert_to_md(file_path_str, output_path_str, summarize, use_ai, complete)
