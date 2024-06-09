from flask import Flask, render_template, request
    import qrcode
    import os
    from datetime import datetime
    
    app = Flask(__name__)
    
    @app.route('/', methods=['GET', 'POST'])
    def display_qr():
        qr_filename = None
        if request.method == 'POST':
            text = request.form.get('text', 'Example text')
            # Generate QR code
            qr_image = qrcode.make(text)
            
            # Save QR code as an image with a unique filename
            timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
            qr_filename = f'qrcode_{timestamp}.png'
            qr_image.save(os.path.join('static', qr_filename))
        
        return render_template('qr_display.html', qr_filename=qr_filename)
    
    if __name__ == '__main__':
        app.run(debug=True)