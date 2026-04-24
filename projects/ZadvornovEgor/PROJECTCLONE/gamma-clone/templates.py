"""
Built-in theme presets for presentation rendering.

Each theme defines a complete visual identity: colors, fonts, and background.
Themes are used both by pptx_builder (PPTX export) and preview (HTML cards).
"""

from models import ThemeConfig

_THEMES: dict[str, ThemeConfig] = {
    "professional": ThemeConfig(
        name="Professional",
        primary_color="#1a365d",
        secondary_color="#2b6cb0",
        font_heading="Arial",
        font_body="Calibri",
        bg_color="#ffffff",
    ),
    "creative": ThemeConfig(
        name="Creative",
        primary_color="#6b21a8",
        secondary_color="#a855f7",
        font_heading="Georgia",
        font_body="Verdana",
        bg_color="#faf5ff",
    ),
    "minimalist": ThemeConfig(
        name="Minimalist",
        primary_color="#1a1a1a",
        secondary_color="#525252",
        font_heading="Helvetica",
        font_body="Helvetica",
        bg_color="#fafafa",
    ),
}


def get_theme(name: str) -> ThemeConfig:
    """Return a theme by name (case-insensitive). Falls back to 'professional'."""
    return _THEMES.get(name.lower(), _THEMES["professional"])


def get_available_themes() -> list[str]:
    """Return display names of all available themes."""
    return [t.name for t in _THEMES.values()]


def get_theme_key_by_display_name(display_name: str) -> str:
    """Map display name back to dict key, e.g. 'Creative' -> 'creative'."""
    for key, theme in _THEMES.items():
        if theme.name == display_name:
            return key
    return "professional"
