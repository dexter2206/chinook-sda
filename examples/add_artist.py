from models import Artist
from db import get_engine, session_scope


if __name__ == "__main__":
    grechuta = Artist(name="Marek Grechuta")

    engine = get_engine()

    with session_scope(engine) as session:
        session.add(grechuta)
        session.commit()

        print(f"Grechuta has id: {grechuta.id}")