""" command """
import logging
from backend.domain.ports import UnitOfWork
from backend.application.messages import CreateCreditSimulationRequest
from backend.application.messages import CreateCreditSimulationResponse
from backend.application.validators import CreateCreditSimulationValidator
from backend.application.validators import CreateCreditSimulationBizValidator


class CreateCreditSimulationCommand:
    """ command """

    def __init__(self, uow: UnitOfWork, logger: logging):
        self.uow = uow
        self.log = logger

    def handle(self, request: CreateCreditSimulationRequest) -> CreateCreditSimulationResponse:
        """ handle """
        # 1. formal checks
        validator = CreateCreditSimulationValidator()
        validator.validate_and_throw(request)
        self.log.info("request validated")
        # 2. business checks
        biz_validator = CreateCreditSimulationBizValidator()
        biz_validator.validate_and_throw(request)
        self.log.info("business rules validated")

        return CreateCreditSimulationResponse(request.cashflow)
