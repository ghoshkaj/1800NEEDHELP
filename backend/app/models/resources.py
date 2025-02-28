from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)  # hotel, shelter, etc.
    address = Column(String)
    city = Column(String)
    state = Column(String(2))
    zip_code = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    created_at = Column(DateTime, server_default=func.now())

class ResourceAttribute(Base):
    __tablename__ = "resource_attributes"

    id = Column(Integer, primary_key=True, index=True)
    resource_id = Column(Integer, ForeignKey("resources.id"))
    key = Column(String)
    value = Column(String)
    created_at = Column(DateTime, server_default=func.now())

class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    resource_id = Column(Integer, ForeignKey("resources.id"), unique=True)
    units_available = Column(Integer)
    last_updated = Column(DateTime, server_default=func.now(), onupdate=func.now())

class InventoryHistory(Base):
    __tablename__ = "inventory_history"

    id = Column(Integer, primary_key=True, index=True)
    inventory_id = Column(Integer, ForeignKey("inventory.id"))
    previous_units = Column(Integer)
    new_units = Column(Integer)
    change_type = Column(String)  # 'update', 'reservation'
    created_at = Column(DateTime, server_default=func.now()) 