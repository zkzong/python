import os
import pyexcel
import datetime

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///birth.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)


# here is the destination table
class BirthRegister(Base):
    __tablename__ = 'birth'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    weight = Column(Float)
    birth = Column(Date)

Base.metadata.create_all(engine)

#创建数据
data = [
    ["name", "weight", "birth"],
    ["Adam", 3.4, datetime.date(2017, 2, 3)],
    ["Smith", 4.2, datetime.date(2014, 11, 12)]
]
pyexcel.save_as(array=data,
                dest_file_name="file/birth.xls")

# 导入到Excel文件
session = Session()  # obtain a sql session
pyexcel.save_as(file_name="file/birth.xls",
                name_columns_by_row=0,
                dest_session=session,
                dest_table=BirthRegister)

# 验证结果
sheet = pyexcel.get_sheet(session=session, table=BirthRegister)
print(sheet)
session.close()

