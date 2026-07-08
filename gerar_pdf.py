# -*- coding: utf-8 -*-
"""Converte apresentacao.md em um HTML estilizado para leitura (teleprompter)."""
import html
import re

with open("apresentacao.md", encoding="utf-8") as f:
    linhas = f.read().splitlines()

def formatar_inline(texto):
    # Escapa HTML primeiro
    texto = html.escape(texto)
    # Destaca marcador de pausa: **(pausa)**
    texto = texto.replace("**(pausa)**", '<span class="pausa">[ pausa ]</span>')
    # Negrito genérico restante **...**
    texto = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", texto)
    return texto

partes = []
paragrafo = []

def fechar_paragrafo():
    if paragrafo:
        conteudo = " ".join(paragrafo).strip()
        if conteudo:
            partes.append(f"<p>{formatar_inline(conteudo)}</p>")
        paragrafo.clear()

for linha in linhas:
    s = linha.strip()
    if s.startswith("## "):
        fechar_paragrafo()
        titulo = s[3:].strip()
        # separa titulo e tempo (entre parenteses no fim)
        m = re.search(r"\((.*?)\)\s*$", titulo)
        tempo = ""
        if m:
            tempo = m.group(1)
            titulo = titulo[:m.start()].strip()
        partes.append('<section class="slide">')
        tempo_html = f'<span class="tempo">{html.escape(tempo)}</span>' if tempo else ""
        partes.append(f'<h2>{html.escape(titulo)}{tempo_html}</h2>')
    elif s.startswith("# "):
        fechar_paragrafo()
        partes.append(f'<h1>{html.escape(s[2:].strip())}</h1>')
    elif s.startswith(">"):
        fechar_paragrafo()
        partes.append(f'<p class="nota">{formatar_inline(s.lstrip(">").strip())}</p>')
    elif s == "---":
        fechar_paragrafo()
        # fecha a section aberta (se houver)
        if any("<section" in p for p in partes):
            partes.append("</section>")
    elif s == "":
        fechar_paragrafo()
    else:
        paragrafo.append(s)

fechar_paragrafo()
# garante fechamento da ultima section
abertos = sum(1 for p in partes if p == '<section class="slide">')
fechados = sum(1 for p in partes if p == "</section>")
if abertos > fechados:
    partes.append("</section>")

corpo = "\n".join(partes)

CSS = """
@page { margin: 0; }
body {
  font-family: Arial, sans-serif;
  font-size: 17px;
  line-height: 1.8;
  color: #000;
  margin: 0;
  padding: 40px 55px;
}
h1 { font-size: 26px; margin: 0 0 4px; }
h2 { font-size: 18px; margin: 22px 0 10px; }
h2 .tempo { font-size: 13px; font-weight: normal; }
p { margin: 0 0 12px; }
p.nota { font-size: 13px; margin: 2px 0; }
.pausa { font-weight: bold; }
"""

doc = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Roteiro de Defesa — TaxaJurosPro</title>
<style>{CSS}</style>
</head>
<body>
{corpo}
<script>
window.addEventListener('load', function () {{
  var el = document.documentElement;
  var w = Math.ceil(el.scrollWidth);
  var h = Math.ceil(el.scrollHeight) + 2;
  var s = document.createElement('style');
  s.textContent = '@page {{ size: ' + w + 'px ' + h + 'px; margin: 0; }}';
  document.head.appendChild(s);
}});
</script>
</body>
</html>"""

with open("roteiro.html", "w", encoding="utf-8") as f:
    f.write(doc)

print("roteiro.html gerado com", len(partes), "blocos.")
