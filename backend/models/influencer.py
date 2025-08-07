"""
Influencer Data Models
Pydantic models for influencer-related data structures
"""

from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any, Union
from datetime import datetime
from enum import Enum

class PlatformType(str, Enum):
    """Supported social media platforms"""
    INSTAGRAM = "instagram"
    YOUTUBE = "youtube"
    TIKTOK = "tiktok"
    TWITTER = "twitter"

class InfluencerCategory(str, Enum):
    """Influencer content categories"""
    FASHION = "Fashion & Lifestyle"
    BEAUTY = "Beauty & Cosmetics"
    FITNESS = "Fitness & Wellness"
    FOOD = "Food & Cooking"
    TECH = "Technology"
    TRAVEL = "Travel & Adventure"
    LIFESTYLE = "Lifestyle"
    GAMING = "Gaming"
    EDUCATION = "Education"
    ENTERTAINMENT = "Entertainment"

class EngagementMetrics(BaseModel):
    """Engagement metrics for content"""
    likes: int = Field(ge=0, description="Number of likes")
    comments: int = Field(ge=0, description="Number of comments")
    shares: int = Field(ge=0, description="Number of shares")
    saves: Optional[int] = Field(ge=0, description="Number of saves (Instagram)")
    views: Optional[int] = Field(ge=0, description="Number of views")
    
    @property
    def total_engagement(self) -> int:
        """Calculate total engagement"""
        return self.likes + self.comments + self.shares + (self.saves or 0)

class ContentPost(BaseModel):
    """Individual content post data"""
    id: str = Field(description="Unique post identifier")
    platform: PlatformType = Field(description="Platform where content was posted")
    title: Optional[str] = Field(description="Post title (for YouTube)")
    caption: Optional[str] = Field(description="Post caption/description")
    content_type: str = Field(description="Type of content (image, video, carousel, etc.)")
    url: Optional[str] = Field(description="URL to the content")
    thumbnail_url: Optional[str] = Field(description="Thumbnail image URL")
    published_at: datetime = Field(description="When the content was published")
    engagement: EngagementMetrics = Field(description="Engagement metrics")
    hashtags: List[str] = Field(default=[], description="Hashtags used")
    mentions: List[str] = Field(default=[], description="User mentions")
    duration_seconds: Optional[int] = Field(ge=0, description="Video duration in seconds")

class AudienceDemographics(BaseModel):
    """Audience demographic data"""
    age_groups: Dict[str, float] = Field(description="Age group percentages")
    gender_distribution: Dict[str, float] = Field(description="Gender distribution percentages")
    top_locations: List[Dict[str, Union[str, float]]] = Field(description="Top audience locations")
    interests: List[Dict[str, Union[str, float]]] = Field(description="Audience interests and affinities")
    
    @validator('age_groups')
    def validate_age_groups(cls, v):
        """Validate age group percentages sum to ~100"""
        total = sum(v.values())
        if not 95 <= total <= 105:  # Allow some tolerance
            raise ValueError("Age group percentages should sum to approximately 100")
        return v

class InfluencerMetrics(BaseModel):
    """Core influencer metrics"""
    followers_count: int = Field(ge=0, description="Total follower count")
    following_count: int = Field(ge=0, description="Total following count")
    posts_count: int = Field(ge=0, description="Total posts count")
    engagement_rate: float = Field(ge=0, le=100, description="Average engagement rate percentage")
    avg_likes: int = Field(ge=0, description="Average likes per post")
    avg_comments: int = Field(ge=0, description="Average comments per post")
    avg_views: Optional[int] = Field(ge=0, description="Average views per post")
    reach_rate: Optional[float] = Field(ge=0, le=100, description="Average reach rate percentage")

class AIAnalysis(BaseModel):
    """AI-powered analysis results"""
    match_score: int = Field(ge=0, le=100, description="Brand match score (0-100)")
    authenticity_score: int = Field(ge=0, le=100, description="Authenticity score (0-100)")
    audience_alignment: int = Field(ge=0, le=100, description="Audience alignment score (0-100)")
    content_quality_score: int = Field(ge=0, le=100, description="Content quality score (0-100)")
    engagement_quality_score: int = Field(ge=0, le=100, description="Engagement quality score (0-100)")
    brand_safety_score: int = Field(ge=0, le=100, description="Brand safety score (0-100)")
    
    # AI Insights
    key_insights: List[str] = Field(description="Key AI-generated insights")
    content_themes: List[str] = Field(description="Main content themes")
    posting_frequency: str = Field(description="Posting frequency analysis")
    best_performing_content: List[str] = Field(description="Best performing content types")
    
    # Risk Assessment
    risk_level: str = Field(description="Overall risk level (Low/Medium/High)")
    risk_factors: List[str] = Field(description="Identified risk factors")
    
    analyzed_at: datetime = Field(default_factory=datetime.now, description="When analysis was performed")

