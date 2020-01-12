from models import Playlist, Track, playlists_tracks
from db import Session, get_engine, session_scope


if __name__ == "__main__":
    engine = get_engine(echo=True)
    Session.configure(bind=engine)

    with session_scope() as session:
        track = session.query(Track).first()

        for playlist in session.query(Playlist).filter(Playlist.tracks.contains(track)):
            print(playlist.name)

        for playlist in (
            session.query(Playlist)
            .join(playlists_tracks)
            .filter(playlists_tracks.c.TrackId == track.id)
        ):
            print(playlist.name)
