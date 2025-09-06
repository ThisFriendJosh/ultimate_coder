import json, yaml
from pathlib import Path
import gradio as gr

ROOT = Path(__file__).resolve().parents[1]
SPEC = yaml.safe_load((ROOT/"Codertext.yaml.txt").read_text("utf-8"))["ultimate_coder"]
KB   = yaml.safe_load((ROOT/"ultimate_coder/resources/knowledgebase.yaml").read_text("utf-8"))["knowledgebase"]

def list_modules(track_id):
    for t in SPEC.get("tracks", []):
        if t.get("id")==track_id:
            return [m.get("name","module") for m in t.get("modules",[])]
    return []

def search_kb(q):
    rows=[]
    for sec, items in KB.items():
        if isinstance(items, dict):
            for sub, subitems in items.items():
                for it in (subitems or []):
                    if q.lower() in str(it).lower():
                        rows.append((sec, sub, str(it)))
        else:
            for it in (items or []):
                if q.lower() in str(it).lower():
                    rows.append((sec, "", str(it)))
    return rows

with gr.Blocks() as demo:
    gr.Markdown("# Ultimate Coder – KB Browser")
    tracks = [(t.get("title",t["id"]), t["id"]) for t in SPEC.get("tracks",[])]
    tid = gr.Dropdown(choices=[v for _,v in tracks], label="Track")
    out = gr.JSON(label="Modules")
    btn = gr.Button("List Modules")
    btn.click(lambda x: list_modules(x), tid, out)

    gr.Markdown("## Knowledgebase Search")
    q = gr.Textbox(label="Query")
    res = gr.Dataframe(headers=["section","sub","item"], datatype=["str","str","str"])
    q.change(lambda s: search_kb(s), q, res)

demo.launch()
