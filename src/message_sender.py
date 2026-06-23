"""message sending workflow for contacts stored in supabase."""

import logging

from src.supabase_client import get_contacts
from src.zapi_client import ZAPIClient

logger = logging.getLogger(__name__)

MESSAGE_TEMPLATE = "Olá, {name} tudo bem com você?"
MAX_CONTACTS = 3


def send_messages() -> None:
    """Fetch contacts and send a text message to each valid contact."""
    contacts = get_contacts()

    if not contacts:
        logger.info("No contacts found to process.")
        return

    zapi_client = ZAPIClient()

    for contact in contacts[:MAX_CONTACTS]:
        name = contact.get("nome")
        phone = contact.get("telefone")

        if not name or not phone:
            logger.warning("Skipping contact with missing name or phone: %s", contact)
            continue

        message = MESSAGE_TEMPLATE.format(name=name)
        was_sent = zapi_client.send_text_message(phone=phone, message=message)

        if was_sent:
            logger.info("Message sent successfully to contact %s.", name)
            continue

        logger.error("Failed to send message to contact %s.", name)
