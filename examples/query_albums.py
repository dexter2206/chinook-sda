from models import Album, Artist
from db import get_engine, session_scope, Session


if __name__ == "__main__":
    engine = get_engine(echo=True)

    with session_scope(engine) as session:
        print("Pierwsze dwa albumy:")
        for album in session.query(Album).limit(2):
            print(f"{album.artist.name}: {album.title}")

        artist = session.query(Artist).first()
        print(f"Albumy artysty {artist.name}:")
        for album in artist.albums:
            print(f"- {album.title}")
