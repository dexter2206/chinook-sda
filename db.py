from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def get_engine(echo=False):
    return create_engine(
        "mysql+pymysql://root:mypass@localhost/Chinook?charset=utf8mb4",
        echo=echo
    )
