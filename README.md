# Apresentações (GitHub Pages)

Decks HTML interativos publicados via GitHub Pages.

## URLs

Publicado em [pimentafm.github.io/presentations](https://pimentafm.github.io/presentations/).

| Deck | URL | Conteúdo |
|------|-----|----------|
| Catálogo | [/presentations/](https://pimentafm.github.io/presentations/) | Índice de decks |
| **IDE** | [/presentations/ide/](https://pimentafm.github.io/presentations/ide/) | Infraestruturas de Dados Espaciais — perspectiva SRE |
| **Harness** | [/presentations/harness/](https://pimentafm.github.io/presentations/harness/) | Omni — Spec-Driven Development com agentes de IA |

## Estrutura

```
├── index.html          # catálogo de decks
├── ide/
│   ├── index.html      # deck IDE (fonte do template visual)
│   └── assets/
└── harness/
    ├── index.html      # deck Omni (gerado)
    └── src/
        ├── build_omni_deck.py
        └── _slides_fragment.html
```

## Rebuild do deck Harness

Após editar slides em `harness/src/_slides_fragment.html` ou o template em `ide/index.html`:

```bash
python3 harness/src/build_omni_deck.py
```

O HTML final é escrito em `harness/index.html`.

## Deploy

Push na branch `main` — GitHub Pages publica automaticamente (Settings → Pages → branch `main`, pasta `/`).
