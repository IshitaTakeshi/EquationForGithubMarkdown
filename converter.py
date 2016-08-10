import sys
import os
import re
import urllib
import urllib.parse


urlpattern = "![](https://latex.codecogs.com/gif.latex?{})"
pattern = re.compile("\$[^\$]*\$")


def replace_line(line):
    for p in pattern.findall(line):
        e = urllib.parse.quote(p[1:-1])
        url = urlpattern.format(e)
        line = line.replace(p, url)
    return line


if len(sys.argv) < 2:
    print("Usage: python3 converter.py <markdown file>")
    exit(0)

filename = sys.argv[1]

if filename.endswith(".md"):
    converted = filename.replace(".md", ".converted.md")
elif filename.endswith(".markdown"):
    converted = filename.replace(".markdown", ".converted.markdown")
else:
    converted = filename + ".converted"


text = open(filename, "r").read()
lines = text.split("\n")
edited = "\n".join(map(replace_line, lines))
open(converted, "w").write(edited)
