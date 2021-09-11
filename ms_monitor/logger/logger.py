import logging
import requests
import structlog
from structlog import get_logger

log = get_logger("Structured Logger")
logger = logging.getLogger("Structured Logger")
logger.setLevel(logging.INFO)


def send_to_newrelic(logger, log_method, event_dict):

    headers = {"Api-Key": "ac326d0dff4432daaf868c335e9585c29037NRAL"}
    payload = {
        "message": f"{log_method} - {event_dict['event']}",
        "attributes": event_dict
    }

    response = requests.post("https://log-api.newrelic.com/log/v1", json=payload, headers=headers)
    return event_dict


structlog.configure(
    processors=[send_to_newrelic, structlog.processors.JSONRenderer()],
    logger_factory=structlog.stdlib.LoggerFactory()
)

formatter = structlog.stdlib.ProcessorFormatter(
    processor=structlog.dev.ConsoleRenderer(),
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)
root_logger = logging.getLogger()
root_logger.addHandler(handler)
root_logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("error.log")
file_handler.setFormatter(formatter)
root_logger = logging.getLogger()
root_logger.addHandler(file_handler)
root_logger.setLevel(logging.CRITICAL)
