# Pipeline de dados

## Estágios

1. **script** — prompt estruturado: hook, 3 blocos, CTA.
2. **tts** — gera `narration.wav`.
3. **media** — busca N clipes por keywords do roteiro.
4. **subtitles** — Whisper → word timestamps → ASS com karaoke.
5. **render** — concatena clipes, overlay texto, mix áudio.

## Configuração FFmpeg

Resolução: 1080×1920, 30 fps, H.264, AAC 192k.

Filter complex exemplo: scale+crop central, drawtext para legendas.
