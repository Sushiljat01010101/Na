#!/bin/bash

# 🚀 Navadaya Girls Hostal - Vercel Deployment Script

echo "🏠 Starting Navadaya Girls Hostal deployment process..."

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing Git repository..."
    git init
    git branch -M main
fi

# Add all files
echo "📤 Adding files to Git..."
git add .

# Commit changes
echo "💾 Committing changes..."
git commit -m "Deploy: Navadaya Girls Hostal - $(date)"

# Check if origin exists
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "⚠️  Please add your GitHub repository URL:"
    echo "   git remote add origin YOUR_GITHUB_REPO_URL"
    echo "   Then run this script again."
    exit 1
fi

# Push to GitHub
echo "🚀 Pushing to GitHub..."
git push -u origin main

echo "✅ Files pushed to GitHub successfully!"
echo ""
echo "🌐 Next Steps:"
echo "1. Go to https://vercel.com"
echo "2. Login with GitHub"
echo "3. Import your repository"
echo "4. Add Environment Variables:"
echo "   - TELEGRAM_BOT_TOKEN = 7693479991:AAF00-TVlY6tGmPbCcc9kvGNlNwm1yvQXZI"
echo "   - TELEGRAM_CHAT_ID = 1691680798"
echo "5. Deploy!"
echo ""
echo "🎉 Your app will be live in minutes!"