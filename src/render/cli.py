"""Orquestrador do pipeline de vídeo curto."""

import argparse
from pathlib import Path

import yaml


def run_pipeline(topic: str, output_dir: Path, config: dict) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    script_path = output_dir / "script.txt"
    script_path.write_text(f"# Roteiro: {topic}\n\nHook...\nCorpo...\nCTA...", encoding="utf-8")
    # TODO: TTS, b-roll, whisper, ffmpeg
    final = output_dir / "final.mp4"
    final.write_bytes(b"")  # placeholder
    return final


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    parser.add_argument("--output", type=Path, default=Path("output"))
    parser.add_argument("--config", type=Path, default=Path("config/pipeline.yaml"))
    args = parser.parse_args()
    cfg = {}
    if args.config.exists():
        cfg = yaml.safe_load(args.config.read_text()) or {}
    out = run_pipeline(args.topic, args.output, cfg)
    print(f"Pipeline concluído: {out}")


if __name__ == "__main__":
    main()
