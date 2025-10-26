# myGINNE FastAPI Demo

A simple FastAPI project inspired by **myGINNE**, Egypt's fastest grocery and retail platform. This demo simulates managing **retailers, products, and orders** using FastAPI.

---

## Features

- 🏪 Register retailers
- 📦 Add and list products
- 🛒 Create and list orders
- 📚 Interactive API docs via Swagger UI

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/akshatverma13/myGINNE-FastAPI-demo-project.git
cd myginne-fastapi-demo
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the FastAPI Server

```bash
uvicorn main:app --reload
```

### 6. Access the API

Open your browser and navigate to:
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Test all endpoints interactively through the Swagger UI.

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/retailers` | Add a new retailer |
| `GET` | `/retailers` | List all retailers |
| `POST` | `/products` | Add a new product |
| `GET` | `/products` | List all products |
| `POST` | `/orders` | Create a new order |
| `GET` | `/orders` | List all orders |

---

## Example Usage

### Add a Retailer

```bash
curl -X POST "http://127.0.0.1:8000/retailers" \
  -H "Content-Type: application/json" \
  -d '{"name": "Cairo Supermarket", "location": "Cairo, Egypt"}'
```

### Add a Product

```bash
curl -X POST "http://127.0.0.1:8000/products" \
  -H "Content-Type: application/json" \
  -d '{"name": "Fresh Milk", "price": 25.0, "retailer_id": 1}'
```

### Create an Order

```bash
curl -X POST "http://127.0.0.1:8000/orders" \
  -H "Content-Type: application/json" \
  -d '{"product_ids": [1, 2], "customer_name": "Ahmed Ali"}'
```

---

## Technologies Used

- **FastAPI** - Modern, fast web framework for building APIs
- **Uvicorn** - ASGI server for running FastAPI
- **Python 3.8+** - Programming language

---

## Project Structure

```
myginne-fastapi-demo/
│
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
└── venv/               # Virtual environment (not tracked in git)
```

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Contact

For questions or feedback, please reach out to [Akshat Verma](https://github.com/akshatverma13).

---

**Happy Coding! 🚀**
