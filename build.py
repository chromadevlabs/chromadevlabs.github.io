

import os
import json
import base64
from pathlib import Path

posts = []

def loadPost(path: Path):
    with open(path, "r") as file:
        return file.read()

if __name__ == "__main__":
    for file in os.listdir("posts"):
        path = Path("posts") / Path(file)

        if path.is_file():
            posts.append({
                "name": path.name[0:path.name.find("_")],
                "date": path.name[path.name.find("_") + 1:path.name.rfind(".")],
                "content": loadPost(path).strip()
            })

    encoded = base64.b64encode(bytes(json.dumps(posts), "utf-8")).decode()
    print(f'const data = "{encoded}";\n')
