""" command """
import logging
from backend.domain.ports import UnitOfWork
from backend.application.messages import CreateCreditSimulationRequest
from backend.application.messages import CreateCreditSimulationResponse
from backend.application.validators import CreateCreditSimulationValidator


class CreateCreditSimulationCommand:
    """ command """

    def __init__(self, repository: UnitOfWork, logger: logging):
        self.repo = repository
        self.log = logger

    def handle(self, request: CreateCreditSimulationRequest) -> CreateCreditSimulationResponse:
        """ handle """
        # 1. formal checks
        validator = CreateCreditSimulationValidator()
        validator.validate_and_throw(request)
        self.log.info("request validated")

        amnt = request.credit_simulation.credit_amount
        r = request.credit_simulation.annual_rate / 100 / 12
        n = request.credit_simulation.term

        quota = amnt * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

        outstanding = amnt
        table = []

        for m in range(1, n + 1):
            interest = outstanding * r
            principal = quota - interest
            outstanding -= principal

            table.append({
                "month": m,
                "quota": round(quota, 2),
                "interest": round(interest, 2),
                "principal": round(principal, 2),
                "outstanding": round(max(outstanding, 0), 2)
            })

        return CreateCreditSimulationResponse(table)
