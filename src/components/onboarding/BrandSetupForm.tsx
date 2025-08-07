import React, { useState } from "react";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";
import { ChevronLeft, ChevronRight, Sparkles, Target, Megaphone, DollarSign, Instagram, Youtube } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Form, FormControl, FormDescription, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Checkbox } from "@/components/ui/checkbox";
import { Badge } from "@/components/ui/badge";
import { Progress } from "@/components/ui/progress";
import { useToast } from "@/hooks/use-toast";

const brandSetupSchema = z.object({
  productName: z.string().min(2, "Product name must be at least 2 characters"),
  productDescription: z.string().min(10, "Please provide a detailed description"),
  targetAge: z.array(z.string()).min(1, "Select at least one age group"),
  targetGender: z.array(z.string()).min(1, "Select at least one gender"),
  targetInterests: z.string().min(5, "Please describe target interests"),
  targetRegion: z.string().min(2, "Region is required"),
  brandTone: z.string().min(1, "Please select a brand tone"),
  campaignGoal: z.string().min(1, "Please select a campaign goal"),
  platforms: z.array(z.string()).min(1, "Select at least one platform"),
  budgetLevel: z.string().min(1, "Please select a budget level"),
});

type BrandSetupData = z.infer<typeof brandSetupSchema>;

interface BrandSetupFormProps {
  onComplete: (data: BrandSetupData) => void;
}

const steps = [
  { id: 1, title: "Product Info", description: "Tell us about your product" },
  { id: 2, title: "Target Audience", description: "Who are you trying to reach?" },
  { id: 3, title: "Brand & Campaign", description: "Define your brand voice and goals" },
  { id: 4, title: "Platform & Budget", description: "Choose platforms and budget level" },
];

const brandTones = [
  { value: "friendly", label: "Friendly", description: "Warm and approachable" },
  { value: "playful", label: "Playful", description: "Fun and energetic" },
  { value: "luxury", label: "Luxury", description: "Premium and sophisticated" },
  { value: "professional", label: "Professional", description: "Corporate and trustworthy" },
  { value: "edgy", label: "Edgy", description: "Bold and provocative" },
];

const campaignGoals = [
  { value: "awareness", label: "Brand Awareness", icon: Megaphone },
  { value: "sales", label: "Drive Sales", icon: DollarSign },
  { value: "ugc", label: "User Generated Content", icon: Sparkles },
  { value: "engagement", label: "Engagement", icon: Target },
];

const budgetLevels = [
  { value: "micro", label: "Micro Influencers", description: "1K-100K followers" },
  { value: "mid", label: "Mid-tier Influencers", description: "100K-1M followers" },
  { value: "macro", label: "Macro Influencers", description: "1M+ followers" },
];

