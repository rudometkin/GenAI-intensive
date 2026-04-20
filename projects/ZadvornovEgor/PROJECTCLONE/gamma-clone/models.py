"""
Pydantic data models for the presentation domain.

Three core models:
- SlideContent: a single slide's data (title, bullets, speaker notes)
- Presentation: the full deck (title, ordered slides, theme name)
- ThemeConfig: visual styling (colors, fonts, background)
"""

from pydantic import BaseModel, Field


class SlideContent(BaseModel):
    """A single slide with title, bullet points, and optional speaker notes."""

    title: str = Field(..., min_length=1, description="Slide heading")
    bullets: list[str] = Field(
        default_factory=list,
        description="Bullet points (empty for title slide)",
    )
    notes: str = Field(
        default="",
        description="Speaker notes for this slide",
    )


class Presentation(BaseModel):
    """Complete presentation structure returned by the LLM."""

    title: str = Field(..., min_length=1, description="Deck title")
    slides: list[SlideContent] = Field(
        ..., min_length=1, description="Ordered list of slides"
    )
    theme: str = Field(
        default="professional",
        description="Theme name hint from the LLM",
    )


class ThemeConfig(BaseModel):
    """Visual theme applied when rendering slides."""

    name: str
    primary_color: str = Field(..., description="Hex color, e.g. #1a365d")
    secondary_color: str = Field(..., description="Hex accent color")
    font_heading: str = "Arial"
    font_body: str = "Calibri"
    bg_color: str = "#ffffff"
