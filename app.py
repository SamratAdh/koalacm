from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import send_file
from utils import generate_certificate, validate_user
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Create a Flask application
app = Flask(__name__)

# Set the secret key for session security from environment variable
app.secret_key = os.getenv('SECRET_KEY')

# Set the upload folder for storing generated certificates
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create the upload folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Define the route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Validate user credentials
        if validate_user(username, password):
            session['username'] = username
            return redirect(url_for('create_certificate'))
        else:
            flash('Invalid credentials. Please try again.', 'error')

    return render_template('login.html')

# Define the route for creating a certificate
@app.route('/create_certificate', methods=['GET', 'POST'])
def create_certificate():
    # Redirect to login page if not logged in
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Get form data for certificate generation
        common_name = request.form['common_name']
        organization = request.form['organization']
        valid_days = request.form['valid_days']
        passphrase = request.form.get('passphrase', '')
        bits = request.form['bits']
        digest_algorithm = request.form['digest_algorithm']

        # Generate the certificate components
        private_key, x509_cert, csr = generate_certificate(common_name, organization, valid_days, passphrase, bits, digest_algorithm)

        # Save the components to files
        with open(f'{app.config["UPLOAD_FOLDER"]}/{common_name}_private_key.pem', 'w') as f:
            f.write(private_key)
        with open(f'{app.config["UPLOAD_FOLDER"]}/{common_name}_x509_cert.pem', 'w') as f:
            f.write(x509_cert)
        with open(f'{app.config["UPLOAD_FOLDER"]}/{common_name}_csr.pem', 'w') as f:
            f.write(csr)

        # Flash success messages for the user
        flash('Certificate created successfully!', 'success')
        flash(f'Private Key: {common_name}_private_key.pem', 'private_key')
        flash(f'X.509 Certificate: {common_name}_x509_cert.pem', 'x509_cert')
        flash(f'CSR: {common_name}_csr.pem', 'csr')

    return render_template('create_certificate.html')

# Custom function to send files with the original environment
def send_file_with_environ(filename, environ_base, **kwargs):
   return send_file(filename, environ=environ_base, **kwargs)

# Define the route for downloading files
@app.route('/download/<filename>')
def download(filename):
   return send_file_with_environ(f'{app.config["UPLOAD_FOLDER"]}/{filename}', request.environ, as_attachment=True)

# Define the route for user logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

# Run the application if executed directly
if __name__ == '__main__':
    app.run(debug=True)
