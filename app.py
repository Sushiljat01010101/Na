from flask import Flask, request, jsonify, send_from_directory, send_file
from flask_cors import CORS
import requests
import base64
import io
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from PIL import Image
import json
from datetime import datetime

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# For Vercel deployment
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Telegram configuration - Use environment variables for production
import os
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '7693479991:AAF00-TVlY6tGmPbCcc9kvGNlNwm1yvQXZI')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', '1691680798')

def send_telegram_message(message):
    """Send a text message to Telegram"""
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    response = requests.post(url, data=data)
    return response.json()

def send_telegram_document(file_data, filename, caption=''):
    """Send a PDF document to Telegram"""
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendDocument'
    files = {
        'document': (filename, file_data, 'application/pdf')
    }
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'caption': caption
    }
    response = requests.post(url, files=files, data=data)
    return response.json()

def generate_pdf(form_data):
    """Generate PDF from form data"""
    buffer = io.BytesIO()
    
    # Create PDF
    pdf = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4
    
    # Draw header background
    pdf.setFillColorRGB(0.2, 0.3, 0.6)  # Dark blue
    pdf.rect(0, height - 70, width, 70, fill=1)
    
    # Add header text
    pdf.setFillColorRGB(1, 1, 1)  # White text
    pdf.setFont("Helvetica-Bold", 22)
    pdf.drawString(50, height - 30, "NAVADAYA GIRLS HOSTAL")
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, height - 50, "Student Admission Form")
    
    # Add application ID and date
    pdf.setFillColorRGB(0, 0, 0)  # Black text
    pdf.setFont("Helvetica", 9)
    current_date = datetime.now().strftime("%B %d, %Y")
    app_id = f"HA-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    pdf.drawString(50, height - 85, f"Application ID: {app_id}")
    pdf.drawString(50, height - 100, f"Generated on: {current_date}")
    
    y_position = height - 120
    
    # Student Details Section
    section_height = 150
    pdf.setFillColorRGB(0.9, 0.9, 1)  # Light blue background
    pdf.rect(30, y_position - section_height, width - 60, section_height, fill=1)
    
    pdf.setFillColorRGB(0, 0, 0)  # Black text
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(40, y_position - 20, "STUDENT DETAILS")
    y_position -= 35
    
    pdf.setFont("Helvetica-Bold", 10)
    student_fields = [
        ("Full Name", form_data.get('fullName', '')),
        ("Date of Birth", form_data.get('dateOfBirth', '')),
        ("Gender", form_data.get('gender', '').title()),
        ("Email Address", form_data.get('email', '')),
        ("Phone Number", form_data.get('phone', '')),
        ("Address", form_data.get('address', ''))
    ]
    
    for field, value in student_fields:
        pdf.drawString(45, y_position, f"{field}:")
        pdf.setFont("Helvetica", 9)
        pdf.drawString(150, y_position, str(value)[:50])  # Limit text length
        pdf.setFont("Helvetica-Bold", 10)
        y_position -= 18
    
    y_position -= 20
    
    # Guardian Details Section
    section_height = 100
    pdf.setFillColorRGB(0.9, 1, 0.9)  # Light green background
    pdf.rect(30, y_position - section_height, width - 60, section_height, fill=1)
    
    pdf.setFillColorRGB(0, 0, 0)  # Black text
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(40, y_position - 20, "GUARDIAN DETAILS")
    y_position -= 35
    
    pdf.setFont("Helvetica-Bold", 10)
    guardian_fields = [
        ("Guardian Name", form_data.get('guardianName', '')),
        ("Relation", form_data.get('relation', '').title()),
        ("Guardian Phone", form_data.get('guardianPhone', '')),
        ("Emergency Contact", form_data.get('emergencyContact', ''))
    ]
    
    for field, value in guardian_fields:
        pdf.drawString(45, y_position, f"{field}:")
        pdf.setFont("Helvetica", 9)
        pdf.drawString(150, y_position, str(value))
        pdf.setFont("Helvetica-Bold", 10)
        y_position -= 18
    
    y_position -= 20
    
    # Hostel Details Section
    section_height = 80
    pdf.setFillColorRGB(1, 0.95, 0.9)  # Light orange background
    pdf.rect(30, y_position - section_height, width - 60, section_height, fill=1)
    
    pdf.setFillColorRGB(0, 0, 0)  # Black text
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(40, y_position - 20, "HOSTAL DETAILS")
    y_position -= 35
    
    pdf.setFont("Helvetica-Bold", 10)
    hostel_fields = [
        ("Room Number", form_data.get('roomNumber', '')),
        ("Admission Date", form_data.get('admissionDate', '')),
        ("Stay Duration", form_data.get('stayDuration', ''))
    ]
    
    for field, value in hostel_fields:
        pdf.drawString(45, y_position, f"{field}:")
        pdf.setFont("Helvetica", 9)
        pdf.drawString(150, y_position, str(value))
        pdf.setFont("Helvetica-Bold", 10)
        y_position -= 18
    
    # Attachments summary on first page
    y_position -= 30
    section_height = 80
    pdf.setFillColorRGB(0.95, 0.95, 0.95)  # Light gray background
    pdf.rect(30, y_position - section_height, width - 60, section_height, fill=1)
    
    pdf.setFillColorRGB(0, 0, 0)  # Black text
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(40, y_position - 20, "ATTACHMENTS")
    
    pdf.setFont("Helvetica", 11)
    pdf.drawString(50, y_position - 40, "The following attachments are included on separate pages:")
    
    attachments_info = []
    if 'studentPhoto' in form_data and form_data['studentPhoto']:
        attachments_info.append("• Student Photo (Page 2)")
    if 'idProof' in form_data and form_data['idProof']:
        attachments_info.append("• ID Proof Document (Page 3)")
    if 'signature' in form_data and form_data['signature']:
        attachments_info.append("• Digital Signature (Page 4)")
    
    if not attachments_info:
        attachments_info = ["• No attachments provided"]
    
    for i, attachment in enumerate(attachments_info):
        pdf.drawString(50, y_position - 55 - (i * 15), attachment)
    
    # Add footer
    footer_y = 80
    pdf.setFillColorRGB(0.9, 0.9, 0.9)  # Light gray background
    pdf.rect(0, 0, width, footer_y, fill=1)
    
    pdf.setFillColorRGB(0, 0, 0)  # Black text
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(50, footer_y - 20, "IMPORTANT NOTES:")
    pdf.setFont("Helvetica", 8)
    pdf.drawString(50, footer_y - 35, "• This is a computer-generated document and does not require manual signature.")
    pdf.drawString(50, footer_y - 50, "• Please keep this document for your records and admission process.")
    
    pdf.setFont("Helvetica-Oblique", 8)
    pdf.drawString(350, footer_y - 20, f"Generated: {datetime.now().strftime('%d/%m/%Y at %H:%M')}")
    pdf.drawString(350, footer_y - 35, "Navadaya Girls Hostal Management System")
    pdf.drawString(350, footer_y - 50, "Contact: admission@university.edu")
    pdf.drawString(350, footer_y - 65, f"App ID: {app_id}")
    
    # PAGE 2: Student Photo (Full Page)
    if 'studentPhoto' in form_data and form_data['studentPhoto']:
        try:
            pdf.showPage()  # Start new page
            
            # Page header
            pdf.setFillColorRGB(0.2, 0.3, 0.6)
            pdf.rect(0, height - 60, width, 60, fill=1)
            pdf.setFillColorRGB(1, 1, 1)
            pdf.setFont("Helvetica-Bold", 20)
            pdf.drawString(50, height - 35, "STUDENT PHOTO")
            
            # Add photo
            photo_data = form_data['studentPhoto'].split(',')[1]
            photo_bytes = base64.b64decode(photo_data)
            photo_img = Image.open(io.BytesIO(photo_bytes))
            
            # Calculate dimensions to fit page while maintaining aspect ratio
            max_width = width - 100
            max_height = height - 200
            
            img_width, img_height = photo_img.size
            scale_x = max_width / img_width
            scale_y = max_height / img_height
            scale = min(scale_x, scale_y)
            
            new_width = int(img_width * scale)
            new_height = int(img_height * scale)
            
            photo_img = photo_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            photo_buffer = io.BytesIO()
            photo_img.save(photo_buffer, format='PNG')
            photo_buffer.seek(0)
            
            # Center the image
            x_pos = (width - new_width) / 2
            y_pos = (height - new_height) / 2 - 30
            
            pdf.drawImage(ImageReader(photo_buffer), x_pos, y_pos, width=new_width, height=new_height)
            
            # Add caption
            pdf.setFillColorRGB(0, 0, 0)
            pdf.setFont("Helvetica", 12)
            pdf.drawString(50, 50, f"Student Name: {form_data.get('fullName', 'N/A')}")
            pdf.drawString(50, 30, f"Application ID: {app_id}")
            
        except Exception as e:
            print(f"Error adding student photo page: {e}")
    
    # PAGE 3+: ID Proofs (Multiple Pages)
    if 'idProofs' in form_data and form_data['idProofs']:
        try:
            # Process multiple ID proofs with MAXIMUM quality preservation
            id_proofs = form_data['idProofs'] if isinstance(form_data['idProofs'], list) else [form_data['idProofs']]
            
            for proof_index, id_proof_data in enumerate(id_proofs):
                pdf.showPage()  # Start new page for each ID proof
                
                # Enhanced page header with gradient effect
                pdf.setFillColorRGB(0.1, 0.2, 0.5)
                pdf.rect(0, height - 80, width, 80, fill=1)
                
                # Header border
                pdf.setStrokeColorRGB(0.8, 0.8, 0.8)
                pdf.setLineWidth(2)
                pdf.line(0, height - 80, width, height - 80)
                
                # Main title with document number
                pdf.setFillColorRGB(1, 1, 1)
                pdf.setFont("Helvetica-Bold", 24)
                title_text = f"IDENTITY PROOF DOCUMENT {proof_index + 1}"
                title_width = pdf.stringWidth(title_text, "Helvetica-Bold", 24)
                pdf.drawString((width - title_width) / 2, height - 35, title_text)
                
                # Subtitle
                pdf.setFont("Helvetica", 12)
                subtitle_text = "Official Verification Document"
                subtitle_width = pdf.stringWidth(subtitle_text, "Helvetica", 12)
                pdf.drawString((width - subtitle_width) / 2, height - 55, subtitle_text)
                
                # Process current ID proof
                id_data = id_proof_data.split(',')[1]
                id_bytes = base64.b64decode(id_data)
                id_img = Image.open(io.BytesIO(id_bytes))
                
                # Get original format and preserve it
                original_format = id_img.format or 'PNG'
                
                # Calculate available space with generous margins
                margin_x = 40
                margin_y = 100
                max_width = width - (2 * margin_x)
                max_height = height - margin_y - 120
                
                img_width, img_height = id_img.size
                
                # Check if image fits without resizing
                if img_width <= max_width and img_height <= max_height:
                    # Use original image without any resizing
                    new_width = img_width
                    new_height = img_height
                    final_img = id_img  # No processing needed
                else:
                    # Only resize if absolutely necessary
                    scale_x = max_width / img_width
                    scale_y = max_height / img_height
                    scale = min(scale_x, scale_y)
                    
                    new_width = int(img_width * scale)
                    new_height = int(img_height * scale)
                    
                    # Use highest quality resampling
                    final_img = id_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # Save with MAXIMUM quality settings
                id_buffer = io.BytesIO()
                if original_format.upper() in ['JPEG', 'JPG']:
                    # Highest JPEG quality possible
                    final_img.save(id_buffer, format='JPEG', quality=100, optimize=False, 
                                 subsampling=0, progressive=False)
                else:
                    # Highest PNG quality - no compression
                    final_img.save(id_buffer, format='PNG', optimize=False, compress_level=0)
                id_buffer.seek(0)
                
                # Center the image with better positioning
                x_pos = (width - new_width) / 2
                y_pos = height - margin_y - new_height - 20
                
                # Add image border/frame
                border_width = 3
                pdf.setStrokeColorRGB(0.3, 0.3, 0.3)
                pdf.setLineWidth(border_width)
                pdf.rect(x_pos - border_width, y_pos - border_width, 
                        new_width + (2 * border_width), new_height + (2 * border_width))
                
                # Add the image
                pdf.drawImage(ImageReader(id_buffer), x_pos, y_pos, width=new_width, height=new_height)
                
                # Enhanced information section with better layout
                info_y = y_pos - 40
                
                # Background box for information
                pdf.setFillColorRGB(0.95, 0.95, 0.95)
                pdf.setStrokeColorRGB(0.7, 0.7, 0.7)
                pdf.setLineWidth(1)
                pdf.rect(50, info_y - 60, width - 100, 80, fill=1, stroke=1)
                
                # Information text
                pdf.setFillColorRGB(0, 0, 0)
                pdf.setFont("Helvetica-Bold", 14)
                pdf.drawString(70, info_y - 15, f"DOCUMENT INFORMATION - ID Proof {proof_index + 1}")
                
                pdf.setFont("Helvetica", 11)
                pdf.drawString(70, info_y - 35, f"Student Name: {form_data.get('fullName', 'N/A')}")
                pdf.drawString(70, info_y - 50, f"Application ID: {app_id}")
                
                # Add timestamp and verification info
                current_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                pdf.drawString(width - 250, info_y - 35, f"Verification Date: {current_time}")
                pdf.drawString(width - 250, info_y - 50, f"Image Quality: High Resolution")
                
                # Footer with verification seal
                pdf.setFont("Helvetica-Oblique", 10)
                pdf.setFillColorRGB(0.5, 0.5, 0.5)
                footer_text = "This document is digitally verified and authenticated"
                footer_width = pdf.stringWidth(footer_text, "Helvetica-Oblique", 10)
                pdf.drawString((width - footer_width) / 2, 30, footer_text)
            
        except Exception as e:
            print(f"Error adding ID proof page: {e}")
    
    # PAGE 4: Digital Signature (Full Page)
    if 'signature' in form_data and form_data['signature']:
        try:
            pdf.showPage()  # Start new page
            
            # Page header
            pdf.setFillColorRGB(0.2, 0.3, 0.6)
            pdf.rect(0, height - 60, width, 60, fill=1)
            pdf.setFillColorRGB(1, 1, 1)
            pdf.setFont("Helvetica-Bold", 20)
            pdf.drawString(50, height - 35, "DIGITAL SIGNATURE")
            
            # Add signature
            sig_data = form_data['signature'].split(',')[1]
            sig_bytes = base64.b64decode(sig_data)
            sig_img = Image.open(io.BytesIO(sig_bytes))
            
            # Calculate dimensions to fit page while maintaining aspect ratio
            max_width = width - 200
            max_height = height - 300
            
            img_width, img_height = sig_img.size
            scale_x = max_width / img_width
            scale_y = max_height / img_height
            scale = min(scale_x, scale_y)
            
            new_width = int(img_width * scale)
            new_height = int(img_height * scale)
            
            sig_img = sig_img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            sig_buffer = io.BytesIO()
            sig_img.save(sig_buffer, format='PNG')
            sig_buffer.seek(0)
            
            # Center the image
            x_pos = (width - new_width) / 2
            y_pos = (height - new_height) / 2
            
            pdf.drawImage(ImageReader(sig_buffer), x_pos, y_pos, width=new_width, height=new_height)
            
            # Add signature info
            pdf.setFillColorRGB(0, 0, 0)
            pdf.setFont("Helvetica-Bold", 14)
            pdf.drawString(50, 150, "DECLARATION:")
            pdf.setFont("Helvetica", 12)
            pdf.drawString(50, 130, "I hereby declare that all the information provided above is true and correct to the best of my knowledge.")
            pdf.drawString(50, 110, f"Student Name: {form_data.get('fullName', 'N/A')}")
            pdf.drawString(50, 90, f"Date: {datetime.now().strftime('%d/%m/%Y')}")
            pdf.drawString(50, 70, f"Application ID: {app_id}")
            
        except Exception as e:
            print(f"Error adding signature page: {e}")
    
    pdf.save()
    buffer.seek(0)
    return buffer.getvalue()

