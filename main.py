"""Application entry point."""

from src.supabase_client import get_contacts


def main() -> None:
    """Run the application."""
    contacts = get_contacts()

    if not contacts:
        print("Nenhum contato encontrado.")
        return

    print("Contatos encontrados:")

    for contact in contacts:
        print(f"Nome: {contact['nome']}")
        print(f"Telefone: {contact['telefone']}")
        print("-" * 30)


if __name__ == "__main__":
    main()