""" models """
from typing import List
from pydantic import BaseModel


class InstallmentModel(BaseModel):
    """ installment """
    month: int
    quota: float
    interest: float
    principal: float
    outstanding: float


class InstallmentsModel(BaseModel):
    """ installment """
    installments: List[InstallmentModel]


class CreditSimulationModel(BaseModel):
    """ credit simulation """

    id: int
    credit_amount: float
    annual_rate: float
    term: int
    installments: List[InstallmentModel]