@app.route('/submit-application', methods=['POST'])
def submit_application():
    try:
        form_data = request.get_json()
        
        if not form_data:
            return jsonify({'success': False, 'error': 'No data provided'}), 400
        
        # Generate PDF
        pdf_data = generate_pdf(form_data)
        
        # Create filename
        student_name = form_data.get('fullName', 'Student').replace(' ', '_')
        filename = f"NavadayaGirlsHostal_Application_{student_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        
        # Create caption for Telegram
        caption = f"""🏠 <b>New Hostel Admission Application</b>
        
👤 Student:{form_data.get('fullName', 'N/A')}
📧 <b>Email:</b> {form_data.get('email', 'N/A')}
📱 <b>Phone:</b> {form_data.get('phone', 'N/A')}
🏠 <b>Room:</b> {form_data.get('roomNumber', 'N/A')}
📅 <b>Admission Date:</b> {form_data.get('admissionDate', 'N/A')}
⏰ <b>Duration:</b> {form_data.get('stayDuration', 'N/A')}

📋 Complete application form attached as PDF."""
        
        # Send to Telegram
        result = send_telegram_document(pdf_data, filename, caption)
        
        if result.get('ok'):
            return jsonify({
                'success': True, 
                'message': 'Application submitted successfully!',
                'telegram_message_id': result.get('result', {}).get('message_id')
            })
        else:
            return jsonify({
                'success': False, 
                'error': f'Failed to send to Telegram: {result.get("description", "Unknown error")}'
            }), 500
            
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok', 'message': 'Python backend is running'})

@app.route('/')
def index():
    return send_file('index.html')

# Entry point for Vercel - app will be imported directly

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)