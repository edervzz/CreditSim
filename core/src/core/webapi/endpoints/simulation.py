""" endpoints """
from fastapi import FastAPI
from webapi.models import CreditCalculation


def simulate(app: FastAPI):
    """ simulate endpoint """
    @app.post("/simulate")
    def _(credit: CreditCalculation):
        print(credit)
