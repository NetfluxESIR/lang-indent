import sys
from pathlib import Path
from enum import Enum
from moviepy.editor import VideoFileClip

import typer
import whisper
from whisper.utils import WriteVTT

app = typer.Typer()


class TaskType(str, Enum):
    language_detection = "language_detection"
    subtitle_generation = "subtitle_generation"


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
        task_type: str = typer.Option(
            TaskType.language_detection,
            "-t",
            "--task-type",
            help="Task type to run",
            case_sensitive=False,
            show_default=True,
        ),
        output_dir: Path = typer.Option(
            Path.cwd(),
            "-o",
            "--output-dir",
            exists=True,
            file_okay=False,
            dir_okay=True,
            writable=True,
            readable=True,
            resolve_path=True,
            allow_dash=False,
            help="Output directory path",
        )
) -> None:
    model = whisper.load_model("medium")
    mp3_path = convert_to_mp3(input_file)
    if task_type == TaskType.language_detection:
        language_detection(mp3_path, model)
        return None
    if task_type == TaskType.subtitle_generation:
        subtitle_generation(mp3_path, model, output_dir)
        return None
    else:
        raise typer.BadParameter(f"Task type {task_type} not supported")


def convert_to_mp3(input_file: Path) -> Path:
    try:
        video = VideoFileClip(str(input_file.absolute()))
    except Exception as e:
        raise typer.BadParameter(f"Could not load {input_file} as a video file: {e}")
    mp3_path = input_file.parent / f"{input_file.stem}.mp3"
    try:
        video.audio.write_audiofile(str(mp3_path.absolute()), verbose=False, logger=None)
    except Exception as e:
        raise typer.BadParameter(f"Could not convert {input_file} to mp3: {e}")
    return mp3_path


def language_detection(input_file: Path, model: whisper.Whisper) -> None:
    audio = whisper.load_audio(str(input_file.absolute()))
    audio = whisper.pad_or_trim(audio)
    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(max(probs, key=probs.get))


def subtitle_generation(input_file: Path, model: whisper.Whisper, output_dir: Path) -> None:
    result = model.transcribe(str(input_file.absolute()))
    WriteVTT(output_dir=str(output_dir.absolute())).write_result(result, sys.stdout)


if __name__ == "__main__":
    app()
