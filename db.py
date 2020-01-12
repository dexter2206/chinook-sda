from contextlib import contextmanager
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
        print("Closing session")
        session.close()
