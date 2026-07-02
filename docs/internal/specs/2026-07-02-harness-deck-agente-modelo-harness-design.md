# Design — Base conceitual "Agente = Modelo + Harness" no deck Omni

- **Data:** 2026-07-02
- **Autor:** Fernando Pimenta
- **Deck-alvo:** `harness/` (apresentação Omni, tema violeta)
- **Status:** Approved (2026-07-02) — pronto para handoff ao pipeline SDD (`/feature-discovery`)

## Contexto

O deck `harness/index.html` é **gerado** por `harness/src/build_omni_deck.py`, que:

1. Lê CSS/JS do template `ide/index.html` e aplica o tema violeta (`apply_purple_theme`).
2. Injeta os slides de `harness/src/_slides_fragment.html`.
3. Escreve `harness/index.html`.

Portanto, **toda edição de conteúdo dos slides acontece em `_slides_fragment.html`**; o `index.html` é um artefato regenerado pelo script.

Fluxo atual (17 slides): `01 Capa` → `02 O problema` → `03 O que é Omni` → `04 Agente = Modelo + Harness` (já com sabor Omni: Rules/Skills/MCP, `.omni/`) → `05 Camadas do harness` → pipeline → fechamento.

**Problema:** a apresentação entra no Omni (slide 03) antes de firmar o conceito genérico de "Agente = Modelo + Harness". O conceito só aparece no slide 04, já acoplado ao Omni.

## Objetivo

Adicionar a base conceitual genérica **"Agente = Modelo + Harness"** ANTES de explicar como o Omni funciona, acessível a um público misto (dev + gestão + iniciantes), reusando a identidade visual existente do deck.

## Decisões (do brainstorming)

| Tema | Decisão |
| --- | --- |
| Escopo | **2 slides novos** genéricos |
| Enquadramento | **Anatomia + analogia** (motor → carro): slide "O Modelo" + slide "O Harness (+ equação)" |
| Slide 04 atual | **Re-enquadrar** como a instância Omni da equação (genérico antes, Omni depois) |
| Público | **Todos** (dev + gestão + iniciantes) → analogia simples, baixo jargão, mas concreto |
| Ponto de inserção | Entre o slide 02 (O problema) e o atual 03 (O que é Omni) |

## Nova estrutura (17 → 19 slides)

```text
01 Capa
02 O problema (caos)                 [gancho do rodapé emenda nos novos slides]
03 [NOVO] O Modelo: o motor          ← genérico
04 [NOVO] O Harness: do motor ao carro (+ equação)  ← genérico
05 O que é Omni                      (era 03)
06 O harness do Omni                 (era 04, RE-ENQUADRADO)
07 Camadas do harness                (era 05)
08 Pipeline SDD                      (era 06)
09 Discovery                         (era 07)
10 Planning                          (era 08)
11 TDD                               (era 09)
12 Omni Graph                        (era 10)
13 Ontologias                        (era 11)
14 Anti-alucinação                   (era 12)
15 Pipeline vs Catálogo              (era 13)
16 Tendências IA                     (era 14)
17 CLI e TUI                         (era 15)
18 Roadmap                           (era 16)
19 Fechamento                        (era 17)
```

## Especificação dos slides novos

Convenção de cores do deck: `.accent` = violeta (harness), `.accent-cyan` = ciano (modelo).
Todos os slides seguem o gabarito existente: `meta-bar` (com `dot` + label e `sheet`), `slide-content stack`, `eyebrow` + `h2.section` + `tagline`, componente central com `reveal`/`--delay`, e `foot-bar` com `author` + label à direita.

### Slide 03 (novo) — "O Modelo: o motor"

- **meta-left:** `CONCEITO · O MODELO`
- **data-section:** `Fundação`
- **eyebrow:** `Fundação`
- **h2:** O modelo: o `<span class="accent-cyan">motor</span>`
- **tagline:** Modelo = poder bruto de raciocínio e linguagem (Claude, GPT, Gemini…). Prevê e raciocina sobre texto.
- **Componente:** `layer-grid` com 4 cards (`num` / `name` / `desc`):
  - `01 · PODER` — **Raciocínio e linguagem** — resolve, resume, escreve código, explica.
  - `02 · SEM MEMÓRIA` — **Esquece entre sessões** — nada persiste; cada conversa recomeça do zero.
  - `03 · SEM AÇÃO` — **Não age sozinho** — não lê arquivos, não roda comandos, não usa ferramentas.
  - `04 · SEM GARANTIA` — **Pode alucinar** — inventa APIs e fatos com confiança.
- **Fecho (body-text):** "Um motor potente — mas sozinho, sem chassi, direção ou freios, não leva ninguém a lugar nenhum."
- **foot-bar:** author = "Trocar de modelo aumenta o poder — não as garantias" · label = `MODELO = LLM`

### Slide 04 (novo) — "O Harness: do motor ao carro"

