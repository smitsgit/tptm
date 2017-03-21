import sqlalchemy
from Blue_Yellow.data.modelbase import SqlAlchemyBase

# if we dont do this thing , Python doesnt know that these classes
# are deriving from SqlAlchemyBase required on #19 cause its all runtime and no compile time
import Blue_Yellow.data.album
import Blue_Yellow.data.track


class DbSessionFactory():
    @staticmethod
    def global_init_database(db_file):
        if not db_file:
            raise Exception('You must specify the DB file')

        conn_str = 'sqlite:///' + db_file
        engine = sqlalchemy.create_engine(conn_str)

        # I will look for all the classes who derive from me and then load them in DB
        SqlAlchemyBase.metadata.create_all(engine)

