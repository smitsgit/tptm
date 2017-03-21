import sqlalchemy
import sqlalchemy.orm
from sqlalchemy.ext.orderinglist import ordering_list

from  Blue_Yellow.data.modelbase import SqlAlchemyBase


class Album(SqlAlchemyBase):
    __tablename__ = 'Album'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    year = sqlalchemy.Column(sqlalchemy.Integer)
    price = sqlalchemy.Column(sqlalchemy.Float)
    album_image = sqlalchemy.Column(sqlalchemy.String)
    # Name of the table and back_populates = field
    tracks = sqlalchemy.orm.relationship('Track', back_populates='album',
                                         order_by='Track.display_order',
                                         collection_class=ordering_list('display_order'),
                                         cascade='all')
