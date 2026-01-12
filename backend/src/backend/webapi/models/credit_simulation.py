""" models """
from typing import List
from pydantic import BaseModel


class Installment(BaseModel):
    """ installment """
    period: int
    payment: float
    principal: float
    interest: float
    remaining_balance: float


class CreditSimulation(BaseModel):
    """ credit simulation """
    id: int
    installments: List[Installment]
