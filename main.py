"""Application entry point."""

from src.logger import setup_logging
from src.message_sender import send_messages


def main() -> None:
    """Run the application."""
    setup_logging()
    send_messages()


if __name__ == "__main__":
    main()
