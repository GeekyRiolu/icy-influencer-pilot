"""
Brand Data Models
Pydantic models for brand and campaign-related data structures
"""

from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class BrandTone(str, Enum):
    """Brand communication tones"""
    PROFESSIONAL = "professional"
    FRIENDLY = "friendly"
    LUXURY = "luxury"
    PLAYFUL = "playful"
    EDGY = "edgy"
    CASUAL = "casual"

class CampaignGoal(str, Enum):
    """Campaign objectives"""
    AWARENESS = "awareness"
    SALES = "sales"
    UGC = "ugc"  # User Generated Content
    ENGAGEMENT = "engagement"
    LEADS = "leads"
    BRAND_BUILDING = "brand_building"

class BudgetLevel(str, Enum):
    """Influencer budget tiers"""
    MICRO = "micro"      # 1K-100K followers
    MID = "mid"          # 100K-1M followers
    MACRO = "macro"      # 1M+ followers
    CELEBRITY = "celebrity"  # Celebrity tier

class TargetRegion(str, Enum):
    """Target geographic regions"""
    NORTH_AMERICA = "north-america"
    EUROPE = "europe"
    ASIA_PACIFIC = "asia-pacific"
    LATIN_AMERICA = "latin-america"
    MIDDLE_EAST_AFRICA = "middle-east-africa"
    GLOBAL = "global"

class Platform(str, Enum):
    """Social media platforms"""
    INSTAGRAM = "instagram"
    YOUTUBE = "youtube"
    TIKTOK = "tiktok"
    TWITTER = "twitter"
    LINKEDIN = "linkedin"

class BrandData(BaseModel):
    """Brand information and preferences"""
    # Basic Brand Info
    product_name: str = Field(min_length=2, description="Product or brand name")
    product_description: str = Field(min_length=10, description="Detailed product description")
    brand_website: Optional[str] = Field(description="Brand website URL")
    brand_logo_url: Optional[str] = Field(description="Brand logo URL")
    
    # Target Audience
    target_age: List[str] = Field(min_items=1, description="Target age groups")
    target_gender: List[str] = Field(min_items=1, description="Target gender demographics")
    target_interests: str = Field(min_length=5, description="Target audience interests")
    target_region: TargetRegion = Field(description="Target geographic region")
    
    # Brand Voice & Goals
    brand_tone: BrandTone = Field(description="Brand communication tone")
    campaign_goal: CampaignGoal = Field(description="Primary campaign objective")
    
    # Platform & Budget Preferences
    platforms: List[Platform] = Field(min_items=1, description="Target social media platforms")
    budget_level: BudgetLevel = Field(description="Influencer budget tier")
    
    # Additional Preferences
    preferred_content_types: List[str] = Field(default=[], description="Preferred content formats")
    brand_values: List[str] = Field(default=[], description="Core brand values")
    competitor_brands: List[str] = Field(default=[], description="Competitor brand names")
    avoid_topics: List[str] = Field(default=[], description="Topics to avoid")
    
    # Campaign Specifics
    campaign_duration: Optional[int] = Field(ge=1, le=365, description="Campaign duration in days")
    expected_deliverables: List[str] = Field(default=[], description="Expected content deliverables")
    collaboration_type: str = Field(default="paid", description="Type of collaboration")
    
    # Contact Information
    contact_name: Optional[str] = Field(description="Primary contact name")
    contact_email: Optional[str] = Field(description="Contact email address")
    company_name: Optional[str] = Field(description="Company name")
    
    # Timestamps
    created_at: datetime = Field(default_factory=datetime.now, description="When brand data was created")
    updated_at: datetime = Field(default_factory=datetime.now, description="When brand data was last updated")
    
    @validator('target_age')
    def validate_age_groups(cls, v):
        """Validate age group selections"""
        valid_ages = ["13-17", "18-24", "25-34", "35-44", "45-54", "55+"]
        for age in v:
            if age not in valid_ages:
                raise ValueError(f"Invalid age group: {age}")
        return v
    
    @validator('target_gender')
    def validate_gender_options(cls, v):
        """Validate gender selections"""
        valid_genders = ["Female", "Male", "Non-binary", "All"]
        for gender in v:
            if gender not in valid_genders:
                raise ValueError(f"Invalid gender option: {gender}")
        return v
    
    class Config:
        """Pydantic configuration"""
        use_enum_values = True
        validate_assignment = True

class BrandPreferences(BaseModel):
    """Extended brand preferences for matching"""
    # Content Preferences
    preferred_aesthetics: List[str] = Field(default=[], description="Visual aesthetic preferences")
    content_style: List[str] = Field(default=[], description="Content style preferences")
    posting_frequency: Optional[str] = Field(description="Preferred posting frequency")
    
    # Influencer Preferences
    min_engagement_rate: Optional[float] = Field(ge=0, le=100, description="Minimum engagement rate")
    max_engagement_rate: Optional[float] = Field(ge=0, le=100, description="Maximum engagement rate")
    verified_only: bool = Field(default=False, description="Only work with verified accounts")
    exclude_competitors: bool = Field(default=True, description="Exclude influencers who work with competitors")
    
    # Geographic Preferences
    specific_cities: List[str] = Field(default=[], description="Specific target cities")
    exclude_regions: List[str] = Field(default=[], description="Regions to exclude")
    
    # Language Preferences
    languages: List[str] = Field(default=["English"], description="Preferred content languages")
    
    # Collaboration Preferences
    long_term_partnership: bool = Field(default=False, description="Interest in long-term partnerships")
    exclusive_partnerships: bool = Field(default=False, description="Require exclusive partnerships")
    content_approval_required: bool = Field(default=True, description="Require content approval")
    
    # Budget Constraints
    max_cost_per_post: Optional[float] = Field(ge=0, description="Maximum cost per post")
    total_campaign_budget: Optional[float] = Field(ge=0, description="Total campaign budget")
    payment_terms: str = Field(default="net-30", description="Payment terms")

