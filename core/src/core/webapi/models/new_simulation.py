""" models """
from pydantic import BaseModel


class CreditCalculation(BaseModel):
    """ credit calculation info """

    credit_amount: float
    annual_rate: float
    term: int
