""" endpoints """
import json
import logging
from typing import List
from fastapi import Depends, APIRouter, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from backend.tools import get_db
from backend.application.messages import ReadCreditSimulationRequest
from backend.application.queries import ReadCreditSimulationQuery
from backend.infrastructure.adapters import Adapter
from backend.webapi.models import CreditSimulationModel, InstallmentModel

router = APIRouter()


@router.get("/simulate/{sid}", response_model=CreditSimulationModel)
def _(
    sid: int,
    db: Session = Depends(get_db)
):

    command = ReadCreditSimulationRequest(sid)

    result = ReadCreditSimulationQuery(
        Adapter(db),
        logging.getLogger("read_credit_simulation")
    ).handle(command)

    sched = json.loads(result.credit_simulation.amortization_schedule)

    installments: List[InstallmentModel] = []
    for row in sched:
        i = InstallmentModel(
            month=row["month"],
            quota=row["quota"],
            interest=row["interest"],
            principal=row["principal"],
            outstanding=row["outstanding"]
        )
        installments.append(i)

    data = CreditSimulationModel(
        id=result.credit_simulation.id,
        annual_rate=result.credit_simulation.annual_rate,
        credit_amount=result.credit_simulation.credit_amount,
        term=result.credit_simulation.term,
        installments=installments
    )

    return data
