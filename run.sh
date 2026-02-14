#!/bin/bash
# Quick run script for Avengers AI Operating System

set -e

echo "🛡⚡ Avengers AI Operating System"
echo "=================================="
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  No .env file found!"
    echo "Creating from .env.example..."
    cp .env.example .env
    echo ""
    echo "📝 Please edit .env and add your ANTHROPIC_API_KEY"
    echo "   Then run this script again."
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install/upgrade dependencies
echo "📚 Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "Available commands:"
echo "  Daily cycle:      python main.py --mode daily"
echo "  Research only:    python main.py --mode research"
echo "  Build prototype:  python main.py --mode prototype --concept 'Your Concept'"
echo "  24/7 scheduler:   python scheduler.py"
echo ""

# Ask user what to run
echo "What would you like to do?"
echo "1) Run daily cycle"
echo "2) Run research sweep"
echo "3) Build a prototype"
echo "4) Start 24/7 scheduler"
echo "5) Exit"
echo ""
read -p "Choice (1-5): " choice

case $choice in
    1)
        echo ""
        echo "🚀 Running daily cycle..."
        python main.py --mode daily
        ;;
    2)
        echo ""
        echo "🔍 Running research sweep..."
        python main.py --mode research
        ;;
    3)
        echo ""
        read -p "Enter prototype concept: " concept
        python main.py --mode prototype --concept "$concept"
        ;;
    4)
        echo ""
        echo "⏰ Starting 24/7 scheduler..."
        echo "   Press Ctrl+C to stop"
        python scheduler.py
        ;;
    5)
        echo "👋 Goodbye!"
        exit 0
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac
