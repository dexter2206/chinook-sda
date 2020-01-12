from sqlalchemy import create_engine
from models import Artist
from db import Session, session_scope


if __name__ == "__main__":
    engine = create_engine(
        "mysql+pymysql://root:mypass@localhost/Chinook?charset=utf8mb4"
    )

    with session_scope(engine) as session:
        for artist in session.query(Artist).all():
            print(artist.name)

