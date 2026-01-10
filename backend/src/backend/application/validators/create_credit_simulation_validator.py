""" validator """
from backend.tools import Validator
from backend.application.messages import CreateCreditSimulationRequest


class CreateCreditSimulationValidator(Validator):
    """ validator """

    def __validate__(self, request: CreateCreditSimulationRequest):
        if request.credit_simulation.credit_amount <= 0:
            raise self.as_error(
                ("amount must be greater than 1", "CREA_SIM_001"))
        if request.credit_simulation.annual_rate < 1:
            raise self.as_error(
                ("rate must be greater than 1", "CREA_SIM_002"))
        if request.credit_simulation.term < 1:
            raise self.as_error(
                ("term must be between 1 to 12", "CREA_SIM_003"))


class CreateCreditSimulationBizValidator(Validator):
    """ business validator """

    def __validate__(self, request: CreateCreditSimulationRequest):
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

        request.cashflow = table
