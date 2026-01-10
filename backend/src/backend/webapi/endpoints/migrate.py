""" endpoints """
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.infrastructure.data import base
from backend.tools.engine import get_db

router = APIRouter()


@router.post("/migrate")
def migrate(db: Session = Depends(get_db)):
    """ migrate db """
    base(db)
    print("executing migration")
