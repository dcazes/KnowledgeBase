# Parser Service — minimal HTTP wrapper (TEMPLATE)
# Exposes POST /parse {engine, path, format} -> parsed markdown/json in /data/out
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess, os, json, shutil

app = FastAPI()
IN = "/data/in"
OUT = "/data/out"

class Req(BaseModel):
    engine: str = "docling"   # docling | mineru
    path: str                 # filename inside /data/in
    fmt: str = "markdown"     # markdown | json

@app.post("/parse")
def parse(r: Req):
    src = os.path.join(IN, r.path)
    if not os.path.exists(src):
        raise HTTPException(404, "file not found in /data/in")
    os.makedirs(OUT, exist_ok=True)
    if r.engine == "docling":
        # docling CLI -> markdown or json
        out_fmt = "json" if r.fmt == "json" else "md"
        cmd = ["docling", src, "--output", OUT, "--to", out_fmt]
    elif r.engine == "mineru":
        cmd = ["mineru", "-p", src, "-o", OUT, "-b", "pipeline"]
    else:
        raise HTTPException(400, "unknown engine")
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=300)
    except subprocess.CalledProcessError as e:
        raise HTTPException(500, e.stderr[:500])
    return {"status": "ok", "engine": r.engine, "out": OUT}
