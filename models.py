from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Artist(Base):
    __tablename__ = "Artist"
    id = Column(Integer, primary_key=True, name="ArtistId")
    name = Column(String(120), name="Name")

    albums = relationship("Album", back_populates="artist")

    def __repr__(self):
        return f"<Artist(id={self.id}, name={self.name})>"


class Album(Base):
    __tablename__ = "Album"
    id = Column(Integer, primary_key=True, name="AlbumId")
    title = Column(String(160), name="Title")
    artist_id = Column(Integer, ForeignKey("Artist.ArtistId"), name="ArtistId")

    artist = relationship(Artist, back_populates="albums")

    def __repr__(self):
        return f"<Album(id={self.id}, title={self.title})>"


class MediaType(Base):
    __tablename__="MediaType"
    id = Column(Integer, primary_key=True, name="MediaTypeId")
    name = Column(String(120), name="Name")


class Genre(Base):
    __tablename__ = "Genre"
    id = Column(Integer, primary_key=True, name="GenreId")
    name = Column(String(120), name="Name")
