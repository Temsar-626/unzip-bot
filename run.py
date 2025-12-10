#!/usr/bin/env python
"""
Simple runner script for unzip-bot
This script loads environment variables from .env and starts the bot
"""

import os
import sys
from pathlib import Path


def load_env():
    """Load environment variables from .env file"""
    env_file = Path(__file__).parent / ".env"
    
    if not env_file.exists():
        print("❌ Error: .env file not found!")
        print("Please copy .env.example to .env and fill in your configuration")
        sys.exit(1)
    
    print("📋 Loading environment variables from .env...")
    
    with open(env_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # Skip comments and empty lines
            if not line or line.startswith("#"):
                continue
            
            # Parse key=value pairs
            if "=" in line:
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip()
                
                # Don't set empty values
                if value:
                    os.environ[key] = value
    
    # Check required variables
    required_vars = ["APP_ID", "API_HASH", "BOT_TOKEN", "BOT_OWNER", "LOGS_CHANNEL", "MONGODB_URL"]
    missing_vars = [var for var in required_vars if not os.environ.get(var)]
    
    if missing_vars:
        print(f"❌ Error: Missing required environment variables: {', '.join(missing_vars)}")
        print("Please fill in all required variables in your .env file")
        sys.exit(1)
    
    print("✅ Environment variables loaded successfully")


def main():
    """Main entry point"""
    print("""
🔥 unzip-bot 🔥

Copyright (c) 2022 - 2025 EDM115
MIT License

--> Join @EDM115bots on Telegram
--> Follow EDM115 on Github
    """)
    
    # Load environment variables
    load_env()
    
    # Run the bot using the -m flag (same as python -m unzipbot)
    print("🚀 Starting the bot...")
    try:
        import subprocess
        # Run the module using subprocess
        result = subprocess.run([sys.executable, "-m", "unzipbot"], check=True)
        sys.exit(result.returncode)
    except subprocess.CalledProcessError as e:
        print(f"❌ Bot stopped with error code: {e.returncode}")
        sys.exit(e.returncode)
    except Exception as e:
        print(f"❌ Error starting bot: {e}")
        print("Make sure you have installed all dependencies with: pip install -r requirements.txt")
        sys.exit(1)


if __name__ == "__main__":
    main()
