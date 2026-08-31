<p align="center">
    <img src="./docs/banner.png" alt="geg-tomd Banner" width="200">
</p>

<h1 align="center">geg-tomd</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-f6f6f6?style=for-the-badge&logo=python&logoColor=4eace7" />
  <img src="https://img.shields.io/badge/Gemini-f6f6f6?style=for-the-badge&logo=googlegemini&logoColor=4eace7" />
  <img src="https://img.shields.io/badge/Typer-f6f6f6?style=for-the-badge&logo=python&logoColor=4eace7" />
  <img src="https://img.shields.io/badge/uv-f6f6f6?style=for-the-badge&logo=uv&logoColor=4eace7" />
</p>

<p align="center">
  Ferramenta de linha de comando para converter PDFs, arquivos de texto e Markdown em arquivos <code>.md</code>, com recursos opcionais de IA para resumir e complementar o conteúdo.
</p>

## Funcionalidades

* [x] Conversão de PDF para Markdown
* [x] Suporte a arquivos `.txt` e `.md`
* [x] Extração de conteúdo de PDFs sem IA
* [x] Processamento de PDFs com IA
* [x] Resumo de conteúdo com IA
* [x] Complementação de informações incompletas ou referências sem contexto
* [x] Opções via CLI

## Próximas funcionalidades

* [ ] **Fallback entre modelos** — utilizar outros modelos quando o principal estiver indisponível ou atingir limites.
* [ ] **Detecção do tipo de PDF** — identificar automaticamente documentos com texto extraível, muitas imagens ou necessidade de OCR.
* [ ] **Melhoria dos logs** — adicionar informações mais detalhadas sobre o processamento.
* [ ] **Estruturas de saída configuráveis** — permitir escolher diferentes formatos e organizações para o Markdown gerado.
* [ ] **Camada genérica para geração com IA** — centralizar e reutilizar chamadas à API do Gemini.
* [ ] **Tipagem das entradas da CLI** — melhorar a validação e organização dos parâmetros.

## Instalação

```bash
git clone https://github.com/gabrielescorelguerra/geg-tomd.git
cd geg-tomd

uv sync
```

## Uso

### Conversão básica

```bash
uv run geg-tomd arquivo.pdf
```

### Definir arquivo de saída

```bash
uv run geg-tomd arquivo.pdf -o resultado.md
```

### Resumir o conteúdo

```bash
uv run geg-tomd arquivo.pdf -s
```

### Completar informações

```bash
uv run geg-tomd arquivo.pdf -c
```

### Utilizar IA para processar o PDF

```bash
uv run geg-tomd arquivo.pdf --ai
```

### Combinar opções

```bash
uv run geg-tomd arquivo.pdf -sc --ai
```
