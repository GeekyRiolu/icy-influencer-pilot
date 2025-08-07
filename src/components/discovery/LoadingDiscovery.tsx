import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { Card, CardContent } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { Search, Users, Target, Sparkles, CheckCircle } from "lucide-react";

const discoverySteps = [
  {
    id: 1,
    icon: Search,
    title: "Scanning Social Platforms",
    description: "Searching Instagram and YouTube for relevant influencers...",
    duration: 2000,
  },
  {
    id: 2,
    icon: Target,
    title: "Analyzing Brand Fit",
    description: "Evaluating content alignment with your brand values...",
    duration: 3000,
  },
  {
    id: 3,
    icon: Users,
    title: "Checking Audience Match",
    description: "Analyzing follower demographics and engagement patterns...",
    duration: 2500,
  },
  {
    id: 4,
    icon: Sparkles,
    title: "Calculating Match Scores",
    description: "Using AI to rank influencers by compatibility...",
    duration: 2000,
  },
];

export function LoadingDiscovery() {
  const [currentStep, setCurrentStep] = useState(0);
  const [progress, setProgress] = useState(0);
  const [completedSteps, setCompletedSteps] = useState<number[]>([]);
  const navigate = useNavigate();

  useEffect(() => {
    let totalDuration = 0;
    let currentProgress = 0;

    const runSteps = async () => {
      for (let i = 0; i < discoverySteps.length; i++) {
        const step = discoverySteps[i];
        setCurrentStep(i);
        
        // Animate progress for this step
        const stepProgressIncrement = 100 / discoverySteps.length;
        const stepDuration = step.duration;
        const intervalTime = 50; // Update every 50ms
        const progressPerInterval = stepProgressIncrement / (stepDuration / intervalTime);
        
        await new Promise((resolve) => {
          const interval = setInterval(() => {
            currentProgress += progressPerInterval;
            setProgress(Math.min(currentProgress, (i + 1) * stepProgressIncrement));
            
            if (currentProgress >= (i + 1) * stepProgressIncrement) {
              clearInterval(interval);
              setCompletedSteps(prev => [...prev, i]);
              resolve(void 0);
            }
          }, intervalTime);
        });
      }

      // Wait a moment to show completion
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      // Navigate to results
      navigate('/results');
    };

    runSteps();
  }, [navigate]);

  return (
    <div className="min-h-screen bg-gradient-ice flex items-center justify-center p-4">
      <div className="max-w-2xl w-full">
        {/* Header */}
        <div className="text-center mb-12">
          <div className="inline-flex items-center justify-center w-20 h-20 bg-gradient-primary rounded-full mb-6 animate-pulse-glow">
            <Sparkles className="h-10 w-10 text-white" />
          </div>
          <h1 className="text-4xl font-bold bg-gradient-primary bg-clip-text text-transparent mb-4">
            ICY is Working Its Magic
          </h1>
          <p className="text-xl text-muted-foreground">
            Discovering the perfect influencers for your campaign...
          </p>
        </div>

        {/* Progress */}
        <Card className="bg-gradient-card shadow-soft mb-8">
          <CardContent className="p-8">
            <div className="mb-6">
              <div className="flex justify-between items-center mb-2">
                <span className="text-sm font-medium">Discovery Progress</span>
                <span className="text-sm text-muted-foreground">{Math.round(progress)}%</span>
              </div>
              <Progress value={progress} className="h-3" />
            </div>

            {/* Current Step */}
            {currentStep < discoverySteps.length && (
              <div className="text-center">
                <div className="inline-flex items-center justify-center w-16 h-16 bg-primary/10 rounded-full mb-4">
                  {React.createElement(discoverySteps[currentStep].icon, {
                    className: "h-8 w-8 text-primary animate-pulse"
                  })}
                </div>
                <h3 className="text-xl font-semibold mb-2">
                  {discoverySteps[currentStep].title}
                </h3>
                <p className="text-muted-foreground">
                  {discoverySteps[currentStep].description}
                </p>
              </div>
            )}
          </CardContent>
        </Card>

        {/* Steps List */}
        <div className="space-y-4">
          {discoverySteps.map((step, index) => {
            const StepIcon = step.icon;
            const isCompleted = completedSteps.includes(index);
            const isCurrent = currentStep === index;
            const isPending = currentStep < index;

            return (
              <Card 
                key={step.id}
                className={`transition-all duration-500 ${
                  isCompleted 
                    ? 'bg-success/10 border-success/20' 
                    : isCurrent 
                    ? 'bg-primary/10 border-primary/20 shadow-glow' 
                    : 'bg-gradient-card'
                }`}
              >
                <CardContent className="p-4">
                  <div className="flex items-center space-x-4">
                    <div className={`w-12 h-12 rounded-full flex items-center justify-center ${
                      isCompleted 
                        ? 'bg-success text-success-foreground' 
                        : isCurrent 
                        ? 'bg-primary text-primary-foreground animate-pulse-glow' 
                        : 'bg-muted text-muted-foreground'
                    }`}>
                      {isCompleted ? (
                        <CheckCircle className="h-6 w-6" />
                      ) : (
                        <StepIcon className={`h-6 w-6 ${isCurrent ? 'animate-pulse' : ''}`} />
                      )}
                    </div>
                    <div className="flex-1">
                      <h4 className={`font-medium ${
                        isCompleted ? 'text-success' : isCurrent ? 'text-primary' : 'text-foreground'
                      }`}>
                        {step.title}
                      </h4>
                      <p className="text-sm text-muted-foreground">
                        {step.description}
                      </p>
                    </div>
                    {isCompleted && (
                      <div className="text-success">
                        <CheckCircle className="h-5 w-5" />
                      </div>
                    )}
                  </div>
                </CardContent>
              </Card>
            );
          })}
        </div>

        {/* Fun Facts */}
        <Card className="bg-gradient-card shadow-soft mt-8">
          <CardContent className="p-6 text-center">
            <h3 className="font-semibold mb-2">💡 Did you know?</h3>
            <p className="text-sm text-muted-foreground">
              ICY analyzes over 50+ data points per influencer including engagement rates, 
              audience demographics, content authenticity, and brand safety metrics to ensure 
              the perfect match for your campaign.
            </p>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}