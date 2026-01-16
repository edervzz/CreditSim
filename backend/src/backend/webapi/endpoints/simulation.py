""" endpoints """
import logging
from typing import List
from fastapi import Depends, APIRouter,  BackgroundTasks, Response
from sqlalchemy.orm import Session
from backend.webapi.models import NewCreditSimulationModel, InstallmentsModel, InstallmentModel
from backend.tools import get_db
from backend.infrastructure.integrations import risk_audit_mock
from backend.application.messages import CreateCreditSimulationRequest
from backend.application.commands import CreateCreditSimulationCommand
from backend.infrastructure.adapters import Adapter

router = APIRouter()


@router.post("/simulate", response_model=InstallmentsModel)
def _(
    credit: NewCreditSimulationModel,
    background_tasks: BackgroundTasks,
    response: Response,
    db: Session = Depends(get_db),
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

    instllmnts: List[InstallmentModel] = []
    for row in result.installments:
        i = InstallmentModel(
            month=row["month"],
            quota=row["quota"],
            interest=row["interest"],
            principal=row["principal"],
            outstanding=row["outstanding"]
        )
        instllmnts.append(i)

    data = InstallmentsModel(installments=instllmnts)

    response.headers["item"] = str(result.id)

    return data
