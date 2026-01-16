""" ports """
from abc import ABC
from sqlalchemy.orm import Session
from backend.domain.entities import CreditSimulation
from .abstractions import Creator, ReaderSingle


class CreditSimulationRepository(
        ABC, Creator, ReaderSingle):
    """ credit simulation repository """

    def __init__(self, session: Session):
        self.session = session
        self.query = self.session.query(CreditSimulation)

    def create(self, entity: CreditSimulation):
        raise NotImplementedError(__name__)

    def read(self, _id: int) -> CreditSimulation | None:
        raise NotImplementedError(__name__)
