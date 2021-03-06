import mimetypes
import os
import re

from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table, DateTime, func
from sqlalchemy.orm import relationship, validates
from sqlalchemy.ext.declarative import declarative_base

#TODO: update to BluecopperBase.declarative_base()
Base = declarative_base()

#TODO: inheritate from bluecopper base class
class TFT_Experiment(Base):

    __tablename__ = 'tft_experiment'

    exp_id = Column('experiment_id', String(100), primary_key = True, nullable = False)
    schema_id = Column('schema_id', Integer, 
                        ForeignKey('tft_schema_attribute.schema_id'),
                        nullable=False
                      )

    exp_attr = relationship("TFT_Experiment_Attribute")
    schema_attr = relationship("TFT_Schema_Attribute")

    # @validates()

    def __repr__ (self):
        return "<TFT_Experiment(exp_id='%s', schema_id='%s')>" % (
                self.exp_id, self.schema_id
                )


#TODO: inheritate from bluecopper base class
class TFT_Experiment_Attribute(Base):

    __tablename__ = 'tft_experiment_attributes'

    exp_id = Column('experiment_id', String(100), primary_key = True, nullable = False)
    attr_name_id = Column('attr_name_id', Integer, 
                        ForeignKey('tft_attribute_names.attr_name_id'),
                        nullable=False
                      )
    property_id = Column('property_id', Integer)

    experiment = relationship("TFT_Experiment")
    attribute_name = relationship("TFT_Attribute_Name")

    # @validates()

    def __repr__ (self):
        return "<TFT_Experiment_Attributes(exp_id='%s', attr_name_id='%s', property_id='%s')>" % (
                self.exp_id, self.attr_name_id, self.property_id
                )


#TODO: inheritate from bluecopper base class
class TFT_Attribute_Name(Base):

    __tablename__ = 'tft_attribute_names'

    attr_name_id = Column('attr_name_id', Integer, primary_key = True, nullable = False)
    attr_name = Column('attr_name', String)

    schema_attribute = relationship("TFT_Schema_Attribute")
    sample_attribute = relationship("TFT_Sample_Attribute")
    experiment_attribute = relationship("TFT_Experiment_Attribute")

    # @validates()

    def __repr__ (self):
        return "<TFT_Attribute_Names(attr_name_id='%s', attr_name='%s')>" % (
                self.attr_name_id, self.attr_name
                )


#TODO: inheritate from bluecopper base class
class TFT_Schema_Attribute(Base):

    __tablename__ = 'tft_schema_attribute'

    schema_id = Column('schema_id', Integer, primary_key = True, nullable = False)
    schema_name = Column('schema_name', String)
    attr_name_id = Column('attr_name_id', Integer, ForeignKey('tft_attribute_names.attr_name_id'), nullable=False)
    attr_is_required = Column('attr_is_required', String)
    attr_is_group = Column('attr_is_group', String)
    attr_is_identifier = Column('attr_is_identifier', Integer, ForeignKey('tft_identifier_source.attr_name_id', nullable=False))
    attr_is_annotation = Column('attr_is_annotation', String)

    schema_attribute = relationship("TFT_Experiment")
    attribute_names = relationship("TFT_Attribute_Name")

    # @validates()

    def __repr__ (self):
        return "<TFT_Schema_Attribute(schema_id='%s', schema_name='%s', attr_name_id='%s', attr_is_required='%s', attr_is_group='%s', attr_is_identifier='%s', attr_is_annotation='%s')>" % (
                self.schema_id, self.schema_name, self.attr_name_id, self.attr_is_required, self.attr_is_group, self.attr_is_identifier, self.attr_is_annotation
                )


#TODO: inheritate from bluecopper base class
class TFT_Identifier_Sourc(Base):

    __tablename__ = 'tft_identifier_source'

    attr_name_id = Column('attr_name_id', Integer, primary_key = True, nullable = False)
    attr_url = Column('attr_url', String)

    schema_attribute = relationship("TFT_Schema_Attribute")

    # @validates()

    def __repr__ (self):
        return "<TFT_Identifier_Source(attr_name_id='%s', attr_url='%s')>" % (
                self.attr_name_id, self.attr_url
                )


#TODO: inheritate from bluecopper base class
class TFT_Experiment_Run(Base):

    __tablename__ = 'tft_experiment_run'

    run_id = Column('run_id', String)
    exp_id = Column('exp_id', String)

    # @validates()

    def __repr__ (self):
        return "<TFT_Experiment_Run(run_id='%s', exp_id='%s')>" % (
                self.run_id, self.exp_id
                )


#TODO: inheritate from bluecopper base class
class TFT_Run_Sample(Base):

    __tablename__ = 'tft_run_sample'

    run_id = Column('run_id', String)
    sample_id = Column('sample_id', String)

    # @validates()

    def __repr__ (self):
        return "<TFT_Run_Sample(run_id='%s', sample_id='%s')>" % (
                self.run_id, self.sample_id
                )


#TODO: inheritate from bluecopper base class
class TFT_Exp_Analysis(Base):

    __tablename__ = 'tft_exp_analysis'

    exp_id = Column('exp_id', String)
    analysis_id = Column('analysis_id', String)

    # @validates()

    def __repr__ (self):
        return "<TFT_Exp_Analysis(exp_id='%s', analysis_id='%s')>" % (
                self.exp_id, self.analysis_id
                )


#TODO: inheritate from bluecopper base class
class TFT_Sample_Attributes(Base):

    __tablename__ = 'tft_sample_attributes'

    sample_id = Column('sample_id', String)
    attr_name_id = Column('attr_name_id', String)
    attr_value_id = Column('attr_value_id', String)

    # @validates()

    def __repr__ (self):
        return "<TFT_Sample_Attributes(sample_id='%s', attr_name_id='%s', attr_value_id='%s')>" % (
                self.sample_id, self.attr_name_id, self.attr_value_id
                )


#TODO: inheritate from bluecopper base class
class TFT_Analysis_Comparisons(Base):

    __tablename__ = 'tft_analysis_comparisons'

    analysis_id = Column('analysis_id', String)
    comparison_id = Column('comparison_id', String)

    # @validates()

    def __repr__ (self):
        return "<TFT_Analysis_Comparisons(analysis_id='%s', comparison_id='%s')>" % (
                self.analysis_id, self.comparison_id
                )


#TODO: inheritate from bluecopper base class
class TFT_Property_Relations(Base):

    __tablename__ = 'tft_property_relations'

    relation_id = Column('relation_id', String)
    parent_prop = Column('parent_prop', String)
    child_prop = Column('child_prop', String)

    # @validates()

    def __repr__ (self):
        return "<TFT_Property_Relations(relation_id='%s', parent_prop='%s', child_prop='%s')>" % (
                self.relation_id, self.parent_prop, self.child_prop
                )


#TODO: inheritate from bluecopper base class
class TFT_Comparisons(Base):

    __tablename__ = 'tft_comparisons'

    comparison_id = Column('comparison_id', String)
    attr_value_id_a = Column('attr_value_id_a', String)
    attr_value_id_b = Column('attr_value_id_b', String)
    contrast = Column('contrast', String)
    comparison_name = Column('comparison_name', String)

    # @validates()

    def __repr__ (self):
        return "<TFT_Comparisons(comparison_id='%s', attr_value_id_a='%s', attr_value_id_b='%s', contrast='%s', comparison_name='%s')>" % (
                self.comparison_id, self.attr_value_id_a, self.attr_value_id_b, self.contrast, self.comparison_name
                )

