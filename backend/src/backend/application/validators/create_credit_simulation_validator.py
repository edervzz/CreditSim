""" validator """
from backend.tools import Validator
from backend.application.messages import CreateCreditSimulationRequest


class CreateCreditSimulationValidator(Validator):
    """ validator """

    def __validate__(self, request: CreateCreditSimulationRequest):
        if request.credit_simulation.credit_amount <= 0:
            raise self.as_error(
                ("amount must be greater than 1", "CREA_SIM_001"))
        if request.credit_simulation.annual_rate < 1:
            raise self.as_error(
                ("rate must be greater than 1", "CREA_SIM_002"))
        if request.credit_simulation.term < 1:
            raise self.as_error(
                ("term must be between 1 to 12", "CREA_SIM_003"))
