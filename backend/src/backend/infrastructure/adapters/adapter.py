""" adapters """
from sqlalchemy.orm import Session
from backend.domain.ports import UnitOfWork
from .credit_simulation_adapter import CreditSimulationAdapter


class Adapter(UnitOfWork):
    """ adapter sqlite """

    def __init__(self, session: Session):
        super().__init__(session)

        self.credit_simulation = CreditSimulationAdapter(self.session)

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
