""" messages """
from backend.domain.entities import CreditSimulation


class ReadCreditSimulationRequest:
    """ request """

    def __init__(self, simulation_id: int):
        self.simulation_id = simulation_id
        self.credit_simulation: CreditSimulation


class ReadCreditSimulationResponse:
    """ response """

    def __init__(self, credit_simulation: CreditSimulation):
        self.credit_simulation = credit_simulation
