import sqlalchemy
from sqlalchemy import event
from sqlalchemy import exc
from sqlalchemy import select
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class TFTBase(object):
    base = declarative_base()

    def __init__(self):
        DeprecationWarning("Use BluecopperBase rather than TFTBase")
        pass

    @staticmethod
    def declarative_base():
        """
        Returns a singleton sqlalchemy DeclarativeMeta instance for use with all Commissary ORM classes.
        This is necessary so that all relationships are mapped within the same declarative tablespace.

        :return: sqlalchemy DeclarativeMeta instance
        :rtype: DeclarativeMeta
        """
        return TFTBase.base

    # noinspection PyMethodMayBeStatic
    def engine(self, configuration, prefix="sqlalchemy.tft."):
        """
        Creates a SQLAlchemy engine using the supplied configuration dictionary

        :param configuration: a dict containing at least <<prefix>>.url specifying the database connection URL
        :param prefix: (optional) override the dictionary prefix for the database connection URL
        :return: SQLAlchemy engine
        :rtype: Engine
        """
        return sqlalchemy.engine_from_config(configuration, prefix=prefix)

    def session(self, configuration, prefix="sqlalchemy.tft."):
        """
        Creates a SQLAlchemy session using the supplied configuration dictionary

        :param configuration: a dict containing at least <<prefix>>.url specifying the database connection URL
        :param prefix: (optional) override the dictionary prefix for the database connection URL
        :return: SQLAlchemy session
        :rtype: sqlalchemy.orm.session.Session
        """
        engine = self.engine(configuration, prefix)

        ngp_session_factory = sessionmaker(bind=engine)
        # For threaded use with a webserver, scoped sessions are necessary. This keeps sessions separate for different
        # worker threads while still allowing for registry-like access within the confines of a single thread.
        # http://docs.sqlalchemy.org/en/latest/orm/contextual.html
        session = scoped_session(ngp_session_factory)
        return session
