# ICY - AI Influencer Outreach Platform

<div align="center">
  <img src="https://img.shields.io/badge/React-18.3.1-61DAFB?style=for-the-badge&logo=react&logoColor=white" alt="React" />
  <img src="https://img.shields.io/badge/TypeScript-5.8.3-3178C6?style=for-the-badge&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Vite-5.4.19-646CFF?style=for-the-badge&logo=vite&logoColor=white" alt="Vite" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-3.4.17-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS" />
  <img src="https://img.shields.io/badge/Spline-3D-FF6B6B?style=for-the-badge" alt="Spline 3D" />
</div>

<br />

<div align="center">
  <h3>🚀 Clarity. Focus. Impact.</h3>
  <p>We turn complex ideas into effortless experiences</p>
</div>

## 🌟 Overview

ICY is a cutting-edge AI-powered influencer outreach platform that revolutionizes how brands discover, analyze, and connect with influencers. Built with modern web technologies and featuring an immersive 3D landing experience, ICY streamlines the entire influencer marketing workflow from discovery to campaign tracking.

## ✨ Key Features

### 🔍 Smart Influencer Discovery
- **Cross-platform search** across Instagram & YouTube simultaneously
- **Advanced filtering** by followers, engagement rate, location, and niche
- **Real-time performance metrics** and audience insights
- **AI-powered match scoring** algorithm with up to 94% accuracy

### 🧠 AI Content Analyzer
- **Automated content analysis** with brand alignment scoring
- **Authenticity detection** to identify fake followers and engagement
- **Audience demographics breakdown** with detailed insights
- **Brand safety metrics** and content quality assessment

### 💬 Personalized Message Generator
- **AI-generated outreach messages** tailored to each influencer
- **Content-aware personalization** referencing recent posts
- **Brand voice matching** (professional, casual, luxury, etc.)
- **Ready-to-send templates** with editing capabilities

### 📊 Campaign Tracking Dashboard
- **Real-time response rate monitoring** (24% average response rate)
- **Performance analytics** with reach and engagement metrics
- **ROI tracking** with detailed cost analysis (+180% average ROI)
- **Active campaign management** with status updates

## 🎨 Design Features

- **Immersive 3D Landing Page** powered by Spline
- **Modern Dark Theme** with purple/blue gradients
- **Glassmorphism UI Elements** with backdrop blur effects
- **Responsive Design** optimized for all devices
- **Smooth Animations** and micro-interactions
- **Accessibility-first** component design

## 🛠️ Tech Stack

### Frontend Framework
- **React 18.3.1** - Modern React with hooks and functional components
- **TypeScript 5.8.3** - Type-safe development experience
- **Vite 5.4.19** - Lightning-fast build tool and dev server

### Styling & UI
- **Tailwind CSS 3.4.17** - Utility-first CSS framework
- **shadcn/ui** - High-quality, accessible component library
- **Radix UI** - Unstyled, accessible UI primitives
- **Lucide React** - Beautiful, customizable icon library

### 3D & Animations
- **@splinetool/react-spline** - Interactive 3D scenes and animations
- **Tailwind Animate** - CSS animations and transitions

### Form Handling & Validation
- **React Hook Form 7.61.1** - Performant forms with easy validation
- **Zod 3.25.76** - TypeScript-first schema validation
- **@hookform/resolvers** - Validation resolvers for React Hook Form

### Routing & State Management
- **React Router DOM 6.30.1** - Client-side routing
- **TanStack Query 5.83.0** - Server state management
- **Local Storage** - Client-side data persistence

### Development Tools
- **ESLint** - Code linting and quality
- **TypeScript ESLint** - TypeScript-specific linting rules
- **Autoprefixer** - CSS vendor prefixing

## 🚀 Getting Started

### Prerequisites
- **Node.js 18+**
- **npm** or **yarn** package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/icy-influencer-pilot.git
   cd icy-influencer-pilot
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   ```

4. **Open your browser**
   Navigate to `http://localhost:8080`

### Available Scripts

```bash
npm run dev          # Start development server
npm run build        # Build for production
npm run preview      # Preview production build
npm run lint         # Run ESLint
```

## 📱 User Journey

### 1. **Immersive Landing Experience**
- Interactive 3D Spline scene with "Enter Site" button
- Smooth transition to main application
- Modern dark theme with purple/blue gradients

### 2. **Brand Onboarding (4-Step Process)**
- **Step 1**: Product information and description
- **Step 2**: Target audience definition (age, gender, interests, region)
- **Step 3**: Brand tone and campaign goal selection
- **Step 4**: Platform preferences and budget level

### 3. **AI-Powered Discovery**
- Animated loading sequence showing AI processing steps
- Real-time influencer analysis across Instagram and YouTube
- Match scoring and authenticity verification

### 4. **Comprehensive Results Dashboard**
- **Discovery Tab**: Browse and filter 247+ discovered influencers
- **Analysis Tab**: Deep-dive into content and audience insights
- **Outreach Tab**: AI-generated personalized messages
- **Tracking Tab**: Campaign performance and ROI metrics

## 🎯 Target Audience

