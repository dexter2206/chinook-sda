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

        session.bulk_insert_mappings(
            Track,
            [
                {
                    "name": f"Track no. {i}",
                    "genre_id": genre.id,
                    "media_type_id": media_type.id,
                    "milliseconds": i * 180000 + i * 10,
                    "bytes": 10000000,
                    "unit_price": random.random() * 10,
                    "album_id": album.id,
                    "composer": "Some excellent composer",
                }
                for i in range(20)
            ],
        )

        session.commit()
