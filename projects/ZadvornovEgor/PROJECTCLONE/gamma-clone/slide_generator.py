"""
Orchestrates Claude API calls to generate a structured Presentation.

Flow:
1. Build prompt via prompts.py
2. Call Claude with structured output constraints
3. Parse JSON response into Pydantic model
4. Retry once on parse failure (with a nudge to fix JSON)
"""

import json
import logging
from typing import Callable, Optional

import anthropic

from config import ANTHROPIC_API_KEY, MAX_RETRIES, MODEL_NAME, REQUEST_TIMEOUT
from models import Presentation
from prompts import SYSTEM_PROMPT, get_generation_prompt

logger = logging.getLogger(__name__)

StatusCallback = Optional[Callable[[str], None]]


def _call_claude(messages: list[dict], status_cb: StatusCallback = None) -> str:
    """Send messages to Claude and return the raw text response."""
    if status_cb:
        status_cb("Connecting to Claude API...")

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY, timeout=REQUEST_TIMEOUT)

    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=messages,
    )

    return response.content[0].text


def _parse_response(raw: str) -> Presentation:
    """
    Parse Claude's raw text into a Presentation model.

    Handles common issues:
    - Markdown code fences around JSON
    - Leading/trailing whitespace
    """
    text = raw.strip()

    # Strip markdown fences if present
    if text.startswith("```"):
        first_newline = text.index("\n")
        text = text[first_newline + 1 :]
    if text.endswith("```"):
        text = text[: text.rfind("```")]

    text = text.strip()

    data = json.loads(text)
    return Presentation.model_validate(data)


def generate_presentation(
    topic: str,
    num_slides: int,
    style: str,
    status_cb: StatusCallback = None,
) -> Presentation:
    """
    Generate a complete presentation from a topic string.

    Args:
        topic: Subject of the presentation.
        num_slides: Number of content slides (title + summary added automatically).
        style: Visual/tone style ('professional', 'creative', 'minimalist').
        status_cb: Optional callback receiving status strings for UI updates.

    Returns:
        A validated Presentation object.

    Raises:
        ValueError: If the API response cannot be parsed after retries.
        anthropic.APIError: On network or authentication failures.
    """
    if not ANTHROPIC_API_KEY:
        raise ValueError(
            "ANTHROPIC_API_KEY is not set. "
            "Create a .env file with your key (see .env.example)."
        )

    prompt = get_generation_prompt(topic, num_slides, style)
    messages = [{"role": "user", "content": prompt}]

    if status_cb:
        status_cb("Generating slide outline...")

    raw = _call_claude(messages, status_cb)

    if status_cb:
        status_cb("Parsing response...")

    # First parse attempt
    try:
        return _parse_response(raw)
    except (json.JSONDecodeError, Exception) as first_err:
        logger.warning("First parse failed: %s — retrying with correction prompt", first_err)

    # Retry: send the broken output back and ask Claude to fix it
    if status_cb:
        status_cb("Fixing JSON format, retrying...")

    messages.append({"role": "assistant", "content": raw})
    messages.append({
        "role": "user",
        "content": (
            "The JSON above is malformed. Return ONLY the corrected, valid JSON "
            "with no extra text, no markdown fences. Keep the same content."
        ),
    })

    for attempt in range(MAX_RETRIES):
        raw_retry = _call_claude(messages, status_cb)
        try:
            presentation = _parse_response(raw_retry)
            if status_cb:
                status_cb("Slides generated successfully!")
            return presentation
        except (json.JSONDecodeError, Exception) as retry_err:
            logger.error("Retry %d parse failed: %s", attempt + 1, retry_err)

    raise ValueError(
        "Failed to parse Claude's response into a valid presentation. "
        "Try again or simplify the topic."
    )
