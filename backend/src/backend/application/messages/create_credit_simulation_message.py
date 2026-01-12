""" messages """
from backend.domain.entities import CreditSimulation


class CreateCreditSimulationRequest:
    """ request """

    def __init__(self, annual_rate: float, credit_amount: float, term: int, term_unit: str):

        self.credit_simulation = CreditSimulation()
        self.credit_simulation.annual_rate = annual_rate
        self.credit_simulation.credit_amount = credit_amount
        self.credit_simulation.term = term
        self.credit_simulation.term_unit = term_unit

        self.credit_simulation_id: int
        self.installments: list


class CreateCreditSimulationResponse:
    """ response """

    def __init__(self, _id: int,  installments):
        self.id = _id
        self.installments = installments
