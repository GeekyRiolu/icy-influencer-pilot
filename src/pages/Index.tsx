import React, { Suspense } from "react";
import { useNavigate } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { ArrowRight } from "lucide-react";
import Spline from '@splinetool/react-spline';

const Index = () => {
  const navigate = useNavigate();

  return (
    <div className="relative h-screen w-full overflow-hidden bg-background">
      {/* Spline 3D Scene - Full Screen */}
      <div className="absolute inset-0 z-0">
        <Suspense fallback={
          <div className="flex items-center justify-center h-full bg-background">
            <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-primary"></div>
          </div>
        }>
          <Spline
            scene="https://prod.spline.design/g8GVu0bOgBxDT2Xr/scene.splinecode"
            style={{ width: '100%', height: '100%' }}
          />
        </Suspense>
      </div>

      {/* Overlay Content - Matching the design */}
      <div className="absolute inset-0 z-10 flex flex-col items-center justify-center text-center px-4">
        {/* Main Headline */}
        

        {/* Subtitle */}
        

        {/* Enter Site Button */}
        <Button
          size="lg"
          className="bg-muted/40 backdrop-blur-md border border-border/50 text-foreground hover:bg-muted/60 transition-all duration-300 shadow-glow px-8 py-4 text-lg font-medium rounded-lg"
          onClick={() => navigate('/home')}
        >
          Enter Site
          <ArrowRight className="h-5 w-5 ml-2" />
        </Button>
      </div>
    </div>
  );
};

export default Index;
