# -*- coding: utf-8 -*-
from sqlalchemy import BIGINT
from sqlalchemy import Column, VARCHAR
from sqlalchemy import TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Response(Base):
    __tablename__ = "response"
    id = Column(BIGINT, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(100), nullable=False)
    path = Column(VARCHAR(2000), nullable=False)
    response = Column(TEXT, nullable=False)
