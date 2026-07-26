# Design — Vantagens do Omni no deck Harness

- **Data:** 2026-07-26
- **Autor:** Fernando Pimenta
- **Deck-alvo:** `harness/` (apresentação Omni, tema violeta)
- **Status:** Approved (2026-07-26) — pronto para handoff ao pipeline SDD (`/feature-discovery`)

## Contexto

O deck `harness/index.html` é **gerado** por `harness/src/build_omni_deck.py`, que:

1. Lê CSS/JS do template `ide/index.html` e aplica o tema violeta (`apply_purple_theme`).
2. Injeta os slides de `harness/src/_slides_fragment.html`.
3. Escreve `harness/index.html`.

**Toda edição de conteúdo dos slides acontece em `_slides_fragment.html`**; o `index.html` é artefato regenerado.

### Estado atual (24 slides)

O deck já cobre conceito, método SDD, Omni (slides 15–19), tendências (20), **como usar** (sheet 21 — CLI/TUI) e encerra com Roadmap (22), Recursos (23) e Fechamento (24).

| Sheet | Conteúdo hoje |
|-------|---------------|
| 15–19 | O que é Omni, harness na prática, Omni Graph |
| 20 | Tendências que validam o Omni |
| 21 | CLI e TUI — **Como usar** (comandos + screenshot) |
| 22 | Roadmap — ROI **futuro** do harness (ontology nos gates, metaharness, TOON) |
| 23–24 | Recursos e Fechamento |

**Lacuna:** após "Como usar", falta um slide que traduza **valor de adoção** para gestão (hora/homem, menos retrabalho) e para engenharia (menos alucinação, mais acerto) — sem repetir o bloco técnico dos slides 15–19.

## Objetivo

Adicionar **1 slide novo** após sheet 21 ("Como usar") que comunique:

1. **Gestão / operação** — adoção de AI escala quando a organização entrega mais com **menos hora/homem** e menos retrabalho.
2. **Engenharia** — Omni reduz alucinação e aumenta acerto (ontology, graph-first, gates), apoiando o engenheiro em decisão técnica em vez de desfazer código inventado.
3. **Economia** — tokens e tempo aplicados no lugar certo (graph MCP com caps), sem prometer multiplicadores numéricos.

## Decisões (do brainstorming)

| Tema | Decisão |
| --- | --- |
| Público principal | **Gestão** (hora/homem, adoção em escala) |
| Público secundário | **Dev/Tech** (acurácia, menos alucinação) |
| Abordagem | **1 slide** — grid de 3 pilares + bloco contraste (padrão slide 09 "Por que SDD?") |
| Posição | **Novo sheet 22**, entre "Como usar" (21) e Roadmap (renumerado) |
| Contagem | 24 → **25 slides** (renumerar `SHEET` a partir do novo slide) |
| Tom | Ganho **implícito** de capacidade (222 agents, gates, graph) — **sem** "1 pessoa = 10" ou % inventados |
| Slides 15–19 | **Permanecem inalterados** — o novo slide referencia o que o público já viu, sem reescrever o bloco Sistema |
| Fora de escopo | Segundo slide só de tokens; benchmarks inventados; novos diagramas SVG; alteração de slides 15–19 |

## Nova estrutura (trecho afetado)

```text
21 Como usar (CLI/TUI)               [inalterado]
22 [NOVO] Por que Omni?              ← valor: hora/homem + acurácia + economia
23 Roadmap                           (era 22)
24 Recursos                          (era 23)
25 Fechamento                        (era 24)
```

Todos os slides a partir do novo 22 devem ter `SHEET <em>NN</em> / 25` atualizado.

## Especificação do slide novo

Convenção do deck: `meta-bar`, `slide-content stack dense-slide`, `eyebrow` + `h2.section` + corpo com `reveal`/`--delay`, `foot-bar`.

### Slide 22 (novo) — "Por que Omni?"

- **data-title:** `Por que Omni`
- **data-section:** `Operação`
- **meta-left:** `OPERAÇÃO · VALOR`
- **sheet:** `SHEET <em>22</em> / 25`

