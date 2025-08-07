import React from "react";
import { useNavigate } from "react-router-dom";
import { BrandSetupForm } from "@/components/onboarding/BrandSetupForm";

export default function Onboarding() {
  const navigate = useNavigate();

  const handleSetupComplete = (brandData: any) => {
    console.log("Setup complete! Brand data:", brandData);
    // Store brand data (you might want to use a global state or API call here)
    localStorage.setItem('icyBrandData', JSON.stringify(brandData));

    // Navigate to dashboard
    navigate('/dashboard');
  };

  return (
    <div className="min-h-screen bg-background">
      <div className="container mx-auto py-8">
        <BrandSetupForm onComplete={handleSetupComplete} />
      </div>
    </div>
  );
}