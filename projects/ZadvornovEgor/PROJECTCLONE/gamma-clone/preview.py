"""
HTML preview renderer for in-browser slide cards.

Generates a CSS-grid layout where each slide is shown as a styled card.
The first card (title slide) spans full width; content cards are in a 2-column grid.
Colors and fonts are pulled from the active ThemeConfig.
"""

from models import Presentation, ThemeConfig


def _escape_html(text: str) -> str:
    """Minimal HTML escaping for user-generated content."""
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def render_preview(presentation: Presentation, theme: ThemeConfig) -> str:
    """
    Build an HTML string with styled slide cards.

    Args:
        presentation: The generated presentation data.
        theme: Active theme for colors and fonts.

    Returns:
        Complete HTML/CSS string safe for st.markdown(unsafe_allow_html=True).
    """
    cards_html: list[str] = []

    for idx, slide in enumerate(presentation.slides):
        is_title = idx == 0
        bg = theme.primary_color if is_title else theme.bg_color
        text_color = "#ffffff" if is_title else theme.primary_color
        bullet_color = "#ffffff" if is_title else theme.secondary_color

        bullets_li = "\n".join(
            f'<li style="color:{bullet_color};margin-bottom:6px;">'
            f"{_escape_html(b)}</li>"
            for b in slide.bullets
        )

        span_class = ' class="title-card"' if is_title else ""
        font_size = "24px" if is_title else "18px"

        card = f"""
        <div{span_class} style="
            background:{bg};
            border-radius:12px;
            padding:28px 24px;
            border:1px solid #e2e8f0;
            box-shadow:0 2px 8px rgba(0,0,0,0.06);
        ">
            <div style="
                font-size:11px;
                color:{bullet_color};
                font-family:{theme.font_body},sans-serif;
                margin-bottom:8px;
                opacity:0.7;
            ">Slide {idx + 1}</div>
            <div style="
                font-size:{font_size};
                font-weight:700;
                color:{text_color};
                font-family:{theme.font_heading},sans-serif;
                margin-bottom:14px;
            ">{_escape_html(slide.title)}</div>
            <ul style="
                list-style:none;
                padding:0;
                margin:0;
                font-family:{theme.font_body},sans-serif;
                font-size:14px;
            ">{bullets_li}</ul>
        </div>"""
        cards_html.append(card)

    all_cards = "\n".join(cards_html)

    return f"""
    <style>
        .slide-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            max-width: 900px;
            margin: 0 auto;
        }}
        .slide-grid .title-card {{
            grid-column: 1 / -1;
            text-align: center;
        }}
    </style>
    <div class="slide-grid">
        {all_cards}
    </div>
    """
