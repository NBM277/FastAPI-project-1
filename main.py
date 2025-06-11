from fastapi import FastAPI
from app.routers import staff, customer, car

app = FastAPI()
app.include_router(staff.router)
app.include_router(customer.router)
app.include_router(car.router)
