""" tools """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_db():
    """ get db """
    ng = create_engine(
        "sqlite:///src//backend//infrastructure//data//data.db",
        echo=True
    )

    factory = sessionmaker(bind=ng)
    db = factory()
    try:
        yield db
    finally:
        db.close()
