"""
ICY - AI Influencer Outreach Platform Backend
FastAPI server with simulated Instagram and YouTube API integrations
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import uvicorn
import asyncio
import random
from datetime import datetime, timedelta
import json

# Import our API modules
from api.instagram_api import InstagramAPI
from api.youtube_api import YouTubeAPI
from api.ai_analyzer import AIAnalyzer
from api.message_generator import MessageGenerator
from models.influencer import Influencer, InfluencerProfile
from models.campaign import Campaign, CampaignMetrics
from models.brand import BrandData

# Initialize FastAPI app
app = FastAPI(
    title="ICY AI Influencer Platform API",
    description="Backend API for AI-powered influencer discovery and outreach",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize API clients
instagram_api = InstagramAPI()
youtube_api = YouTubeAPI()
ai_analyzer = AIAnalyzer()
message_generator = MessageGenerator()

# In-memory storage (replace with database in production)
campaigns_db: Dict[str, Campaign] = {}
discovery_tasks: Dict[str, Dict] = {}

# Request/Response Models
class DiscoveryRequest(BaseModel):
    brand_data: BrandData
    platforms: List[str]
    max_results: int = 50

class DiscoveryResponse(BaseModel):
    task_id: str
    status: str
    message: str

class InfluencerListResponse(BaseModel):
    influencers: List[InfluencerProfile]
    total_count: int
    high_matches: int
    medium_matches: int
    low_matches: int

class MessageRequest(BaseModel):
    influencer_id: str
    brand_data: BrandData
    message_type: str = "collaboration"

class MessageResponse(BaseModel):
    message: str
    subject: str
    personalization_score: float

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "ICY AI Influencer Platform API",
        "version": "1.0.0",
        "status": "active",
        "endpoints": {
            "discovery": "/api/v1/discovery",
            "influencers": "/api/v1/influencers",
            "messages": "/api/v1/messages",
            "campaigns": "/api/v1/campaigns",
            "docs": "/docs"
        }
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "services": {
            "instagram_api": "connected",
            "youtube_api": "connected",
            "ai_analyzer": "active",
            "message_generator": "active"
        }
    }

# Discovery endpoints
@app.post("/api/v1/discovery/start", response_model=DiscoveryResponse)
async def start_discovery(request: DiscoveryRequest, background_tasks: BackgroundTasks):
    """Start influencer discovery process"""
    task_id = f"task_{random.randint(10000, 99999)}"
    
    # Initialize discovery task
    discovery_tasks[task_id] = {
        "status": "started",
        "progress": 0,
        "brand_data": request.brand_data.dict(),
        "platforms": request.platforms,
        "max_results": request.max_results,
        "created_at": datetime.now().isoformat(),
        "influencers": []
    }
    
    # Start background discovery process
    background_tasks.add_task(run_discovery_process, task_id, request)
    
    return DiscoveryResponse(
        task_id=task_id,
        status="started",
        message="Discovery process initiated. Use task_id to check progress."
    )

@app.get("/api/v1/discovery/{task_id}/status")
async def get_discovery_status(task_id: str):
    """Get discovery task status"""
    if task_id not in discovery_tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task = discovery_tasks[task_id]
    return {
        "task_id": task_id,
        "status": task["status"],
        "progress": task["progress"],
        "created_at": task["created_at"],
        "influencers_found": len(task["influencers"])
    }

@app.get("/api/v1/discovery/{task_id}/results", response_model=InfluencerListResponse)
async def get_discovery_results(task_id: str):
    """Get discovery results"""
    if task_id not in discovery_tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    
    task = discovery_tasks[task_id]
    if task["status"] != "completed":
        raise HTTPException(status_code=400, detail="Discovery not completed yet")
    
    influencers = task["influencers"]
    
    # Calculate match distribution
    high_matches = len([i for i in influencers if i["match_score"] >= 90])
    medium_matches = len([i for i in influencers if 80 <= i["match_score"] < 90])
    low_matches = len([i for i in influencers if i["match_score"] < 80])
    
    return InfluencerListResponse(
        influencers=[InfluencerProfile(**inf) for inf in influencers],
        total_count=len(influencers),
        high_matches=high_matches,
        medium_matches=medium_matches,
        low_matches=low_matches
    )

# Influencer endpoints
@app.get("/api/v1/influencers/{influencer_id}")
async def get_influencer_details(influencer_id: str):
    """Get detailed influencer information"""
    # Simulate fetching from database
    await asyncio.sleep(0.5)  # Simulate API delay
    
    # Generate mock detailed data
    influencer_data = await ai_analyzer.get_detailed_analysis(influencer_id)
    return influencer_data

@app.get("/api/v1/influencers/{influencer_id}/content")
async def get_influencer_content(influencer_id: str, limit: int = 10):
    """Get recent content from influencer"""
    # Determine platform and fetch content
    if "instagram" in influencer_id:
        content = await instagram_api.get_recent_posts(influencer_id, limit)
    else:
        content = await youtube_api.get_recent_videos(influencer_id, limit)
    
    return {"content": content, "total": len(content)}

# Message generation endpoints
@app.post("/api/v1/messages/generate", response_model=MessageResponse)
async def generate_message(request: MessageRequest):
    """Generate personalized outreach message"""
    message_data = await message_generator.generate_personalized_message(
        request.influencer_id,
        request.brand_data,
        request.message_type
    )
    
    return MessageResponse(**message_data)

@app.post("/api/v1/messages/send")
async def send_message(influencer_id: str, message: str, subject: str):
    """Send message to influencer (simulated)"""
    # Simulate sending message
    await asyncio.sleep(1)
    
    # Random success/failure for demo
    success = random.choice([True, True, True, False])  # 75% success rate
    
    if success:
        return {
            "status": "sent",
            "message": "Message sent successfully",
            "sent_at": datetime.now().isoformat()
        }
    else:
        return {
            "status": "failed",
            "message": "Failed to send message",
            "error": "Influencer inbox full or unavailable"
        }

# Campaign management endpoints
@app.post("/api/v1/campaigns")
async def create_campaign(campaign_data: Dict[str, Any]):
    """Create new campaign"""
    campaign_id = f"campaign_{random.randint(10000, 99999)}"
    
    campaign = Campaign(
        id=campaign_id,
        name=campaign_data.get("name", "Untitled Campaign"),
        brand_data=BrandData(**campaign_data["brand_data"]),
        created_at=datetime.now(),
        status="active"
    )
    
    campaigns_db[campaign_id] = campaign
    
    return {"campaign_id": campaign_id, "status": "created"}

@app.get("/api/v1/campaigns/{campaign_id}/metrics")
async def get_campaign_metrics(campaign_id: str):
    """Get campaign performance metrics"""
    if campaign_id not in campaigns_db:
        raise HTTPException(status_code=404, detail="Campaign not found")
    
    # Generate mock metrics
    metrics = CampaignMetrics(
        total_reach=random.randint(100000, 5000000),
        total_engagement=random.randint(5000, 200000),
        response_rate=round(random.uniform(15.0, 35.0), 1),
        conversion_rate=round(random.uniform(1.5, 8.0), 1),
        roi_percentage=round(random.uniform(120.0, 300.0), 1),
        messages_sent=random.randint(20, 100),
        responses_received=random.randint(5, 30),
        collaborations_confirmed=random.randint(2, 15)
    )
    
    return metrics.dict()

# Background task for discovery process
async def run_discovery_process(task_id: str, request: DiscoveryRequest):
    """Background task to simulate influencer discovery"""
    task = discovery_tasks[task_id]
    
    try:
        # Simulate discovery steps
        steps = [
            ("Scanning Instagram...", 25),
            ("Scanning YouTube...", 50),
            ("Analyzing content...", 75),
            ("Calculating matches...", 100)
        ]
        
        for step_name, progress in steps:
            task["status"] = f"processing: {step_name}"
            task["progress"] = progress
            await asyncio.sleep(2)  # Simulate processing time
        
        # Generate mock influencers based on brand data
        influencers = []
        
        # Instagram influencers
        if "instagram" in request.platforms:
            instagram_influencers = await instagram_api.discover_influencers(
                request.brand_data, request.max_results // 2
            )
            influencers.extend(instagram_influencers)
        
        # YouTube influencers
        if "youtube" in request.platforms:
            youtube_influencers = await youtube_api.discover_influencers(
                request.brand_data, request.max_results // 2
            )
            influencers.extend(youtube_influencers)
        
        # Analyze and score influencers
        analyzed_influencers = []
        for influencer in influencers:
            analysis = await ai_analyzer.analyze_influencer(influencer, request.brand_data)
            analyzed_influencers.append(analysis)
        
        # Sort by match score
        analyzed_influencers.sort(key=lambda x: x["match_score"], reverse=True)
        
        task["influencers"] = analyzed_influencers
        task["status"] = "completed"
        task["completed_at"] = datetime.now().isoformat()
        
    except Exception as e:
        task["status"] = "failed"
        task["error"] = str(e)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
