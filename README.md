# Designecommerceproductu

Backend API for Designecommerceproductu

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI + SQLAlchemy
- **Frontend Source**: GitHub ([Repository](https://github.com/HimaShankarReddyEguturi/Designecommerceproductui.git))

## Project Structure

```
Designecommerceproductu/
├── frontend/          # Frontend application
├── backend/           # Backend API
├── README.md          # This file
└── docker-compose.yml # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
```

## Features

- Product management
- Order management
- Customer management
- JWT authentication

## API Endpoints

- `GET /api/products` - Get all products.
- `GET /api/products/{product_id}` - Get product details.
- `POST /api/products` - Create new product.
- `PUT /api/products/{product_id}` - Update product.
- `DELETE /api/products/{product_id}` - Delete product.
- `POST /api/orders` - Create new order.
- `GET /api/orders` - Get all orders.
- `GET /api/orders/{order_id}` - Get order details.
- `PUT /api/orders/{order_id}` - Update order.
- `DELETE /api/orders/{order_id}` - Delete order.

## License

MIT
