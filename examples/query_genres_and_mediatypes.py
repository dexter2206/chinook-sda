from models import Genre, MediaType
from db import Session, get_engine, session_scope


if __name__ == "__main__":
    engine = get_engine()

    with session_scope(engine) as session:

        print("All media types:")
        for media_type in session.query(MediaType):
            print("-", media_type.name)

        print("All genres:")
        for genre in session.query(Genre):
            print("-", genre.name)