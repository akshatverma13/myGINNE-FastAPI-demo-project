from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="myGINNE Retail Demo API",
    description="A simple FastAPI demo inspired by myGINNE's mission to digitize local retail operations.",
    version="1.0.0"
)

class Retailer(BaseModel):
    store_name: str
    owner_name: str
    location: str
    contact: str

class Product(BaseModel):
    product_name: str
    price: float
    quantity: int

class Order(BaseModel):
    retailer_name: str
    items: List[str]
    total_amount: float

retailers_db = []
products_db = []
orders_db = []

@app.post("/retailers")
def register_retailer(retailer: Retailer):
    retailers_db.append(retailer)
    return {"message": "Retailer registered successfully", "total_retailers": len(retailers_db)}

@app.get("/retailers")
def list_retailers():
    return {"registered_retailers": retailers_db}

@app.post("/products")
def add_product(product: Product):
    products_db.append(product)
    return {"message": "Product added", "total_products": len(products_db)}

@app.get("/products")
def list_products():
    return {"available_products": products_db}

  
@app.post("/orders")
def create_order(order: Order):
    orders_db.append(order)
    return {"message": "Order created successfully", "total_orders": len(orders_db)}

@app.get("/orders")
def list_orders():
    return {"recent_orders": orders_db}
    
@app.get("/")
def home():
    return {
        "message": "Welcome to myGINNE Retail Demo API",
        "description": "This demo simulates how retailers, products, and orders could be managed using FastAPI.",
        "endpoints": ["/retailers", "/products", "/orders"]
    }
