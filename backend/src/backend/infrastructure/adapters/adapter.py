""" adapters """
from sqlalchemy.orm import Session
from backend.domain.ports import UnitOfWork, CreditSimulationRepository


class Adapter(UnitOfWork):
    """ adapter sqlite """

    def __init__(self, session: Session):
        super().__init__(session)

        self.simulate = CreditSimulationRepository(self.session)
