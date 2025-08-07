import React from "react";
import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Sparkles, Target, Users, TrendingUp, ArrowRight, Search, BarChart3, MessageSquare } from "lucide-react";

const Index = () => {
  const navigate = useNavigate();

  const features = [
    {
      icon: Search,
      title: "AI-Powered Discovery",
      description: "Find perfect influencers using advanced AI algorithms that analyze content, audience, and brand fit."
    },
    {
      icon: Target,
      title: "Brand Matching",
      description: "Get precise compatibility scores based on your brand values, target audience, and campaign goals."
    },
    {
      icon: MessageSquare,
      title: "Personalized Outreach",
      description: "Generate custom messages that resonate with each influencer's style and audience."
    },
    {
      icon: BarChart3,
      title: "Campaign Analytics",
      description: "Track performance, engagement rates, and ROI with comprehensive analytics dashboard."
    }
  ];

  return (
    <div className="min-h-screen bg-gradient-ice">
      {/* Hero Section */}
      <div className="container mx-auto px-4 py-16">
        <div className="max-w-4xl mx-auto text-center">
          {/* Logo/Brand */}
          <div className="inline-flex items-center justify-center w-20 h-20 bg-gradient-primary rounded-full mb-8 animate-pulse-glow">
            <Sparkles className="h-10 w-10 text-white" />
          </div>
          
          {/* Main Headline */}
          <h1 className="text-6xl font-bold mb-6">
            <span className="bg-gradient-primary bg-clip-text text-transparent">
              ICY
            </span>
            <br />
            <span className="text-foreground">
              Smart Influencer Outreach
            </span>
          </h1>
          
          <p className="text-xl text-muted-foreground mb-8 max-w-2xl mx-auto">
            Discover, analyze, and connect with the perfect influencers for your brand. 
            Our AI-driven platform makes influencer marketing effortless and effective.
          </p>

          <div className="flex flex-col sm:flex-row gap-4 justify-center mb-12">
            <Button 
              size="lg" 
              className="bg-gradient-primary hover:shadow-glow"
              onClick={() => navigate('/onboarding')}
            >
              Get Started Free
              <ArrowRight className="h-5 w-5 ml-2" />
            </Button>
            <Button 
              size="lg" 
              variant="outline"
              onClick={() => navigate('/dashboard')}
            >
              View Demo
              <Search className="h-5 w-5 ml-2" />
            </Button>
          </div>

          {/* Trust Badges */}
          <div className="flex flex-wrap justify-center gap-4 mb-16">
            <Badge variant="secondary" className="px-4 py-2">
              <Users className="h-4 w-4 mr-2" />
              10K+ Influencers Analyzed
            </Badge>
            <Badge variant="secondary" className="px-4 py-2">
              <TrendingUp className="h-4 w-4 mr-2" />
              95% Match Accuracy
            </Badge>
            <Badge variant="secondary" className="px-4 py-2">
              <Sparkles className="h-4 w-4 mr-2" />
              AI-Powered Matching
            </Badge>
          </div>
        </div>

        {/* Features Grid */}
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-12">
            <h2 className="text-3xl font-bold mb-4">Why Choose ICY?</h2>
            <p className="text-muted-foreground text-lg">
              Everything you need to run successful influencer campaigns
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {features.map((feature, index) => {
              const Icon = feature.icon;
              return (
                <Card key={index} className="bg-gradient-card shadow-soft hover:shadow-glow transition-all duration-300 group">
                  <CardHeader className="pb-4">
                    <div className="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center mb-4 group-hover:bg-primary/20 transition-colors">
                      <Icon className="h-6 w-6 text-primary" />
                    </div>
                    <CardTitle className="text-lg">{feature.title}</CardTitle>
                  </CardHeader>
                  <CardContent className="pt-0">
                    <CardDescription className="text-sm">
                      {feature.description}
                    </CardDescription>
                  </CardContent>
                </Card>
              );
            })}
          </div>
        </div>

        {/* CTA Section */}
        <div className="max-w-4xl mx-auto mt-20">
          <Card className="bg-gradient-primary text-primary-foreground shadow-glow">
            <CardContent className="p-12 text-center">
              <h2 className="text-3xl font-bold mb-4">Ready to Transform Your Influencer Marketing?</h2>
              <p className="text-xl mb-8 opacity-90">
                Join hundreds of brands using ICY to find and connect with perfect influencers
              </p>
              <Button 
                size="lg" 
                variant="secondary"
                className="bg-white text-primary hover:bg-white/90"
                onClick={() => navigate('/onboarding')}
              >
                Start Your Campaign Today
                <Sparkles className="h-5 w-5 ml-2" />
              </Button>
            </CardContent>
          </Card>
        </div>
      </div>

      {/* Footer */}
      <footer className="border-t bg-background/95 backdrop-blur">
        <div className="container mx-auto px-4 py-8">
          <div className="flex flex-col md:flex-row items-center justify-between">
            <div className="flex items-center space-x-4 mb-4 md:mb-0">
              <div className="text-xl font-bold bg-gradient-primary bg-clip-text text-transparent">
                ICY
              </div>
              <Badge variant="outline" className="text-xs">
                AI Influencer Outreach Platform
              </Badge>
            </div>
            <p className="text-sm text-muted-foreground">
              © 2024 ICY. All rights reserved.
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default Index;
