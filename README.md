<div align="center">

# Pipeline autônomo de vídeos curtos

<p>
  <a href="https://github.com/SrSatriano/autonomous-short-form-video-pipeline"><img src="https://img.shields.io/badge/GitHub-autonomous-short-form-video-pipeline-24292e?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
  <a href="https://srsatriano.github.io/portfolio-matheus-satriano/"><img src="https://img.shields.io/badge/Portfólio-web-0891b2?style=for-the-badge" alt="Portfólio" /></a>
</p>

<p>
  <img src="https://img.shields.io/badge/versão-1.0.0-0ea5e9?style=flat-square" alt="versão" />
  <img src="https://img.shields.io/badge/Tier-2-8b5cf6?style=flat-square" alt="tier" />
  <img src="https://img.shields.io/badge/demo-em_evolutivo-f59e0b?style=flat-square" alt="demo" />
  <img src="https://img.shields.io/badge/licença-MIT-22c55e?style=flat-square" alt="licença" />
  <img src="https://img.shields.io/badge/idioma-pt--BR-blue?style=flat-square" alt="idioma" />
  <img src="https://img.shields.io/badge/CI-GitHub_Actions-8b5cf6?style=flat-square" alt="ci" />
</p>

<p><strong>Do tema ao MP4 vertical: roteiro, TTS, b-roll, legendas e render.</strong></p>

<p>
  Autor: <a href="https://github.com/SrSatriano">@SrSatriano</a> ·
  Release <strong>1.0.0</strong> (2026-03-26)
</p>

</div>

---

## Índice

1. [Visão geral](#visão-geral)
2. [Problema e solução](#problema-e-solução)
3. [Para quem é](#para-quem-é)
4. [Casos de uso](#casos-de-uso)
5. [Funcionalidades](#funcionalidades)
6. [Stack tecnológica](#stack-tecnológica)
7. [Arquitetura](#arquitetura)
8. [Estrutura do repositório](#estrutura-do-repositório)
9. [Pré-requisitos](#pré-requisitos)
10. [Instalação e execução](#instalação-e-execução)
11. [Configuração](#configuração)
12. [Testes](#testes)
13. [Performance](#performance)
14. [Deploy e operação](#deploy-e-operação)
15. [Limitações conhecidas](#limitações-conhecidas)
16. [Roadmap](#roadmap)
17. [Documentação complementar](#documentação-complementar)
18. [Segurança e licença](#segurança-e-licença)

---

## Visão geral

Este repositório faz parte do **portfólio de engenharia** mantido por [@SrSatriano](https://github.com/SrSatriano). A versão **1.0.0** entrega implementação do núcleo do produto, testes automatizados, pipeline de integração contínua e documentação operacional em **português brasileiro**.

O objetivo é permitir que você clone, execute e evolua o projeto com clareza — do desenvolvimento local ao deploy em produção.

## Problema e solução

| | |
|---|---|
| **Problema** | Produzir Shorts/Reels manualmente consome horas por peça. |
| **Solução** | Pipeline YAML com estágios medidos e saída 9:16 pronta para publicação. |

## Para quem é

Criadores de conteúdo e agências de marketing.

## Casos de uso

- Canal de dicas automatizado
- Testes A/B de hooks

## Funcionalidades

- [x] Pipeline configurável em YAML
- [x] Legendas ASS com word timing
- [x] NVENC / VideoToolbox / AMF
- [x] Métricas por estágio
- [x] Saída TikTok/Shorts

## Stack tecnológica

| Camada | Tecnologias |
|--------|-------------|
| **Principal** | Python, FFmpeg, Whisper, APIs de LLM |

## Arquitetura

```mermaid
flowchart LR
  T[Tema] --> R[Roteiro LLM]
  R --> TTS[TTS]
  TTS --> FF[FFmpeg / legendas]
  FF --> MP4[Vídeo 9:16]
```

Detalhamento de componentes, fluxos de dados e decisões de design: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Estrutura do repositório

| Caminho | Descrição |
|---------|-----------|
| `src/render/` | CLI de render |
| `config/` | Presets de pipeline |

## Pré-requisitos

Python 3.11+, FFmpeg no PATH, GPU opcional.

## Instalação e execução

```bash
git clone https://github.com/SrSatriano/autonomous-short-form-video-pipeline.git
cd autonomous-short-form-video-pipeline
```

```bash
python -m src.render.cli --topic "produtividade" --output output/
```

## Configuração

| Variável | Descrição | Exemplo |
|----------|-----------|--------|
| `OPENAI_API_KEY` | Roteiro LLM | `sk-...` |

> **Importante:** nunca faça commit de arquivos `.env` com segredos reais. Use `.env.example` como referência.

## Testes

Execute a suíte de testes antes de abrir pull requests:

```bash
pytest tests/ -q
```

A pipeline [`.github/workflows/ci.yml`](.github/workflows/ci.yml) repete build e testes em cada push para `main`.

## Performance

| Vídeo 60 s 1080×1920 | Tempo (GPU) |
|------------------------|-------------|
| | ~2,8 min |

Metodologia, hardware de referência e flags de compilação: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Deploy e operação

| Guia | Conteúdo |
|------|----------|
| [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) | Homologação, produção e rollback |
| [docs/OPERATIONS.md](docs/OPERATIONS.md) | Monitoramento, alertas e incidentes |

## Limitações conhecidas

- B-roll stock requer chaves de API externas

## Roadmap

- Editor de timeline simples

## Documentação complementar

| Documento | Descrição |
|-----------|-----------|
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Arquitetura e decisões técnicas |
| [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) | Deploy passo a passo |
| [docs/OPERATIONS.md](docs/OPERATIONS.md) | Runbook operacional |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Como contribuir |
| [CHANGELOG.md](CHANGELOG.md) | Histórico de versões |
| [SECURITY.md](SECURITY.md) | Política de segurança |
| [AUTHORS.md](AUTHORS.md) | Créditos |

## Segurança e licença

- Dependências revisadas na release **1.0.0**
- Vulnerabilidades: siga [SECURITY.md](SECURITY.md)
- Licença: [MIT](LICENSE) © SrSatriano 2026

---

<p align="center">
  <a href="https://srsatriano.github.io/portfolio-matheus-satriano/">Portfólio completo</a> ·
  <a href="https://github.com/SrSatriano">@SrSatriano</a> ·
  <a href="https://github.com/SrSatriano/autonomous-short-form-video-pipeline">Este repositório</a>
</p>
