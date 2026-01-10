""" ports """
from sqlalchemy.orm import Session
from .repositories import CreditSimulationRepository


class UnitOfWork:
    """ uow """

    def __init__(self, session: Session):
        self.session = session
        self.credit_simulation: CreditSimulationRepository

    def commit(self):
        """ commit work """
        self.session.commit()

    def rollback(self):
        """ rollback work """
        self.session.rollback()

    def close_session(self):
        """ close session """
        self.session.close()
