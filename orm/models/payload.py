from sqlalchemy import Column, Integer, String, ForeignKey,relationship
from orm.database import db_session
from orm.models.base import BaseModel


class Payload(BaseModel):
    __tablename__ = 'payload'

    id = Column(Integer, primary_key=True, autoincrement=True)
    phone = Column(String(200), default=None, comment='Номер телефона')
    address = Column(String(400), default=None, comment='Адрес')
    email = Column(String(200), default=None, comment='Емаил')
    details = Column(String(200), default=None, comment='ФИО')
    variant_id = Column(Integer, ForeignKey('variant.id'), comment='Вариант')
    region_id = Column(Integer, ForeignKey('region.id'), comment='Регион')
    sub_variant_id = Column(Integer, ForeignKey('sub_variant.id'), comment='Подвариант')

    
