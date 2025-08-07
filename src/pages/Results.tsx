import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Progress } from "@/components/ui/progress";
import { 
  ArrowLeft, 
  Instagram, 
  Youtube, 
  Users, 
  TrendingUp, 
  MessageSquare, 
  Eye, 
  Heart, 
  Share2,
  CheckCircle,
  AlertCircle,
  Star,
  Send,
  BarChart3,
  Target,
  Globe,
  Calendar,
  DollarSign
} from "lucide-react";

// Mock data for demonstration
const mockInfluencers = [
  {
    id: 1,
    name: "Sarah Chen",
    handle: "@sarahstyle",
    platform: "instagram",
    followers: 125000,
    engagement: 4.2,
    location: "Los Angeles, CA",
    niche: "Fashion & Lifestyle",
    avatar: "https://images.unsplash.com/photo-1494790108755-2616b612b786?w=150&h=150&fit=crop&crop=face",
    matchScore: 94,
    authenticity: 92,
    audienceMatch: 89,
    recentPost: "Just dropped my sustainable fashion haul! 🌱✨",
    demographics: { female: 78, age2535: 65, age1824: 25 },
    avgViews: 45000,
    avgLikes: 5200,
    estimatedCost: "$800-1200"
  },
  {
    id: 2,
    name: "Alex Rodriguez",
    handle: "@alexfitness",
    platform: "youtube",
    followers: 89000,
    engagement: 6.8,
    location: "Miami, FL",
    niche: "Fitness & Wellness",
    avatar: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&h=150&fit=crop&crop=face",
    matchScore: 91,
    authenticity: 96,
    audienceMatch: 85,
    recentPost: "New workout routine that changed my life! Link in bio 💪",
    demographics: { female: 45, age2535: 55, age1824: 30 },
    avgViews: 12000,
    avgLikes: 820,
    estimatedCost: "$600-900"
  },
  {
    id: 3,
    name: "Emma Thompson",
    handle: "@emmaeats",
    platform: "instagram",
    followers: 67000,
    engagement: 5.1,
    location: "New York, NY",
    niche: "Food & Cooking",
    avatar: "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=150&h=150&fit=crop&crop=face",
    matchScore: 88,
    authenticity: 94,
    audienceMatch: 82,
    recentPost: "Homemade pasta night! Recipe in my stories 🍝",
    demographics: { female: 72, age2535: 48, age1824: 35 },
    avgViews: 8500,
    avgLikes: 430,
    estimatedCost: "$400-700"
  }
];

const campaignMetrics = {
  totalInfluencers: 247,
  highMatch: 23,
  mediumMatch: 89,
  lowMatch: 135,
  avgEngagement: 4.7,
  avgAuthenticity: 91,
  estimatedReach: 2400000,
  estimatedCost: "$15,000-25,000"
};

