from fastapi import APIRouter, Depends, HTTPException, status
from app.database import get_db
from sqlalchemy.orm import Session
from typing import List
from app.model import Car as CarModel
from app.schemas import Car, CarCreate


router = APIRouter(prefix="/cars", tags=["Cars"])


@router.post("/", response_model=Car, status_code=status.HTTP_201_CREATED)
async def create_car(car: CarCreate, db: Session = Depends(get_db)):
    new_car = CarModel(**car.dict())
    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    return new_car



@router.get("/", response_model=List[Car])
async def get_cars(db: Session = Depends(get_db)):
    return db.query(CarModel).all()


@router.get("/{car_id}", response_model=Car)
async def get_car(car_id: int, db: Session = Depends(get_db)):
    car = db.query(CarModel).filter(CarModel.id == car_id).first()
    if not car:
        raise HTTPException(status_code=404, detail="Car not found")
    return car


@router.put("/{car_id}", response_model=Car)
async def update_car(car_id: int, car: CarCreate, db: Session = Depends(get_db)):
    db_car = db.query(CarModel).filter(CarModel.id == car_id).first()
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    
    for key, value in car.dict().items():
        setattr(db_car, key, value)

    db.commit()
    db.refresh(db_car)
    return db_car


@router.delete("/{car_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_car(car_id: int, db: Session = Depends(get_db)):
    db_car = db.query(CarModel).filter(CarModel.id == car_id).first()
    if not db_car:
        raise HTTPException(status_code=404, detail="Car not found")
    db.delete(db_car)
    db.commit()
    return None

