import logging
import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from config import Config as config


logger = logging.getLogger(__name__)


# Returns what I understand to be a session maker object
def connect(url, echo=False):
    print("Creating engine with url <%r>" % (url,))
    engine = create_engine(url, echo=echo)
    Session = sessionmaker(bind=engine)
    return Session


def create_url_from_parts(username, password, host, dbname):
    password = urllib.parse.quote_plus(password)
    url = "mysql+pymysql://%s:%s@%s/%s" % (username, password, host, dbname)
    logger.error(url)
    return url


def create_tables(Session):
    session = Session()
    Base.metadata.create_all(session.get_bind().engine)
    session.close()

Session = connect(
    create_url_from_parts(
        config.db_username,
        config.db_password,
        config.db_host,
        config.db_name
        ))