class BrandProfile(BaseModel):
    """Complete brand profile with preferences"""
    id: str = Field(description="Unique brand profile identifier")
    brand_data: BrandData = Field(description="Core brand information")
    preferences: BrandPreferences = Field(description="Extended brand preferences")
    
    # Campaign History
    previous_campaigns: List[str] = Field(default=[], description="Previous campaign IDs")
    successful_influencers: List[str] = Field(default=[], description="Previously successful influencer IDs")
    blacklisted_influencers: List[str] = Field(default=[], description="Blacklisted influencer IDs")
    
    # Performance Metrics
    avg_campaign_roi: Optional[float] = Field(description="Average campaign ROI")
    avg_engagement_rate: Optional[float] = Field(description="Average campaign engagement rate")
    total_campaigns_run: int = Field(default=0, description="Total campaigns run")
    
    # Status
    is_active: bool = Field(default=True, description="Brand profile active status")
    subscription_tier: str = Field(default="basic", description="Subscription tier")
    
    # Timestamps
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    class Config:
        """Pydantic configuration"""
        use_enum_values = True
        validate_assignment = True

class BrandMatchingCriteria(BaseModel):
    """Criteria for matching brands with influencers"""
    # Audience Alignment
    audience_overlap_threshold: float = Field(ge=0, le=1, default=0.3, description="Minimum audience overlap")
    demographic_match_weight: float = Field(ge=0, le=1, default=0.25, description="Weight for demographic matching")
    interest_match_weight: float = Field(ge=0, le=1, default=0.3, description="Weight for interest matching")
    
    # Content Alignment
    content_category_weight: float = Field(ge=0, le=1, default=0.2, description="Weight for content category")
    brand_mention_bonus: float = Field(ge=0, le=1, default=0.1, description="Bonus for previous brand mentions")
    content_quality_weight: float = Field(ge=0, le=1, default=0.15, description="Weight for content quality")
    
    # Performance Metrics
    engagement_rate_weight: float = Field(ge=0, le=1, default=0.2, description="Weight for engagement rate")
    authenticity_weight: float = Field(ge=0, le=1, default=0.25, description="Weight for authenticity score")
    growth_rate_weight: float = Field(ge=0, le=1, default=0.1, description="Weight for growth rate")
    
    # Risk Factors
    brand_safety_weight: float = Field(ge=0, le=1, default=0.3, description="Weight for brand safety")
    controversy_penalty: float = Field(ge=0, le=1, default=0.5, description="Penalty for controversial content")
    
    @validator('*')
    def validate_weights_sum(cls, v, values, field):
        """Ensure weights are reasonable"""
        if field.name.endswith('_weight') and v > 1:
            raise ValueError(f"{field.name} cannot exceed 1.0")
        return v

class BrandAnalytics(BaseModel):
    """Brand performance analytics"""
    # Campaign Performance
    total_campaigns: int = Field(ge=0, description="Total campaigns run")
    active_campaigns: int = Field(ge=0, description="Currently active campaigns")
    avg_campaign_duration: float = Field(ge=0, description="Average campaign duration in days")
    
    # Financial Metrics
    total_spend: float = Field(ge=0, description="Total amount spent on campaigns")
    avg_cost_per_campaign: float = Field(ge=0, description="Average cost per campaign")
    avg_roi: float = Field(description="Average return on investment")
    
    # Reach and Engagement
    total_reach: int = Field(ge=0, description="Total reach across all campaigns")
    total_impressions: int = Field(ge=0, description="Total impressions")
    avg_engagement_rate: float = Field(ge=0, le=100, description="Average engagement rate")
    
    # Influencer Metrics
    total_influencers_worked_with: int = Field(ge=0, description="Total unique influencers")
    avg_influencers_per_campaign: float = Field(ge=0, description="Average influencers per campaign")
    top_performing_influencers: List[str] = Field(default=[], description="Top performing influencer IDs")
    
    # Content Metrics
    total_content_pieces: int = Field(ge=0, description="Total content pieces created")
    avg_content_per_campaign: float = Field(ge=0, description="Average content pieces per campaign")
    most_successful_content_types: List[str] = Field(default=[], description="Most successful content types")
    
    # Time-based Analytics
    best_performing_months: List[str] = Field(default=[], description="Best performing months")
    seasonal_trends: Dict[str, float] = Field(default={}, description="Seasonal performance trends")
    
    # Generated Insights
    key_insights: List[str] = Field(default=[], description="AI-generated key insights")
    recommendations: List[str] = Field(default=[], description="AI-generated recommendations")
    
    # Timestamps
    analytics_period_start: datetime = Field(description="Analytics period start date")
    analytics_period_end: datetime = Field(description="Analytics period end date")
    generated_at: datetime = Field(default_factory=datetime.now, description="When analytics were generated")
