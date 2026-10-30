#!/usr/bin/env python3
"""Build IDE (Data Engineering) presentation from the IDE deck template.

Reaproveita CSS, JS e lightbox de ide/index.html e troca apenas os slides
pelo conteúdo de _slides_fragment.html. Assets são lidos de ../ide/assets.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
REF = ROOT / "ide" / "index.html"
OUT = ROOT / "ide-data" / "index.html"
SLIDES = Path(__file__).parent / "_slides_fragment.html"

TITLE = "Infraestruturas de Dados Espaciais — Perspectiva Engenharia de Dados"

# Accent: âmbar topográfico → azul (tema do deck de engenharia de dados)
BLUE = "#60a5fa"
BLUE_RGB = "96, 165, 250"


def apply_blue_theme(text: str) -> str:
    text = text.replace("#f5b73d", BLUE)
    text = text.replace("rgba(245, 183, 61,", f"rgba({BLUE_RGB},")
    return text.replace("rgba(245,183,61", f"rgba({BLUE_RGB.replace(' ', '')}")


ref = apply_blue_theme(REF.read_text())
slides = SLIDES.read_text()

# Região de slides: do comentário que antecede o primeiro <section class="slide">
# até o comentário que antecede o lightbox.
first_slide = ref.index('<section class="slide"')
start = ref.rindex("<!-- =====", 0, first_slide)
lightbox = ref.index('<div class="lightbox" id="lightbox">')
end = ref.rindex("<!-- =====", 0, lightbox)

total = slides.count('<section class="slide"')
slides = slides.replace("{{TOTAL}}", f"{total:02d}")

# Ícones sociais (LinkedIn, GitHub, Lattes) vêm da capa do deck IDE.
s0 = ref.index('<div class="socials">') + len('<div class="socials">')
s1 = ref.index('<span class="author">', s0)
slides = slides.replace("{{SOCIAL_LINKS}}", ref[s0:s1].strip())

html = ref[:start] + slides.strip() + "\n\n    " + ref[end:]

# Exemplos de SQL/Python deste deck são mais largos que os 64ch do template.
EXTRA_CSS = """
      .code-block { max-width: min(104ch, 92vw); }
      .col-card .code-block { max-width: 100%; }
"""
style_end = html.index("</style>")
html = html[:style_end] + EXTRA_CSS + "    " + html[style_end:]

t0 = html.index("<title>") + len("<title>")
t1 = html.index("</title>", t0)
html = html[:t0] + TITLE + html[t1:]

# Assets do lightbox continuam no deck IDE original.
html = html.replace('src="assets/', 'src="../ide/assets/')

OUT.write_text(html)
print(f"wrote {OUT.relative_to(ROOT)} · {total} slides")
