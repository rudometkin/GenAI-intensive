"""
SlideDeck AI -- Streamlit application entry point.

Run with:  streamlit run app.py
"""

import logging

import streamlit as st

from config import ANTHROPIC_API_KEY, DEFAULT_SLIDES, MAX_SLIDES, MIN_SLIDES
from models import Presentation, ThemeConfig
from pptx_builder import build_pptx
from preview import render_preview
from slide_generator import generate_presentation
from templates import get_available_themes, get_theme, get_theme_key_by_display_name

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

st.set_page_config(
    page_title="SlideDeck AI",
    page_icon="\U0001f3ac",
    layout="wide",
)

# ── Header ───────────────────────────────────────────────────────────────────

st.title("SlideDeck AI")
st.caption("AI-powered presentation generator  --  describe your topic, get a slide deck")

# ── Sidebar ──────────────────────────────────────────────────────────────────

with st.sidebar:
    st.header("Settings")

    topic = st.text_area(
        "Presentation topic",
        placeholder="e.g. Introduction to Machine Learning for Business Leaders",
        height=100,
    )

    num_slides = st.slider(
        "Content slides",
        min_value=MIN_SLIDES,
        max_value=MAX_SLIDES,
        value=DEFAULT_SLIDES,
        help="Title and summary slides are added automatically.",
    )

    theme_names = get_available_themes()
    selected_theme_display = st.selectbox("Theme", theme_names, index=0)
    theme_key = get_theme_key_by_display_name(selected_theme_display)

    style_options = ["professional", "creative", "minimalist"]
    style = st.selectbox(
        "Tone / style",
        style_options,
        index=style_options.index(theme_key) if theme_key in style_options else 0,
    )

    generate_clicked = st.button("Generate presentation", type="primary", use_container_width=True)

    st.divider()
    st.markdown(
        "Built with [Streamlit](https://streamlit.io), "
        "[Claude API](https://docs.anthropic.com), "
        "and [python-pptx](https://python-pptx.readthedocs.io)."
    )

# ── API key check ────────────────────────────────────────────────────────────

if not ANTHROPIC_API_KEY:
    st.warning(
        "**ANTHROPIC_API_KEY not found.** "
        "Create a `.env` file in the project root (see `.env.example`)."
    )

# ── Generation flow ──────────────────────────────────────────────────────────

if generate_clicked:
    if not topic.strip():
        st.error("Please enter a topic in the sidebar.")
        st.stop()

    if not ANTHROPIC_API_KEY:
        st.error("Cannot generate without an API key.")
        st.stop()

    theme: ThemeConfig = get_theme(theme_key)

    with st.status("Generating presentation...", expanded=True) as status:
        try:

            def update_status(msg: str) -> None:
                st.write(msg)

            update_status("Generating outline...")

            presentation: Presentation = generate_presentation(
                topic=topic.strip(),
                num_slides=num_slides,
                style=style,
                status_cb=update_status,
            )

            update_status("Building PPTX file...")
            pptx_bytes = build_pptx(presentation, theme)

            update_status("Rendering preview...")
            html = render_preview(presentation, theme)

            status.update(label="Done!", state="complete", expanded=False)

        except ValueError as ve:
            status.update(label="Generation failed", state="error")
            st.error(str(ve))
            st.stop()
        except Exception as exc:
            status.update(label="Unexpected error", state="error")
            logger.exception("Generation failed")
            st.error(f"Something went wrong: {exc}")
            st.stop()

    # Store in session state so preview survives re-renders
    st.session_state["presentation"] = presentation
    st.session_state["pptx_bytes"] = pptx_bytes
    st.session_state["preview_html"] = html
    st.session_state["theme_key"] = theme_key

# ── Display results ──────────────────────────────────────────────────────────

if "presentation" in st.session_state:
    presentation = st.session_state["presentation"]
    pptx_bytes = st.session_state["pptx_bytes"]
    html = st.session_state["preview_html"]

    col_preview, col_info = st.columns([3, 1])

    with col_preview:
        st.subheader(presentation.title)
        st.markdown(html, unsafe_allow_html=True)

    with col_info:
        st.metric("Total slides", len(presentation.slides))
        st.download_button(
            label="Download .pptx",
            data=pptx_bytes,
            file_name=f"{presentation.title[:40].replace(' ', '_')}.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            use_container_width=True,
        )
        st.divider()
        st.caption("Slide titles:")
        for i, s in enumerate(presentation.slides, 1):
            st.text(f"{i}. {s.title}")
