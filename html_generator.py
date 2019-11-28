# -*- _coding: utf-8 -*-
"""
Created on Thu Nov 28 13:57:54 2019

@author: ULB-IT2
"""

authors = ["Darwin", "Lovelace", "Hawkin", "Noether"]

output_fh = open("list.html", "w")

scaffold_start = """<!DOCTYPE html>
<html>
<head>
<title>Titel dieser wunderbaren Seite</title>
</head>
<body>

<h1>Eine grandiose Überschrift</h1>

<p>Ein nicht weniger toller Abschnitt.</p>

<ul>
"""

output_fh.write(scaffold_start)

scaffold_middle = ""

for author in authors:
    scaffold_middle = scaffold_middle + "<li>" + author + "</li>\n"
    #print(scaffold_middle)
    #print("--------------")

output_fh.write(scaffold_middle)

# <li>Erstes Element</l>
# <li>Zweites Element</l>

scaffold_end = """
</ul>

</body>

</html>"""


output_fh.write(scaffold_end)
output_fh.close()



""" output_fh = open("list.html", "w") #Es wird eine Datei namens list.html eröffnet.
output_fh.write(scaffold) #In die Datei kommen die Daten aus scaffold.
output_fh.close() #Die Datei schließen."""


