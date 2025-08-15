# 🏠 Navadaya Girls Hostel - Admission Form System

![Navadaya Girls Hostel Logo](attached_assets/generated_images/Navadaya_Girls_Hostel_Logo_29e6110e.png)

A comprehensive web-based admission form application for Navadaya Girls Hostel that allows students to submit their admission applications with photo capture, digital signatures, and PDF generation capabilities.

## ✨ Features

### 📋 Multi-Step Form Interface
- **7-Step Progressive Form** with real-time validation
- **Draft Auto-Save** functionality
- **Progress Tracking** with visual indicators
- **Cross-field Validation** for complex business rules

### 📸 Media & Document Handling
- **Camera Integration** for photo capture (Environment/User camera switching)
- **Digital Signatures** using HTML5 Canvas
- **Multiple ID Proof Upload** (up to 5 documents)
- **High-Quality Image Processing** with no compression loss

### 📄 PDF Generation & Submission
- **Client-side PDF Generation** using jsPDF
- **Professional PDF Layout** with hostel branding
- **Automatic Telegram Integration** for form submissions
- **QR Code Generation** for form identification

### 🎨 User Interface
- **Responsive Design** (Mobile-first approach)
- **Dual Theme Support** (Light/Dark modes)
- **Smooth Animations** and transitions
- **Section-based Color Coding**

### 💾 Data Management
- **Local Storage** for draft management
- **Form History** maintenance
- **Data Sanitization** and validation
- **Settings Persistence**

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Flask and dependencies

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd navadaya-girls-hostel
   ```

2. **Install dependencies**
   ```bash
   pip install flask flask-cors requests reportlab pillow
   ```

3. **Set up environment variables**
   ```bash
   export TELEGRAM_BOT_TOKEN=your_bot_token
   export TELEGRAM_CHAT_ID=your_chat_id
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://localhost:5000
   ```

## 🔧 Technology Stack

### Frontend
- **HTML5/CSS3/JavaScript** (Vanilla ES6)
- **Progressive Web App** architecture
- **CSS Grid/Flexbox** for responsive layouts
- **WebRTC API** for camera access

### Backend
- **Flask** (Python web framework)
- **Flask-CORS** for cross-origin requests
- **ReportLab** for PDF generation
- **Pillow (PIL)** for image processing

### External Libraries
- **jsPDF** - PDF document generation
- **HTML2Canvas** - DOM to canvas conversion
- **SignaturePad** - Digital signature capture
- **QRCode.js** - QR code generation
- **Font Awesome** - Icon library

### APIs & Services
- **Telegram Bot API** - Form submission notifications
- **MediaDevices API** - Camera access
- **LocalStorage API** - Client-side data persistence

## 📁 Project Structure

```
navadaya-girls-hostel/
├── app.py                 # Main Flask application
├── index.html             # Frontend interface
├── css/
│   ├── styles.css         # Main stylesheet
│   └── animations.css     # Animation definitions
├── js/
│   ├── app.js            # Main application logic
│   ├── camera.js         # Camera functionality
│   ├── signature.js      # Digital signature handling
│   ├── pdf-generator.js  # PDF generation
│   ├── telegram.js       # Telegram integration
│   ├── validation.js     # Form validation
│   └── storage.js        # Local storage management
├── assets/
│   └── logo.svg          # Hostel logo
└── attached_assets/
    └── generated_images/  # Generated logo and assets
```

## 🌐 Deployment

### Render Deployment

1. **Build Command:**
   ```bash
   pip install flask flask-cors requests reportlab pillow
   ```

2. **Start Command:**
   ```bash
   python app.py
   ```

3. **Environment Variables:**
   - `TELEGRAM_BOT_TOKEN` = Your Telegram Bot Token
   - `TELEGRAM_CHAT_ID` = Your Telegram Chat ID

## 📋 Form Sections

1. **Student Information**
   - Basic details (Name, DOB, Contact)
   - Academic information
   - Photo capture

2. **Guardian Information**
   - Parent/Guardian details
   - Contact information
   - Emergency contacts

3. **Hostel Preferences**
   - Room preferences
   - Accommodation details
   - Special requirements

4. **Documents**
   - Multiple ID proof upload
   - Academic certificates
   - Medical certificates

5. **Declaration**
   - Digital signature
   - Terms acceptance
   - Final submission

## 🔧 Configuration

### Telegram Bot Setup
1. Create a bot using [@BotFather](https://t.me/BotFather)
2. Get your bot token
3. Add bot to your channel/group
4. Get chat ID
5. Update environment variables

### Camera Permissions
- Ensure HTTPS for production (camera requires secure context)
- Grant camera permissions in browser
- Test on multiple devices

## 🛠️ Development

### Local Development
```bash
# Install development dependencies
pip install flask flask-cors requests reportlab pillow

# Run in debug mode
python app.py
```

### Adding New Features
- Follow the existing class-based architecture
- Add validation rules in `validation.js`
- Update PDF generation in `pdf-generator.js`
- Test across multiple devices and browsers

## 📱 Browser Support
- ✅ Chrome 70+
- ✅ Firefox 65+
- ✅ Safari 12+
- ✅ Edge 79+
- ✅ Mobile browsers (iOS Safari, Chrome Mobile)

## 🔒 Security Features
- Input sanitization and validation
- Base64 encoding for image data
- Environment variable configuration
- No sensitive data in client-side code

## 📄 License

This project is developed for Navadaya Girls Hostel admission management.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

For support and queries, contact the hostel administration or submit an issue in this repository.

---

**🏠 Made with ❤️ for Navadaya Girls Hostel**