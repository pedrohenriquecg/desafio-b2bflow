"""Supabase client and contact retrieval."""

from supabase import create_client

from src.config import SUPABASE_KEY, SUPABASE_URL, validate_supabase_config


def get_contacts(limit: int = 3) -> list[dict]:
    """Fetch contacts from Supabase."""
    validate_supabase_config()

    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    response = (
        supabase
        .table("contatos")
        .select("id, nome, telefone")
        .limit(limit)
        .execute()
    )

    return response.data