- **meta-left:** `CONCEITO · O HARNESS`
- **data-section:** `Fundação`
- **eyebrow:** `Fundação`
- **h2:** O harness: do motor ao `<span class="accent">carro</span>`
- **tagline:** Harness = tudo ao redor do modelo para ele agir com segurança e propósito.
- **Componente:** `term-table` (peça genérica → função):
  - Contexto → o que o modelo enxerga (instruções, dados relevantes)
  - Ferramentas → ler/escrever arquivos, rodar comandos, buscar
  - Memória / Estado → o que persiste entre passos e sessões
  - Controle de fluxo → etapas, ordem, quando parar
  - Guardrails → regras, revisão e gates que barram o erro
- **Linha-equação em destaque:** `Agente = <span class="accent-cyan">Modelo</span> + <span class="accent">Harness</span>` — renderizada grande e centralizada, reusando tokens de tipografia existentes (`var(--font-display)`, `clamp(...)`).
- **Fecho (body-text):** "Motor (modelo) + chassi, direção e freios (harness) = um carro em que você confia para dirigir."
- **foot-bar:** author = "O harness canaliza o poder do modelo em comportamento confiável" · label = `AGENTE = MODELO + HARNESS`

## Re-enquadramento do slide 04 atual (→ novo slide 06)

Mantém a tabela `term-table` existente (LLM→raciocínio bruto; Rules+Skills+MCP→orquestração; Agents+Gates+`.omni/`→confiável e auditável) e o parágrafo final. Muda apenas o topo para sinalizar que é a **instância Omni**, não a re-explicação da equação:

| Campo | De | Para |
| --- | --- | --- |
| meta-left | `CONCEITO CENTRAL` | `OMNI · HARNESS NA PRÁTICA` |
| eyebrow | `Equação` | `Na prática` |
| h2 | `Agente = Modelo + Harness` | `O harness do <span class="accent">Omni</span>` |
| tagline | (nova) | "Como o Omni implementa cada parte do harness." |

## Renumeração

- Total em todos os rótulos `SHEET <em>NN</em> / 17` passa para `/ 19`.
- Slides a partir do antigo 03 deslocam +2 no `NN`.
- Nav dots são gerados por JS a partir dos `.slide`, sem contagem hardcoded — não requerem ajuste.

## Seções (`data-section`) — manter contíguas

O `section-progress` (JS em `ide/index.html`, `setupSectionProgress`) agrupa por `data-section` e calcula a largura da barra pelo **primeiro e último** slide com aquele nome. Logo, **slides de uma mesma seção precisam ser contíguos**; um nome repetido em blocos separados gera uma barra com span errado.

Hoje a ordem é `… Sistema (O que é Omni) → Fundação (equação, camadas) …`. Inserir 2 slides "Fundação" antes de "O que é Omni" dividiria "Fundação" em dois blocos. Correção: os 2 slides novos ficam em **`Fundação`** (base conceitual genérica) e os slides Omni-específicos migram para **`Sistema`**.

| Slide | `data-section` |
| --- | --- |
| 03 (novo) O Modelo | `Fundação` |
| 04 (novo) O Harness | `Fundação` |
| 05 O que é Omni (era 03) | `Sistema` (inalterado) |
| 06 O harness do Omni (era 04) | `Fundação` → **`Sistema`** |
| 07 Camadas do harness (era 05) | `Fundação` → **`Sistema`** |

Resultado (contíguo): `Intro · Contexto · Fundação(03–04) · Sistema(05–07) · Pipeline · Conhecimento · Ecossistema · Tendências · Operação · Wrap-up`. Semântica fica mais limpa: `Fundação` = conceito genérico, `Sistema` = o Omni.

## Mecânica de build

1. Editar `harness/src/_slides_fragment.html` (inserir 2 slides, re-enquadrar antigo 04, renumerar SHEET).
2. Rodar `python3 harness/src/build_omni_deck.py` para regenerar `harness/index.html`.
3. Conferir contagem impressa (`19 slides`) e abrir o HTML para validar visual.

## Fora de escopo (não-objetivos)

- Não mexer no template `ide/index.html` nem no tema/CSS.
- Não alterar o conteúdo dos slides do pipeline (Discovery/Planning/TDD/…) além da renumeração.
- Não introduzir novos componentes visuais nem dependências; reusar os existentes.
- Não editar `harness/index.html` à mão (é artefato gerado).

## Critérios de aceite

- [ ] `_slides_fragment.html` contém 19 slides na ordem especificada.
- [ ] Os 2 slides novos aparecem antes de "O que é Omni", com o conteúdo/analogia acima.
- [ ] Slide 04 atual re-enquadrado (novos meta-left/eyebrow/h2/tagline), tabela preservada.
- [ ] Todos os rótulos `SHEET NN / 19` corretos e sequenciais (01…19).
- [ ] `data-section` contíguas: `Fundação` = 03–04; `Sistema` = 05–07 (sem blocos repetidos).
- [ ] `build_omni_deck.py` roda sem erro e imprime 19 slides.
- [ ] Deck abre no navegador com identidade visual intacta (tema violeta, reveal/animações).
