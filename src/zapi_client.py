"""Client for sending messages through the Z-API."""

import logging

import requests

from src.config import ZAPI_INSTANCE_ID, ZAPI_TOKEN, validate_zapi_config

logger = logging.getLogger(__name__)


class ZAPIClient:
    """Handle communication with the Z-API messaging endpoint."""

    BASE_URL = "https://api.z-api.io"

    def __init__(
        self,
        instance_id: str | None = ZAPI_INSTANCE_ID,
        token: str | None = ZAPI_TOKEN,
        timeout: int = 15,
    ) -> None:
        """Initialize the Z-API client with credentials and request timeout."""
        validate_zapi_config()

        self.instance_id = instance_id
        self.token = token
        self.timeout = timeout

    @property
    def send_text_endpoint(self) -> str:
        """Return the endpoint used to send text messages."""
        return (
            f"{self.BASE_URL}/instances/{self.instance_id}"
            f"/token/{self.token}/send-text"
        )

    def send_text_message(self, phone: str, message: str) -> bool:
        """Send a text message to a phone number through Z-API."""
        if not phone:
            logger.error("Message not sent: phone number is missing.")
            return False

        if not message:
            logger.error("Message not sent: message is missing.")
            return False

        payload = {
            "phone": phone,
            "message": message,
        }

        try:
            response = requests.post(
                self.send_text_endpoint,
                json=payload,
                timeout=self.timeout,
            )
            response.raise_for_status()
        except requests.exceptions.Timeout:
            logger.exception("Timeout while sending Z-API message to %s.", phone)
            return False
        except requests.exceptions.HTTPError as error:
            logger.error(
                "Z-API returned an error while sending message to %s. "
                "Status code: %s. Response: %s",
                phone,
                error.response.status_code if error.response else "unknown",
                error.response.text if error.response else "No response body",
            )
            return False
        except requests.exceptions.RequestException:
            logger.exception("Failed to send Z-API message to %s.", phone)
            return False

        logger.info("Z-API message sent successfully to %s.", phone)
        return True