**Eyebrow:** `Adoção de AI em escala`

**h2:** `Por que <span class="accent">Omni</span>?`

**tagline:** A adoção de AI depende de **menos hora/homem** e **menos retrabalho** — com qualidade que o engenheiro consegue confiar.

**Componente:** `layer-grid` com 3 cards (`num` / `name` / `desc`):

| num | name | desc |
|-----|------|------|
| `01 · OPERAÇÃO` | **Menos gente, mais entrega** | 1 operador orquestra **222 agents** (discovery, planning, review, domínio) — sem montar squad para cada feature. Estado em `.omni/` permite retomar, auditar e escalar sem perder contexto. |
| `02 · ACURÁCIA` | **Menos alucinação, mais acerto** | **Ontology + graph-first + gates** bloqueiam avanço quando vocabulário ou contexto está errado. Engenheiro valida evidência em disco — não adivinha se a AI inventou API ou conceito. |
| `03 · ECONOMIA` | **Tokens e tempo no lugar certo** | **Graph MCP** com caps (4KB/8KB) em vez de jogar o repositório inteiro no prompt. Menos contexto desperdiçado = menos custo de API **e** menos hora/homem em retrabalho. |

**Contraste** (`code-block flow compact`, após o grid):

```html
<span class="cm">Sem Omni:</span>  prompt solto → código frágil → refazer → mais gente e mais tempo<br/>
<span class="cm">Com Omni:</span>  spec → gate → código com critério → menos ciclos de correção
```

**Pills:** `menos hora/homem` · `menos alucinação` · `graph-first` · `estado em disco` · `quem escreve ≠ quem revisa`

**foot-bar:** author = `Omni amplifica a capacidade de entrega — o engenheiro foca em decisão técnica, não em desfazer alucinação` · label = `VALOR OMNI`

### Relação com slides adjacentes

| Slide | Papel narrativo |
|-------|-----------------|
| 21 Como usar | **Como** operar (CLI/TUI) |
| **22 Por que Omni** (novo) | **Por que** adotar — ganho atual em hora/homem e acurácia |
| 23 Roadmap | **Para onde** evoluir — ROI futuro (ontology nos gates, metaharness, TOON) |

Evitar duplicar bullets do Roadmap; o slide 22 fala de benefícios **já disponíveis** com o framework atual.

## Ajustes em slides existentes

Nenhuma alteração de conteúdo nos slides 15–19 ou 21.

**Renumeração obrigatória:** sheets 22–24 atuais passam a 23–25 (`SHEET <em>NN</em> / 25`).

**README:** atualizar contagem de slides na tabela de decks (24 → 25).

## Build e verificação

```bash
python3 harness/src/build_omni_deck.py
```

Checklist pós-implementação:

1. `harness/index.html` regenerado sem erros.
2. Todos os slides exibem `SHEET xx / 25`.
3. Slide 22 novo renderiza `layer-grid` + contraste + pills sem overflow em viewport padrão do deck.
4. Navegação sequencial 21 → 22 → 23 mantém narrativa (como usar → valor → roadmap).
5. Slides 15–19 permanecem byte-a-byte equivalentes em conteúdo (salvo renumeração de sheet).

## Arquivos tocados

| Arquivo | Ação |
|---------|------|
| `harness/src/_slides_fragment.html` | Inserir slide 22; renumerar sheets 22–24 → 23–25 |
| `harness/index.html` | Regenerar via build script |
| `README.md` | Atualizar contagem de slides (24 → 25) |
| `harness/src/build_omni_deck.py` | Alterar apenas se hardcodar total de slides (verificar na implementação) |

## Handoff SDD

Após aprovação deste spec:

```text
/feature-discovery --title "Vantagens Omni no deck harness" --idea-file docs/internal/specs/2026-07-26-harness-deck-omni-vantagens-design.md
```

**Pré-requisito:** `.omni/` no repositório (`omni project init` na raiz do projeto).
