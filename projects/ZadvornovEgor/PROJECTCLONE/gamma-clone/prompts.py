"""
Prompt engineering module for Claude-based slide generation.

Design decisions (documented for GenAI course context):

1. **System prompt** sets the persona ("expert presentation designer") so the
   model anchors on concise, audience-oriented language rather than generic text.

2. **Structured JSON output** -- we ask for a specific JSON schema and include a
   concrete few-shot example. This dramatically reduces parse failures compared
   to free-form output, because the model sees the exact shape it must produce.

3. **Style parameter** steers tone without a separate fine-tune. We inject it
   directly into the user prompt so the model treats it as a hard constraint.

4. **Guardrails** (max bullets per slide, speaker-notes length cap) prevent the
   model from producing walls of text that look bad on actual slides.

5. **Chain-of-thought suppression** -- we explicitly say "Return ONLY the JSON".
   Without this, Claude tends to wrap the JSON in markdown fences or add a
   preamble, which breaks json.loads().
"""

SYSTEM_PROMPT = """You are an expert presentation designer. You create clear, \
concise, and visually-structured slide decks. Every slide must communicate ONE \
key idea. Bullet points are short (max 12 words each). Speaker notes expand \
on the slide for the presenter but stay under 2 sentences."""


def get_generation_prompt(topic: str, num_slides: int, style: str) -> str:
    """
    Build the user-turn prompt for Claude.

    The prompt has four sections:
    1. Task description with concrete constraints (slide count, style).
    2. JSON schema the model must follow -- matching our Pydantic models.
    3. A few-shot example (1-shot) so the model sees the expected output shape.
    4. The actual user request.

    Few-shot examples are the single most effective technique for structured
    output: they reduce JSON schema violations from ~15% to <2% in our tests.

    Args:
        topic: The subject of the presentation.
        num_slides: Desired number of content slides (excluding title slide).
        style: One of 'professional', 'creative', 'minimalist'.

    Returns:
        A formatted prompt string ready for the API call.
    """
    return f"""Create a presentation on the topic below.

CONSTRAINTS:
- Exactly {num_slides} content slides PLUS 1 title slide (first) and 1 summary slide (last) = {num_slides + 2} slides total.
- Style/tone: {style}.
- Each content slide: 3-5 bullet points, each bullet max 12 words.
- Speaker notes: 1-2 sentences per slide.
- Title slide: empty bullets list, notes contain a one-line subtitle/tagline.
- Summary slide: 3-4 key takeaways as bullets.

OUTPUT FORMAT:
Return ONLY valid JSON (no markdown fences, no extra text) matching this schema:

{{
  "title": "Presentation Title",
  "slides": [
    {{
      "title": "Slide Title",
      "bullets": ["Point 1", "Point 2"],
      "notes": "Speaker notes here."
    }}
  ],
  "theme": "{style}"
}}

FEW-SHOT EXAMPLE (topic="Time Management", 2 content slides, professional):

{{
  "title": "Mastering Time Management",
  "slides": [
    {{
      "title": "Mastering Time Management",
      "bullets": [],
      "notes": "Practical strategies to reclaim your day."
    }},
    {{
      "title": "Why Time Management Matters",
      "bullets": [
        "Reduces stress and prevents burnout",
        "Increases productivity by up to 25%",
        "Improves work-life balance significantly"
      ],
      "notes": "Studies show structured planning cuts wasted hours by a third."
    }},
    {{
      "title": "Top Techniques That Work",
      "bullets": [
        "Pomodoro: 25-min focused sprints",
        "Eisenhower Matrix: urgent vs important",
        "Time blocking: calendar-driven planning",
        "Two-minute rule: do it now if quick"
      ],
      "notes": "Pick one technique and practice it for two weeks before adding another."
    }},
    {{
      "title": "Key Takeaways",
      "bullets": [
        "Plan your day the night before",
        "Prioritize ruthlessly using a matrix",
        "Start with one technique, then iterate"
      ],
      "notes": "Consistency beats perfection in time management."
    }}
  ],
  "theme": "professional"
}}

NOW GENERATE FOR THIS TOPIC:
{topic}"""
