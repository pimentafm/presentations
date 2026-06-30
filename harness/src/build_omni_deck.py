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
"""
if ".closing-quote" not in css:
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
          <svg viewBox="0 0 800 420" width="800" style="max-width:90vw;border:1px solid rgba(244,236,216,0.1);border-radius:6px;background:#060a14">
            <text x="400" y="36" text-anchor="middle" fill="#a78bfa" font-family="Roboto Mono,monospace" font-size="14">Omni Graph MCP — fluxo de contexto</text>
            <rect x="40" y="70" width="160" height="56" rx="4" fill="rgba(244,236,216,0.05)" stroke="#4dd4d6"/>
            <text x="120" y="104" text-anchor="middle" fill="#f4ecd8" font-family="Roboto Mono" font-size="12">code-index</text>
            <rect x="320" y="70" width="160" height="56" rx="4" fill="rgba(244,236,216,0.05)" stroke="#a78bfa"/>
            <text x="400" y="104" text-anchor="middle" fill="#f4ecd8" font-family="Roboto Mono" font-size="12">knowledge-graph</text>
            <rect x="600" y="70" width="160" height="56" rx="4" fill="rgba(244,236,216,0.05)" stroke="#ed5a3e"/>
            <text x="680" y="104" text-anchor="middle" fill="#f4ecd8" font-family="Roboto Mono" font-size="12">MCP server</text>
            <line x1="200" y1="98" x2="320" y2="98" stroke="#f4ecd8" opacity="0.4"/>
            <line x1="480" y1="98" x2="600" y2="98" stroke="#f4ecd8" opacity="0.4"/>
            <rect x="120" y="200" width="200" height="70" rx="4" fill="rgba(167,139,250,0.08)" stroke="#a78bfa"/>
            <text x="220" y="232" text-anchor="middle" fill="#a78bfa" font-family="Roboto Mono" font-size="11">ontology_bundle</text>
            <text x="220" y="252" text-anchor="middle" fill="#f4ecd8" font-size="10" opacity="0.6">≤4KB · concepts · gaps</text>
            <rect x="480" y="200" width="200" height="70" rx="4" fill="rgba(77,212,214,0.08)" stroke="#4dd4d6"/>
            <text x="580" y="232" text-anchor="middle" fill="#4dd4d6" font-family="Roboto Mono" font-size="11">context_bundle</text>
            <text x="580" y="252" text-anchor="middle" fill="#f4ecd8" font-size="10" opacity="0.6">módulo · símbolos · SDD</text>
            <line x1="680" y1="126" x2="580" y2="200" stroke="#4dd4d6" opacity="0.35"/>
            <line x1="680" y1="126" x2="220" y2="200" stroke="#a78bfa" opacity="0.35"/>
            <rect x="280" y="330" width="240" height="56" rx="4" fill="rgba(244,236,216,0.04)" stroke="rgba(244,236,216,0.2)"/>
            <text x="400" y="364" text-anchor="middle" fill="#f4ecd8" font-family="Roboto Mono" font-size="12">SDD Agents (discovery · planning · TDD)</text>
            <line x1="220" y1="270" x2="340" y2="330" stroke="#a78bfa" opacity="0.3"/>
            <line x1="580" y1="270" x2="460" y2="330" stroke="#4dd4d6" opacity="0.3"/>
          </svg>
          <div class="lightbox-caption">Omni Graph MCP — ontology_bundle e context_bundle para agentes SDD</div>
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
    <title>Omni — Spec-Driven Development com Agentes de IA</title>
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
