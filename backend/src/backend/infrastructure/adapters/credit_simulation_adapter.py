""" adapter """

from backend.domain.entities import CreditSimulation
from backend.domain.ports import CreditSimulationRepository


class CreditSimulationAdapter(CreditSimulationRepository):
    """ credit simulation adapter """

    def create(self, entity: CreditSimulation):
        self.session.add(entity)

    def read(self, _id: int):
        return self.query.where(CreditSimulation.id == _id).one_or_none()
