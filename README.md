# Apresentações

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-live-2ea043?style=flat-square&logo=githubpages&logoColor=white)](https://pimentafm.github.io/presentations/)
[![HTML5](https://img.shields.io/badge/decks-HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)](https://pimentafm.github.io/presentations/)
[![Python](https://img.shields.io/badge/build-Python%203-3776AB?style=flat-square&logo=python&logoColor=white)](harness/src/build_omni_deck.py)
[![Last commit](https://img.shields.io/github/last-commit/pimentafm/presentations?style=flat-square&logo=git)](https://github.com/pimentafm/presentations/commits/main)
[![Repo](https://img.shields.io/github/stars/pimentafm/presentations?style=social)](https://github.com/pimentafm/presentations)

Decks HTML interativos, sem dependências de runtime — publicados via [GitHub Pages](https://pimentafm.github.io/presentations/).

Navegação: **setas** ou **espaço** para avançar, **scroll** entre slides, **F** para tela cheia.

## Decks

| Deck | URL | Conteúdo |
|------|-----|----------|
| **Catálogo** | [/presentations/](https://pimentafm.github.io/presentations/) | Índice de decks |
| **IDE** | [/presentations/ide/](https://pimentafm.github.io/presentations/ide/) | Infraestruturas de Dados Espaciais — perspectiva SRE |
| **Harness** | [/presentations/harness/](https://pimentafm.github.io/presentations/harness/) | Omni — Agent = Model + Harness, SDD, ontologia, knowledge graph e ecossistema de agents (24 slides) |

## Estrutura

```
├── index.html                    # catálogo de decks
├── ide/
│   ├── index.html                # deck IDE (template visual de referência)
│   └── assets/
└── harness/
    ├── index.html                # deck Omni (gerado)
    ├── omni.png                  # asset da capa / branding
    ├── tui.png                   # screenshot da TUI Omni
    └── src/
        ├── build_omni_deck.py    # gera harness/index.html a partir do template IDE
        └── _slides_fragment.html # conteúdo dos slides (fonte de edição)
```

## Editar o deck Harness

1. Altere os slides em `harness/src/_slides_fragment.html`.
2. Se precisar ajustar layout/CSS compartilhado ou tema violeta, edite `harness/src/build_omni_deck.py` (ou o template base em `ide/index.html`).
3. Regere o HTML:

```bash
python3 harness/src/build_omni_deck.py
```

O build escreve `harness/index.html` (não edite esse arquivo diretamente — ele é artefato gerado).

## Deploy

Push na branch `main`. O GitHub Pages publica automaticamente a raiz do repositório (`Settings → Pages → Deploy from branch main /`).

## Autor

[Fernando Pimenta](https://github.com/pimentafm)
