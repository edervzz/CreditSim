""" ports """
from abc import ABC
from sqlalchemy.orm import Session
from backend.domain.entities import CreditSimulation
from .abstractions import Creator


class CreditSimulationRepository(
        ABC, Creator):
    """ credit simulation repository """

    def __init__(self, session: Session):
        self.session = session
        self.query = self.session.query(CreditSimulation)

    def create(self, entity: CreditSimulation):
        raise NotImplementedError(__name__)
