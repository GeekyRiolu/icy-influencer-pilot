"""
YouTube API Integration Module
Simulates YouTube Data API v3 calls for influencer discovery and analysis
"""

import asyncio
import random
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta
import json

class YouTubeAPI:
    """Simulated YouTube API client"""
    
    def __init__(self):
        self.api_version = "v3"
        self.base_url = "https://www.googleapis.com/youtube/v3"
        self.api_key = "simulated_youtube_api_key"
        
        # Mock YouTube influencer database
        self.mock_influencers = [
            {
                "id": "youtube_001",
                "channel_id": "UC_alexfitness123",
                "channel_name": "Alex Rodriguez Fitness",
                "display_name": "Alex Rodriguez",
                "subscriber_count": 89000,
                "video_count": 245,
                "view_count": 12500000,
                "description": "Your go-to fitness coach! 💪 New workout videos every Tuesday & Friday. Transform your body and mind with science-based training.",
                "profile_image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&h=150&fit=crop&crop=face",
                "banner_image": "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=800&h=200&fit=crop",
                "country": "US",
                "custom_url": "@alexfitness",
                "published_at": "2020-03-15T10:00:00Z",
                "category": "Fitness & Wellness",
                "location": "Miami, FL",
                "engagement_rate": 6.8,
                "avg_views": 12000,
                "avg_likes": 820,
                "avg_comments": 95,
                "recent_videos": [
                    {
                        "id": "video_001",
                        "title": "New workout routine that changed my life! Full body transformation",
                        "description": "This 30-minute full body workout will challenge every muscle group...",
                        "view_count": 25000,
                        "like_count": 1200,
                        "comment_count": 156,
                        "published_at": "2024-01-10T15:30:00Z",
                        "duration": "PT30M15S",
                        "tags": ["fitness", "workout", "transformation", "health"]
                    }
                ]
            },
            {
                "id": "youtube_002",
                "channel_id": "UC_techreview456",
                "channel_name": "Tech Insights Daily",
                "display_name": "Marcus Kim",
                "subscriber_count": 156000,
                "video_count": 380,
                "view_count": 28000000,
                "description": "Latest tech reviews, unboxings, and tutorials! 📱💻 Helping you make smart tech decisions since 2019.",
                "profile_image": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=150&h=150&fit=crop&crop=face",
                "banner_image": "https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=800&h=200&fit=crop",
                "country": "US",
                "custom_url": "@techinsightsdaily",
                "published_at": "2019-08-22T14:20:00Z",
                "category": "Technology",
                "location": "San Jose, CA",
                "engagement_rate": 4.5,
                "avg_views": 18500,
                "avg_likes": 1100,
                "avg_comments": 180,
                "recent_videos": [
                    {
                        "id": "video_002",
                        "title": "iPhone 15 Pro Max Review - Is it worth the upgrade?",
                        "description": "Complete review of the new iPhone 15 Pro Max after 2 weeks of use...",
                        "view_count": 45000,
                        "like_count": 2100,
                        "comment_count": 320,
                        "published_at": "2024-01-08T12:00:00Z",
                        "duration": "PT15M42S",
                        "tags": ["iphone", "review", "apple", "tech", "smartphone"]
                    }
                ]
            },
            {
                "id": "youtube_003",
                "channel_id": "UC_cookingwithsara789",
                "channel_name": "Cooking with Sara",
                "display_name": "Sara Williams",
                "subscriber_count": 234000,
                "video_count": 520,
                "view_count": 45000000,
                "description": "Easy, delicious recipes for home cooks! 👩‍🍳 New recipe videos every Monday, Wednesday & Saturday.",
                "profile_image": "https://images.unsplash.com/photo-1494790108755-2616b612b786?w=150&h=150&fit=crop&crop=face",
                "banner_image": "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=800&h=200&fit=crop",
                "country": "US",
                "custom_url": "@cookingwithsara",
                "published_at": "2018-11-10T09:15:00Z",
                "category": "Food & Cooking",
                "location": "Austin, TX",
                "engagement_rate": 5.2,
                "avg_views": 22000,
                "avg_likes": 1400,
                "avg_comments": 220,
                "recent_videos": [
                    {
                        "id": "video_003",
                        "title": "Perfect Homemade Pizza in 30 Minutes | Easy Recipe",
                        "description": "Learn how to make restaurant-quality pizza at home with simple ingredients...",
                        "view_count": 38000,
                        "like_count": 1800,
                        "comment_count": 285,
                        "published_at": "2024-01-12T18:00:00Z",
                        "duration": "PT12M30S",
                        "tags": ["pizza", "recipe", "cooking", "homemade", "easy"]
                    }
                ]
            }
        ]
    
    async def discover_influencers(self, brand_data: Dict, max_results: int = 25) -> List[Dict]:
        """Discover YouTube influencers based on brand criteria"""
        await asyncio.sleep(2.0)  # Simulate API delay
        
        discovered = []
        
        # Use existing mock data
        for influencer in self.mock_influencers:
            discovered.append(self._format_influencer_data(influencer))
        
        # Generate additional random influencers
        additional_count = max_results - len(discovered)
        for i in range(additional_count):
            mock_influencer = self._generate_mock_influencer(i + 200)
            discovered.append(self._format_influencer_data(mock_influencer))
        
        return discovered[:max_results]
    
    async def get_channel_details(self, channel_id: str) -> Dict[str, Any]:
        """Get YouTube channel details"""
        await asyncio.sleep(0.6)
        
        # Find in mock data or generate
        for influencer in self.mock_influencers:
            if influencer["channel_id"] == channel_id:
                return influencer
        
        # Generate mock channel if not found
        return self._generate_mock_influencer(random.randint(2000, 9999))
    
    async def get_channel_videos(self, channel_id: str, max_results: int = 20) -> List[Dict]:
        """Get recent videos from a channel"""
        await asyncio.sleep(1.0)
        
        videos = []
        for i in range(max_results):
            video = {
                "id": f"video_{channel_id}_{i}",
                "title": self._generate_video_title(),
                "description": self._generate_video_description(),
                "published_at": (datetime.now() - timedelta(days=i*3)).isoformat(),
                "duration": f"PT{random.randint(5, 45)}M{random.randint(10, 59)}S",
                "view_count": random.randint(1000, 100000),
                "like_count": random.randint(50, 5000),
                "comment_count": random.randint(10, 800),
                "thumbnail_url": f"https://img.youtube.com/vi/video_{channel_id}_{i}/maxresdefault.jpg",
                "tags": self._generate_video_tags(),
                "category_id": str(random.randint(1, 28))
            }
            videos.append(video)
        
        return videos
    
    async def get_recent_videos(self, influencer_id: str, limit: int = 10) -> List[Dict]:
        """Get recent videos with engagement data"""
        await asyncio.sleep(0.8)
        
        videos = []
        for i in range(limit):
            video = {
                "id": f"video_{influencer_id}_{i}",
                "type": "youtube_video",
                "title": self._generate_video_title(),
                "description": self._generate_video_description(),
                "engagement": {
                    "views": random.randint(5000, 50000),
                    "likes": random.randint(200, 3000),
                    "comments": random.randint(20, 500),
                    "shares": random.randint(10, 200),
                    "subscribers_gained": random.randint(5, 100)
                },
                "published_at": (datetime.now() - timedelta(days=i*2)).isoformat(),
                "duration_seconds": random.randint(300, 1800),
                "tags": self._generate_video_tags(),
                "category": random.choice(["Education", "Entertainment", "How-to", "Review"])
            }
            videos.append(video)
        
        return videos
    
    async def get_channel_analytics(self, channel_id: str) -> Dict[str, Any]:
        """Get channel analytics and audience insights"""
        await asyncio.sleep(1.5)
        
        return {
            "subscriber_growth": {
                "last_30_days": random.randint(500, 5000),
                "last_90_days": random.randint(1500, 15000),
                "growth_rate": round(random.uniform(2.0, 15.0), 2)
            },
            "view_analytics": {
                "total_views_last_30_days": random.randint(50000, 500000),
                "avg_view_duration": f"{random.randint(3, 12)}:{random.randint(10, 59)}",
                "audience_retention": round(random.uniform(45.0, 75.0), 1)
            },
            "demographics": {
                "age_groups": {
                    "13-17": random.randint(8, 20),
                    "18-24": random.randint(25, 40),
                    "25-34": random.randint(20, 35),
                    "35-44": random.randint(10, 20),
                    "45-54": random.randint(5, 15),
                    "55+": random.randint(2, 10)
                },
                "gender": {
                    "male": random.randint(40, 70),
                    "female": random.randint(30, 60),
                    "other": random.randint(1, 3)
                },
                "top_countries": [
                    {"country": "United States", "percentage": random.randint(35, 55)},
                    {"country": "United Kingdom", "percentage": random.randint(8, 15)},
                    {"country": "Canada", "percentage": random.randint(6, 12)},
                    {"country": "Australia", "percentage": random.randint(4, 8)},
                    {"country": "Germany", "percentage": random.randint(3, 7)}
                ]
            },
            "engagement_metrics": {
                "avg_likes_per_video": random.randint(500, 5000),
                "avg_comments_per_video": random.randint(50, 800),
                "subscriber_engagement_rate": round(random.uniform(3.0, 12.0), 2),
                "click_through_rate": round(random.uniform(4.0, 15.0), 2)
            },
            "revenue_estimates": {
                "estimated_monthly_earnings": f"${random.randint(500, 15000):,}",
                "cpm_range": f"${random.uniform(1.0, 8.0):.2f} - ${random.uniform(8.0, 15.0):.2f}",
                "brand_deal_rate": f"${random.randint(1000, 25000):,} per video"
            }
        }
    
    async def search_channels(self, query: str, max_results: int = 25) -> List[Dict]:
        """Search for channels based on query"""
        await asyncio.sleep(1.2)
        
        results = []
        for i in range(max_results):
            channel = self._generate_mock_influencer(i + 3000)
            # Modify some fields to match search query
            if "fitness" in query.lower():
                channel["category"] = "Fitness & Wellness"
                channel["channel_name"] = f"Fitness Channel {i}"
            elif "tech" in query.lower():
                channel["category"] = "Technology"
                channel["channel_name"] = f"Tech Review {i}"
            elif "food" in query.lower():
                channel["category"] = "Food & Cooking"
                channel["channel_name"] = f"Cooking Channel {i}"
            
            results.append(self._format_influencer_data(channel))
        
        return results
    
    async def get_video_comments(self, video_id: str, max_results: int = 50) -> List[Dict]:
        """Get comments from a video"""
        await asyncio.sleep(0.7)
        
        comments = []
        for i in range(max_results):
            comment = {
                "id": f"comment_{video_id}_{i}",
                "author": f"User{random.randint(1000, 9999)}",
                "text": self._generate_comment_text(),
                "like_count": random.randint(0, 100),
                "published_at": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat(),
                "reply_count": random.randint(0, 10)
            }
            comments.append(comment)
        
        return comments
    
    def _format_influencer_data(self, influencer: Dict) -> Dict:
        """Format influencer data for API response"""
        return {
            "id": influencer["id"],
            "platform": "youtube",
            "username": influencer["custom_url"],
            "display_name": influencer["display_name"],
            "followers": influencer["subscriber_count"],
            "engagement_rate": influencer["engagement_rate"],
            "category": influencer["category"],
            "location": influencer["location"],
            "profile_image": influencer["profile_image"],
            "bio": influencer["description"],
            "verified": random.choice([True, False]),
            "business_account": True,
            "avg_views": influencer["avg_views"],
            "avg_likes": influencer["avg_likes"],
            "video_count": influencer["video_count"],
            "recent_post": influencer["recent_videos"][0]["title"] if influencer["recent_videos"] else ""
        }
    
    def _generate_mock_influencer(self, index: int) -> Dict:
        """Generate a mock YouTube influencer"""
        categories = ["Technology", "Gaming", "Beauty", "Fitness", "Food", "Travel", "Education", "Entertainment"]
        locations = ["Los Angeles", "New York", "London", "Toronto", "Sydney", "Berlin", "Tokyo"]
        
        subscribers = random.randint(10000, 1000000)
        engagement_rate = round(random.uniform(3.0, 10.0), 1)
        
        return {
            "id": f"youtube_{index:03d}",
            "channel_id": f"UC_channel_{index}",
            "channel_name": f"Channel {index}",
            "display_name": f"Creator {index}",
            "subscriber_count": subscribers,
            "video_count": random.randint(50, 800),
            "view_count": subscribers * random.randint(20, 100),
            "description": f"Welcome to my channel! Creating {random.choice(categories).lower()} content daily.",
            "profile_image": f"https://images.unsplash.com/photo-{1600000000 + index}?w=150&h=150&fit=crop&crop=face",
            "banner_image": f"https://images.unsplash.com/photo-{1600000000 + index + 1000}?w=800&h=200&fit=crop",
            "country": "US",
            "custom_url": f"@creator{index}",
            "published_at": (datetime.now() - timedelta(days=random.randint(365, 2000))).isoformat(),
            "category": random.choice(categories),
            "location": random.choice(locations),
            "engagement_rate": engagement_rate,
            "avg_views": int(subscribers * 0.1),
            "avg_likes": int(subscribers * engagement_rate / 100),
            "avg_comments": int(subscribers * engagement_rate / 100 * 0.1),
            "recent_videos": [
                {
                    "id": f"video_{index}_001",
                    "title": self._generate_video_title(),
                    "description": self._generate_video_description(),
                    "view_count": int(subscribers * 0.1),
                    "like_count": int(subscribers * engagement_rate / 100),
                    "comment_count": int(subscribers * engagement_rate / 100 * 0.1),
                    "published_at": datetime.now().isoformat(),
                    "duration": f"PT{random.randint(5, 30)}M{random.randint(10, 59)}S",
                    "tags": self._generate_video_tags()
                }
            ]
        }
    
    def _generate_video_title(self) -> str:
        """Generate a mock video title"""
        titles = [
            "You Won't Believe What Happened Next!",
            "The Ultimate Guide to Success",
            "My Honest Review After 30 Days",
            "This Changed Everything for Me",
            "Why Everyone is Talking About This",
            "The Secret They Don't Want You to Know",
            "I Tried This for a Week - Here's What Happened",
            "The Best Tips for Beginners"
        ]
        return random.choice(titles)
    
    def _generate_video_description(self) -> str:
        """Generate a mock video description"""
        descriptions = [
            "In this video, I share my experience and tips that have helped me grow...",
            "Today we're diving deep into the topic that everyone's been asking about...",
            "After months of research, I'm finally ready to share my findings with you...",
            "This comprehensive guide will walk you through everything you need to know...",
            "Join me as I explore this fascinating topic and share my insights..."
        ]
        return random.choice(descriptions)
    
    def _generate_video_tags(self) -> List[str]:
        """Generate mock video tags"""
        all_tags = [
            "tutorial", "review", "tips", "guide", "howto", "lifestyle", "vlog",
            "education", "entertainment", "funny", "trending", "viral", "new",
            "best", "top", "amazing", "incredible", "must-watch", "exclusive"
        ]
        return random.sample(all_tags, random.randint(3, 8))
    
    def _generate_comment_text(self) -> str:
        """Generate mock comment text"""
        comments = [
            "Great video! Thanks for sharing this.",
            "This was so helpful, exactly what I needed!",
            "Amazing content as always! Keep it up!",
            "Could you make a video about...?",
            "First! Love your videos!",
            "This deserves more views!",
            "Thanks for the detailed explanation!",
            "Can't wait for the next video!"
        ]
        return random.choice(comments)
