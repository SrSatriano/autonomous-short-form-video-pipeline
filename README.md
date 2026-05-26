# Autonomous Short-Form Video Pipeline

Pipeline completo: tema → roteiro (LLM) → TTS → b-rolls → legendas dinâmicas → render 9:16 (TikTok/Shorts).

## Stack

- Python, FFmpeg, Whisper
- APIs de imagem (configuráveis)

## Fluxograma do pipeline

```
 Tema ──► LLM Script ──► TTS Audio ──► Whisper (timing)
   │                                        │
   └──► Image API (b-rolls) ◄───────────────┘
                    │
                    ▼
            FFmpeg Compose (9:16)
                    │
                    ▼
              output/final.mp4
```

Diagrama: [docs/PIPELINE.md](docs/PIPELINE.md)

## Dependências — FFmpeg com aceleração

### Linux (NVENC)

```bash
# Verificar suporte
ffmpeg -encoders | grep nvenc

# Build com NVENC requer libnvidia-encode
sudo apt install ffmpeg nvidia-cuda-toolkit
```

### macOS (VideoToolbox)

```bash
ffmpeg -hwaccel videotoolbox -i input.mp4 -c:v h264_videotoolbox output.mp4
```

### Windows

Use build gyan.dev com `--enable-nvenc` ou AMF para AMD.

## Métricas de renderização (referência)

| Etapa | Tempo (vídeo 60s) |
|-------|-------------------|
| Roteiro LLM | 5–15 s |
| TTS | 10–30 s |
| B-roll download | 20–60 s |
| Whisper + legendas | 30–90 s |
| FFmpeg (GPU) | 15–45 s |
| **Total** | **~2–4 min** |

CPU-only: 2–3× mais lento.

## Uso

```bash
pip install -r requirements.txt
cp config/pipeline.yaml.example config/pipeline.yaml
python -m src.render.cli --topic "5 hábitos produtivos" --output output/
```

## Estrutura

| Pasta | Função |
|-------|--------|
| `src/script/` | Geração de roteiro |
| `src/tts/` | Narração |
| `src/media/` | B-rolls |
| `src/subtitles/` | ASS/SRT dinâmico |
| `src/render/` | FFmpeg |
