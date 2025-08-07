#!/usr/bin/env python3
"""
ICY AI Influencer Platform Backend Startup Script
Handles environment setup, dependency checks, and server startup
"""

import sys
import os
import subprocess
import platform
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 9):
        print("❌ Python 3.9 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    else:
        print(f"✅ Python {sys.version.split()[0]} detected")

def check_virtual_environment():
    """Check if running in virtual environment"""
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Virtual environment detected")
        return True
    else:
        print("⚠️  Not running in virtual environment")
        print("Recommendation: Create and activate a virtual environment")
        return False

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def check_dependencies():
    """Check if required dependencies are installed"""
    required_packages = [
        "fastapi",
        "uvicorn",
        "pydantic",
        "httpx",
        "python-multipart"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing packages: {', '.join(missing_packages)}")
        return False
    else:
        print("✅ All required dependencies are installed")
        return True

def create_directories():
    """Create necessary directories"""
    directories = [
        "logs",
        "data",
        "uploads",
        "cache"
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
    
    print("✅ Directories created")

def setup_environment():
    """Setup environment variables"""
    env_file = Path(".env")
    
    if not env_file.exists():
        print("⚠️  .env file not found, creating default...")
        
        default_env = """# ICY AI Influencer Platform Backend Configuration

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True
ENVIRONMENT=development

# CORS Origins (comma-separated)
CORS_ORIGINS=http://localhost:8080,http://localhost:3000

# Database Configuration (for production)
# DATABASE_URL=postgresql://user:password@localhost/icy_db

# External API Keys (for real integration)
# INSTAGRAM_ACCESS_TOKEN=your_instagram_token
# YOUTUBE_API_KEY=your_youtube_api_key
# OPENAI_API_KEY=your_openai_key

# Redis Configuration (for caching)
# REDIS_URL=redis://localhost:6379

# Email Service Configuration
# SENDGRID_API_KEY=your_sendgrid_key

# Logging Configuration
LOG_LEVEL=INFO
LOG_FORMAT=json

# Security
SECRET_KEY=your-secret-key-change-in-production
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Rate Limiting
RATE_LIMIT_REQUESTS=100
RATE_LIMIT_WINDOW=60

# File Upload
MAX_FILE_SIZE=10485760  # 10MB
ALLOWED_FILE_TYPES=jpg,jpeg,png,gif,mp4,mov

# AI Configuration
AI_MODEL_VERSION=v2.1
CONFIDENCE_THRESHOLD=0.75
"""
        
        with open(env_file, "w") as f:
            f.write(default_env)
        
        print("✅ Default .env file created")
    else:
        print("✅ .env file found")

def check_port_availability(port=8000):
    """Check if port is available"""
    import socket
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(('localhost', port))
            print(f"✅ Port {port} is available")
            return True
        except OSError:
            print(f"❌ Port {port} is already in use")
            return False

def start_server(host="0.0.0.0", port=8000, reload=True):
    """Start the FastAPI server"""
    print(f"🚀 Starting ICY AI Influencer Platform Backend...")
    print(f"   Host: {host}")
    print(f"   Port: {port}")
    print(f"   Reload: {reload}")
    print(f"   API Docs: http://localhost:{port}/docs")
    print(f"   ReDoc: http://localhost:{port}/redoc")
    print()
    
    try:
        import uvicorn
        uvicorn.run(
            "main:app",
            host=host,
            port=port,
            reload=reload,
            log_level="info",
            access_log=True
        )
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Server error: {e}")
        sys.exit(1)

def print_banner():
    """Print startup banner"""
    banner = """
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║    ██╗ ██████╗██╗   ██╗    ██████╗  █████╗  ██████╗██╗  ██╗ ║
║    ██║██╔════╝╚██╗ ██╔╝    ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝ ║
║    ██║██║      ╚████╔╝     ██████╔╝███████║██║     █████╔╝  ║
║    ██║██║       ╚██╔╝      ██╔══██╗██╔══██║██║     ██╔═██╗  ║
║    ██║╚██████╗   ██║       ██████╔╝██║  ██║╚██████╗██║  ██╗ ║
║    ╚═╝ ╚═════╝   ╚═╝       ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ║
║                                                              ║
║              AI Influencer Outreach Platform                 ║
║                        Backend API                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
    print(banner)

def main():
    """Main startup function"""
    print_banner()
    
    print("🔍 Running startup checks...")
    print()
    
    # System checks
    check_python_version()
    check_virtual_environment()
    
    # Environment setup
    setup_environment()
    create_directories()
    
    # Dependency checks
    if not check_dependencies():
        print("📦 Installing missing dependencies...")
        if not install_dependencies():
            print("❌ Failed to install dependencies. Please install manually:")
            print("   pip install -r requirements.txt")
            sys.exit(1)
    
    # Port availability
    if not check_port_availability():
        print("⚠️  Port 8000 is in use. Trying port 8001...")
        if check_port_availability(8001):
            port = 8001
        else:
            print("❌ No available ports found. Please stop other services.")
            sys.exit(1)
    else:
        port = 8000
    
    print()
    print("✅ All checks passed!")
    print()
    
    # Start server
    start_server(port=port)

if __name__ == "__main__":
    main()