### Primary Users
- **Marketing Teams** - Scale influencer outreach without hiring more people
- **Digital Agencies** - Manage multiple brand campaigns efficiently
- **D2C Brands** - Find cost-effective influencers that convert
- **Social Media Teams** - Build authentic influencer relationships at scale

### Use Cases
- **Brand Awareness Campaigns** - Reach new audiences effectively
- **Product Launches** - Generate buzz and authentic reviews
- **User-Generated Content** - Drive authentic brand advocacy
- **Sales Conversion** - Direct revenue through influencer partnerships

## 📊 Platform Metrics & Sample Data

The platform showcases realistic performance data:

### Discovery Metrics
- **247 total influencers** discovered across platforms
- **23 high-quality matches** (90%+ compatibility score)
- **89 medium matches** (80-89% compatibility)
- **2.4M estimated total reach** across all campaigns

### Performance Analytics
- **24% average response rate** for outreach messages
- **4.7% average engagement rate** across influencers
- **91% average authenticity score** (real followers)
- **+180% average ROI** on influencer investments

### Sample Influencer Profiles
- **Sarah Chen** (@sarahstyle) - 125K followers, 94% match, Fashion & Lifestyle
- **Alex Rodriguez** (@alexfitness) - 89K followers, 91% match, Fitness & Wellness
- **Emma Thompson** (@emmaeats) - 67K followers, 88% match, Food & Cooking

## 🏗️ Project Structure

```
src/
├── components/              # Reusable UI components
│   ├── ui/                 # shadcn/ui base components
│   ├── onboarding/         # Onboarding flow components
│   └── discovery/          # Discovery process components
├── pages/                  # Route-level page components
│   ├── Index.tsx          # 3D Spline landing page
│   ├── Home.tsx           # Main marketing page
│   ├── Onboarding.tsx     # Brand setup flow
│   ├── Dashboard.tsx      # User dashboard
│   ├── Discovery.tsx      # AI discovery process
│   └── Results.tsx        # Comprehensive results page
├── hooks/                  # Custom React hooks
├── lib/                    # Utility functions and helpers
└── styles/                 # Global styles and theme configuration
```

## 🎨 Customization

### Theme Configuration
The platform uses a custom dark theme with purple/blue gradients. Customize colors in:
- `src/index.css` - CSS custom properties and color variables
- `tailwind.config.ts` - Tailwind theme extensions and custom colors

### Key Theme Colors
```css
--primary: 260 100% 70%;           /* Purple primary */
--primary-glow: 280 100% 80%;      /* Purple glow effect */
--background: 0 0% 6%;             /* Dark background */
--foreground: 0 0% 95%;            /* Light text */
--card: 0 0% 8%;                   /* Card background */
--border: 240 10% 15%;             /* Border color */
```

### Adding New Features
1. Create components in appropriate directories
2. Add routes in `src/App.tsx`
3. Update navigation flows and user journeys
4. Maintain TypeScript types and Zod validation schemas
5. Follow existing design patterns and theme consistency

## 🚀 Deployment

### Recommended Platforms
- **Vercel** (Optimized for Vite projects)
- **Netlify** (Easy static site deployment)
- **GitHub Pages** (Free hosting for public repos)
- **AWS S3 + CloudFront** (Enterprise-grade hosting)

### Build Process
```bash
npm run build        # Creates optimized production build
npm run preview      # Test production build locally
```

### Environment Variables
No environment variables required for the demo version. For production:
- API endpoints for real influencer data
- Authentication tokens
- Analytics tracking IDs

## 🔧 Development Guidelines

### Code Style
- **TypeScript** for all new components
- **Functional components** with hooks
- **Tailwind CSS** for styling (avoid custom CSS)
- **shadcn/ui** components for consistency

### Component Structure
```tsx
// Example component structure
import React from "react";
import { Button } from "@/components/ui/button";

interface ComponentProps {
  title: string;
  onAction: () => void;
}

export function Component({ title, onAction }: ComponentProps) {
  return (
    <div className="bg-card border-border rounded-lg p-6">
      <h2 className="text-foreground font-semibold">{title}</h2>
      <Button onClick={onAction} className="bg-gradient-primary">
        Action
      </Button>
    </div>
  );
}
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Guidelines
- Follow existing code style and patterns
- Add TypeScript types for all new code
- Test components across different screen sizes
- Maintain accessibility standards
- Update documentation for new features

## 📞 Support & Contact

- **Email**: support@icy-platform.com
- **Discord**: [Join our community](https://discord.gg/icy-platform)
- **Documentation**: [docs.icy-platform.com](https://docs.icy-platform.com)
- **Issues**: [GitHub Issues](https://github.com/yourusername/icy-influencer-pilot/issues)

---

<div align="center">
  <p><strong>Built with ❤️ by the ICY Team</strong></p>
  <p><em>Transforming influencer marketing through AI innovation</em></p>

  <br />

  <p>
    <a href="https://lovable.dev/projects/f6109e51-a664-475d-952d-c751beebb33f">🚀 View on Lovable</a> •
    <a href="#getting-started">📖 Get Started</a> •
    <a href="#features">✨ Features</a> •
    <a href="#deployment">🌐 Deploy</a>
  </p>
</div>
