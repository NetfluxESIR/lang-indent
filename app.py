from pathlib import Path

import typer


app = typer.Typer()


@app.command()
def run(
    input_file: Path = typer.Option(
        ...,
        "-i",
        "--input",
        exists=True,
        file_okay=True,
        dir_okay=False,
        writable=False,
        readable=True,
        resolve_path=True,
        allow_dash=False,
        help="Input file path",
    ),
    output_file: Path = typer.Option(
        ...,
        "-o",
        "--output",
        exists=False,
        file_okay=True,
        dir_okay=False,
        writable=True,
        readable=False,
        resolve_path=True,
        allow_dash=False,
        help="Output file path",
    ),
):
    typer.echo(f"Running with input {input_file} and output {output_file}")


if __name__ == "__main__":
    app()
