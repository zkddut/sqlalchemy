from ..orm.tft import *
from ..util.readTFT import readTFT
from sqlalchemy import create_engine, MetaData, select
from sqlalchemy.orm import sessionmaker

class backend:
  def __init__(self):
    pass

  def get(self):
    #query from db and show on web page
    print("I am in get")

  def post(self):
    #obtain input from front-end or defaule value
    enginepath = 'sqlite:///test.sqlite'
    tftpathlist = ['Lipidyzer_TFT1.xlsx', 'Lipidyzer_TFT2.xlsx', 'Multiquant_TFT1.xlsx', 'Multiquant_TFT2.xlsx']
    SchemaID = 0
    engine = create_engine(enginepath)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    for tftpath in tftpathlist:
      #read from excel and store into tb
      df = readTFT(tftpath)
      
      ExperimentID = df['Objective'][0]

      print(ExperimentID)
      new_exp = Experiment(experimentID = ExperimentID, schemaID = SchemaID)
      session.add(new_exp)
      session.flush()

      SchemaID += 1
