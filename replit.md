# Navadaya Girls Hostal - Admission Form System

## Overview

This is a comprehensive web-based Navadaya Girls Hostal admission form application that allows students to submit their admission applications with photo capture, digital signatures, and PDF generation capabilities. The system provides a multi-step form interface with real-time validation, draft saving, and Telegram integration for form submissions. It's built as a progressive web application with support for both light and dark themes, camera access for document capture, and local storage for draft management.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Pure HTML/CSS/JavaScript**: No frameworks used, relying on vanilla JavaScript with ES6 classes
- **Multi-step Form Interface**: Progressive form with 7 steps including progress tracking and validation
- **Modular Component System**: Separate JavaScript classes for different functionalities (Camera, Signature, PDF, Storage, etc.)
- **CSS Grid/Flexbox Layout**: Modern CSS layout techniques with custom CSS variables for theming
- **Progressive Web App**: Designed with responsive design principles and theme switching capabilities

### State Management
- **Class-based Architecture**: Each major functionality encapsulated in its own class (NavadayaGirlsHostalApp, CameraHandler, SignatureHandler, etc.)
- **Local State Management**: Form data stored in the main app controller with automatic draft saving
- **Event-driven Architecture**: Heavy use of event listeners for component communication

### User Interface Design
- **Theme System**: Dual theme support (light/dark) with CSS custom properties
- **Animation Framework**: Custom CSS animations for smooth transitions and user feedback
- **Responsive Design**: Mobile-first approach with flexible layouts
- **Section-based Color Coding**: Different background colors for student, guardian, and hostal sections

### Media Handling
- **Camera Integration**: WebRTC API for photo capture with environment/user camera switching
- **Digital Signatures**: HTML5 Canvas with SignaturePad library for collecting signatures
- **Image Processing**: HTML2Canvas for converting DOM elements to images
- **Document Generation**: Client-side PDF generation using jsPDF

### Data Persistence
- **Local Storage**: Draft management with compression support and version tracking
- **Form History**: Maintains history of submitted forms with configurable limits
- **Settings Storage**: User preferences and application settings persistence
- **Data Sanitization**: Built-in data cleaning and validation before storage

### Validation Framework
- **Real-time Validation**: Debounced validation with immediate user feedback
- **Rule-based System**: Configurable validation rules with custom validators
- **Multi-field Validation**: Cross-field validation for complex business rules
- **Error Management**: Comprehensive error messaging with user-friendly feedback

## External Dependencies

### Core Libraries
- **jsPDF**: PDF document generation with support for tables and images
- **HTML2Canvas**: DOM to canvas conversion for PDF embedding
- **SignaturePad**: Digital signature capture with touch and mouse support
- **QRCode.js**: QR code generation for form identification
- **Font Awesome**: Icon library for UI elements
- **Google Fonts**: Inter font family for typography

### Browser APIs
- **MediaDevices API**: Camera access for photo capture
- **Canvas API**: Image manipulation and signature handling
- **LocalStorage API**: Client-side data persistence
- **File API**: File handling and blob management

### HTTP Server
- **http-server**: Development server for static file serving (Node.js dependency)

### External Services
- **Telegram Bot API**: Form submission and notification system
- **CDN Services**: External hosting for JavaScript libraries and fonts
- **Camera Hardware**: Device camera access for photo capture
- **Python Backend**: Flask server for PDF generation and Telegram integration

### Development Tools
- **NPM**: Package management for development dependencies
- **Static File Server**: Local development environment setup

The application is designed to work entirely in the browser with minimal server requirements, making it suitable for deployment on static hosting platforms while maintaining rich functionality through client-side processing and external API integrations.