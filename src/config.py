"""Application configuration."""

import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


def validate_supabase_config() -> None:
    """Validate required Supabase environment variables."""
    if not SUPABASE_URL:
        raise EnvironmentError("Missing SUPABASE_URL environment variable.")

    if not SUPABASE_KEY:
        raise EnvironmentError("Missing SUPABASE_KEY environment variable.")