def getindextext():
    html = buildindextext()
    return html

def buildindextext():
    html = htmlstart + headerstart + """This is a header test""" + headerend + htmlend
    return html

#------------------------------
# start building a table

# start with tags
# start html tags
htmlstart = """<html>"""
htmlend = """</html>"""

# start head tags
headstart = """<head>"""
headend = """</head>"""

# start headings
starth1 = """<h1>"""
endh1 = """</h1>"""

starth2 = """<h2>"""
endh2 = """</h2>"""

starth3 = """<h3>"""
endh3 = """</h3>"""

# start body tags
openbody = """<body>"""
closebody = """</body>"""

# start header
headerstart = """<header>"""
headerend = """</header>"""

# start table tags
opentable = """<table>"""
closetable = """</table>"""

