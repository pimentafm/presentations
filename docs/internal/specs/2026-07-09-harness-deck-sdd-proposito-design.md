# Design — Propósito do SDD no deck Harness

- **Data:** 2026-07-09
- **Autor:** Fernando Pimenta
- **Deck-alvo:** `harness/` (apresentação Omni, tema violeta)
- **Projeto de referência:** `/Users/C20823Q/Documents/workspace/omni` (framework SDD)
- **Status:** Approved (2026-07-09) — pronto para handoff ao pipeline SDD (`/feature-discovery`)

## Contexto

O deck `harness/index.html` é **gerado** por `harness/src/build_omni_deck.py`, que:

1. Lê CSS/JS do template `ide/index.html` e aplica o tema violeta (`apply_purple_theme`).
2. Injeta os slides de `harness/src/_slides_fragment.html`.
3. Escreve `harness/index.html`.

**Toda edição de conteúdo dos slides acontece em `_slides_fragment.html`**; o `index.html` é artefato regenerado.

### Estado atual (22 slides)

O deck já explica **como** o SDD funciona (pipeline, gates, fases 09–12), mas o **porquê** aparece só de passagem:

| Slide | Conteúdo SDD hoje |
|-------|------------------|
| 05 Glossário | "escrever o *o quê* antes do código" |
| 02 O problema | Caos sem estrutura — memória, vocabulário, etapas, papéis |
| 08 Anti-alucinação | Transição: "entramos no método de entrega (SDD)" |
| 09 Pipeline SDD | Fases + gates + comandos — foco operacional |

No projeto Omni (`docs/user-guide/sdd-pipeline.md`, `.omni/README.md`), o propósito do SDD está mais explícito: pipeline com gates, estado em disco, separação de papéis, entrega auditable.

## Objetivo

Adicionar ao deck uma mensagem clara sobre o **propósito do SDD** para público misto (dev + gestão + iniciantes), com ênfase equilibrada em:

1. **Problema → solução** — fim do "vibe coding"
2. **Garantias de engenharia** — estado em disco, gates, papéis separados
3. **Valor de negócio** — previsibilidade, rastreabilidade, confiança

## Decisões (do brainstorming)

| Tema | Decisão |
| --- | --- |
| Ênfase | **Mix equilibrado** (problema + engenharia + negócio) |
| Abordagem | **1 slide novo** entre Anti-alucinação e Pipeline SDD |
| Escopo | Slide novo + ajustes leves em glossário e rodapé do slide 08 |
| Contagem | 22 → **23 slides** (renumerar `SHEET` a partir do novo slide) |
| Fora de escopo | Novos diagramas SVG; slides extras por fase; referências longas a Spec Kit/Kiro |

## Nova estrutura (trecho afetado)

```text
08 Anti-alucinação                   [rodapé ajustado]
09 [NOVO] Por que SDD?               ← propósito (mix D)
10 Pipeline SDD                      (era 09)
11 Discovery                         (era 10)
12 Planning                          (era 11)
13 TDD                               (era 12)
14 Pipeline vs Catálogo              (era 13)
…
23 Fechamento                        (era 22)
```

Todos os slides após o novo 09 devem ter `SHEET <em>NN</em> / 23` atualizado.

## Especificação do slide novo

Convenção do deck: `meta-bar`, `slide-content stack`, `eyebrow` + `h2.section` + corpo com `reveal`/`--delay`, `foot-bar`.

### Slide 09 (novo) — "Por que SDD?"

- **data-title:** `Por que SDD`
- **data-section:** `Método`
- **meta-left:** `MÉTODO · PROPÓSITO`
- **sheet:** `SHEET <em>09</em> / 23`

**Eyebrow:** `Do caos à entrega com evidência`

**h2:** `Por que <span class="accent">SDD</span>?`

**tagline:** Spec-Driven Development — o harness aplicado ao **fluxo de entrega**: especificar e validar antes de codificar.

**Componente:** `layer-grid` com 3 cards (`num` / `name` / `desc`):

| num | name | desc |
|-----|------|------|
| `01 · PROBLEMA` | **Fim do vibe coding** | Pedido solto vira código sem critério. SDD força: ideia → spec → gate → só então implementar. |
| `02 · ENGENHARIA` | **Garantias no disco** | Estado em `.omni/`, não no chat. Gates quantitativos. Quem escreve ≠ quem revisa. |
| `03 · NEGÓCIO` | **Entrega confiável** | Previsível, rastreável e auditável — decisões GO/NO-GO registradas antes de investir em código. |

**Contraste** (`code-block flow compact`, `--delay` após o grid):

```html
<span class="cm">Sem SDD:</span>  prompt → código → surpresa → retrabalho<br/>
<span class="cm">Com SDD:</span>  ideia → spec → validação → código com critério
```

**Pills:** `spec antes de código` · `estado em arquivos` · `papéis separados` · `retomar de onde parou`

**foot-bar:** author = `SDD não é burocracia — é método para o agent não pular etapas` · label = `PROPÓSITO SDD`

## Ajustes em slides existentes

### Slide 05 — Glossário, entrada SDD

**De:**

> Desenvolvimento guiado por especificação — escrever o "o quê" *antes* do código.

**Para:**

> Desenvolvimento guiado por especificação — definir e validar o *o quê* **antes** do código, com gates entre fases e estado salvo em disco.

### Slide 08 — foot-bar author

**De:**

> Com vocabulary e graph prontos, entramos no método de entrega (SDD)

**Para:**

> Com vocabulary e graph prontos, o próximo passo é o método — mas por quê SDD?

### Slide 10 (ex-09) — Pipeline SDD

Sem mudança estrutural obrigatória. O `term-note` inicial pode permanecer; o propósito fica no slide 09.

## Build e verificação

```bash
python harness/src/build_omni_deck.py
```

Checklist pós-implementação:

1. `harness/index.html` regenerado sem erros.
2. Todos os slides exibem `SHEET xx / 23`.
3. Slide 09 novo renderiza `layer-grid` + contraste + pills sem overflow.
4. Navegação sequencial 08 → 09 → 10 mantém narrativa.

## Arquivos tocados

| Arquivo | Ação |
|---------|------|
| `harness/src/_slides_fragment.html` | Inserir slide 09; ajustar glossário e rodapé 08; renumerar sheets |
| `harness/index.html` | Regenerar via build script |
| `harness/src/build_omni_deck.py` | Alterar apenas se o script hardcodar total de slides (verificar) |

## Handoff SDD

Após aprovação deste spec:

```text
/feature-discovery --title "Propósito SDD no deck harness" --idea-file docs/internal/specs/2026-07-09-harness-deck-sdd-proposito-design.md
```
