
#TODO: inheritate from bluecopper base class
class TFT_Experimen(Base):

    __tablename__ = 'tft_experiment'

    exp_id = Column('exp_id', String)
    schema_id = Column('schema_id', String)

    # @validates()

    def __repr__ (self):
        return "<TFT_Experiment(exp_id='%s', schema_id='%s')>" % (
                self.exp_id, self.schema_id
                )


#TODO: inheritate from bluecopper base class
class TFT_Experiment_Attribute(Base):

    __tablename__ = 'tft_experiment_attributes'

    exp_id = Column('exp_id', String)
    attr_name_id = Column('attr_name_id', String)
    property_id = Column('property_id', String)

    # @validates()

    def __repr__ (self):
        return "<TFT_Experiment_Attributes(exp_id='%s', attr_name_id='%s', property_id='%s')>" % (
                self.exp_id, self.attr_name_id, self.property_id
                )


#TODO: inheritate from bluecopper base class
class TFT_Attribute_Name(Base):

    __tablename__ = 'tft_attribute_names'

    attr_name_id = Column('attr_name_id', String)
    attr_name = Column('attr_name', String)

    # @validates()

    def __repr__ (self):
        return "<TFT_Attribute_Names(attr_name_id='%s', attr_name='%s')>" % (
                self.attr_name_id, self.attr_name
                )


#TODO: inheritate from bluecopper base class
class TFT_Schema_Att(Base):

    __tablename__ = 'tft_schema_attr'

    schema_id = Column('schema_id', String)
    schema_name = Column('schema_name', String)
    attr_name_id = Column('attr_name_id', String)
    attr_is_required = Column('attr_is_required', String)
    attr_is_group = Column('attr_is_group', String)
    attr_is_identifier = Column('attr_is_identifier', String)
    attr_is_annotation = Column('attr_is_annotation', String)

    # @validates()

    def __repr__ (self):
        return "<TFT_Schema_Attr(schema_id='%s', schema_name='%s', attr_name_id='%s', attr_is_required='%s', attr_is_group='%s', attr_is_identifier='%s', attr_is_annotation='%s')>" % (
                self.schema_id, self.schema_name, self.attr_name_id, self.attr_is_required, self.attr_is_group, self.attr_is_identifier, self.attr_is_annotation
                )


#TODO: inheritate from bluecopper base class
class TFT_Identifier_Sourc(Base):

    __tablename__ = 'tft_identifier_source'

    attr_name_id = Column('attr_name_id', String)
    attr_url = Column('attr_url', String)

    # @validates()

    def __repr__ (self):
        return "<TFT_Identifier_Source(attr_name_id='%s', attr_url='%s')>" % (
                self.attr_name_id, self.attr_url
                )


#TODO: inheritate from bluecopper base class
class TFT_Experiment_Ru(Base):

    __tablename__ = 'tft_experiment_run'

    run_id = Column('run_id', String)
    exp_id = Column('exp_id', String)

    # @validates()

    def __repr__ (self):
        return "<TFT_Experiment_Run(run_id='%s', exp_id='%s')>" % (
                self.run_id, self.exp_id
                )


#TODO: inheritate from bluecopper base class
class TFT_Run_Sampl(Base):

    __tablename__ = 'tft_run_sample'

    run_id = Column('run_id', String)
    sample_id = Column('sample_id', String)

    # @validates()

    def __repr__ (self):
        return "<TFT_Run_Sample(run_id='%s', sample_id='%s')>" % (
                self.run_id, self.sample_id
                )


#TODO: inheritate from bluecopper base class
class TFT_Exp_Analysi(Base):

    __tablename__ = 'tft_exp_analysis'

    exp_id = Column('exp_id', String)
    analysis_id = Column('analysis_id', String)

    # @validates()

    def __repr__ (self):
        return "<TFT_Exp_Analysis(exp_id='%s', analysis_id='%s')>" % (
                self.exp_id, self.analysis_id
                )


#TODO: inheritate from bluecopper base class
class TFT_Sample_Attribute(Base):

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
class TFT_Analysis_Comparison(Base):

    __tablename__ = 'tft_analysis_comparisons'

    analysis_id = Column('analysis_id', String)
    comparison_id = Column('comparison_id', String)

    # @validates()

    def __repr__ (self):
        return "<TFT_Analysis_Comparisons(analysis_id='%s', comparison_id='%s')>" % (
                self.analysis_id, self.comparison_id
                )


#TODO: inheritate from bluecopper base class
class TFT_Property_Relation(Base):

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
class TFT_Comparison(Base):

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


#TODO: inheritate from bluecopper base class
class (Base):

    __tablename__ = ''