export default function Results() {
  const [selectedInfluencer, setSelectedInfluencer] = useState(mockInfluencers[0]);
  const [activeTab, setActiveTab] = useState("discovery");
  const navigate = useNavigate();

  const getScoreColor = (score: number) => {
    if (score >= 90) return "text-green-500";
    if (score >= 80) return "text-yellow-500";
    return "text-red-500";
  };

  const getScoreBadge = (score: number) => {
    if (score >= 90) return "bg-green-500/20 text-green-400 border-green-500/30";
    if (score >= 80) return "bg-yellow-500/20 text-yellow-400 border-yellow-500/30";
    return "bg-red-500/20 text-red-400 border-red-500/30";
  };

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border bg-background/95 backdrop-blur">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <Button variant="ghost" onClick={() => navigate('/dashboard')} className="hover:bg-muted/50">
                <ArrowLeft className="h-4 w-4 mr-2" />
                Back to Dashboard
              </Button>
              <div className="text-2xl font-bold bg-gradient-primary bg-clip-text text-transparent">
                ICY
              </div>
            </div>
            <Badge variant="outline" className="border-border">
              Campaign Results
            </Badge>
          </div>
        </div>
      </header>

      <div className="container mx-auto px-4 py-8">
        <div className="max-w-7xl mx-auto">
          {/* Results Header */}
          <div className="mb-8">
            <h1 className="text-3xl font-bold mb-2 text-foreground">🎉 Discovery Complete!</h1>
            <p className="text-muted-foreground">
              Found {campaignMetrics.totalInfluencers} influencers with {campaignMetrics.highMatch} high-quality matches
            </p>
          </div>

          {/* Campaign Overview */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
            <Card className="bg-card border-border">
              <CardContent className="p-6">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm text-muted-foreground">Total Found</p>
                    <p className="text-2xl font-bold text-foreground">{campaignMetrics.totalInfluencers}</p>
                  </div>
                  <Users className="h-8 w-8 text-primary" />
                </div>
              </CardContent>
            </Card>

            <Card className="bg-card border-border">
              <CardContent className="p-6">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm text-muted-foreground">High Matches</p>
                    <p className="text-2xl font-bold text-green-400">{campaignMetrics.highMatch}</p>
                  </div>
                  <Target className="h-8 w-8 text-green-400" />
                </div>
              </CardContent>
            </Card>

            <Card className="bg-card border-border">
              <CardContent className="p-6">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm text-muted-foreground">Est. Reach</p>
                    <p className="text-2xl font-bold text-foreground">{(campaignMetrics.estimatedReach / 1000000).toFixed(1)}M</p>
                  </div>
                  <TrendingUp className="h-8 w-8 text-primary" />
                </div>
              </CardContent>
            </Card>

            <Card className="bg-card border-border">
              <CardContent className="p-6">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm text-muted-foreground">Est. Cost</p>
                    <p className="text-lg font-bold text-foreground">{campaignMetrics.estimatedCost}</p>
                  </div>
                  <DollarSign className="h-8 w-8 text-primary" />
                </div>
              </CardContent>
            </Card>
          </div>

          {/* Main Content Tabs */}
          <Tabs value={activeTab} onValueChange={setActiveTab} className="space-y-6">
            <TabsList className="grid w-full grid-cols-4 bg-muted/20">
              <TabsTrigger value="discovery" className="data-[state=active]:bg-primary data-[state=active]:text-white">
                Smart Discovery
              </TabsTrigger>
              <TabsTrigger value="analysis" className="data-[state=active]:bg-primary data-[state=active]:text-white">
                AI Analysis
              </TabsTrigger>
              <TabsTrigger value="outreach" className="data-[state=active]:bg-primary data-[state=active]:text-white">
                Outreach
              </TabsTrigger>
              <TabsTrigger value="tracking" className="data-[state=active]:bg-primary data-[state=active]:text-white">
                Campaign Tracking
              </TabsTrigger>
            </TabsList>

            {/* Smart Discovery Tab */}
            <TabsContent value="discovery" className="space-y-6">
              <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                {/* Influencer List */}
                <div className="lg:col-span-2 space-y-4">
                  <h3 className="text-xl font-semibold text-foreground">Top Matches</h3>
                  {mockInfluencers.map((influencer) => (
                    <Card 
                      key={influencer.id} 
                      className={`cursor-pointer transition-all border-border ${
                        selectedInfluencer.id === influencer.id 
                          ? 'ring-2 ring-primary bg-primary/5' 
                          : 'hover:bg-muted/30'
                      }`}
                      onClick={() => setSelectedInfluencer(influencer)}
                    >
                      <CardContent className="p-6">
                        <div className="flex items-start space-x-4">
                          <img 
                            src={influencer.avatar} 
                            alt={influencer.name}
                            className="w-16 h-16 rounded-full object-cover"
                          />
                          <div className="flex-1">
                            <div className="flex items-center justify-between mb-2">
                              <div>
                                <h4 className="font-semibold text-foreground">{influencer.name}</h4>
                                <p className="text-sm text-muted-foreground flex items-center">
                                  {influencer.platform === 'instagram' ? 
                                    <Instagram className="h-4 w-4 mr-1" /> : 
                                    <Youtube className="h-4 w-4 mr-1" />
                                  }
                                  {influencer.handle}
                                </p>
                              </div>
                              <Badge className={`${getScoreBadge(influencer.matchScore)}`}>
                                {influencer.matchScore}% Match
                              </Badge>
                            </div>
                            <div className="flex items-center space-x-4 text-sm text-muted-foreground">
                              <span className="flex items-center">
                                <Users className="h-4 w-4 mr-1" />
                                {(influencer.followers / 1000).toFixed(0)}K
                              </span>
                              <span className="flex items-center">
                                <TrendingUp className="h-4 w-4 mr-1" />
                                {influencer.engagement}%
                              </span>
                              <span className="flex items-center">
                                <Globe className="h-4 w-4 mr-1" />
                                {influencer.location}
                              </span>
                            </div>
                            <p className="text-sm mt-2 text-muted-foreground">"{influencer.recentPost}"</p>
                          </div>
                        </div>
                      </CardContent>
                    </Card>
                  ))}
                </div>

                {/* Selected Influencer Details */}
                <div className="space-y-6">
                  <Card className="bg-card border-border">
                    <CardHeader>
                      <CardTitle className="text-foreground">Detailed Analysis</CardTitle>
                      <CardDescription>In-depth metrics for {selectedInfluencer.name}</CardDescription>
                    </CardHeader>
                    <CardContent className="space-y-4">
                      <div>
                        <div className="flex justify-between items-center mb-2">
                          <span className="text-sm text-muted-foreground">Match Score</span>
                          <span className={`font-semibold ${getScoreColor(selectedInfluencer.matchScore)}`}>
                            {selectedInfluencer.matchScore}%
                          </span>
                        </div>
                        <Progress value={selectedInfluencer.matchScore} className="h-2" />
                      </div>

                      <div>
                        <div className="flex justify-between items-center mb-2">
                          <span className="text-sm text-muted-foreground">Authenticity</span>
                          <span className={`font-semibold ${getScoreColor(selectedInfluencer.authenticity)}`}>
                            {selectedInfluencer.authenticity}%
                          </span>
                        </div>
                        <Progress value={selectedInfluencer.authenticity} className="h-2" />
                      </div>

                      <div>
                        <div className="flex justify-between items-center mb-2">
                          <span className="text-sm text-muted-foreground">Audience Match</span>
                          <span className={`font-semibold ${getScoreColor(selectedInfluencer.audienceMatch)}`}>
                            {selectedInfluencer.audienceMatch}%
                          </span>
                        </div>
                        <Progress value={selectedInfluencer.audienceMatch} className="h-2" />
                      </div>

                      <div className="pt-4 border-t border-border">
                        <h4 className="font-medium mb-3 text-foreground">Audience Demographics</h4>
                        <div className="space-y-2 text-sm">
                          <div className="flex justify-between">
                            <span className="text-muted-foreground">Female</span>
                            <span className="text-foreground">{selectedInfluencer.demographics.female}%</span>
                          </div>
                          <div className="flex justify-between">
                            <span className="text-muted-foreground">Age 25-35</span>
                            <span className="text-foreground">{selectedInfluencer.demographics.age2535}%</span>
                          </div>
                          <div className="flex justify-between">
                            <span className="text-muted-foreground">Age 18-24</span>
                            <span className="text-foreground">{selectedInfluencer.demographics.age1824}%</span>
                          </div>
                        </div>
                      </div>

                      <div className="pt-4 border-t border-border">
                        <h4 className="font-medium mb-3 text-foreground">Performance</h4>
                        <div className="space-y-2 text-sm">
                          <div className="flex justify-between">
                            <span className="text-muted-foreground">Avg Views</span>
                            <span className="text-foreground">{(selectedInfluencer.avgViews / 1000).toFixed(1)}K</span>
                          </div>
                          <div className="flex justify-between">
                            <span className="text-muted-foreground">Avg Likes</span>
                            <span className="text-foreground">{(selectedInfluencer.avgLikes / 1000).toFixed(1)}K</span>
                          </div>
                          <div className="flex justify-between">
                            <span className="text-muted-foreground">Est. Cost</span>
                            <span className="text-foreground">{selectedInfluencer.estimatedCost}</span>
                          </div>
                        </div>
                      </div>
                    </CardContent>
                  </Card>
                </div>
              </div>
            </TabsContent>

            {/* AI Analysis Tab */}
            <TabsContent value="analysis" className="space-y-6">
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <Card className="bg-card border-border">
                  <CardHeader>
                    <CardTitle className="flex items-center gap-2 text-foreground">
                      <BarChart3 className="h-5 w-5 text-primary" />
                      Content Analysis
                    </CardTitle>
                    <CardDescription>AI-powered content evaluation</CardDescription>
                  </CardHeader>
                  <CardContent className="space-y-4">
                    <div className="space-y-3">
                      <div className="flex items-center justify-between p-3 bg-muted/20 rounded-lg">
                        <div className="flex items-center space-x-2">
                          <CheckCircle className="h-4 w-4 text-green-400" />
                          <span className="text-sm text-foreground">Brand Alignment</span>
                        </div>
                        <Badge className="bg-green-500/20 text-green-400 border-green-500/30">Excellent</Badge>
                      </div>
                      <div className="flex items-center justify-between p-3 bg-muted/20 rounded-lg">
                        <div className="flex items-center space-x-2">
                          <CheckCircle className="h-4 w-4 text-green-400" />
                          <span className="text-sm text-foreground">Content Quality</span>
                        </div>
                        <Badge className="bg-green-500/20 text-green-400 border-green-500/30">High</Badge>
                      </div>
                      <div className="flex items-center justify-between p-3 bg-muted/20 rounded-lg">
                        <div className="flex items-center space-x-2">
                          <AlertCircle className="h-4 w-4 text-yellow-400" />
                          <span className="text-sm text-foreground">Posting Frequency</span>
                        </div>
                        <Badge className="bg-yellow-500/20 text-yellow-400 border-yellow-500/30">Moderate</Badge>
                      </div>
                    </div>
                    <div className="pt-4 border-t border-border">
                      <h4 className="font-medium mb-2 text-foreground">Recent Content Themes</h4>
                      <div className="flex flex-wrap gap-2">
                        <Badge variant="secondary" className="bg-muted border-border">Sustainability</Badge>
                        <Badge variant="secondary" className="bg-muted border-border">Fashion</Badge>
                        <Badge variant="secondary" className="bg-muted border-border">Lifestyle</Badge>
                        <Badge variant="secondary" className="bg-muted border-border">Reviews</Badge>
                      </div>
                    </div>
                  </CardContent>
                </Card>

                <Card className="bg-card border-border">
                  <CardHeader>
                    <CardTitle className="flex items-center gap-2 text-foreground">
                      <Users className="h-5 w-5 text-primary" />
                      Audience Insights
                    </CardTitle>
                    <CardDescription>Deep audience analysis</CardDescription>
                  </CardHeader>
                  <CardContent className="space-y-4">
                    <div>
                      <h4 className="font-medium mb-3 text-foreground">Audience Overlap</h4>
                      <div className="space-y-2">
                        <div className="flex justify-between items-center">
                          <span className="text-sm text-muted-foreground">Your Target Audience</span>
                          <span className="text-sm font-medium text-green-400">78% Match</span>
                        </div>
                        <Progress value={78} className="h-2" />
                      </div>
                    </div>
                    <div>
                      <h4 className="font-medium mb-3 text-foreground">Engagement Quality</h4>
                      <div className="grid grid-cols-2 gap-4 text-sm">
                        <div className="text-center p-3 bg-muted/20 rounded-lg">
                          <div className="text-lg font-bold text-foreground">4.2%</div>
                          <div className="text-muted-foreground">Avg Engagement</div>
                        </div>
                        <div className="text-center p-3 bg-muted/20 rounded-lg">
                          <div className="text-lg font-bold text-foreground">92%</div>
                          <div className="text-muted-foreground">Real Followers</div>
                        </div>
                      </div>
                    </div>
                    <div>
                      <h4 className="font-medium mb-3 text-foreground">Top Interests</h4>
                      <div className="space-y-2 text-sm">
                        <div className="flex justify-between">
                          <span className="text-muted-foreground">Fashion & Style</span>
                          <span className="text-foreground">45%</span>
                        </div>
                        <div className="flex justify-between">
                          <span className="text-muted-foreground">Sustainability</span>
                          <span className="text-foreground">32%</span>
                        </div>
                        <div className="flex justify-between">
                          <span className="text-muted-foreground">Beauty</span>
                          <span className="text-foreground">28%</span>
                        </div>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </div>
            </TabsContent>

            {/* Outreach Tab */}
            <TabsContent value="outreach" className="space-y-6">
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <Card className="bg-card border-border">
                  <CardHeader>
                    <CardTitle className="flex items-center gap-2 text-foreground">
                      <MessageSquare className="h-5 w-5 text-primary" />
                      Personalized Messages
                    </CardTitle>
                    <CardDescription>AI-generated outreach messages</CardDescription>
                  </CardHeader>
                  <CardContent className="space-y-4">
                    <div className="p-4 bg-muted/20 rounded-lg border border-border">
                      <div className="flex items-center justify-between mb-3">
                        <span className="font-medium text-foreground">Message for Sarah Chen</span>
                        <Badge className="bg-primary/20 text-primary border-primary/30">Generated</Badge>
                      </div>
                      <div className="text-sm text-muted-foreground space-y-2">
                        <p>Hi Sarah! 👋</p>
                        <p>I absolutely loved your recent sustainable fashion haul post - the way you styled that vintage blazer was incredible! Your commitment to eco-friendly fashion aligns perfectly with our brand values.</p>
                        <p>We'd love to collaborate with you on our new sustainable clothing line. Would you be interested in discussing a partnership?</p>
                        <p>Best regards,<br/>The ICY Team</p>
                      </div>
                      <div className="flex space-x-2 mt-4">
                        <Button size="sm" className="bg-gradient-primary border-0">
                          <Send className="h-4 w-4 mr-2" />
                          Send Message
                        </Button>
                        <Button size="sm" variant="outline" className="border-border hover:bg-muted/50">
                          Edit
                        </Button>
                      </div>
                    </div>

                    <div className="p-4 bg-muted/20 rounded-lg border border-border">
                      <div className="flex items-center justify-between mb-3">
                        <span className="font-medium text-foreground">Message for Alex Rodriguez</span>
                        <Badge className="bg-primary/20 text-primary border-primary/30">Generated</Badge>
                      </div>
                      <div className="text-sm text-muted-foreground space-y-2">
                        <p>Hey Alex! 💪</p>
                        <p>Your latest workout routine video was amazing - I can see why your community loves your authentic approach to fitness! Your engagement with your audience is exactly what we're looking for.</p>
                        <p>We have a new fitness product line that would be perfect for your audience. Interested in learning more?</p>
                        <p>Cheers,<br/>The ICY Team</p>
                      </div>
                      <div className="flex space-x-2 mt-4">
                        <Button size="sm" className="bg-gradient-primary border-0">
                          <Send className="h-4 w-4 mr-2" />
                          Send Message
                        </Button>
                        <Button size="sm" variant="outline" className="border-border hover:bg-muted/50">
                          Edit
                        </Button>
                      </div>
                    </div>
                  </CardContent>
                </Card>

                <Card className="bg-card border-border">
                  <CardHeader>
                    <CardTitle className="flex items-center gap-2 text-foreground">
                      <TrendingUp className="h-5 w-5 text-primary" />
                      Outreach Strategy
                    </CardTitle>
                    <CardDescription>Optimized campaign approach</CardDescription>
                  </CardHeader>
                  <CardContent className="space-y-4">
                    <div className="space-y-3">
                      <div className="p-3 bg-muted/20 rounded-lg">
                        <div className="flex items-center justify-between mb-2">
                          <span className="font-medium text-foreground">Phase 1: Top Tier</span>
                          <Badge className="bg-green-500/20 text-green-400 border-green-500/30">5 Influencers</Badge>
                        </div>
                        <p className="text-sm text-muted-foreground">Target highest-match influencers first for maximum impact</p>
                      </div>
                      <div className="p-3 bg-muted/20 rounded-lg">
                        <div className="flex items-center justify-between mb-2">
                          <span className="font-medium text-foreground">Phase 2: Mid Tier</span>
                          <Badge className="bg-yellow-500/20 text-yellow-400 border-yellow-500/30">12 Influencers</Badge>
                        </div>
                        <p className="text-sm text-muted-foreground">Follow up with good matches for broader reach</p>
                      </div>
                      <div className="p-3 bg-muted/20 rounded-lg">
                        <div className="flex items-center justify-between mb-2">
                          <span className="font-medium text-foreground">Phase 3: Volume</span>
                          <Badge className="bg-blue-500/20 text-blue-400 border-blue-500/30">25 Influencers</Badge>
                        </div>
                        <p className="text-sm text-muted-foreground">Scale with micro-influencers for cost efficiency</p>
                      </div>
                    </div>

                    <div className="pt-4 border-t border-border">
                      <h4 className="font-medium mb-3 text-foreground">Recommended Timeline</h4>
                      <div className="space-y-2 text-sm">
                        <div className="flex items-center space-x-2">
                          <Calendar className="h-4 w-4 text-primary" />
                          <span className="text-muted-foreground">Week 1:</span>
                          <span className="text-foreground">Initial outreach to top 5</span>
                        </div>
                        <div className="flex items-center space-x-2">
                          <Calendar className="h-4 w-4 text-primary" />
                          <span className="text-muted-foreground">Week 2:</span>
                          <span className="text-foreground">Follow-ups and mid-tier outreach</span>
                        </div>
                        <div className="flex items-center space-x-2">
                          <Calendar className="h-4 w-4 text-primary" />
                          <span className="text-muted-foreground">Week 3:</span>
                          <span className="text-foreground">Volume outreach and negotiations</span>
                        </div>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </div>
            </TabsContent>

            {/* Campaign Tracking Tab */}
            <TabsContent value="tracking" className="space-y-6">
              <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <Card className="bg-card border-border">
                  <CardHeader>
                    <CardTitle className="text-foreground">Response Rates</CardTitle>
                    <CardDescription>Outreach performance metrics</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-4">
                      <div className="text-center">
                        <div className="text-3xl font-bold text-primary">24%</div>
                        <div className="text-sm text-muted-foreground">Overall Response Rate</div>
                      </div>
                      <div className="space-y-2">
                        <div className="flex justify-between text-sm">
                          <span className="text-muted-foreground">Messages Sent</span>
                          <span className="text-foreground">42</span>
                        </div>
                        <div className="flex justify-between text-sm">
                          <span className="text-muted-foreground">Responses</span>
                          <span className="text-foreground">10</span>
                        </div>
                        <div className="flex justify-between text-sm">
                          <span className="text-muted-foreground">Interested</span>
                          <span className="text-green-400">7</span>
                        </div>
                        <div className="flex justify-between text-sm">
                          <span className="text-muted-foreground">Confirmed</span>
                          <span className="text-green-400">3</span>
                        </div>
                      </div>
                    </div>
                  </CardContent>
                </Card>

                <Card className="bg-card border-border">
                  <CardHeader>
                    <CardTitle className="text-foreground">Campaign Performance</CardTitle>
                    <CardDescription>Live campaign metrics</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-4">
                      <div className="grid grid-cols-2 gap-4 text-center">
                        <div>
                          <div className="text-2xl font-bold text-foreground">1.2M</div>
                          <div className="text-xs text-muted-foreground">Total Reach</div>
                        </div>
                        <div>
                          <div className="text-2xl font-bold text-foreground">45K</div>
                          <div className="text-xs text-muted-foreground">Engagements</div>
                        </div>
                      </div>
                      <div className="space-y-2">
                        <div className="flex justify-between text-sm">
                          <span className="text-muted-foreground">Click-through Rate</span>
                          <span className="text-foreground">3.8%</span>
                        </div>
                        <div className="flex justify-between text-sm">
                          <span className="text-muted-foreground">Conversion Rate</span>
                          <span className="text-foreground">2.1%</span>
                        </div>
                        <div className="flex justify-between text-sm">
                          <span className="text-muted-foreground">Cost per Click</span>
                          <span className="text-foreground">$0.85</span>
                        </div>
                        <div className="flex justify-between text-sm">
                          <span className="text-muted-foreground">ROI</span>
                          <span className="text-green-400">+180%</span>
                        </div>
                      </div>
                    </div>
                  </CardContent>
                </Card>

                <Card className="bg-card border-border">
                  <CardHeader>
                    <CardTitle className="text-foreground">Active Campaigns</CardTitle>
                    <CardDescription>Current collaborations</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-3">
                      <div className="p-3 bg-muted/20 rounded-lg">
                        <div className="flex items-center justify-between mb-1">
                          <span className="font-medium text-sm text-foreground">Sarah Chen</span>
                          <Badge className="bg-green-500/20 text-green-400 border-green-500/30 text-xs">Live</Badge>
                        </div>
                        <div className="text-xs text-muted-foreground">Instagram Story + Post</div>
                        <div className="text-xs text-muted-foreground">Est. reach: 125K</div>
                      </div>
                      <div className="p-3 bg-muted/20 rounded-lg">
                        <div className="flex items-center justify-between mb-1">
                          <span className="font-medium text-sm text-foreground">Alex Rodriguez</span>
                          <Badge className="bg-yellow-500/20 text-yellow-400 border-yellow-500/30 text-xs">Pending</Badge>
                        </div>
                        <div className="text-xs text-muted-foreground">YouTube Video</div>
                        <div className="text-xs text-muted-foreground">Est. reach: 89K</div>
                      </div>
                      <div className="p-3 bg-muted/20 rounded-lg">
                        <div className="flex items-center justify-between mb-1">
                          <span className="font-medium text-sm text-foreground">Emma Thompson</span>
                          <Badge className="bg-blue-500/20 text-blue-400 border-blue-500/30 text-xs">Negotiating</Badge>
                        </div>
                        <div className="text-xs text-muted-foreground">Instagram Reel</div>
                        <div className="text-xs text-muted-foreground">Est. reach: 67K</div>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </div>

              <Card className="bg-card border-border">
                <CardHeader>
                  <CardTitle className="text-foreground">Performance Insights</CardTitle>
                  <CardDescription>AI-powered recommendations</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div className="space-y-3">
                      <h4 className="font-medium text-foreground">What's Working</h4>
                      <div className="space-y-2">
                        <div className="flex items-center space-x-2 text-sm">
                          <CheckCircle className="h-4 w-4 text-green-400" />
                          <span className="text-muted-foreground">Fashion influencers show 40% higher engagement</span>
                        </div>
                        <div className="flex items-center space-x-2 text-sm">
                          <CheckCircle className="h-4 w-4 text-green-400" />
                          <span className="text-muted-foreground">Instagram Stories drive 60% more clicks</span>
                        </div>
                        <div className="flex items-center space-x-2 text-sm">
                          <CheckCircle className="h-4 w-4 text-green-400" />
                          <span className="text-muted-foreground">Personalized messages get 3x more responses</span>
                        </div>
                      </div>
                    </div>
                    <div className="space-y-3">
                      <h4 className="font-medium text-foreground">Recommendations</h4>
                      <div className="space-y-2">
                        <div className="flex items-center space-x-2 text-sm">
                          <Star className="h-4 w-4 text-yellow-400" />
                          <span className="text-muted-foreground">Focus on micro-influencers (10K-100K followers)</span>
                        </div>
                        <div className="flex items-center space-x-2 text-sm">
                          <Star className="h-4 w-4 text-yellow-400" />
                          <span className="text-muted-foreground">Increase video content collaborations</span>
                        </div>
                        <div className="flex items-center space-x-2 text-sm">
                          <Star className="h-4 w-4 text-yellow-400" />
                          <span className="text-muted-foreground">Target lifestyle + sustainability niches</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </CardContent>
              </Card>
            </TabsContent>
          </Tabs>
        </div>
      </div>
    </div>
  );
}
