import mimetypes
import os
import re

from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table, DateTime, func
from sqlalchemy.orm import relationship, validates
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Experiment(Base):

    __tablename__ = 'experiment'

    experimentID = Column('experimentID', String, primary_key = True, nullable = False)
    schemaID = Column('schemaID', Integer, primary_key = True, nullable = False)

