<p align="center">
    <img src="./docs/banner.png" alt="geg-tomd Banner" width="200">
</p>

<h1 align="center">geg-tomd</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-0062AF?style=for-the-badge&logo=python&logoColor=f6f6f6" />
  <img src="https://img.shields.io/badge/Gemini-0062AF?style=for-the-badge&logo=googlegemini&logoColor=f6f6f6" />
  <img src="https://img.shields.io/badge/Typer-0062AF?style=for-the-badge&logo=python&logoColor=f6f6f6" />
  <img src="https://img.shields.io/badge/uv-0062AF?style=for-the-badge&logo=uv&logoColor=f6f6f6" />
</p>

<p align="center">
  Ferramenta CLI para converter PDFs, arquivos de texto e Markdown em arquivos <code>.md</code>, com recursos opcionais de IA para resumir e complementar o conteúdo.
</p>

## Funcionalidades

- [x] Suporte a arquivos `pdf`, `.txt` e `.md`
- [x] Extração de conteúdo de PDFs comm e sem IA
- [x] Resumo de conteúdo com IA
- [x] Complementação de informações incompletas ou referências sem contexto
- [x] Reconstrução do diretório de entrada no diretório de saída
- [x] Opções via CLI

## Próximas funcionalidades

- [ ] **Fallback entre modelos** — utilizar outros modelos quando o principal estiver indisponível ou atingir limites.
- [ ] **Detecção do tipo de PDF** — identificar automaticamente documentos com texto extraível, muitas imagens ou necessidade de OCR.
- [ ] **Melhoria dos logs** — adicionar informações mais detalhadas sobre o processamento.
- [ ] **Estruturas de saída configuráveis** — permitir escolher diferentes formatos e organizações para o Markdown gerado.
- [ ] **Tipagem das entradas da CLI** — melhorar a validação e organização dos parâmetros.

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

### Opções

| Opção               | Descrição                        |
| ------------------- | -------------------------------- |
| `-o`, `--output`    | Define o arquivo de saída        |
| `-s`, `--summarize` | Resume o conteúdo                |
| `-c`, `--complete`  | Completa informações incompletas |
| `--ai`              | Utiliza IA para processar PDFs   |

As opções podem ser combinadas:

```bash
uv run geg-tomd arquivo.pdf -o resultado.md -sc --ai
```

