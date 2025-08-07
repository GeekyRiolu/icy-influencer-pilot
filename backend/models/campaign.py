"""
Campaign Data Models
Pydantic models for campaign management and tracking
"""

from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any, Union
from datetime import datetime, date
from enum import Enum
from .brand import BrandData
from .influencer import InfluencerProfile

class CampaignStatus(str, Enum):
    """Campaign status options"""
    DRAFT = "draft"
    PLANNING = "planning"
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class CollaborationStatus(str, Enum):
    """Individual collaboration status"""
    PENDING = "pending"
    CONTACTED = "contacted"
    NEGOTIATING = "negotiating"
    CONFIRMED = "confirmed"
    IN_PROGRESS = "in_progress"
    CONTENT_SUBMITTED = "content_submitted"
    CONTENT_APPROVED = "content_approved"
    PUBLISHED = "published"
    COMPLETED = "completed"
    DECLINED = "declined"
    CANCELLED = "cancelled"

class ContentType(str, Enum):
    """Types of content deliverables"""
    INSTAGRAM_POST = "instagram_post"
    INSTAGRAM_STORY = "instagram_story"
    INSTAGRAM_REEL = "instagram_reel"
    YOUTUBE_VIDEO = "youtube_video"
    YOUTUBE_SHORT = "youtube_short"
    TIKTOK_VIDEO = "tiktok_video"
    TWITTER_POST = "twitter_post"
    BLOG_POST = "blog_post"
    PODCAST_MENTION = "podcast_mention"

class MessageTemplate(BaseModel):
    """Outreach message template"""
    id: str = Field(description="Template identifier")
    name: str = Field(description="Template name")
    subject_line: str = Field(description="Email subject line")
    message_body: str = Field(description="Message content")
    brand_tone: str = Field(description="Brand tone used")
    personalization_level: float = Field(ge=0, le=1, description="Personalization score")
    success_rate: Optional[float] = Field(ge=0, le=1, description="Historical success rate")
    created_at: datetime = Field(default_factory=datetime.now)

class OutreachMessage(BaseModel):
    """Individual outreach message"""
    id: str = Field(description="Message identifier")
    influencer_id: str = Field(description="Target influencer ID")
    template_id: Optional[str] = Field(description="Template used")
    subject_line: str = Field(description="Email subject")
    message_body: str = Field(description="Message content")
    personalization_score: float = Field(ge=0, le=1, description="Personalization level")
    
    # Status Tracking
    sent_at: Optional[datetime] = Field(description="When message was sent")
    opened_at: Optional[datetime] = Field(description="When message was opened")
    replied_at: Optional[datetime] = Field(description="When influencer replied")
    
    # Response Data
    response_received: bool = Field(default=False, description="Whether response was received")
    response_positive: Optional[bool] = Field(description="Whether response was positive")
    response_text: Optional[str] = Field(description="Response content")
    
    # Follow-up
    follow_up_sent: bool = Field(default=False, description="Whether follow-up was sent")
    follow_up_count: int = Field(default=0, description="Number of follow-ups sent")
    
    created_at: datetime = Field(default_factory=datetime.now)

