#!python

import os
import sys
import json
import base64
import markdown

from pathlib  import Path
from datetime import datetime

def loadPost(path: Path):
    if "md" in path.suffix.lower():
        with open(path, "r") as file:
            return markdown.markdown(file.read())
    elif "html" in path.suffix.lower():
        with open(path, "r") as file:
            return file.read()

    assert(False)

if __name__ == "__main__":
    posts = []

    if "--new" in sys.argv:
        name = sys.argv[2]
        path = Path(f"posts/{name}_" + datetime.now().strftime("%d-%m-%Y")).with_suffix(".md")
        with open(path.absolute(), "w") as file:
            file.write('NewPost\n')

    for file in os.listdir("posts"):
        path = Path("posts") / Path(file)

        if path.is_file():
            posts.append({
                "name": path.name[0:path.name.find("_")],
                "date": path.name[path.name.find("_") + 1:path.name.rfind(".")],
                "content": loadPost(path).strip()
            })

    encoded = base64.b64encode(bytes(json.dumps(posts), "utf-8")).decode()
    with open("data.js", "w") as file:
        file.write(f'const data = "{encoded}";\n')
