"""application logging configuration."""

import logging


def setup_logging() -> None:
    """Configure global application logging."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )
