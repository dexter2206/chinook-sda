from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Artist(Base):
    __tablename__ = "Artist"
    id = Column(Integer, primary_key=True, name="ArtistId")
    name = Column(String(120), name="Name")

    def __repr__(self):
        return f"<Artist(id={self.id}, name={self.name})>"