export function BrandSetupForm({ onComplete }: BrandSetupFormProps) {
  const [currentStep, setCurrentStep] = useState(1);
  const { toast } = useToast();

  const form = useForm<BrandSetupData>({
    resolver: zodResolver(brandSetupSchema),
    defaultValues: {
      productName: "",
      productDescription: "",
      targetAge: [],
      targetGender: [],
      targetInterests: "",
      targetRegion: "",
      brandTone: "",
      campaignGoal: "",
      platforms: [],
      budgetLevel: "",
    },
  });

  const nextStep = () => {
    if (currentStep < steps.length) {
      setCurrentStep(currentStep + 1);
    }
  };

  const prevStep = () => {
    if (currentStep > 1) {
      setCurrentStep(currentStep - 1);
    }
  };

  const onSubmit = (data: BrandSetupData) => {
    console.log("Brand setup data:", data);
    toast({
      title: "Brand setup complete!",
      description: "Starting influencer discovery...",
    });
    onComplete(data);
  };

  const progress = (currentStep / steps.length) * 100;

  const renderStep = () => {
    switch (currentStep) {
      case 1:
        return (
          <div className="space-y-6">
            <FormField
              control={form.control}
              name="productName"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Product Name *</FormLabel>
                  <FormControl>
                    <Input placeholder="e.g., EcoClean Skincare" {...field} />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />
            
            <FormField
              control={form.control}
              name="productDescription"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Product Description *</FormLabel>
                  <FormControl>
                    <Textarea 
                      placeholder="Describe your product, its benefits, and what makes it unique..."
                      className="min-h-[100px]"
                      {...field} 
                    />
                  </FormControl>
                  <FormDescription>
                    Provide details about your product to help us find the perfect influencers
                  </FormDescription>
                  <FormMessage />
                </FormItem>
              )}
            />
          </div>
        );

      case 2:
        return (
          <div className="space-y-6">
            <FormField
              control={form.control}
              name="targetAge"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Target Age Groups *</FormLabel>
                  <div className="flex flex-wrap gap-2">
                    {["13-17", "18-24", "25-34", "35-44", "45-54", "55+"].map((age) => (
                      <label key={age} className="flex items-center space-x-2 cursor-pointer">
                        <Checkbox
                          checked={field.value?.includes(age)}
                          onCheckedChange={(checked) => {
                            const newValue = checked 
                              ? [...(field.value || []), age]
                              : field.value?.filter(v => v !== age) || [];
                            field.onChange(newValue);
                          }}
                        />
                        <Badge variant="outline">{age}</Badge>
                      </label>
                    ))}
                  </div>
                  <FormMessage />
                </FormItem>
              )}
            />

            <FormField
              control={form.control}
              name="targetGender"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Target Gender *</FormLabel>
                  <div className="flex flex-wrap gap-2">
                    {["Female", "Male", "Non-binary", "All"].map((gender) => (
                      <label key={gender} className="flex items-center space-x-2 cursor-pointer">
                        <Checkbox
                          checked={field.value?.includes(gender)}
                          onCheckedChange={(checked) => {
                            const newValue = checked 
                              ? [...(field.value || []), gender]
                              : field.value?.filter(v => v !== gender) || [];
                            field.onChange(newValue);
                          }}
                        />
                        <Badge variant="outline">{gender}</Badge>
                      </label>
                    ))}
                  </div>
                  <FormMessage />
                </FormItem>
              )}
            />

            <FormField
              control={form.control}
              name="targetInterests"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Target Interests *</FormLabel>
                  <FormControl>
                    <Textarea 
                      placeholder="e.g., skincare, sustainability, wellness, beauty, lifestyle..."
                      {...field} 
                    />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />

            <FormField
              control={form.control}
              name="targetRegion"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Target Region *</FormLabel>
                  <Select onValueChange={field.onChange} defaultValue={field.value}>
                    <FormControl>
                      <SelectTrigger>
                        <SelectValue placeholder="Select region" />
                      </SelectTrigger>
                    </FormControl>
                    <SelectContent>
                      <SelectItem value="north-america">North America</SelectItem>
                      <SelectItem value="europe">Europe</SelectItem>
                      <SelectItem value="asia-pacific">Asia Pacific</SelectItem>
                      <SelectItem value="latin-america">Latin America</SelectItem>
                      <SelectItem value="middle-east-africa">Middle East & Africa</SelectItem>
                      <SelectItem value="global">Global</SelectItem>
                    </SelectContent>
                  </Select>
                  <FormMessage />
                </FormItem>
              )}
            />
          </div>
        );

      case 3:
        return (
          <div className="space-y-6">
            <FormField
              control={form.control}
              name="brandTone"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Brand Tone *</FormLabel>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                    {brandTones.map((tone) => (
                      <Card
                        key={tone.value}
                        className={`cursor-pointer transition-all hover:shadow-soft bg-card border-border ${
                          field.value === tone.value ? 'ring-2 ring-primary bg-primary/10' : ''
                        }`}
                        onClick={() => field.onChange(tone.value)}
                      >
                        <CardContent className="p-4">
                          <h4 className="font-medium text-foreground">{tone.label}</h4>
                          <p className="text-sm text-muted-foreground">{tone.description}</p>
                        </CardContent>
                      </Card>
                    ))}
                  </div>
                  <FormMessage />
                </FormItem>
              )}
            />

            <FormField
              control={form.control}
              name="campaignGoal"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Campaign Goal *</FormLabel>
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                    {campaignGoals.map((goal) => {
                      const Icon = goal.icon;
                      return (
                        <Card
                          key={goal.value}
                          className={`cursor-pointer transition-all hover:shadow-soft bg-card border-border ${
                            field.value === goal.value ? 'ring-2 ring-primary bg-primary/10' : ''
                          }`}
                          onClick={() => field.onChange(goal.value)}
                        >
                          <CardContent className="p-4 flex items-center space-x-3">
                            <Icon className="h-5 w-5 text-primary" />
                            <span className="font-medium text-foreground">{goal.label}</span>
                          </CardContent>
                        </Card>
                      );
                    })}
                  </div>
                  <FormMessage />
                </FormItem>
              )}
            />
          </div>
        );

      case 4:
        return (
          <div className="space-y-6">
            <FormField
              control={form.control}
              name="platforms"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Platform Focus *</FormLabel>
                  <div className="flex gap-4">
                    {[
                      { value: "instagram", label: "Instagram", icon: Instagram },
                      { value: "youtube", label: "YouTube", icon: Youtube }
                    ].map((platform) => {
                      const Icon = platform.icon;
                      return (
                        <label key={platform.value} className="flex items-center space-x-2 cursor-pointer">
                          <Checkbox
                            checked={field.value?.includes(platform.value)}
                            onCheckedChange={(checked) => {
                              const newValue = checked 
                                ? [...(field.value || []), platform.value]
                                : field.value?.filter(v => v !== platform.value) || [];
                              field.onChange(newValue);
                            }}
                          />
                          <div className="flex items-center space-x-2">
                            <Icon className="h-5 w-5" />
                            <span>{platform.label}</span>
                          </div>
                        </label>
                      );
                    })}
                  </div>
                  <FormMessage />
                </FormItem>
              )}
            />

            <FormField
              control={form.control}
              name="budgetLevel"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Influencer Tier *</FormLabel>
                  <div className="space-y-3">
                    {budgetLevels.map((level) => (
                      <Card
                        key={level.value}
                        className={`cursor-pointer transition-all hover:shadow-soft bg-card border-border ${
                          field.value === level.value ? 'ring-2 ring-primary bg-primary/10' : ''
                        }`}
                        onClick={() => field.onChange(level.value)}
                      >
                        <CardContent className="p-4">
                          <h4 className="font-medium text-foreground">{level.label}</h4>
                          <p className="text-sm text-muted-foreground">{level.description}</p>
                        </CardContent>
                      </Card>
                    ))}
                  </div>
                  <FormMessage />
                </FormItem>
              )}
            />
          </div>
        );

      default:
        return null;
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-6">
      <div className="mb-8">
        <h1 className="text-3xl font-bold bg-gradient-primary bg-clip-text text-transparent mb-2">
          Set Up Your Brand
        </h1>
        <p className="text-muted-foreground">
          Let's get to know your brand so we can find the perfect influencers
        </p>
      </div>

      {/* Progress */}
      <div className="mb-8">
        <div className="flex justify-between items-center mb-2">
          <span className="text-sm font-medium">Step {currentStep} of {steps.length}</span>
          <span className="text-sm text-muted-foreground">{Math.round(progress)}% complete</span>
        </div>
        <Progress value={progress} className="h-2" />
      </div>

      {/* Steps */}
      <div className="flex justify-between mb-8">
        {steps.map((step) => (
          <div key={step.id} className={`flex-1 ${step.id !== steps.length ? 'mr-4' : ''}`}>
            <div className={`flex items-center ${step.id <= currentStep ? 'text-primary' : 'text-muted-foreground'}`}>
              <div 
                className={`w-8 h-8 rounded-full flex items-center justify-center text-sm font-medium ${
                  step.id < currentStep 
                    ? 'bg-primary text-primary-foreground' 
                    : step.id === currentStep
                    ? 'bg-primary text-primary-foreground animate-pulse-glow'
                    : 'bg-muted text-muted-foreground'
                }`}
              >
                {step.id}
              </div>
              <div className="ml-2">
                <p className="font-medium text-sm">{step.title}</p>
                <p className="text-xs text-muted-foreground">{step.description}</p>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Form */}
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)}>
          <Card className="bg-card border-border shadow-soft">
            <CardHeader>
              <CardTitle className="text-foreground">{steps[currentStep - 1].title}</CardTitle>
              <CardDescription className="text-muted-foreground">{steps[currentStep - 1].description}</CardDescription>
            </CardHeader>
            <CardContent>
              {renderStep()}
            </CardContent>
          </Card>

          {/* Navigation */}
          <div className="flex justify-between mt-8">
            <Button
              type="button"
              variant="outline"
              onClick={prevStep}
              disabled={currentStep === 1}
              className="border-border hover:bg-muted/50"
            >
              <ChevronLeft className="h-4 w-4 mr-2" />
              Previous
            </Button>

            {currentStep === steps.length ? (
              <Button type="submit" className="bg-gradient-primary hover:shadow-purple border-0">
                Complete Setup
                <Sparkles className="h-4 w-4 ml-2" />
              </Button>
            ) : (
              <Button type="button" onClick={nextStep} className="bg-gradient-primary border-0">
                Next
                <ChevronRight className="h-4 w-4 ml-2" />
              </Button>
            )}
          </div>
        </form>
      </Form>
    </div>
  );
}