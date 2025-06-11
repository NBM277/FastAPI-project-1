from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class StaffBase(BaseModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    phone_number: str
    created_at: datetime

class StaffCreate(StaffBase):
    pass

class Staff(StaffBase):
    id: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True



class CustomerBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    phone_number: str
    created_at: datetime
    staff_id: int

class CustomerCreate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True




class CarBase(BaseModel):
    brand: str
    year: int
    color: str
    price: int
    customer_id: int
    model: str

class CarCreate(CarBase):
    pass

class Car(CarBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True