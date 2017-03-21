import sqlalchemy
from Blue_Yellow.data.modelbase import SqlAlchemyBase


class Track(SqlAlchemyBase):
      __tablename__ = 'Track'
      id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
      name = sqlalchemy.Column(sqlalchemy.String)
      length = sqlalchemy.Column(sqlalchemy.Integer)
      audio_url = sqlalchemy.Column(sqlalchemy.String)
      video_url = sqlalchemy.Column(sqlalchemy.String)
      display_order = sqlalchemy.Column(sqlalchemy.Integer)