""" validator """
from backend.tools import Validator
from backend.application.messages import ReadCreditSimulationRequest
from backend.domain.ports import UnitOfWork


class ReadCreditSimulationValidator(Validator):
    """ validator """

    def __validate__(self, request: ReadCreditSimulationRequest):
        if request.simulation_id <= 0:
            raise self.as_error(
                ("simulation id must be greater than zero", "READ_SIM_001"))


class ReadCreditSimulationBizValidator(Validator):
    """ business validator"""

    def __init__(self, uow: UnitOfWork):
        super().__init__()
        self.uow = uow

    def __validate__(self, request: ReadCreditSimulationRequest):
        request.credit_simulation = self.uow.credit_simulation.read(
            request.simulation_id)

        if request.credit_simulation is None:
            raise self.as_not_found((
                f"simulation id {request.simulation_id} does not exists",
                "READ_SIM_002"))
