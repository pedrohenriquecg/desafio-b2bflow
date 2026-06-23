"""Application entry point."""

from src.message_sender import send_messages


def main() -> None:
    """Run the application."""
    send_messages()


if __name__ == "__main__":
    main()
