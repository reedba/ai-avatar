# AI Avatar

An interactive AI avatar application featuring speech-to-text and text-to-speech capabilities with live interaction. Built with FastAPI backend and React frontend.

## Project Structure

```
ai-avatar/
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── api/         # API routes
│   │   ├── core/        # Core configuration
│   │   ├── models/      # Pydantic models
│   │   ├── services/    # Business logic
│   │   └── main.py      # FastAPI application
│   ├── requirements.txt
│   ├── .env.example
│   └── run.py
├── frontend/             # React frontend
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
└── README.md
```

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn

### Backend Setup (FastAPI)

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Create a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create environment file:**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env with your preferred settings
   ```

5. **Run the FastAPI server:**
   ```bash
   # Option 1: Using the run script
   python run.py
   
   # Option 2: Using uvicorn directly
   uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
   ```

   The API will be available at: `http://localhost:8000`
   
   Interactive API docs: `http://localhost:8000/docs`

### Frontend Setup (React)

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

   The React app will be available at: `http://localhost:5173`

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ai-avatar
   ```

2. **Start the backend:**
   ```bash
   cd backend
   python -m venv venv
   venv\Scripts\activate  # Windows
   # source venv/bin/activate  # macOS/Linux
   pip install -r requirements.txt
   cp .env.example .env
   python run.py
   ```

3. **Start the frontend (in a new terminal):**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

4. **Access the application:**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## API Endpoints

### Health Check
- `GET /health` - Health check endpoint

### Avatars
- `POST /api/v1/avatar/` - Create a new avatar
- `GET /api/v1/avatar/` - Get all avatars
- `GET /api/v1/avatar/{avatar_id}` - Get avatar by ID
- `PUT /api/v1/avatar/{avatar_id}` - Update avatar
- `DELETE /api/v1/avatar/{avatar_id}` - Delete avatar

### Users
- `POST /api/v1/users/` - Create a new user
- `GET /api/v1/users/` - Get all users
- `GET /api/v1/users/{user_id}` - Get user by ID

## Development

### Backend Development
- The FastAPI server runs with hot reload enabled
- API documentation is automatically generated at `/docs`
- Configuration is managed through environment variables

### Frontend Development
- Vite provides fast hot module replacement
- React components are in the `src/` directory
- API calls should be made to `http://localhost:8000`

## Technologies Used

### Backend
- **FastAPI** - Modern Python web framework
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - ASGI server implementation

### Frontend
- **React** - JavaScript library for building user interfaces
- **Vite** - Fast build tool and development server
- **Axios** - HTTP client for API requests

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
