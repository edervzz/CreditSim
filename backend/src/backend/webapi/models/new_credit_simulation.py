""" models """
from pydantic import BaseModel


class NewCreditSimulationModel(BaseModel):
    """ credit calculation info """

    credit_amount: float
    annual_rate: float
    term: int
