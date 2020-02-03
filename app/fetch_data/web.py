import sqlalchemy as db
import app.fetch_data as fd

def get_data(galaxy, messier):
    engine = db.create_engine("mysql+pymysql://root:@localhost/python-galaxies"
                           .format(user="root",
                                   pw="",
                                   db="python-galaxies"))
    connection = engine.connect()
    metadata = db.MetaData()
    con_table = db.Table('data_galaxies', metadata, autoload=True, autoload_with=engine)
    if galaxy is None:
        query = db.select([con_table]).where(con_table.columns.messier_name == messier)
    elif messier is None:
        query = db.select([con_table]).where(con_table.columns.galaxy_name == galaxy)
    else:
        query = db.select([con_table]).where(
            db.and_(con_table.columns.messier_name == messier, con_table.columns.galaxy_name == galaxy))
    res = connection.execute(query)
    cols = connection.execute(query).keys()
    return fd.sql_to_json(res, cols)