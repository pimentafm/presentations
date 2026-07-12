#!/usr/bin/env python3
"""Build Omni SDD presentation from the IDE deck template."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
REF = ROOT / "ide" / "index.html"
OUT = ROOT / "harness" / "index.html"
SLIDES = Path(__file__).parent / "_slides_fragment.html"

# Accent: âmbar topográfico → violeta (Omni theme)
PURPLE = "#a78bfa"
PURPLE_RGB = "167, 139, 250"


def apply_purple_theme(text: str) -> str:
    text = text.replace("#f5b73d", PURPLE)
    text = text.replace("rgba(245, 183, 61,", f"rgba({PURPLE_RGB},")
    text = text.replace("rgba(245,183,61", f"rgba({PURPLE_RGB.replace(' ', '')}")
    text = text.replace("âmbar topográfico", "violeta")
    text = text.replace("'amber'", "'violet'")
    text = text.replace("p.tint === 'amber'", "p.tint === 'violet'")
    return text


ref = REF.read_text()
s0 = ref.index("<style>") + len("<style>")
s1 = ref.index("</style>", s0)
css = apply_purple_theme(ref[s0:s1])
css = css.replace(
    "--topo: #a78bfa;",
    f"--topo: {PURPLE};\n        --topo-deep: #8b5cf6;",
)

script_marker = ref.rindex("<script>")
script_end = ref.rindex("</script>")
js = apply_purple_theme(ref[script_marker + len("<script>") : script_end])

extra_css = """
      .closing-quote {
        font-family: var(--font-display);
        font-size: clamp(1rem, 2.2vw, 1.5rem);
        font-weight: 400;
        font-style: italic;
        line-height: 1.45;
        color: var(--ink-mute);
        max-width: 62ch;
      }
      .closing-quote strong { color: var(--topo); font-style: normal; font-weight: 700; }
      .term-note {
        font-size: var(--small-size);
        color: var(--ink-mute);
        line-height: 1.45;
        max-width: 62ch;
      }
      .term-note strong { color: var(--ink); font-weight: 500; }
      .glossary-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: clamp(0.35rem, 0.7vw, 0.55rem);
        max-width: min(95vw, 1200px);
      }
      @media (max-width: 1100px) { .glossary-grid { grid-template-columns: repeat(3, 1fr); } }
      @media (max-width: 600px) { .glossary-grid { grid-template-columns: 1fr; } }
      .glossary-item {
        padding: clamp(0.55rem, 1vw, 0.85rem) clamp(0.7rem, 1.2vw, 1rem);
        border: 1px solid var(--hairline);
        border-radius: 4px;
        background: rgba(244, 236, 216, 0.02);
      }
      .glossary-item dt {
        font-family: var(--font-mono);
        font-size: var(--micro-size);
        letter-spacing: 0.06em;
        text-transform: uppercase;
        color: var(--topo);
        margin-bottom: 0.25rem;
      }
      .glossary-item dd {
        font-size: var(--small-size);
        color: var(--ink-mute);
        line-height: 1.4;
      }
      .code-block.flow {
        white-space: normal;
        overflow-x: visible;
        overflow-wrap: break-word;
        max-width: min(72ch, 96vw);
        line-height: 1.55;
      }
      .code-block.compact {
        font-size: clamp(0.58rem, 1.05vw, 0.72rem);
        padding: clamp(0.45rem, 1vw, 0.7rem) clamp(0.6rem, 1.2vw, 0.95rem);
        max-width: min(78ch, 96vw);
        line-height: 1.42;
        white-space: pre-wrap;
      }
      .example-label {
        font-family: var(--font-mono);
        font-size: var(--micro-size);
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: var(--ink-faint);
        margin-bottom: 0.3rem;
      }
      .ex-line {
        display: block;
        margin-top: 0.35rem;
        font-family: var(--font-mono);
        font-size: calc(var(--small-size) * 0.86);
        color: var(--ink-faint);
        font-weight: 400;
        line-height: 1.35;
      }
      .ex-line code { color: var(--uplink); }
      .anti-panel {
        width: 100%;
        max-width: min(95vw, 980px);
        margin: 0 auto;
        border: 1px solid var(--hairline);
        border-radius: 6px;
        background: linear-gradient(165deg, rgba(237, 90, 62, 0.05) 0%, rgba(244, 236, 216, 0.02) 38%, rgba(6, 10, 20, 0.15) 100%);
        overflow: hidden;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.22);
      }
      .anti-panel-head {
        padding: clamp(0.55rem, 1.1vh, 0.8rem) clamp(1rem, 2vw, 1.4rem);
        border-bottom: 1px solid var(--hairline);
        background: rgba(237, 90, 62, 0.07);
        font-family: var(--font-mono);
        font-size: var(--small-size);
        color: var(--ink-mute);
        text-align: center;
        letter-spacing: 0.02em;
      }
      .anti-panel-head strong { color: var(--survey); font-weight: 600; }
      .anti-problem-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 0;
      }
      @media (max-width: 820px) {
        .anti-problem-grid { grid-template-columns: 1fr; }
        .anti-problem-grid .layer { border-right: none !important; border-bottom: 1px solid var(--hairline); }
        .anti-problem-grid .layer:last-child { border-bottom: none; }
      }
      .anti-problem-grid .layer {
        border: none;
        border-radius: 0;
        border-right: 1px solid var(--hairline);
        background: transparent;
        padding: clamp(0.75rem, 1.5vw, 1.15rem) clamp(0.85rem, 1.6vw, 1.25rem);
      }
      .anti-problem-grid .layer::after { display: none; }
      .anti-problem-grid .layer:last-child { border-right: none; }
      .anti-problem-grid .layer .num { color: var(--survey); letter-spacing: 0.12em; }
      .anti-problem-grid .layer .name { font-size: clamp(0.95rem, 1.75vw, 1.25rem); }
      .anti-solution {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: clamp(0.4rem, 0.9vh, 0.65rem);
        padding: clamp(0.8rem, 1.6vh, 1.15rem) clamp(1rem, 2vw, 1.5rem);
        border-top: 1px solid var(--hairline);
        background: rgba(167, 139, 250, 0.04);
      }
      .anti-solution-flow {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        gap: clamp(0.35rem, 0.9vw, 0.7rem);
      }
      .anti-solution-step {
        padding: 0.4rem 0.75rem;
        border: 1px solid rgba(167, 139, 250, 0.35);
        border-radius: 4px;
        background: rgba(167, 139, 250, 0.1);
        color: var(--topo);
        font-family: var(--font-mono);
        font-size: clamp(0.72rem, 1.2vw, 0.85rem);
        font-weight: 600;
        letter-spacing: 0.04em;
        text-transform: lowercase;
      }
      .anti-solution-step.uplink {
        border-color: rgba(77, 212, 214, 0.4);
        background: rgba(77, 212, 214, 0.1);
        color: var(--uplink);
      }
      .anti-solution-arrow {
        color: var(--ink-faint);
        font-family: var(--font-mono);
        font-size: var(--small-size);
        opacity: 0.55;
      }
      .anti-solution-note {
        margin: 0;
        text-align: center;
        font-size: var(--micro-size);
        color: var(--ink-faint);
        line-height: 1.45;
        max-width: 48ch;
      }
      .slide-content.tdd-slide { gap: clamp(0.45rem, 1.1vh, 1rem); }
      .slide-content.tdd-slide .feature-list { gap: clamp(0.28rem, 0.75vh, 0.6rem); }
      .foot-bar .social-link--text {
        display: inline;
        font-family: inherit;
        font-size: inherit;
        letter-spacing: inherit;
      }

      /* —— Harness: viewport fit (meta/foot clearance + dense slides) —— */
      .slide-content {
        box-sizing: border-box;
      }
      .slide-content:not(.stack) {
        padding-top: clamp(2.85rem, 6vh, 4rem) !important;
        padding-bottom: clamp(2.85rem, 6vh, 4rem) !important;
      }
      .slide-content.stack {
        --safe-y: clamp(2.85rem, 6vh, 4rem);
        padding: var(--safe-y) clamp(1rem, 3.5vw, 2.75rem) !important;
        justify-content: center;
        align-items: stretch;
        gap: clamp(0.32rem, 0.85vh, 0.7rem);
        min-height: 0;
      }
      .slide:has(.foot-bar .socials) .slide-content.stack {
        padding-bottom: clamp(3.35rem, 7.5vh, 4.75rem) !important;
      }
      .slide-content.dense-slide {
        gap: clamp(0.26rem, 0.7vh, 0.58rem);
      }
      .slide-content.stack .tagline {
        line-height: 1.35;
      }
      .slide-content.dense-slide .term-note {
        font-size: var(--micro-size);
        line-height: 1.35;
      }
      .term-table.compact-rows {
        font-size: var(--micro-size);
      }
      .term-table.compact-rows thead th {
        padding: clamp(0.2rem, 0.45vh, 0.35rem) clamp(0.45rem, 0.9vw, 0.7rem);
      }
      .term-table.compact-rows tbody td {
        padding: clamp(0.18rem, 0.4vh, 0.32rem) clamp(0.45rem, 0.9vw, 0.7rem);
        line-height: 1.3;
        vertical-align: top;
      }
      .term-table.compact-rows td.you {
        white-space: nowrap;
        width: clamp(52px, 9vw, 72px);
      }
      .term-table.compact-rows td.arrow {
        width: clamp(18px, 3vw, 28px);
        padding-left: 0;
        padding-right: 0;
      }
      .term-table.compact-rows td.geo {
        font-weight: 400;
      }
      .slide-content.dense-slide .pills {
        gap: clamp(0.22rem, 0.45vh, 0.4rem);
        justify-content: center;
      }
      .slide-content.dense-slide .pills .pill {
        font-size: var(--micro-size);
        padding: 0.18rem 0.5rem;
        white-space: normal;
        text-align: center;
      }
      .slide-content.glossary-slide {
        gap: clamp(0.3rem, 0.8vh, 0.55rem);
      }
      .slide-content.glossary-slide .glossary-grid {
        gap: clamp(0.28rem, 0.55vw, 0.45rem);
      }
      .slide-content.glossary-slide .glossary-item {
        padding: clamp(0.38rem, 0.75vw, 0.6rem) clamp(0.55rem, 1vw, 0.8rem);
      }
      .slide-content.glossary-slide .glossary-item dd {
        font-size: var(--micro-size);
        line-height: 1.28;
      }
      .slide-content.cli-slide.dense-slide .metric-list {
        gap: clamp(0.28rem, 0.6vh, 0.45rem);
      }
      .slide-content.cli-slide.dense-slide .metric-list li {
        font-size: var(--micro-size);
      }
      /* Centralização vertical em todos os slides (capa + stack) */
      .slide .slide-content {
        justify-content: center !important;
      }
      /* Títulos h2 uniformes em todos os sheets */
      .slide .slide-content h2.section {
        font-size: var(--h2-size) !important;
        line-height: 1.02;
      }
      @media (max-height: 780px) {
        .slide-content.glossary-slide .glossary-grid {
          grid-template-columns: repeat(3, 1fr);
        }
      }
      @media (max-height: 680px) {
        .slide-content.glossary-slide .glossary-grid {
          grid-template-columns: repeat(2, 1fr);
        }
      }
      @media (max-height: 650px) {
        .slide-content.glossary-slide .eyebrow,
        .slide-content.glossary-slide .term-note {
          display: none;
        }
        .slide-content.glossary-slide .glossary-grid {
          grid-template-columns: repeat(4, 1fr);
          gap: 0.22rem;
        }
        .slide-content.glossary-slide .glossary-item {
          padding: 0.28rem 0.4rem;
        }
        .slide-content.glossary-slide .glossary-item dt {
          font-size: calc(var(--micro-size) * 0.88);
          margin-bottom: 0.08rem;
        }
        .slide-content.glossary-slide .glossary-item dd {
          font-size: calc(var(--micro-size) * 0.82);
          line-height: 1.18;
        }
      }

      /* Nav de seções abaixo da meta-bar (evita sobreposição) */
      .section-progress {
        top: clamp(2.35rem, 4.8vh, 3.15rem);
      }
      @media (max-width: 900px) {
        .section-seg-label { display: none; }
      }

      /* Slides densos: arch-stack, layer-grid, anti-panel */
      .slide-content.arch-slide .arch-stack,
      .slide-content.dense-slide .arch-stack {
        gap: clamp(0.18rem, 0.45vh, 0.38rem);
      }
      .slide-content.arch-slide .arch-layer,
      .slide-content.dense-slide .arch-layer {
        padding: clamp(0.32rem, 0.65vh, 0.55rem) clamp(0.55rem, 1.1vw, 0.85rem);
        gap: clamp(0.35rem, 0.75vw, 0.65rem);
        grid-template-columns: clamp(84px, 13vw, 132px) 1fr;
      }
      .slide-content.arch-slide .arch-layer .layer-tools,
      .slide-content.dense-slide .arch-layer .layer-tools {
        font-size: clamp(0.72rem, 1.35vw, 0.98rem);
        line-height: 1.18;
      }
      .slide-content.trends-slide .layer-grid {
        grid-template-columns: repeat(3, 1fr);
        gap: clamp(0.22rem, 0.5vw, 0.4rem);
      }
      .slide-content.dense-slide .layer-grid {
        gap: clamp(0.24rem, 0.52vw, 0.42rem);
      }
      .slide-content.dense-slide .layer-grid .layer {
        padding: clamp(0.32rem, 0.65vh, 0.52rem);
      }
      .slide-content.dense-slide .layer-grid .layer .desc {
        font-size: var(--micro-size);
        line-height: 1.22;
      }
      .slide-content.anti-slide.dense-slide .closing-quote {
        font-size: clamp(0.92rem, 2vw, 1.28rem) !important;
        line-height: 1.35;
      }
      .slide-content.anti-slide.dense-slide .anti-problem-grid .layer .desc {
        font-size: var(--micro-size);
        line-height: 1.2;
      }
      .slide-content.ontology-slide .code-block.compact {
        font-size: calc(var(--micro-size) * 0.92);
        line-height: 1.22;
        padding: clamp(0.35rem, 0.7vh, 0.55rem) clamp(0.5rem, 1vw, 0.75rem);
      }
      .slide-content.harness-slide .term-table {
        font-size: var(--micro-size);
      }
      .slide-content.harness-slide .term-table tbody td {
        padding: clamp(0.15rem, 0.35vh, 0.28rem) clamp(0.4rem, 0.85vw, 0.65rem);
        line-height: 1.28;
      }
      @media (max-height: 820px) {
        .slide-content.ontology-slide .body-text { display: none; }
        .slide-content.ontology-slide .term-table { display: none; }
        .slide-content.harness-slide .body-text { font-size: clamp(1rem, 2.4vw, 1.6rem) !important; }
        .slide-content.harness-slide .term-note { display: none; }
      }
      @media (max-height: 700px) {
        .slide-content.anti-slide .anti-solution-note { display: none; }
        .slide-content.arch-slide .body-text { display: none; }
        .slide-content.arch-slide.dense-slide .closing-quote { font-size: clamp(0.85rem, 1.8vw, 1.05rem) !important; }
      }
