"""
AI Message Generator Module
Generates personalized outreach messages for influencer collaborations
"""

import asyncio
import random
from typing import Dict, List, Any, Optional
from datetime import datetime
import re

class MessageGenerator:
    """AI-powered personalized message generator"""
    
    def __init__(self):
        self.model_version = "ICY-MessageAI-v1.5"
        
        # Message templates by brand tone
        self.templates = {
            "professional": {
                "greeting": [
                    "Dear {name},",
                    "Hello {name},",
                    "Hi {name},"
                ],
                "opening": [
                    "I hope this message finds you well.",
                    "I trust you're doing well.",
                    "I hope you're having a great day."
                ],
                "compliment": [
                    "I've been following your content and am impressed by your {content_focus}.",
                    "Your recent work on {content_focus} caught our attention.",
                    "We admire your expertise in {content_focus}."
                ],
                "proposal": [
                    "We would like to explore a potential collaboration opportunity.",
                    "I'd love to discuss a partnership opportunity with you.",
                    "We have an exciting collaboration proposal for you."
                ],
                "closing": [
                    "I look forward to hearing from you.",
                    "Please let me know if you're interested.",
                    "I'd be happy to discuss this further at your convenience."
                ]
            },
            "friendly": {
                "greeting": [
                    "Hey {name}! 👋",
                    "Hi {name}!",
                    "Hello {name}! 😊"
                ],
                "opening": [
                    "Hope you're having an amazing day!",
                    "I hope you're doing well!",
                    "Hope all is good with you!"
                ],
                "compliment": [
                    "I absolutely love your content about {content_focus}! 💕",
                    "Your {content_focus} posts are incredible!",
                    "I'm such a fan of your {content_focus} content! ✨"
                ],
                "proposal": [
                    "I'd love to chat about a fun collaboration opportunity!",
                    "We have an exciting partnership idea for you!",
                    "Would you be interested in working together on something cool?"
                ],
                "closing": [
                    "Can't wait to hear from you! 🌟",
                    "Hope to connect soon!",
                    "Looking forward to your thoughts! 💭"
                ]
            },
            "luxury": {
                "greeting": [
                    "Dear {name},",
                    "Greetings {name},"
                ],
                "opening": [
                    "I trust this message finds you in excellent spirits.",
                    "I hope this note reaches you well."
                ],
                "compliment": [
                    "Your sophisticated approach to {content_focus} aligns perfectly with our brand values.",
                    "We've been captivated by your elegant {content_focus} content.",
                    "Your refined taste in {content_focus} resonates with our luxury brand."
                ],
                "proposal": [
                    "We would be honored to collaborate with you on an exclusive partnership.",
                    "I'd like to present an exclusive collaboration opportunity.",
                    "We have a premium partnership proposal that I believe would interest you."
                ],
                "closing": [
                    "I would be delighted to discuss this opportunity further.",
                    "I look forward to the possibility of working together.",
                    "Please let me know if this aligns with your interests."
                ]
            },
            "playful": {
                "greeting": [
                    "Hey there {name}! 🎉",
                    "Hi {name}! ✨",
                    "Hello amazing {name}! 🌟"
                ],
                "opening": [
                    "Hope you're having the best day ever!",
                    "Sending good vibes your way! ✨",
                    "Hope your day is as awesome as your content! 🔥"
                ],
                "compliment": [
                    "Your {content_focus} content is absolutely fire! 🔥",
                    "I'm obsessed with your {content_focus} posts! 😍",
                    "Your {content_focus} game is on point! 💯"
                ],
                "proposal": [
                    "We've got something super exciting to share with you! 🎊",
                    "Ready for an epic collaboration? 🚀",
                    "Want to create something amazing together? ✨"
                ],
                "closing": [
                    "Let's make magic happen! ✨",
                    "Can't wait to hear your thoughts! 🎉",
                    "Ready to rock this together? 🤘"
                ]
            }
        }
        
        # Content-specific references
        self.content_references = {
            "fashion": ["styling", "outfit coordination", "fashion sense", "trendsetting"],
            "beauty": ["makeup artistry", "skincare routine", "beauty tips", "glam looks"],
            "fitness": ["workout routines", "fitness journey", "health tips", "transformation"],
            "food": ["recipe creation", "cooking skills", "food photography", "culinary expertise"],
            "tech": ["tech reviews", "product insights", "technical knowledge", "innovation coverage"],
            "lifestyle": ["lifestyle content", "daily inspiration", "life tips", "authentic sharing"],
            "travel": ["travel adventures", "destination guides", "travel photography", "wanderlust content"]
        }
    
    async def generate_personalized_message(self, influencer_id: str, brand_data: Dict, message_type: str = "collaboration") -> Dict[str, Any]:
        """Generate a personalized outreach message"""
        await asyncio.sleep(0.8)  # Simulate AI processing
        
        # Get influencer data (simulated)
        influencer_data = await self._get_influencer_context(influencer_id)
        
        # Determine brand tone
        brand_tone = brand_data.get("brandTone", "friendly")
        if brand_tone not in self.templates:
            brand_tone = "friendly"
        
        # Generate message components
        message_parts = await self._generate_message_parts(
            influencer_data, brand_data, brand_tone, message_type
        )
        
        # Assemble final message
        full_message = self._assemble_message(message_parts)
        
        # Generate subject line
        subject = await self._generate_subject_line(influencer_data, brand_data, message_type)
        
        # Calculate personalization score
        personalization_score = self._calculate_personalization_score(message_parts, influencer_data)
        
        return {
            "message": full_message,
            "subject": subject,
            "personalization_score": personalization_score,
            "message_type": message_type,
            "brand_tone": brand_tone,
            "generated_at": datetime.now().isoformat(),
            "influencer_id": influencer_id
        }
    
    async def _get_influencer_context(self, influencer_id: str) -> Dict[str, Any]:
        """Get influencer context for personalization"""
        await asyncio.sleep(0.2)
        
        # Simulate fetching influencer data
        mock_data = {
            "instagram_001": {
                "name": "Sarah Chen",
                "username": "sarahstyle",
                "platform": "instagram",
                "category": "fashion",
                "recent_post": "Just dropped my sustainable fashion haul! 🌱✨",
                "follower_count": 125000,
                "engagement_rate": 4.2,
                "content_themes": ["sustainable fashion", "styling tips", "eco-friendly finds"]
            },
            "youtube_001": {
                "name": "Alex Rodriguez",
                "username": "alexfitness",
                "platform": "youtube",
                "category": "fitness",
                "recent_post": "New workout routine that changed my life! Full body transformation",
                "follower_count": 89000,
                "engagement_rate": 6.8,
                "content_themes": ["workout routines", "fitness transformation", "health tips"]
            },
            "instagram_002": {
                "name": "Emma Thompson",
                "username": "emmaeats",
                "platform": "instagram",
                "category": "food",
                "recent_post": "Homemade pasta night! 🍝 This creamy mushroom linguine is pure comfort food",
                "follower_count": 67000,
                "engagement_rate": 5.1,
                "content_themes": ["home cooking", "easy recipes", "comfort food"]
            }
        }
        
        return mock_data.get(influencer_id, {
            "name": "Creator",
            "username": "creator",
            "platform": "instagram",
            "category": "lifestyle",
            "recent_post": "Creating amazing content daily!",
            "follower_count": random.randint(10000, 200000),
            "engagement_rate": round(random.uniform(3.0, 7.0), 1),
            "content_themes": ["lifestyle", "daily inspiration", "authentic content"]
        })
    
    async def _generate_message_parts(self, influencer_data: Dict, brand_data: Dict, brand_tone: str, message_type: str) -> Dict[str, str]:
        """Generate individual message components"""
        await asyncio.sleep(0.3)
        
        template = self.templates[brand_tone]
        name = influencer_data.get("name", "there")
        category = influencer_data.get("category", "lifestyle")
        
        # Get content focus for personalization
        content_focus = random.choice(self.content_references.get(category, ["content"]))
        
        # Generate each part
        parts = {
            "greeting": random.choice(template["greeting"]).format(name=name),
            "opening": random.choice(template["opening"]),
            "compliment": random.choice(template["compliment"]).format(content_focus=content_focus),
            "personal_reference": await self._generate_personal_reference(influencer_data),
            "brand_introduction": await self._generate_brand_introduction(brand_data, brand_tone),
            "proposal": random.choice(template["proposal"]),
            "value_proposition": await self._generate_value_proposition(brand_data, influencer_data),
            "call_to_action": await self._generate_call_to_action(brand_tone),
            "closing": random.choice(template["closing"])
        }
        
        return parts
    
    async def _generate_personal_reference(self, influencer_data: Dict) -> str:
        """Generate a personal reference to recent content"""
        await asyncio.sleep(0.1)
        
        recent_post = influencer_data.get("recent_post", "")
        platform = influencer_data.get("platform", "instagram")
        
        if not recent_post:
            return ""
        
        # Extract key elements from recent post
        if "sustainable" in recent_post.lower():
            return "I especially loved your recent post about sustainable fashion - it really resonates with our brand values!"
        elif "workout" in recent_post.lower() or "fitness" in recent_post.lower():
            return "Your latest workout video was incredible - the transformation results speak for themselves!"
        elif "recipe" in recent_post.lower() or "cooking" in recent_post.lower():
            return "That homemade pasta recipe you shared looked absolutely delicious!"
        elif platform == "youtube":
            return "Your recent video content has been amazing - the production quality is top-notch!"
        else:
            return "I saw your recent post and it perfectly captures what we love about your content!"
    
    async def _generate_brand_introduction(self, brand_data: Dict, brand_tone: str) -> str:
        """Generate brand introduction"""
        await asyncio.sleep(0.1)
        
        product_name = brand_data.get("productName", "our brand")
        product_description = brand_data.get("productDescription", "")
        
        if brand_tone == "professional":
            return f"I'm reaching out from {product_name}. {product_description[:100]}..."
        elif brand_tone == "friendly":
            return f"I'm from the team at {product_name}! We're all about {product_description[:80]}..."
        elif brand_tone == "luxury":
            return f"I represent {product_name}, a premium brand that {product_description[:90]}..."
        else:  # playful
            return f"I'm with the awesome team at {product_name}! We're doing some cool stuff with {product_description[:70]}..."
    
    async def _generate_value_proposition(self, brand_data: Dict, influencer_data: Dict) -> str:
        """Generate value proposition for the collaboration"""
        await asyncio.sleep(0.1)
        
        campaign_goal = brand_data.get("campaignGoal", "awareness")
        follower_count = influencer_data.get("follower_count", 0)
        
        value_props = {
            "awareness": "This collaboration would help introduce our brand to your amazing community while providing your followers with products they'll genuinely love.",
            "sales": "We're looking for authentic partnerships that drive real value for both your audience and our brand.",
            "ugc": "We'd love to work with you to create authentic content that showcases our products in your unique style.",
            "engagement": "This partnership would create engaging content that resonates with your audience while highlighting our brand values."
        }
        
        base_prop = value_props.get(campaign_goal, value_props["awareness"])
        
        # Add follower-specific benefits
        if follower_count > 100000:
            base_prop += " Given your impressive reach, this could be a fantastic opportunity for both of us!"
        else:
            base_prop += " Your engaged community is exactly the audience we're looking to connect with!"
        
        return base_prop
    
    async def _generate_call_to_action(self, brand_tone: str) -> str:
        """Generate appropriate call to action"""
        await asyncio.sleep(0.05)
        
        ctas = {
            "professional": "Would you be available for a brief call this week to discuss the details?",
            "friendly": "Would you be up for a quick chat about this? I'd love to hear your thoughts!",
            "luxury": "I would be delighted to arrange a call to discuss this exclusive opportunity.",
            "playful": "Want to hop on a call and brainstorm some amazing content ideas together?"
        }
        
        return ctas.get(brand_tone, ctas["friendly"])
    
    async def _generate_subject_line(self, influencer_data: Dict, brand_data: Dict, message_type: str) -> str:
        """Generate compelling subject line"""
        await asyncio.sleep(0.1)
        
        name = influencer_data.get("name", "Creator")
        product_name = brand_data.get("productName", "Brand")
        brand_tone = brand_data.get("brandTone", "friendly")
        
        subject_templates = {
            "professional": [
                f"Collaboration Opportunity - {product_name} x {name}",
                f"Partnership Proposal for {name}",
                f"Brand Collaboration Inquiry - {product_name}"
            ],
            "friendly": [
                f"Hey {name}! Collaboration opportunity 🌟",
                f"Would love to work with you, {name}! ✨",
                f"Exciting partnership idea for you, {name}!"
            ],
            "luxury": [
                f"Exclusive Partnership Opportunity - {product_name}",
                f"Premium Collaboration Proposal for {name}",
                f"Luxury Brand Partnership - {product_name}"
            ],
            "playful": [
                f"Let's create something amazing together, {name}! 🎉",
                f"Epic collab opportunity for you! 🚀",
                f"Ready to make some magic, {name}? ✨"
            ]
        }
        
        templates = subject_templates.get(brand_tone, subject_templates["friendly"])
        return random.choice(templates)
    
    def _assemble_message(self, parts: Dict[str, str]) -> str:
        """Assemble the final message from parts"""
        message_parts = [
            parts["greeting"],
            "",  # Empty line
            parts["opening"],
            "",
            parts["compliment"],
            parts["personal_reference"],
            "",
            parts["brand_introduction"],
            "",
            parts["proposal"],
            parts["value_proposition"],
            "",
            parts["call_to_action"],
            "",
            parts["closing"],
            "",
            "Best regards,",
            "The ICY Team"
        ]
        
        # Remove empty parts and join
        filtered_parts = [part for part in message_parts if part is not None and part != ""]
        return "\n".join(filtered_parts)
    
    def _calculate_personalization_score(self, parts: Dict[str, str], influencer_data: Dict) -> float:
        """Calculate how personalized the message is"""
        score = 0.5  # Base score
        
        # Check for name usage
        name = influencer_data.get("name", "")
        if name and name in parts.get("greeting", ""):
            score += 0.15
        
        # Check for personal reference
        if parts.get("personal_reference") and len(parts["personal_reference"]) > 10:
            score += 0.2
        
        # Check for category-specific content
        category = influencer_data.get("category", "")
        message_text = " ".join(parts.values()).lower()
        if category and category in message_text:
            score += 0.1
        
        # Check for platform-specific references
        platform = influencer_data.get("platform", "")
        if platform and platform in message_text:
            score += 0.05
        
        return min(score, 0.95)  # Cap at 95%
