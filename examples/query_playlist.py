from models import Playlist
from db import Session, session_scope, get_engine


if __name__ == "__main__":
    engine = get_engine()

    with session_scope(engine) as session:
        playlist = session.query(Playlist).first()
        print(f"Playlist {playlist.name}")
        for track in playlist.tracks:
            print(" - ", track.name)