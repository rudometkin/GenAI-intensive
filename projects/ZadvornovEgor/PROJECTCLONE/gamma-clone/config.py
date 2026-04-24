"""
Application configuration loaded from environment variables.

Uses python-dotenv to load .env file, with sensible defaults
for all non-secret values.
"""

import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")

MODEL_NAME: str = os.getenv("MODEL_NAME", "claude-haiku-4-5-20251001")
MAX_SLIDES: int = int(os.getenv("MAX_SLIDES", "10"))
MIN_SLIDES: int = int(os.getenv("MIN_SLIDES", "3"))
DEFAULT_SLIDES: int = int(os.getenv("DEFAULT_SLIDES", "5"))

MAX_RETRIES: int = 1
REQUEST_TIMEOUT: int = 120
