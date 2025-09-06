import json, os, re, webbrowser
from pathlib import Path

import streamlit as st
import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC_PATH = ROOT / "Codertext.yaml.txt"
KB_PATH   = ROOT / "ultimate_coder" / "resources" / "knowledgebase.yaml"
STATE_DIR = ROOT / "ui"
STATE_PATH = STATE_DIR / "progress.json"

# ---------- helpers ----------
def load_yaml(p: Path, default=None):
    try:
        with p.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception:
        return default

def save_json(p: Path, data: dict):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def load_state():
    if STATE_PATH.exists():
        try:
            return json.loads(STATE_PATH.read_text("utf-8"))
        except Exception:
            pass
    return {"completed": {}, "notes": {}}

def set_completed(state: dict, module_key: str, done: bool):
    state["completed"][module_key] = bool(done)
    save_json(STATE_PATH, state)

def set_note(state: dict, module_key: str, note: str):
    state["notes"][module_key] = note
    save_json(STATE_PATH, state)

def flat_str(x):
    if isinstance(x, (list, tuple, set)):
        return " ".join(flat_str(i) for i in x)
    if isinstance(x, dict):
        return " ".join(f"{k} {flat_str(v)}" for k, v in x.items())
    return str(x)

# ---------- load data ----------
spec = load_yaml(SPEC_PATH, default={}) or {}
kb   = load_yaml(KB_PATH, default={"knowledgebase": {}}) or {}
kb   = kb.get("knowledgebase", {})
state = load_state()

uc = spec.get("ultimate_coder", {})
tracks = uc.get("tracks", [])

# ---------- UI ----------
st.set_page_config(page_title="Ultimate Coder", layout="wide")
st.title("🧭 Ultimate Coder – Control Panel")

with st.sidebar:
    st.header("Tracks & Modules")
    track_titles = []
    for t in tracks:
        t_title = t.get("title") or t.get("id", "track")
        t_id = t.get("id", t_title.lower().replace(" ", "_"))
        track_titles.append((t_id, t_title, t))

    # pick a track
    track_label_map = {tid: ttl for tid, ttl, _ in track_titles}
    choice_tid = st.selectbox("Select track", options=[tid for tid,_,_ in track_titles],
                              format_func=lambda tid: track_label_map[tid])
    active_track = next((t for tid,_,t in track_titles if tid == choice_tid), None)

    st.markdown("---")
    st.subheader("Quick Actions")
    if st.button("Open Syllabus"):
        (ROOT / "ultimate_coder" / "docs" / "syllabus.md").exists() and webbrowser.open_new_tab(
            (ROOT / "ultimate_coder" / "docs" / "syllabus.md").as_uri()
        )
    if st.button("Open Knowledgebase YAML"):
        KB_PATH.exists() and webbrowser.open_new_tab(KB_PATH.as_uri())

# main columns
col_left, col_right = st.columns([2, 1])

# -------- LEFT: Modules of selected track --------
with col_left:
    if active_track:
        st.subheader(f"📚 {active_track.get('title', active_track.get('id','Track'))}")
        mods = active_track.get("modules", [])
        for idx, m in enumerate(mods, start=1):
            mod_name = m.get("name", f"Module {idx}")
            mod_key = f"{active_track.get('id','track')}::{mod_name}"
            with st.expander(f"{idx}. {mod_name}", expanded=False):
                # meta
                weeks = m.get("weeks")
                skills = m.get("skills", [])
                project = m.get("project") or m.get("exercise") or m.get("optional_lab", {}).get("title")
                guardrails = m.get("guardrails", [])
                assessment = m.get("assessment", {})

                if weeks: st.markdown(f"**Weeks:** {weeks}")
                if skills: st.markdown("**Skills:** " + ", ".join(map(str, skills)))
                if project:
                    st.markdown("**Project/Exercise:**")
                    st.code(flat_str(project), language="text")

                if guardrails:
                    st.markdown("**Guardrails:**")
                    for g in guardrails: st.write(f"- {g}")

                if assessment:
                    st.markdown("**Assessment/Rubric:**")
                    st.code(yaml.safe_dump(assessment, sort_keys=False), language="yaml")

                # progress + notes
                done = state["completed"].get(mod_key, False)
                new_done = st.checkbox("Mark complete", value=done, key=f"cb_{mod_key}")
                if new_done != done:
                    set_completed(state, mod_key, new_done)

                note_val = state["notes"].get(mod_key, "")
                new_note = st.text_area("Notes / links / todos", value=note_val, key=f"note_{mod_key}", height=120)
                if new_note != note_val:
                    set_note(state, mod_key, new_note)

# -------- RIGHT: Knowledgebase search --------
with col_right:
    st.subheader("📚 Knowledgebase Search")
    q = st.text_input("Search (e.g., 'Rust', 'SRE', 'OpenDSA')", "")
    # flatten & filter
    results = []
    pattern = re.compile(re.escape(q), re.IGNORECASE) if q else None

    for section, items in kb.items():
        if isinstance(items, dict):
            for sub, subitems in items.items():
                lst = subitems if isinstance(subitems, list) else (subitems or [])
                for it in lst:
                    s = str(it)
                    if not pattern or pattern.search(s):
                        results.append((section, sub, s))
        else:
            # list form
            for it in (items or []):
                s = str(it)
                if not pattern or pattern.search(s):
                    results.append((section, None, s))

    if q:
        st.caption(f"{len(results)} result(s)")
    else:
        st.caption("Type to filter knowledgebase…")

    for section, sub, item in results[:200]:
        with st.container(border=True):
            st.markdown(f"**{section}**" + (f" · _{sub}_" if sub else ""))
            st.write(item)
            # basic link detection
            m = re.search(r"(https?://\S+)", item)
            if m:
                st.link_button("Open link", m.group(1))

st.markdown("---")
st.caption("Progress is saved to `ui/progress.json`. Edit YAML then refresh to see changes.")
