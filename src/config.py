"""Application configuration."""

import os

from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")


def validate_supabase_config() -> None:
    """Validate required Supabase environment variables."""
    if not SUPABASE_URL:
        raise EnvironmentError("Missing SUPABASE_URL environment variable.")

    if not SUPABASE_KEY:
        raise EnvironmentError("Missing SUPABASE_KEY environment variable.")


def validate_zapi_config() -> None:
    """Validate required Z-API environment variables."""
    if not ZAPI_INSTANCE_ID:
        raise EnvironmentError("Missing ZAPI_INSTANCE_ID environment variable.")

    if not ZAPI_TOKEN:
        raise EnvironmentError("Missing ZAPI_TOKEN environment variable.")
