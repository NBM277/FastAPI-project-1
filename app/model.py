from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from datetime import datetime
from typing import Optional, List

class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(15), unique=True, nullable=False)  
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow())
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    staff_id: Mapped[int] = mapped_column(ForeignKey("staff.id"), nullable=False)

    staff: Mapped["Staff"] = relationship("Staff", back_populates="customers")
    cars: Mapped[List["Car"]] = relationship("Car", back_populates="customer", cascade="all, delete-orphan")

class Car(Base):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id", ondelete="CASCADE"), nullable=False)
    brand: Mapped[str] = mapped_column(String(50), nullable=False)  
    model: Mapped[str] = mapped_column(String(50), nullable=False)  
    year: Mapped[int] = mapped_column(Integer, nullable=False)  
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    color: Mapped[str] = mapped_column(String(20), nullable=False)

    customer: Mapped["Customer"] = relationship("Customer", back_populates="cars")

class Staff(Base):
    __tablename__ = "staff"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    phone_number: Mapped[str] = mapped_column(String(15), unique=True, nullable=False)  
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow())

    customers: Mapped[List["Customer"]] = relationship("Customer", back_populates="staff")