class ContentDeliverable(BaseModel):
    """Content deliverable specification"""
    id: str = Field(description="Deliverable identifier")
    content_type: ContentType = Field(description="Type of content")
    description: str = Field(description="Deliverable description")
    requirements: List[str] = Field(default=[], description="Specific requirements")
    due_date: Optional[date] = Field(description="Due date for deliverable")
    
    # Approval Process
    requires_approval: bool = Field(default=True, description="Whether approval is required")
    approved: Optional[bool] = Field(description="Approval status")
    approval_notes: Optional[str] = Field(description="Approval feedback")
    approved_at: Optional[datetime] = Field(description="When approved")
    
    # Content URLs
    draft_url: Optional[str] = Field(description="Draft content URL")
    final_url: Optional[str] = Field(description="Final published content URL")
    
    # Performance
    views: Optional[int] = Field(ge=0, description="Content views")
    likes: Optional[int] = Field(ge=0, description="Content likes")
    comments: Optional[int] = Field(ge=0, description="Content comments")
    shares: Optional[int] = Field(ge=0, description="Content shares")
    
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class Collaboration(BaseModel):
    """Individual influencer collaboration"""
    id: str = Field(description="Collaboration identifier")
    campaign_id: str = Field(description="Parent campaign ID")
    influencer_id: str = Field(description="Influencer ID")
    
    # Status and Timeline
    status: CollaborationStatus = Field(description="Current collaboration status")
    started_at: Optional[datetime] = Field(description="When collaboration started")
    expected_completion: Optional[date] = Field(description="Expected completion date")
    completed_at: Optional[datetime] = Field(description="When collaboration completed")
    
    # Financial Terms
    agreed_rate: Optional[float] = Field(ge=0, description="Agreed collaboration rate")
    payment_terms: str = Field(default="net-30", description="Payment terms")
    paid: bool = Field(default=False, description="Whether payment has been made")
    paid_at: Optional[datetime] = Field(description="When payment was made")
    
    # Content Deliverables
    deliverables: List[ContentDeliverable] = Field(default=[], description="Content deliverables")
    
    # Communication
    outreach_messages: List[OutreachMessage] = Field(default=[], description="Outreach messages")
    notes: List[str] = Field(default=[], description="Collaboration notes")
    
    # Performance Tracking
    estimated_reach: Optional[int] = Field(ge=0, description="Estimated reach")
    actual_reach: Optional[int] = Field(ge=0, description="Actual reach achieved")
    estimated_engagement: Optional[int] = Field(ge=0, description="Estimated engagement")
    actual_engagement: Optional[int] = Field(ge=0, description="Actual engagement")
    
    # ROI Calculation
    estimated_roi: Optional[float] = Field(description="Estimated ROI")
    actual_roi: Optional[float] = Field(description="Actual ROI")
    
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class CampaignMetrics(BaseModel):
    """Campaign performance metrics"""
    # Reach and Impressions
    total_reach: int = Field(ge=0, description="Total campaign reach")
    total_impressions: int = Field(ge=0, description="Total impressions")
    unique_reach: int = Field(ge=0, description="Unique users reached")
    
    # Engagement Metrics
    total_engagement: int = Field(ge=0, description="Total engagement actions")
    total_likes: int = Field(ge=0, description="Total likes")
    total_comments: int = Field(ge=0, description="Total comments")
    total_shares: int = Field(ge=0, description="Total shares")
    avg_engagement_rate: float = Field(ge=0, description="Average engagement rate")
    
    # Conversion Metrics
    click_through_rate: float = Field(ge=0, le=100, description="Click-through rate percentage")
    conversion_rate: float = Field(ge=0, le=100, description="Conversion rate percentage")
    total_conversions: int = Field(ge=0, description="Total conversions")
    cost_per_conversion: Optional[float] = Field(ge=0, description="Cost per conversion")
    
    # Financial Metrics
    total_spend: float = Field(ge=0, description="Total campaign spend")
    cost_per_click: Optional[float] = Field(ge=0, description="Cost per click")
    cost_per_engagement: Optional[float] = Field(ge=0, description="Cost per engagement")
    roi_percentage: float = Field(description="Return on investment percentage")
    
    # Outreach Metrics
    messages_sent: int = Field(ge=0, description="Total outreach messages sent")
    responses_received: int = Field(ge=0, description="Responses received")
    response_rate: float = Field(ge=0, le=100, description="Response rate percentage")
    collaborations_confirmed: int = Field(ge=0, description="Collaborations confirmed")
    
    # Content Metrics
    content_pieces_created: int = Field(ge=0, description="Total content pieces created")
    content_approval_rate: float = Field(ge=0, le=100, description="Content approval rate")
    avg_content_performance: float = Field(ge=0, description="Average content performance score")
    
    # Time-based Metrics
    avg_response_time_hours: Optional[float] = Field(ge=0, description="Average response time in hours")
    avg_content_creation_days: Optional[float] = Field(ge=0, description="Average content creation time in days")
    
    calculated_at: datetime = Field(default_factory=datetime.now, description="When metrics were calculated")

