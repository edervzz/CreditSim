""" tools """
import random
import time
import logging


def risk_audit_mock(simulation_id: str):
    """ mock """
    logger = logging.getLogger("risk_audit")
    try:

        delay = random.uniform(1, 3)
        time.sleep(delay)
        if random.random() <= 0.10:
            raise TimeoutError("Risk scoring service failed")
        logger.info("Scoring OK")

    except TimeoutError as e:
        logger.error("Audit failed", exc_info=e)
