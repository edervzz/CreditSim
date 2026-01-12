""" migrations """

from sqlalchemy import Column, Float, Integer, String, Text
from sqlalchemy import MetaData, Table
from sqlalchemy.orm import Session


def base(session: Session) -> str:
    """base tables"""

    metadata_obj = MetaData()

    Table(
        "credit_simulations",
        metadata_obj,
        Column(
            "id", Integer,
            primary_key=True,
            autoincrement=True,
            comment="Simulation ID"),
        Column(
            "credit_amount", Float,
            nullable=False,
            comment="Credit amount"),
        Column(
            "annual_rate", Float,
            nullable=False,
            comment="Annual rate"),
        Column(
            "term", Integer,
            nullable=False,
            comment="Term"),
        Column(
            "term_unit", String(1),
            nullable=False,
            comment="Term unit"),
        Column(
            "amortization_schedule", Text,
            nullable=False,
            comment="Amortization Schedule"),
        comment="Credit simulations."
    )

    metadata_obj.create_all(session.bind)