"""
if ".glossary-grid" not in css or ".slide-content.dense-slide" not in css:
    css += extra_css

graph_bg = """
    <div id="world-map" aria-hidden="true">
      <svg viewBox="0 0 720 360" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
        <defs>
          <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
            <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#f4ecd8" stroke-width="0.3" opacity="0.3"/>
          </pattern>
        </defs>
        <rect width="720" height="360" fill="url(#grid)"/>
        <g stroke="#f4ecd8" fill="none" stroke-width="0.6" opacity="0.25">
          <circle cx="360" cy="180" r="120"/><circle cx="360" cy="180" r="80"/><circle cx="360" cy="180" r="40"/>
          <line x1="240" y1="180" x2="480" y2="180"/><line x1="360" y1="60" x2="360" y2="300"/>
        </g>
        <g fill="#f4ecd8" opacity="0.4">
          <circle cx="200" cy="120" r="4"/><circle cx="320" cy="90" r="3"/><circle cx="450" cy="140" r="5"/>
          <circle cx="520" cy="200" r="3"/><circle cx="280" cy="220" r="4"/><circle cx="400" cy="250" r="3"/>
          <circle cx="180" cy="260" r="3"/><circle cx="580" cy="130" r="4"/>
        </g>
        <g stroke="#a78bfa" stroke-width="0.8" opacity="0.2">
          <line x1="200" y1="120" x2="320" y2="90"/><line x1="320" y1="90" x2="450" y2="140"/>
          <line x1="450" y1="140" x2="520" y2="200"/><line x1="280" y1="220" x2="400" y2="250"/>
          <line x1="200" y1="120" x2="280" y2="220"/><line x1="400" y1="250" x2="520" y2="200"/>
        </g>
      </svg>
    </div>
