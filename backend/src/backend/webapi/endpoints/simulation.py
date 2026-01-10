""" endpoints """
import logging
from fastapi import Depends, APIRouter, status, BackgroundTasks
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from backend.webapi.models import NewCreditSimulationModel
from backend.tools import get_db
from backend.infrastructure.integrations import risk_audit_mock
from backend.application.messages import CreateCreditSimulationRequest
from backend.application.commands import CreateCreditSimulationCommand
from backend.infrastructure.adapters import Adapter

router = APIRouter()


@router.post("/simulate")
def _(
    credit: NewCreditSimulationModel,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):

    command = CreateCreditSimulationRequest(
        credit.annual_rate,
        credit.credit_amount,
        credit.term,
        "M"
    )
    result = CreateCreditSimulationCommand(
        Adapter(db),
        logging.getLogger("credit_simulation")
    ).handle(command)

    background_tasks.add_task(
        risk_audit_mock,
        result.id,
    )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"cashflow": result.cashflow}
    )
