""" adapter """

from backend.domain.entities import CreditSimulation
from backend.domain.ports import CreditSimulationRepository


class CreditSimulationAdapter(CreditSimulationRepository):
    """ credit simulation adapter """

    def create(self, entity: CreditSimulation):
        self.session.add(entity)