class Campaign(BaseModel):
    """Main campaign model"""
    id: str = Field(description="Unique campaign identifier")
    name: str = Field(min_length=1, description="Campaign name")
    description: Optional[str] = Field(description="Campaign description")
    
    # Brand Information
    brand_data: BrandData = Field(description="Associated brand data")
    
    # Campaign Timeline
    status: CampaignStatus = Field(description="Current campaign status")
    start_date: Optional[date] = Field(description="Campaign start date")
    end_date: Optional[date] = Field(description="Campaign end date")
    duration_days: Optional[int] = Field(ge=1, description="Campaign duration in days")
    
    # Budget and Goals
    total_budget: Optional[float] = Field(ge=0, description="Total campaign budget")
    spent_budget: float = Field(ge=0, default=0, description="Amount spent so far")
    target_reach: Optional[int] = Field(ge=0, description="Target reach goal")
    target_engagement: Optional[int] = Field(ge=0, description="Target engagement goal")
    target_conversions: Optional[int] = Field(ge=0, description="Target conversion goal")
    
    # Influencer Management
    target_influencer_count: Optional[int] = Field(ge=1, description="Target number of influencers")
    collaborations: List[Collaboration] = Field(default=[], description="Campaign collaborations")
    
    # Content Strategy
    content_themes: List[str] = Field(default=[], description="Content themes")
    required_hashtags: List[str] = Field(default=[], description="Required hashtags")
    brand_mentions_required: bool = Field(default=True, description="Whether brand mentions are required")
    
    # Performance Tracking
    metrics: Optional[CampaignMetrics] = Field(description="Campaign performance metrics")
    
    # Campaign Settings
    auto_approve_content: bool = Field(default=False, description="Auto-approve content")
    allow_competitor_mentions: bool = Field(default=False, description="Allow competitor mentions")
    require_disclosure: bool = Field(default=True, description="Require sponsored content disclosure")
    
    # Team and Permissions
    created_by: str = Field(description="User who created the campaign")
    team_members: List[str] = Field(default=[], description="Team member IDs with access")
    
    # Timestamps
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    @validator('end_date')
    def validate_end_date(cls, v, values):
        """Ensure end date is after start date"""
        if 'start_date' in values and values['start_date'] and v:
            if v <= values['start_date']:
                raise ValueError("End date must be after start date")
        return v
    
    @validator('spent_budget')
    def validate_spent_budget(cls, v, values):
        """Ensure spent budget doesn't exceed total budget"""
        if 'total_budget' in values and values['total_budget'] and v > values['total_budget']:
            raise ValueError("Spent budget cannot exceed total budget")
        return v
    
    class Config:
        """Pydantic configuration"""
        use_enum_values = True
        validate_assignment = True

class CampaignSummary(BaseModel):
    """Campaign summary for dashboard views"""
    id: str
    name: str
    status: CampaignStatus
    brand_name: str
    start_date: Optional[date]
    end_date: Optional[date]
    total_budget: Optional[float]
    spent_budget: float
    collaborations_count: int
    active_collaborations: int
    completed_collaborations: int
    total_reach: Optional[int]
    total_engagement: Optional[int]
    roi_percentage: Optional[float]
    created_at: datetime
    
    class Config:
        use_enum_values = True

class CampaignAnalytics(BaseModel):
    """Detailed campaign analytics"""
    campaign_id: str
    metrics: CampaignMetrics
    
    # Performance Trends
    daily_metrics: List[Dict[str, Any]] = Field(default=[], description="Daily performance data")
    weekly_metrics: List[Dict[str, Any]] = Field(default=[], description="Weekly performance data")
    
    # Influencer Performance
    top_performing_influencers: List[Dict[str, Any]] = Field(default=[], description="Top performing influencers")
    influencer_performance_comparison: List[Dict[str, Any]] = Field(default=[], description="Influencer comparison data")
    
    # Content Performance
    top_performing_content: List[Dict[str, Any]] = Field(default=[], description="Top performing content")
    content_type_performance: Dict[str, float] = Field(default={}, description="Performance by content type")
    
    # Audience Insights
    audience_demographics: Dict[str, Any] = Field(default={}, description="Audience demographic data")
    audience_engagement_patterns: Dict[str, Any] = Field(default={}, description="Engagement patterns")
    
    # Recommendations
    optimization_recommendations: List[str] = Field(default=[], description="AI-generated recommendations")
    budget_recommendations: List[str] = Field(default=[], description="Budget optimization suggestions")
    
    generated_at: datetime = Field(default_factory=datetime.now)
