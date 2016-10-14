# -*- coding: utf-8 -*-
import logging as log
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from http_mocker.utils import FailedOperation

DATABASES_MASTER = {
    "dialect": "mysql",
    "username": "root",
    "password": "root",
    "host": "127.0.0.1",
    "port": "3306",
    "database": "http_mock",
}


def _create_master_engine():
    db_url = "%s+mysqlconnector://%s:%s@%s:%s/%s" % (DATABASES_MASTER.get("dialect"), DATABASES_MASTER.get("username"),
                                                     DATABASES_MASTER.get("password"), DATABASES_MASTER.get("host"),
                                                     DATABASES_MASTER.get("port"), DATABASES_MASTER.get("database"))
    return create_engine(
        db_url, echo=False, connect_args={"charset": "utf8mb4", 'time_zone': '+00:00', 'connection_timeout': 30},
        pool_recycle=50)


@contextmanager
def session_scope():
    session = sessionmaker(bind=_create_master_engine(), expire_on_commit=False)()
    try:
        yield session
        session.commit()
    except FailedOperation as e:
        session.rollback()
        log.error("Failed Operation: %s" % e)
        raise
    except Exception as e:
        session.rollback()
        import traceback
        log.error(traceback.format_exc())
        raise FailedOperation(key="unknown_exception", message="Server Internal Error...")
    finally:
        session.close()
