# 🚀 Navadaya Girls Hostal - Vercel Deployment Guide

## 📋 Pre-Deployment Checklist

### 1. **GitHub Repository Setup**
```bash
# अपने प्रोजेक्ट को GitHub पर push करें
git init
git add .
git commit -m "Initial commit - Navadaya Girls Hostal"
git branch -M main
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

### 2. **Environment Variables (जरूरी!)**
Vercel dashboard में ये environment variables add करें:

- `TELEGRAM_BOT_TOKEN` = `7693479991:AAF00-TVlY6tGmPbCcc9kvGNlNwm1yvQXZI`
- `TELEGRAM_CHAT_ID` = `1691680798`

## 🌐 Vercel Deployment Steps

### **Step 1: Vercel Account Setup**
1. [Vercel.com](https://vercel.com) पर जाकर GitHub से login करें
2. "New Project" button पर click करें
3. अपनी GitHub repository select करें

### **Step 2: Project Configuration**
```json
Framework Preset: Other
Build Command: (Leave empty)
Output Directory: (Leave empty)
Install Command: pip install -r requirements.txt
```

### **Step 3: Environment Variables Setup**
1. Project Settings → Environment Variables में जाएं
2. Add करें:
   - `TELEGRAM_BOT_TOKEN` = `7693479991:AAF00-TVlY6tGmPbCcc9kvGNlNwm1yvQXZI`
   - `TELEGRAM_CHAT_ID` = `1691680798`

### **Step 4: Deploy**
1. "Deploy" button पर click करें
2. Deployment process complete होने का wait करें
3. आपको live URL मिलेगा

## 📁 Required Files Structure
```
project/
├── app.py              # Main Flask application
├── vercel.json         # Vercel configuration
├── index.html          # Frontend
├── css/                # Stylesheets
├── js/                 # JavaScript files
├── assets/             # Images and assets
└── DEPLOYMENT_GUIDE.md # This file
```

## 🔧 Important Notes

### **Static Files Serving**
- सभी CSS, JS, images automatically serve होंगे
- URL structure same रहेगा

### **File Upload Limits**
- Maximum file size: 16MB
- Vercel का 30-second function timeout है

### **Database Note**
- Currently local storage use हो रहा है
- Production के लिए database की जरूरत हो सकती है

## 🚀 Quick Deploy Commands
```bash
# Install Vercel CLI (optional)
npm i -g vercel

# Deploy from command line
vercel

# Follow the prompts
```

## 📱 Testing Your Deployment
1. Live URL पर जाएं
2. Form भरकर test करें
3. Telegram पर message check करें
4. PDF generation test करें

## 🔗 Useful Links
- [Vercel Documentation](https://vercel.com/docs)
- [Python on Vercel](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
- [Environment Variables](https://vercel.com/docs/concepts/projects/environment-variables)

## 🆘 Troubleshooting
- **Function timeout**: File size कम करें या processing optimize करें
- **Static files not loading**: vercel.json routes check करें
- **Environment variables**: Vercel dashboard में properly set करें

---
✅ **Ready to Deploy!** 🎉