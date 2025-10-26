# myGINNE FastAPI Demo

A simple FastAPI project inspired by **myGINNE**, Egypt’s fastest grocery and retail platform.

This demo simulates managing **retailers, products, and orders** using FastAPI.

---

## Features

- Register retailers
- Add and list products
- Create and list orders
- Interactive API docs via Swagger UI

---

## Setup Instructions

1. Clone the repo
```bash
git clone https://github.com/akshatverma13/myGINNE-FastAPI-demo-project.git
cd myginne-fastapi-demo


Create virtual environment

python -m venv venv


Activate virtual environment

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Install dependencies

pip install -r requirements.txt


Run the FastAPI server

uvicorn main:app --reload


Open browser to http://127.0.0.1:8000/docs

Test all endpoints interactively.

Endpoints

POST /retailers – Add a retailer

GET /retailers – List retailers

POST /products – Add a product

GET /products – List products

POST /orders – Create an order

GET /orders – List orders
