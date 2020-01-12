import random

from models import Artist, Album, Track, MediaType, Genre
from db import get_engine, session_scope

if __name__ == "__main__":
    engine = get_engine(echo=True)

    with session_scope(engine) as session:
        artist = Artist(name="New Artist")
        album = Album(title="Greatest hits", artist=artist)

        genre = session.query(Genre).first()
        media_type = session.query(MediaType).first()

        tracks = [
            Track(
                name=f"Track no. {i}",
                genre=genre,
                media_type=media_type,
                milliseconds=i * 180000 + i * 10,
                bytes=10000000,
                unit_price=random.random() * 10,
                album=album,
                composer="Some excellent composer",
            )
            for i in range(20)
        ]

        session.add_all(tracks)
        session.commit()