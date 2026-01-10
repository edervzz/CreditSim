""" domains """
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class CreditSimulation(Base):
    """ credit simulation """
    __tablename__ = "credit_simulations"

    id: Mapped[int] = mapped_column(primary_key=True)

    credit_amount: Mapped[float] = mapped_column(nullable=False)

    annual_rate: Mapped[float] = mapped_column(nullable=False)

    term: Mapped[int] = mapped_column(nullable=False)

    term_unit: Mapped[str] = mapped_column(nullable=False)
