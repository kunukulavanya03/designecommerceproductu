# designecommerceproductu

Backend API for designecommerceproductu

## Tech Stack

- **Frontend**: React
- **Backend**: FastAPI + SQLAlchemy
- **Frontend Source**: GitHub ([Repository](https://github.com/HimaShankarReddyEguturi/Designecommerceproductui.git))

## Project Structure

```
designecommerceproductu/
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

- user registration
- user login
- product management

## API Endpoints

- `POST /api/register` - Endpoint for user registration. Accepts username, email, and password.
- `POST /api/login` - Endpoint for user login. Accepts credentials and returns a JWT token.
- `GET /api/products` - Endpoint to retrieve all products. Requires authentication.
- `POST /api/admin/products` - Endpoint for admins to create new products. Requires admin authentication.
- `PUT /api/admin/products/{product_id}` - Endpoint for admins to update existing products. Requires admin authentication.
- `DELETE /api/admin/products/{product_id}` - Endpoint for admins to delete products. Requires admin authentication.

## License

MIT
