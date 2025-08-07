# ICY AI Influencer Platform - Backend API

This is the backend API for the ICY AI Influencer Platform, built with FastAPI and simulating real Instagram and YouTube API integrations for demonstration purposes.

## 🚀 Features

### Core API Endpoints
- **Influencer Discovery**: AI-powered influencer search across Instagram and YouTube
- **Content Analysis**: Automated content quality and brand alignment analysis
- **Message Generation**: Personalized outreach message creation
- **Campaign Management**: Complete campaign lifecycle management
- **Performance Tracking**: Real-time analytics and ROI tracking

### Simulated Integrations
- **Instagram Graph API**: Profile data, posts, stories, audience insights
- **YouTube Data API v3**: Channel data, videos, analytics, demographics
- **AI Content Analyzer**: Brand alignment, authenticity scoring, risk assessment
- **Message Generator**: Personalized outreach with multiple brand tones

## 🛠️ Tech Stack

- **FastAPI 0.104.1** - Modern, fast web framework for building APIs
- **Pydantic 2.5.0** - Data validation using Python type annotations
- **Uvicorn** - Lightning-fast ASGI server
- **AsyncIO** - Asynchronous programming for high performance
- **Python 3.9+** - Modern Python with type hints

## 📁 Project Structure

```
backend/
├── main.py                 # FastAPI application entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── api/                   # API integration modules
│   ├── instagram_api.py   # Instagram API simulation
│   ├── youtube_api.py     # YouTube API simulation
│   ├── ai_analyzer.py     # AI analysis engine
│   └── message_generator.py # Message generation AI
├── models/                # Pydantic data models
│   ├── influencer.py      # Influencer data models
│   ├── brand.py          # Brand data models
│   └── campaign.py       # Campaign data models
└── docs/                 # API documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Installation

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the development server**
   ```bash
   python main.py
   ```
   
   Or using uvicorn directly:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

5. **Access the API**
   - API Base URL: `http://localhost:8000`
   - Interactive Docs: `http://localhost:8000/docs`
   - ReDoc Documentation: `http://localhost:8000/redoc`

## 📚 API Endpoints

### Core Endpoints

#### Health Check
```http
GET /health
```
Returns API health status and service availability.

#### Discovery
```http
POST /api/v1/discovery/start
```
Start influencer discovery process with brand criteria.

```http
GET /api/v1/discovery/{task_id}/status
```
Check discovery task progress.

```http
GET /api/v1/discovery/{task_id}/results
```
Get discovery results with influencer profiles.

#### Influencers
```http
GET /api/v1/influencers/{influencer_id}
```
Get detailed influencer information and AI analysis.

```http
GET /api/v1/influencers/{influencer_id}/content
```
Get recent content from influencer with engagement data.

#### Messages
```http
POST /api/v1/messages/generate
```
Generate personalized outreach message for specific influencer.

```http
POST /api/v1/messages/send
```
Send message to influencer (simulated).

#### Campaigns
```http
POST /api/v1/campaigns
```
Create new campaign.

```http
GET /api/v1/campaigns/{campaign_id}/metrics
```
Get campaign performance metrics and analytics.

## 🤖 AI Features

### Smart Discovery Algorithm
- **Cross-platform search** across Instagram and YouTube
- **Brand alignment scoring** using content analysis
- **Audience matching** based on demographics and interests
- **Authenticity detection** to identify fake followers

### Content Analysis Engine
- **Brand safety assessment** for controversial content
- **Content quality scoring** based on visual and textual analysis
- **Engagement authenticity** detection
- **Trend analysis** and hashtag performance

### Message Generation AI
- **Personalized outreach** referencing recent content
- **Brand tone matching** (professional, friendly, luxury, playful)
- **A/B testing** for message optimization
- **Response prediction** scoring

## 📊 Sample Data

The API includes realistic mock data for demonstration:

### Influencers
- **Sarah Chen** (@sarahstyle) - 125K followers, Fashion & Lifestyle
- **Alex Rodriguez** (@alexfitness) - 89K followers, Fitness & Wellness  
- **Emma Thompson** (@emmaeats) - 67K followers, Food & Cooking

### Metrics
- **247 total influencers** in discovery results
- **24% average response rate** for outreach
- **91% average authenticity score**
- **+180% average ROI** on campaigns

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the backend directory:

```env
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True

# Database (for production)
DATABASE_URL=postgresql://user:password@localhost/icy_db

# External APIs (for real integration)
INSTAGRAM_ACCESS_TOKEN=your_instagram_token
YOUTUBE_API_KEY=your_youtube_api_key
OPENAI_API_KEY=your_openai_key

# Redis (for caching)
REDIS_URL=redis://localhost:6379

# Email Service (for outreach)
SENDGRID_API_KEY=your_sendgrid_key
```

### CORS Configuration
The API is configured to accept requests from:
- `http://localhost:8080` (Frontend development)
- `http://localhost:3000` (Alternative frontend port)

## 🧪 Testing

### Run Tests
```bash
pytest
```

### Run with Coverage
```bash
pytest --cov=. --cov-report=html
```

### Load Testing
```bash
locust -f tests/load_test.py --host=http://localhost:8000
```

## 📈 Performance

### Optimization Features
- **Async/await** for non-blocking operations
- **Background tasks** for long-running processes
- **Response caching** for frequently accessed data
- **Database connection pooling**
- **Rate limiting** to prevent abuse

### Monitoring
- **Health checks** for service monitoring
- **Structured logging** with request tracing
- **Performance metrics** collection
- **Error tracking** with Sentry integration

## 🔒 Security

### Security Features
- **CORS protection** with allowed origins
- **Request validation** using Pydantic models
- **Rate limiting** on API endpoints
- **Input sanitization** for all user data
- **Error handling** without information leakage

### Authentication (Future)
- JWT token-based authentication
- Role-based access control
- API key management
- OAuth integration

## 🚀 Deployment

### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Production Considerations
- Use PostgreSQL or MySQL for data persistence
- Implement Redis for caching and session storage
- Set up Nginx as reverse proxy
- Configure SSL/TLS certificates
- Implement proper logging and monitoring
- Set up automated backups

## 📖 API Documentation

### Interactive Documentation
Visit `http://localhost:8000/docs` for Swagger UI with:
- Complete API endpoint documentation
- Request/response schemas
- Interactive testing interface
- Authentication examples

### ReDoc Documentation
Visit `http://localhost:8000/redoc` for clean, readable documentation.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

### Code Style
- Follow PEP 8 style guidelines
- Use type hints for all functions
- Add docstrings for all modules and functions
- Format code with Black
- Sort imports with isort

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue on GitHub
- Email: backend-support@icy-platform.com
- Documentation: [API Docs](http://localhost:8000/docs)

---

**Built with ❤️ by the ICY Team**

*Transforming influencer marketing through AI innovation*
