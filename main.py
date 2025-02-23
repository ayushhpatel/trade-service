from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from database import SessionLocal
from models import Order as OrderModel
from sqlalchemy.exc import SQLAlchemyError

app = FastAPI(title="Trade Service API")

# Dependency: get a database session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schema for incoming order data
class Order(BaseModel):
    symbol: str
    price: float
    quantity: int
    order_type: str

# Pydantic schema for responses (includes an id)
class OrderResponse(Order):
    id: int

@app.post("/orders", response_model=OrderResponse)
def create_order(order: Order, db: Session = Depends(get_db)):
    db_order = OrderModel(
        symbol=order.symbol,
        price=order.price,
        quantity=order.quantity,
        order_type=order.order_type
    )
    try:
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error creating order")
    return db_order

@app.get("/orders", response_model=List[OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    orders = db.query(OrderModel).all()
    return orders
