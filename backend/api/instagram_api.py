"""
Instagram API Integration Module
Simulates Instagram Graph API and Instagram Basic Display API calls
"""

import asyncio
import random
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta
import json

class InstagramAPI:
    """Simulated Instagram API client"""
    
    def __init__(self):
        self.api_version = "v18.0"
        self.base_url = "https://graph.instagram.com"
        self.access_token = "simulated_instagram_token"
        
        # Mock Instagram influencer database
        self.mock_influencers = [
            {
                "id": "instagram_001",
                "username": "sarahstyle",
                "full_name": "Sarah Chen",
                "followers_count": 125000,
                "following_count": 1200,
                "media_count": 850,
                "biography": "Sustainable fashion enthusiast 🌱 | Style tips & eco-friendly finds | Collab: sarah@email.com",
                "profile_picture_url": "https://images.unsplash.com/photo-1494790108755-2616b612b786?w=150&h=150&fit=crop&crop=face",
                "is_verified": False,
                "is_business_account": True,
                "category": "Fashion & Lifestyle",
                "location": "Los Angeles, CA",
                "engagement_rate": 4.2,
                "avg_likes": 5200,
                "avg_comments": 180,
                "avg_views": 45000,
                "recent_posts": [
                    {
                        "id": "post_001",
                        "caption": "Just dropped my sustainable fashion haul! 🌱✨ These pieces are not only gorgeous but also ethically made. Swipe to see my styling tips! #SustainableFashion #EcoStyle",
                        "media_type": "CAROUSEL_ALBUM",
                        "like_count": 6800,
                        "comments_count": 245,
                        "timestamp": "2024-01-15T10:30:00Z",
                        "hashtags": ["#SustainableFashion", "#EcoStyle", "#OOTD", "#Conscious"]
                    }
                ]
            },
            {
                "id": "instagram_002",
                "username": "emmaeats",
                "full_name": "Emma Thompson",
                "followers_count": 67000,
                "following_count": 890,
                "media_count": 1200,
                "biography": "Food lover & home chef 🍝 | Easy recipes for busy lives | Recipe requests welcome!",
                "profile_picture_url": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=150&h=150&fit=crop&crop=face",
                "is_verified": False,
                "is_business_account": True,
                "category": "Food & Cooking",
                "location": "New York, NY",
                "engagement_rate": 5.1,
                "avg_likes": 3400,
                "avg_comments": 120,
                "avg_views": 8500,
                "recent_posts": [
                    {
                        "id": "post_002",
                        "caption": "Homemade pasta night! 🍝 This creamy mushroom linguine is pure comfort food. Recipe in my stories - it's easier than you think!",
                        "media_type": "IMAGE",
                        "like_count": 4200,
                        "comments_count": 156,
                        "timestamp": "2024-01-14T18:45:00Z",
                        "hashtags": ["#HomeCooking", "#PastaNight", "#ComfortFood", "#Recipe"]
                    }
                ]
            },
            {
                "id": "instagram_003",
                "username": "mindfulmoments",
                "full_name": "Jessica Park",
                "followers_count": 89000,
                "following_count": 650,
                "media_count": 720,
                "biography": "Wellness coach & mindfulness advocate 🧘‍♀️ | Daily inspiration for mental health | Book a session ⬇️",
                "profile_picture_url": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=150&h=150&fit=crop&crop=face",
                "is_verified": True,
                "is_business_account": True,
                "category": "Health & Wellness",
                "location": "San Francisco, CA",
                "engagement_rate": 6.8,
                "avg_likes": 6100,
                "avg_comments": 280,
                "avg_views": 12000,
                "recent_posts": [
                    {
                        "id": "post_003",
                        "caption": "Morning meditation changed my life ✨ Starting your day with just 5 minutes of mindfulness can transform your entire mindset. What's your morning ritual?",
                        "media_type": "VIDEO",
                        "like_count": 7800,
                        "comments_count": 320,
                        "timestamp": "2024-01-13T07:00:00Z",
                        "hashtags": ["#Mindfulness", "#MorningRitual", "#Meditation", "#Wellness"]
                    }
                ]
            }
        ]
    
    async def discover_influencers(self, brand_data: Dict, max_results: int = 25) -> List[Dict]:
        """Discover Instagram influencers based on brand criteria"""
        await asyncio.sleep(1.5)  # Simulate API delay
        
        # Filter and generate influencers based on brand data
        discovered = []
        
        # Use existing mock data
        for influencer in self.mock_influencers:
            discovered.append(self._format_influencer_data(influencer))
        
        # Generate additional random influencers
        additional_count = max_results - len(discovered)
        for i in range(additional_count):
            mock_influencer = self._generate_mock_influencer(i + 100)
            discovered.append(self._format_influencer_data(mock_influencer))
        
        return discovered[:max_results]
    
    async def get_user_profile(self, username: str) -> Dict[str, Any]:
        """Get Instagram user profile information"""
        await asyncio.sleep(0.5)
        
        # Find in mock data or generate
        for influencer in self.mock_influencers:
            if influencer["username"] == username:
                return influencer
        
        # Generate mock profile if not found
        return self._generate_mock_influencer(random.randint(1000, 9999))
    
    async def get_user_media(self, user_id: str, limit: int = 12) -> List[Dict]:
        """Get recent media posts from user"""
        await asyncio.sleep(0.8)
        
        media_posts = []
        for i in range(limit):
            post = {
                "id": f"media_{user_id}_{i}",
                "media_type": random.choice(["IMAGE", "VIDEO", "CAROUSEL_ALBUM"]),
                "media_url": f"https://example.com/media/{user_id}_{i}.jpg",
                "caption": self._generate_mock_caption(),
                "like_count": random.randint(500, 10000),
                "comments_count": random.randint(20, 500),
                "timestamp": (datetime.now() - timedelta(days=i)).isoformat(),
                "hashtags": self._generate_hashtags()
            }
            media_posts.append(post)
        
        return media_posts
    
    async def get_recent_posts(self, influencer_id: str, limit: int = 10) -> List[Dict]:
        """Get recent posts with engagement data"""
        await asyncio.sleep(0.6)
        
        posts = []
        for i in range(limit):
            post = {
                "id": f"post_{influencer_id}_{i}",
                "type": "instagram_post",
                "content": self._generate_mock_caption(),
                "engagement": {
                    "likes": random.randint(1000, 15000),
                    "comments": random.randint(50, 800),
                    "shares": random.randint(10, 200),
                    "saves": random.randint(100, 2000)
                },
                "posted_at": (datetime.now() - timedelta(days=i)).isoformat(),
                "hashtags": self._generate_hashtags(),
                "mentions": random.randint(0, 5)
            }
            posts.append(post)
        
        return posts
    
    async def get_audience_insights(self, user_id: str) -> Dict[str, Any]:
        """Get audience demographics and insights"""
        await asyncio.sleep(1.2)
        
        return {
            "demographics": {
                "age_groups": {
                    "13-17": random.randint(5, 15),
                    "18-24": random.randint(20, 35),
                    "25-34": random.randint(25, 45),
                    "35-44": random.randint(15, 25),
                    "45-54": random.randint(5, 15),
                    "55+": random.randint(2, 8)
                },
                "gender": {
                    "female": random.randint(45, 85),
                    "male": random.randint(15, 55),
                    "other": random.randint(1, 5)
                },
                "top_locations": [
                    {"city": "Los Angeles", "percentage": random.randint(8, 15)},
                    {"city": "New York", "percentage": random.randint(6, 12)},
                    {"city": "Chicago", "percentage": random.randint(4, 8)},
                    {"city": "Miami", "percentage": random.randint(3, 7)},
                    {"city": "San Francisco", "percentage": random.randint(3, 6)}
                ]
            },
            "interests": [
                {"category": "Fashion", "affinity": random.randint(60, 95)},
                {"category": "Beauty", "affinity": random.randint(40, 80)},
                {"category": "Lifestyle", "affinity": random.randint(50, 85)},
                {"category": "Travel", "affinity": random.randint(30, 70)},
                {"category": "Food", "affinity": random.randint(25, 65)}
            ],
            "engagement_patterns": {
                "best_posting_times": ["9:00 AM", "1:00 PM", "7:00 PM"],
                "peak_days": ["Tuesday", "Wednesday", "Sunday"],
                "avg_session_duration": f"{random.randint(2, 8)} minutes"
            }
        }
    
    async def analyze_hashtag_performance(self, hashtags: List[str]) -> Dict[str, Any]:
        """Analyze hashtag performance and reach"""
        await asyncio.sleep(0.4)
        
        hashtag_data = {}
        for hashtag in hashtags:
            hashtag_data[hashtag] = {
                "post_count": random.randint(10000, 1000000),
                "avg_engagement": round(random.uniform(2.0, 8.0), 2),
                "difficulty": random.choice(["Low", "Medium", "High"]),
                "trend": random.choice(["Rising", "Stable", "Declining"])
            }
        
        return hashtag_data
    
    def _format_influencer_data(self, influencer: Dict) -> Dict:
        """Format influencer data for API response"""
        return {
            "id": influencer["id"],
            "platform": "instagram",
            "username": influencer["username"],
            "display_name": influencer["full_name"],
            "followers": influencer["followers_count"],
            "engagement_rate": influencer["engagement_rate"],
            "category": influencer["category"],
            "location": influencer["location"],
            "profile_image": influencer["profile_picture_url"],
            "bio": influencer["biography"],
            "verified": influencer["is_verified"],
            "business_account": influencer["is_business_account"],
            "avg_likes": influencer["avg_likes"],
            "avg_comments": influencer["avg_comments"],
            "recent_post": influencer["recent_posts"][0]["caption"] if influencer["recent_posts"] else ""
        }
    
    def _generate_mock_influencer(self, index: int) -> Dict:
        """Generate a mock influencer profile"""
        categories = ["Fashion", "Beauty", "Fitness", "Food", "Travel", "Lifestyle", "Tech", "Art"]
        locations = ["Los Angeles", "New York", "Miami", "Chicago", "Austin", "Seattle", "Denver"]
        
        followers = random.randint(10000, 500000)
        engagement_rate = round(random.uniform(2.0, 8.0), 1)
        
        return {
            "id": f"instagram_{index:03d}",
            "username": f"influencer_{index}",
            "full_name": f"Influencer {index}",
            "followers_count": followers,
            "following_count": random.randint(500, 2000),
            "media_count": random.randint(200, 1500),
            "biography": f"{random.choice(categories)} enthusiast | Creating content daily | DM for collabs",
            "profile_picture_url": f"https://images.unsplash.com/photo-{1500000000 + index}?w=150&h=150&fit=crop&crop=face",
            "is_verified": random.choice([True, False]),
            "is_business_account": True,
            "category": random.choice(categories),
            "location": random.choice(locations),
            "engagement_rate": engagement_rate,
            "avg_likes": int(followers * engagement_rate / 100),
            "avg_comments": int(followers * engagement_rate / 100 * 0.1),
            "avg_views": int(followers * 0.3),
            "recent_posts": [
                {
                    "id": f"post_{index}_001",
                    "caption": self._generate_mock_caption(),
                    "media_type": "IMAGE",
                    "like_count": int(followers * engagement_rate / 100),
                    "comments_count": int(followers * engagement_rate / 100 * 0.1),
                    "timestamp": datetime.now().isoformat(),
                    "hashtags": self._generate_hashtags()
                }
            ]
        }
    
    def _generate_mock_caption(self) -> str:
        """Generate a mock Instagram caption"""
        captions = [
            "Loving this new look! What do you think? ✨",
            "Another day, another adventure! 🌟",
            "Sharing my latest favorites with you all! 💕",
            "Can't believe how amazing this turned out! 🔥",
            "Grateful for all the support from you amazing people! 🙏",
            "New week, new goals! Who's with me? 💪",
            "This has been on my wishlist forever! Finally got it! 🛍️",
            "Throwback to this incredible moment! Missing it already 📸"
        ]
        return random.choice(captions)
    
    def _generate_hashtags(self) -> List[str]:
        """Generate mock hashtags"""
        all_hashtags = [
            "#fashion", "#style", "#ootd", "#beauty", "#lifestyle", "#instagood",
            "#photooftheday", "#love", "#beautiful", "#happy", "#follow", "#like4like",
            "#instadaily", "#selfie", "#me", "#cute", "#tbt", "#followme", "#nature",
            "#fitness", "#food", "#travel", "#art", "#music", "#photography"
        ]
        return random.sample(all_hashtags, random.randint(3, 8))
