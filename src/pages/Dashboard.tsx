import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Sparkles, Target, Users, TrendingUp, Search, BarChart3, MessageSquare, Settings } from "lucide-react";

interface BrandData {
  productName: string;
  productDescription: string;
  targetAge: string[];
  targetGender: string[];
  targetInterests: string;
  targetRegion: string;
  brandTone: string;
  campaignGoal: string;
  platforms: string[];
  budgetLevel: string;
}

export default function Dashboard() {
  const [brandData, setBrandData] = useState<BrandData | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    const storedData = localStorage.getItem('icyBrandData');
    if (storedData) {
      setBrandData(JSON.parse(storedData));
    } else {
      // If no brand data, redirect to onboarding
      navigate('/onboarding');
    }
  }, [navigate]);

  if (!brandData) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary"></div>
      </div>
    );
  }

  const handleStartDiscovery = () => {
    navigate('/discovery');
  };

  const platformLabels = {
    instagram: "Instagram",
    youtube: "YouTube"
  };

  const goalLabels = {
    awareness: "Brand Awareness",
    sales: "Drive Sales",
    ugc: "User Generated Content",
    engagement: "Engagement"
  };

  const budgetLabels = {
    micro: "Micro Influencers",
    mid: "Mid-tier Influencers", 
    macro: "Macro Influencers"
  };

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="border-b border-border bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <div className="text-2xl font-bold bg-gradient-primary bg-clip-text text-transparent">
                ICY
              </div>
              <Badge variant="outline" className="text-xs border-border">
                AI Influencer Outreach
              </Badge>
            </div>
            <Button variant="outline" size="sm" className="border-border hover:bg-muted/50">
              <Settings className="h-4 w-4 mr-2" />
              Settings
            </Button>
          </div>
        </div>
      </header>

      <div className="container mx-auto px-4 py-8">
        <div className="max-w-6xl mx-auto">
          {/* Welcome Section */}
          <div className="mb-8">
            <h1 className="text-3xl font-bold mb-2">Welcome back! 👋</h1>
            <p className="text-muted-foreground">
              Ready to find perfect influencers for {brandData.productName}?
            </p>
          </div>

          {/* Brand Summary Card */}
          <Card className="bg-card border-border shadow-soft mb-8">
            <CardHeader>
              <div className="flex items-center justify-between">
                <div>
                  <CardTitle className="flex items-center gap-2 text-foreground">
                    <Target className="h-5 w-5 text-primary" />
                    {brandData.productName}
                  </CardTitle>
                  <CardDescription className="mt-2 text-muted-foreground">
                    {brandData.productDescription}
                  </CardDescription>
                </div>
                <Button variant="outline" size="sm" className="border-border hover:bg-muted/50">
                  Edit Setup
                </Button>
              </div>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                <div>
                  <h4 className="font-medium mb-2">Target Audience</h4>
                  <div className="flex flex-wrap gap-1">
                    {brandData.targetAge.map(age => (
                      <Badge key={age} variant="secondary" className="text-xs">{age}</Badge>
                    ))}
                  </div>
                  <div className="flex flex-wrap gap-1 mt-1">
                    {brandData.targetGender.map(gender => (
                      <Badge key={gender} variant="outline" className="text-xs">{gender}</Badge>
                    ))}
                  </div>
                </div>
                
                <div>
                  <h4 className="font-medium mb-2">Campaign Goal</h4>
                  <Badge variant="default">{goalLabels[brandData.campaignGoal as keyof typeof goalLabels]}</Badge>
                </div>

                <div>
                  <h4 className="font-medium mb-2">Platforms</h4>
                  <div className="flex flex-wrap gap-1">
                    {brandData.platforms.map(platform => (
                      <Badge key={platform} variant="secondary">
                        {platformLabels[platform as keyof typeof platformLabels]}
                      </Badge>
                    ))}
                  </div>
                </div>

                <div>
                  <h4 className="font-medium mb-2">Influencer Tier</h4>
                  <Badge variant="outline">
                    {budgetLabels[brandData.budgetLevel as keyof typeof budgetLabels]}
                  </Badge>
                </div>
              </div>
            </CardContent>
          </Card>

          {/* Main Action */}
          <Card className="bg-gradient-primary text-white shadow-purple mb-8 border-0">
            <CardContent className="p-8 text-center">
              <Sparkles className="h-16 w-16 mx-auto mb-4 animate-pulse-glow" />
              <h2 className="text-2xl font-bold mb-2">Ready to Find Influencers?</h2>
              <p className="mb-6 opacity-90">
                Our AI will analyze thousands of influencers to find perfect matches for your brand
              </p>
              <Button
                size="lg"
                variant="secondary"
                className="bg-white text-primary hover:bg-white/90 border-0"
                onClick={handleStartDiscovery}
              >
                <Search className="h-5 w-5 mr-2" />
                Start Influencer Discovery
              </Button>
            </CardContent>
          </Card>

          {/* Stats Overview */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
            <Card className="bg-card border-border shadow-soft">
              <CardContent className="p-6">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm text-muted-foreground">Total Campaigns</p>
                    <p className="text-2xl font-bold text-foreground">0</p>
                  </div>
                  <BarChart3 className="h-8 w-8 text-primary" />
                </div>
              </CardContent>
            </Card>

            <Card className="bg-card border-border shadow-soft">
              <CardContent className="p-6">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm text-muted-foreground">Influencers Found</p>
                    <p className="text-2xl font-bold text-foreground">0</p>
                  </div>
                  <Users className="h-8 w-8 text-primary" />
                </div>
              </CardContent>
            </Card>

            <Card className="bg-card border-border shadow-soft">
              <CardContent className="p-6">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="text-sm text-muted-foreground">Messages Sent</p>
                    <p className="text-2xl font-bold text-foreground">0</p>
                  </div>
                  <MessageSquare className="h-8 w-8 text-primary" />
                </div>
              </CardContent>
            </Card>
          </div>

          {/* Quick Actions */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <Card className="bg-card border-border shadow-soft">
              <CardHeader>
                <CardTitle className="flex items-center gap-2 text-foreground">
                  <Search className="h-5 w-5 text-primary" />
                  Discover Influencers
                </CardTitle>
                <CardDescription className="text-muted-foreground">
                  Find influencers that match your brand and audience
                </CardDescription>
              </CardHeader>
              <CardContent>
                <Button className="w-full bg-gradient-primary border-0" onClick={handleStartDiscovery}>
                  Start Discovery
                </Button>
              </CardContent>
            </Card>

            <Card className="bg-card border-border shadow-soft">
              <CardHeader>
                <CardTitle className="flex items-center gap-2 text-foreground">
                  <TrendingUp className="h-5 w-5 text-primary" />
                  Campaign Analytics
                </CardTitle>
                <CardDescription className="text-muted-foreground">
                  Track your campaign performance and ROI
                </CardDescription>
              </CardHeader>
              <CardContent>
                <Button variant="outline" className="w-full border-border hover:bg-muted/50" disabled>
                  View Analytics
                </Button>
              </CardContent>
            </Card>
          </div>
        </div>
      </div>
    </div>
  );
}