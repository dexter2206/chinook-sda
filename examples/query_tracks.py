from models import Track
from db import session_scope, Session, get_engine


if __name__ == "__main__":
    engine = get_engine()

    with session_scope(engine) as session:
        track = session.query(Track)[2]
        print("Name:", track.name)
        print("Album:", track.album.title)
        print("Genre:", track.genre.name)
        print("Media type:", track.media_type.name)