class CollaborationEstimate(BaseModel):
    """Collaboration cost and effort estimates"""
    estimated_cost_range: str = Field(description="Estimated collaboration cost range")
    recommended_content_types: List[str] = Field(description="Recommended content types")
    estimated_reach: str = Field(description="Estimated campaign reach")
    estimated_engagement: str = Field(description="Estimated engagement")
    collaboration_potential: str = Field(description="Overall collaboration potential assessment")

class Influencer(BaseModel):
    """Base influencer model"""
    id: str = Field(description="Unique influencer identifier")
    platform: PlatformType = Field(description="Primary platform")
    username: str = Field(description="Platform username/handle")
    display_name: str = Field(description="Display name")
    bio: Optional[str] = Field(description="Bio/description")
    profile_image_url: Optional[str] = Field(description="Profile image URL")
    profile_url: Optional[str] = Field(description="Profile URL")
    
    # Verification and Account Type
    is_verified: bool = Field(default=False, description="Verified account status")
    is_business_account: bool = Field(default=False, description="Business account status")
    
    # Category and Location
    category: InfluencerCategory = Field(description="Primary content category")
    location: Optional[str] = Field(description="Location/region")
    
    # Metrics
    metrics: InfluencerMetrics = Field(description="Core metrics")
    
    # Recent Content
    recent_posts: List[ContentPost] = Field(default=[], description="Recent posts")
    
    # Timestamps
    created_at: datetime = Field(default_factory=datetime.now, description="When record was created")
    updated_at: datetime = Field(default_factory=datetime.now, description="When record was last updated")

class InfluencerProfile(Influencer):
    """Extended influencer profile with analysis"""
    # Extended Data
    audience_demographics: Optional[AudienceDemographics] = Field(description="Audience demographic data")
    ai_analysis: Optional[AIAnalysis] = Field(description="AI analysis results")
    collaboration_estimate: Optional[CollaborationEstimate] = Field(description="Collaboration estimates")
    
    # Additional Metrics
    growth_rate: Optional[float] = Field(description="Follower growth rate percentage")
    posting_frequency_per_week: Optional[float] = Field(description="Average posts per week")
    best_posting_times: List[str] = Field(default=[], description="Optimal posting times")
    
    # Content Analysis
    top_hashtags: List[str] = Field(default=[], description="Most used hashtags")
    content_pillars: List[str] = Field(default=[], description="Main content pillars")
    brand_mentions: List[str] = Field(default=[], description="Brands mentioned in content")
    
    # Collaboration History
    previous_collaborations: List[str] = Field(default=[], description="Previous brand collaborations")
    collaboration_frequency: Optional[str] = Field(description="How often they do collaborations")
    
    # Contact Information
    contact_email: Optional[str] = Field(description="Contact email")
    management_contact: Optional[str] = Field(description="Management/agency contact")
    
    class Config:
        """Pydantic configuration"""
        use_enum_values = True
        validate_assignment = True
        arbitrary_types_allowed = True

class InfluencerSearchFilters(BaseModel):
    """Search filters for influencer discovery"""
    platforms: List[PlatformType] = Field(description="Platforms to search")
    categories: List[InfluencerCategory] = Field(description="Content categories")
    min_followers: Optional[int] = Field(ge=0, description="Minimum follower count")
    max_followers: Optional[int] = Field(ge=0, description="Maximum follower count")
    min_engagement_rate: Optional[float] = Field(ge=0, le=100, description="Minimum engagement rate")
    max_engagement_rate: Optional[float] = Field(ge=0, le=100, description="Maximum engagement rate")
    locations: List[str] = Field(default=[], description="Target locations")
    verified_only: bool = Field(default=False, description="Only verified accounts")
    business_accounts_only: bool = Field(default=False, description="Only business accounts")
    keywords: List[str] = Field(default=[], description="Keywords to search for")
    exclude_keywords: List[str] = Field(default=[], description="Keywords to exclude")
    
    @validator('max_followers')
    def validate_follower_range(cls, v, values):
        """Validate follower range"""
        if 'min_followers' in values and values['min_followers'] and v:
            if v < values['min_followers']:
                raise ValueError("max_followers must be greater than min_followers")
        return v

class InfluencerDiscoveryResult(BaseModel):
    """Result of influencer discovery process"""
    total_found: int = Field(ge=0, description="Total influencers found")
    high_match_count: int = Field(ge=0, description="High match influencers (90%+)")
    medium_match_count: int = Field(ge=0, description="Medium match influencers (80-89%)")
    low_match_count: int = Field(ge=0, description="Low match influencers (<80%)")
    influencers: List[InfluencerProfile] = Field(description="Discovered influencers")
    search_filters: InfluencerSearchFilters = Field(description="Filters used for search")
    discovery_time: float = Field(description="Time taken for discovery in seconds")
    created_at: datetime = Field(default_factory=datetime.now, description="When discovery was performed")

class InfluencerListResponse(BaseModel):
    """API response for influencer lists"""
    influencers: List[InfluencerProfile]
    total_count: int
    high_matches: int
    medium_matches: int
    low_matches: int
    page: int = 1
    per_page: int = 50
    has_more: bool = False
