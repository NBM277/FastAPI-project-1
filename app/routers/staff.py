from fastapi import APIRouter, Depends, HTTPException, status
from app.model import Staff as StaffModel
from app.schemas import Staff, StaffCreate
from sqlalchemy.orm import Session
from app.database import get_db
from typing import List

router = APIRouter(prefix="/staff", tags=["Staff"])

@router.post("/", response_model=Staff, status_code=status.HTTP_201_CREATED)
async def create_staff(staff: StaffCreate, db: Session = Depends(get_db)):
    new_staff = StaffModel(**staff.dict())
    db.add(new_staff)
    db.commit()
    db.refresh(new_staff)
    return new_staff


@router.get("/", response_model=List[Staff])
async def get_staffs(db: Session = Depends(get_db)):
    return db.query(StaffModel).all()


@router.get("/{staff_id}", response_model=Staff)
async def get_staff(staff_id: int, db: Session = Depends(get_db)):
    staff = db.query(StaffModel).filter(StaffModel.id == staff_id).first()
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    return staff


@router.put("/{staff_id}", response_model=Staff)
async def update_staff(staff_id: int, staff: StaffCreate, db: Session = Depends(get_db)):
    db_staff = db.query(StaffModel).filter(StaffModel.id == staff_id).first()
    if not db_staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    
    for key, value in staff.dict().items():
        setattr(db_staff, key, value)

    db.commit()
    db.refresh(db_staff)
    return db_staff


@router.delete("/{staff_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_staff(staff_id: int, db: Session = Depends(get_db)):
    db_staff = db.query(StaffModel).filter(StaffModel.id == staff_id).first()
    if not db_staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    db.delete(db_staff)
    db.commit()
    return None
