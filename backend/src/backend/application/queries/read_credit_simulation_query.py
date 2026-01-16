""" queries """
import logging
from backend.application.messages import ReadCreditSimulationRequest
from backend.application.messages import ReadCreditSimulationResponse
from backend.application.validators import ReadCreditSimulationValidator
from backend.application.validators import ReadCreditSimulationBizValidator
from backend.domain.ports import UnitOfWork


class ReadCreditSimulationQuery:
    """ query """

    def __init__(self, uow: UnitOfWork, logger: logging):
        self.uow = uow
        self.log = logger

    def handle(self, request: ReadCreditSimulationRequest) -> ReadCreditSimulationResponse:
        """ handle """
        # 1. formal check
        validator = ReadCreditSimulationValidator()
        validator.validate_and_throw(request)
        self.log.info("request validated")
        # 2. business checks
        biz_validator = ReadCreditSimulationBizValidator(self.uow)
        biz_validator.validate_and_throw(request)
        self.log.info("business rules validated")

        return ReadCreditSimulationResponse(request.credit_simulation)