"""

lightbox = """
    <div class="lightbox" id="lightbox">
      <button class="lightbox-close" aria-label="Fechar">&times;</button>
      <div class="lightbox-content" id="lightboxContent">
        <div class="lightbox-figure" data-lightbox-group="graph-mcp">
          <svg viewBox="0 0 1000 680" width="1000" style="max-width:min(94vw,1000px);max-height:78vh;border:1px solid rgba(244,236,216,0.12);border-radius:8px;background:#060a14" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <marker id="arr" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
                <path d="M0,0 L8,4 L0,8 Z" fill="#f4ecd8" opacity="0.55"/>
              </marker>
              <marker id="arr-cyan" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
                <path d="M0,0 L8,4 L0,8 Z" fill="#4dd4d6" opacity="0.8"/>
              </marker>
              <marker id="arr-violet" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto">
                <path d="M0,0 L8,4 L0,8 Z" fill="#a78bfa" opacity="0.8"/>
              </marker>
            </defs>

            <text x="500" y="32" text-anchor="middle" fill="#a78bfa" font-family="Roboto Mono,monospace" font-size="15" font-weight="500">Knowledge Graph — do repositório à AI (fluxo completo)</text>
            <text x="500" y="52" text-anchor="middle" fill="#f4ecd8" font-size="11" opacity="0.55">Omni Graph MCP · consultas compactas e rastreáveis · ≤4KB por pacote</text>

            <!-- LANE LABELS -->
            <text x="18" y="98" fill="#f4ecd8" font-family="Roboto Mono" font-size="9" opacity="0.45" transform="rotate(-90 18 98)">FONTES</text>
            <text x="18" y="198" fill="#f4ecd8" font-family="Roboto Mono" font-size="9" opacity="0.45" transform="rotate(-90 18 198)">BUILD</text>
            <text x="18" y="298" fill="#f4ecd8" font-family="Roboto Mono" font-size="9" opacity="0.45" transform="rotate(-90 18 298)">GRAFO</text>
            <text x="18" y="408" fill="#f4ecd8" font-family="Roboto Mono" font-size="9" opacity="0.45" transform="rotate(-90 18 408)">MCP</text>
            <text x="18" y="538" fill="#f4ecd8" font-family="Roboto Mono" font-size="9" opacity="0.45" transform="rotate(-90 18 538)">AGENT</text>

            <!-- ROW 1 · FONTES -->
            <rect x="44" y="68" width="900" height="72" rx="6" fill="rgba(244,236,216,0.02)" stroke="rgba(244,236,216,0.12)"/>
            <rect x="60" y="82" width="200" height="44" rx="4" fill="rgba(244,236,216,0.04)" stroke="rgba(244,236,216,0.25)"/>
            <text x="160" y="100" text-anchor="middle" fill="#f4ecd8" font-family="Roboto Mono" font-size="11">repositório</text>
            <text x="160" y="116" text-anchor="middle" fill="#f4ecd8" font-size="9" opacity="0.5">src/ · docs/ · testes</text>
            <rect x="280" y="82" width="200" height="44" rx="4" fill="rgba(167,139,250,0.06)" stroke="#a78bfa" stroke-opacity="0.5"/>
            <text x="380" y="100" text-anchor="middle" fill="#a78bfa" font-family="Roboto Mono" font-size="11">ontology.yaml</text>
            <text x="380" y="116" text-anchor="middle" fill="#f4ecd8" font-size="9" opacity="0.5">conceitos · sinônimos</text>
            <rect x="500" y="82" width="220" height="44" rx="4" fill="rgba(77,212,214,0.06)" stroke="#4dd4d6" stroke-opacity="0.5"/>
            <text x="610" y="100" text-anchor="middle" fill="#4dd4d6" font-family="Roboto Mono" font-size="11">.omni/features|bugs/</text>
            <text x="610" y="116" text-anchor="middle" fill="#f4ecd8" font-size="9" opacity="0.5">spec · tasks · gates SDD</text>
            <rect x="740" y="82" width="188" height="44" rx="4" fill="rgba(237,90,62,0.06)" stroke="#ed5a3e" stroke-opacity="0.45"/>
            <text x="834" y="100" text-anchor="middle" fill="#ed5a3e" font-family="Roboto Mono" font-size="11">sem graph</text>
            <text x="834" y="116" text-anchor="middle" fill="#f4ecd8" font-size="9" opacity="0.5">40+ arquivos ao acaso ✗</text>

            <line x1="500" y1="140" x2="500" y2="158" stroke="#f4ecd8" stroke-width="1.2" opacity="0.35" marker-end="url(#arr)"/>

            <!-- ROW 2 · BUILD -->
            <rect x="44" y="158" width="900" height="88" rx="6" fill="rgba(244,236,216,0.02)" stroke="rgba(244,236,216,0.12)"/>
            <rect x="60" y="172" width="155" height="60" rx="4" fill="rgba(77,212,214,0.05)" stroke="#4dd4d6" stroke-opacity="0.6"/>
            <text x="137" y="194" text-anchor="middle" fill="#4dd4d6" font-family="Roboto Mono" font-size="10">Tree-sitter</text>
            <text x="137" y="210" text-anchor="middle" fill="#f4ecd8" font-size="9" opacity="0.55">AST · símbolos</text>
            <text x="137" y="224" text-anchor="middle" fill="#f4ecd8" font-size="9" opacity="0.55">imports · calls</text>
            <line x1="215" y1="202" x2="248" y2="202" stroke="#f4ecd8" opacity="0.4" marker-end="url(#arr)"/>
            <rect x="248" y="172" width="175" height="60" rx="4" fill="rgba(244,236,216,0.04)" stroke="rgba(244,236,216,0.3)"/>
            <text x="335" y="194" text-anchor="middle" fill="#f4ecd8" font-family="Roboto Mono" font-size="10">code-index.json</text>
            <text x="335" y="212" text-anchor="middle" fill="#f4ecd8" font-size="9" opacity="0.5">índice estruturado</text>
            <line x1="423" y1="202" x2="456" y2="202" stroke="#f4ecd8" opacity="0.4" marker-end="url(#arr)"/>
            <rect x="456" y="172" width="195" height="60" rx="4" fill="rgba(167,139,250,0.06)" stroke="#a78bfa" stroke-opacity="0.6"/>
            <text x="553" y="194" text-anchor="middle" fill="#a78bfa" font-family="Roboto Mono" font-size="10">omni graph build</text>
            <text x="553" y="212" text-anchor="middle" fill="#f4ecd8" font-size="9" opacity="0.5">liga código + ontology</text>
            <line x1="651" y1="202" x2="684" y2="202" stroke="#f4ecd8" opacity="0.4" marker-end="url(#arr)"/>
            <rect x="684" y="172" width="244" height="60" rx="4" fill="rgba(244,236,216,0.04)" stroke="rgba(244,236,216,0.35)"/>
            <text x="806" y="194" text-anchor="middle" fill="#f4ecd8" font-family="Roboto Mono" font-size="10">knowledge-graph.sqlite</text>
            <text x="806" y="212" text-anchor="middle" fill="#f4ecd8" font-size="9" opacity="0.5">nós · arestas · pesos</text>

            <line x1="500" y1="246" x2="500" y2="264" stroke="#f4ecd8" stroke-width="1.2" opacity="0.35" marker-end="url(#arr)"/>

            <!-- ROW 3 · GRAFO (nós) -->
            <rect x="44" y="264" width="900" height="88" rx="6" fill="rgba(244,236,216,0.02)" stroke="rgba(244,236,216,0.12)"/>
            <text x="500" y="282" text-anchor="middle" fill="#f4ecd8" font-size="10" opacity="0.6">nós no grafo — cada um com ID, tipo e relações</text>
            <circle cx="130" cy="318" r="22" fill="rgba(77,212,214,0.1)" stroke="#4dd4d6"/>
            <text x="130" y="322" text-anchor="middle" fill="#4dd4d6" font-family="Roboto Mono" font-size="9">file</text>
            <circle cx="250" cy="318" r="22" fill="rgba(77,212,214,0.1)" stroke="#4dd4d6"/>
            <text x="250" y="322" text-anchor="middle" fill="#4dd4d6" font-family="Roboto Mono" font-size="9">symbol</text>
            <circle cx="370" cy="318" r="22" fill="rgba(167,139,250,0.1)" stroke="#a78bfa"/>
            <text x="370" y="322" text-anchor="middle" fill="#a78bfa" font-family="Roboto Mono" font-size="9">module</text>
            <circle cx="490" cy="318" r="22" fill="rgba(167,139,250,0.1)" stroke="#a78bfa"/>
            <text x="490" y="322" text-anchor="middle" fill="#a78bfa" font-family="Roboto Mono" font-size="9">concept</text>
            <circle cx="610" cy="318" r="22" fill="rgba(244,236,216,0.06)" stroke="rgba(244,236,216,0.4)"/>
            <text x="610" y="322" text-anchor="middle" fill="#f4ecd8" font-family="Roboto Mono" font-size="9">doc</text>
            <circle cx="730" cy="318" r="22" fill="rgba(244,236,216,0.06)" stroke="rgba(244,236,216,0.4)"/>
            <text x="730" y="322" text-anchor="middle" fill="#f4ecd8" font-family="Roboto Mono" font-size="9">feature</text>
            <circle cx="850" cy="318" r="22" fill="rgba(237,90,62,0.08)" stroke="#ed5a3e" stroke-opacity="0.6"/>
            <text x="850" y="322" text-anchor="middle" fill="#ed5a3e" font-family="Roboto Mono" font-size="9">domain</text>
            <line x1="152" y1="318" x2="228" y2="318" stroke="#4dd4d6" opacity="0.35"/>
            <line x1="272" y1="318" x2="348" y2="318" stroke="#a78bfa" opacity="0.35"/>
            <line x1="392" y1="318" x2="468" y2="318" stroke="#a78bfa" opacity="0.35"/>
            <line x1="512" y1="318" x2="588" y2="318" stroke="#f4ecd8" opacity="0.25"/>
            <line x1="632" y1="318" x2="708" y2="318" stroke="#f4ecd8" opacity="0.25"/>
            <text x="500" y="348" text-anchor="middle" fill="#f4ecd8" font-size="9" opacity="0.45">ex.: concept:bureau_score → symbol:calc_score() → file:src/risk/score.py</text>

            <line x1="500" y1="352" x2="500" y2="370" stroke="#f4ecd8" stroke-width="1.2" opacity="0.35" marker-end="url(#arr)"/>

            <!-- ROW 4 · MCP SERVER + TOOLS -->
            <rect x="44" y="370" width="900" height="118" rx="6" fill="rgba(237,90,62,0.04)" stroke="#ed5a3e" stroke-opacity="0.35"/>
            <rect x="60" y="384" width="168" height="90" rx="4" fill="rgba(237,90,62,0.08)" stroke="#ed5a3e" stroke-opacity="0.55"/>
            <text x="144" y="406" text-anchor="middle" fill="#ed5a3e" font-family="Roboto Mono" font-size="11">Omni Graph</text>
            <text x="144" y="422" text-anchor="middle" fill="#ed5a3e" font-family="Roboto Mono" font-size="11">MCP server</text>
            <text x="144" y="442" text-anchor="middle" fill="#f4ecd8" font-size="9" opacity="0.55">stdio · Cursor</text>
            <text x="144" y="458" text-anchor="middle" fill="#f4ecd8" font-size="9" opacity="0.55">omni preflight</text>
            <line x1="228" y1="429" x2="258" y2="429" stroke="#ed5a3e" opacity="0.5" marker-end="url(#arr)"/>
            <rect x="258" y="386" width="672" height="86" rx="4" fill="rgba(244,236,216,0.03)" stroke="rgba(244,236,216,0.2)"/>
            <text x="276" y="406" fill="#f4ecd8" font-family="Roboto Mono" font-size="9" opacity="0.65">ferramentas expostas à AI:</text>
            <text x="276" y="426" fill="#4dd4d6" font-family="Roboto Mono" font-size="9">graph_search</text>
            <text x="390" y="426" fill="#4dd4d6" font-family="Roboto Mono" font-size="9">graph_neighbors</text>
            <text x="530" y="426" fill="#4dd4d6" font-family="Roboto Mono" font-size="9">graph_strong_neighbors</text>
            <text x="710" y="426" fill="#4dd4d6" font-family="Roboto Mono" font-size="9">graph_traverse</text>
            <text x="276" y="448" fill="#a78bfa" font-family="Roboto Mono" font-size="9">graph_ontology_bundle</text>
            <text x="450" y="448" fill="#a78bfa" font-family="Roboto Mono" font-size="9">graph_context_bundle</text>
            <text x="610" y="448" fill="#a78bfa" font-family="Roboto Mono" font-size="9">graph_symbol_summaries</text>
            <text x="276" y="468" fill="#4dd4d6" font-family="Roboto Mono" font-size="9">graph_semantic_search</text>
            <text x="450" y="468" fill="#f4ecd8" font-size="9" opacity="0.45">busca · vizinhos · semântica · pacotes ≤4KB</text>

            <line x1="500" y1="488" x2="500" y2="506" stroke="#f4ecd8" stroke-width="1.2" opacity="0.35" marker-end="url(#arr)"/>

            <!-- ROW 5 · PACOTES (exemplo) -->
            <rect x="44" y="506" width="900" height="108" rx="6" fill="rgba(244,236,216,0.02)" stroke="rgba(244,236,216,0.12)"/>
            <text x="500" y="524" text-anchor="middle" fill="#f4ecd8" font-size="10" opacity="0.6">exemplo · feature <tspan fill="#a78bfa" font-family="Roboto Mono">login-oauth</tspan> — 2 chamadas em vez de ler o repo inteiro</text>
            <rect x="60" y="536" width="420" height="68" rx="4" fill="rgba(167,139,250,0.08)" stroke="#a78bfa" stroke-opacity="0.55"/>
            <text x="76" y="556" fill="#a78bfa" font-family="Roboto Mono" font-size="10">graph_ontology_bundle(feature_id)</text>
            <text x="76" y="574" fill="#f4ecd8" font-size="9" opacity="0.65">→ concepts · contexts · gaps · warnings</text>
            <text x="76" y="590" fill="#f4ecd8" font-size="9" opacity="0.45">vocabulário oficial antes de codificar</text>
            <rect x="508" y="536" width="420" height="68" rx="4" fill="rgba(77,212,214,0.08)" stroke="#4dd4d6" stroke-opacity="0.55"/>
            <text x="524" y="556" fill="#4dd4d6" font-family="Roboto Mono" font-size="10">graph_context_bundle(path)</text>
            <text x="524" y="574" fill="#f4ecd8" font-size="9" opacity="0.65">→ módulo · símbolos · vizinhos · SDD state</text>
            <text x="524" y="590" fill="#f4ecd8" font-size="9" opacity="0.45">ex.: path=src/auth/handler.py</text>

            <line x1="270" y1="614" x2="270" y2="632" stroke="#a78bfa" opacity="0.5" marker-end="url(#arr-violet)"/>
            <line x1="718" y1="614" x2="718" y2="632" stroke="#4dd4d6" opacity="0.5" marker-end="url(#arr-cyan)"/>

            <!-- ROW 6 · AGENTES SDD -->
            <rect x="44" y="632" width="900" height="44" rx="6" fill="rgba(244,236,216,0.03)" stroke="rgba(244,236,216,0.18)"/>
            <rect x="60" y="642" width="155" height="24" rx="3" fill="rgba(167,139,250,0.12)" stroke="#a78bfa" stroke-opacity="0.4"/>
            <text x="137" y="658" text-anchor="middle" fill="#a78bfa" font-family="Roboto Mono" font-size="9">discovery</text>
            <line x1="215" y1="654" x2="235" y2="654" stroke="#f4ecd8" opacity="0.3"/>
            <rect x="235" y="642" width="155" height="24" rx="3" fill="rgba(167,139,250,0.08)" stroke="#a78bfa" stroke-opacity="0.35"/>
            <text x="312" y="658" text-anchor="middle" fill="#a78bfa" font-family="Roboto Mono" font-size="9">planning</text>
            <line x1="390" y1="654" x2="410" y2="654" stroke="#f4ecd8" opacity="0.3"/>
            <rect x="410" y="642" width="155" height="24" rx="3" fill="rgba(77,212,214,0.1)" stroke="#4dd4d6" stroke-opacity="0.4"/>
            <text x="487" y="658" text-anchor="middle" fill="#4dd4d6" font-family="Roboto Mono" font-size="9">TDD</text>
            <line x1="565" y1="654" x2="585" y2="654" stroke="#f4ecd8" opacity="0.3"/>
            <rect x="585" y="642" width="155" height="24" rx="3" fill="rgba(244,236,216,0.05)" stroke="rgba(244,236,216,0.3)"/>
            <text x="662" y="658" text-anchor="middle" fill="#f4ecd8" font-family="Roboto Mono" font-size="9">workflow-review</text>
            <text x="820" y="658" text-anchor="middle" fill="#f4ecd8" font-size="9" opacity="0.5">feature + bug · contexto auditável</text>
          </svg>
          <div class="lightbox-caption">6 camadas · build offline → consulta MCP → pacotes ≤4KB → agents SDD · rastreável no chat</div>
        </div>
      </div>
    </div>
"""

slides_html = SLIDES.read_text()
graph_bg = apply_purple_theme(graph_bg)
lightbox = apply_purple_theme(lightbox)

html = f"""<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Omni — Spec-Driven Development com AI Agents</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;0,500;0,700;0,900;1,400;1,700;1,900&family=Roboto+Mono:wght@300;400;500;700&display=swap" rel="stylesheet" />
    <style>
{css}
    </style>
  </head>
  <body>
{graph_bg}
    <canvas id="particle-canvas" aria-hidden="true"></canvas>
    <div class="cursor-ring" id="cursorRing"></div>
    <div class="magnifier-lens" id="magnifierLens"></div>
    <div class="progress-bar" id="progressBar"></div>
    <nav class="section-progress" id="sectionProgress" aria-label="Seções da apresentação"></nav>
    <nav class="nav-dots" id="navDots" aria-label="Navegação de slides"></nav>

{slides_html}

{lightbox}

    <script>
{js}
    </script>
  </body>
</html>
"""

OUT.write_text(html)
slide_count = html.count('class="slide"')
print(f"Written {OUT} ({len(html):,} bytes, {slide_count} slides)")
