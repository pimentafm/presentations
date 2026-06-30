# Apresentações (GitHub Pages)

Decks HTML interativos publicados via GitHub Pages.

## URLs

| Deck | Caminho | Conteúdo |
|------|---------|----------|
| **IDE** | `/ide/` | Infraestruturas de Dados Espaciais — perspectiva SRE |
| **Harness** | `/harness/` | Omni — Spec-Driven Development com agentes de IA |

### Site na raiz (`pimentafm.github.io/ide`)

Para servir em `https://pimentafm.github.io/ide` (sem prefixo `/presentations`), renomeie o repositório para `pimentafm.github.io`:

```bash
gh repo rename pimentafm.github.io --repo pimentafm/presentations
```

Depois do rename, as URLs ficam:

- https://pimentafm.github.io/
- https://pimentafm.github.io/ide/
- https://pimentafm.github.io/harness/

Enquanto o repositório se chamar `presentations`, as URLs usam o prefixo do projeto:

- https://pimentafm.github.io/presentations/ide/
- https://pimentafm.github.io/presentations/harness/

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
