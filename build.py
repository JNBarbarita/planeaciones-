# Arma las páginas del sitio a partir de app.html (la misma app que se publica dentro de Claude):
#   index.html     -> la app de la escuela, con el banco compartido banco.json
#   maestras.html  -> "Mi banco de planeaciones": cada maestra guarda su propio banco en su dispositivo
# Uso: python3 build.py   (desde esta carpeta)
import os

aqui = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(aqui, "app.html"), encoding="utf-8").read()
fin_head = src.index("</style>") + len("</style>")
head, body = src[:fin_head], src[fin_head:]


def pagina(manifest, titulo_app, extra=""):
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f'<link rel="manifest" href="{manifest}">\n<link rel="icon" href="img/icono-192.png">\n'
            '<link rel="apple-touch-icon" href="img/icono-180.png">\n'
            '<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="mobile-web-app-capable" content="yes">\n'
            f'<meta name="apple-mobile-web-app-title" content="{titulo_app}">\n<meta name="theme-color" content="#1f4e79">\n'
            + extra + head + '\n</head>\n<body>' + body + '</body>\n</html>\n')


def escribe(nombre, texto):
    open(os.path.join(aqui, nombre), "w", encoding="utf-8").write(texto)
    print(nombre, len(texto))


# firebase-config.js: datos del proyecto de Firebase (bancos de las maestras en línea). Solo en el sitio, no en Claude.
FB = '<script src="firebase-config.js"></script>\n'
escribe("index.html", pagina("manifest.webmanifest", "Planeaciones", FB))

personal = pagina("manifest-maestras.webmanifest", "Mi banco", FB + "<script>window.BANCO_PERSONAL = true;</script>\n")
for a, b in (("<title>Banco de Planeaciones</title>", "<title>Mi banco de planeaciones</title>"),
             ("<b>Banco de Planeaciones</b>", "<b>Mi banco de planeaciones</b>")):
    assert personal.count(a) == 1, a
    personal = personal.replace(a, b)
escribe("maestras.html", personal)
