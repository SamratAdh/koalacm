# Project Startup - Koala Certificate Manager

## Overview

Welcome to the GitHub repository KoalaCM a collaborative project undertaken during the third year by a team of four individuals. The project focuses on the development of the Koala Certificate Manager, a web application built with Flask, designed to simplify the generation and management of self-signed certificates.

## Project Details

- **Project Name:** Koala Certificate Manager
- **Project Type:** Last Year Project
- **Team Members:** Samrat, Ilias, Ismail, Jelle

## Features

1. **User Authentication:**
   - Users can log in with a username and password (Currently, only one pre-programmed user, koala, is supported).

2. **Certificate Generation:**
   - Users can generate self-signed certificates with customizable fields such as the common name, organization, validity period, optional password protection, and more to be added in the future.

3. **Certificate Download:**
   - After generating a certificate, users can individually download the private key, X.509 certificate, and CSR (Certificate Signing Request).

4. **Styling and User Feedback:**
   - The application has a clean and responsive user interface.
   - Success and error messages are displayed to provide feedback on the certificate generation process.

## Usage

1. **Login:**
   - Visit the application and log in using the provided login page.

2. **Create Certificate:**
   - After logging in, navigate to the "Create Certificate" page.
   - Fill in the required fields for generating a certificate.
   - Click the "Generate Certificate" button.

3. **Download Certificates:**
   - Upon successful certificate generation, the user receives messages with the file names of the generated certificates.
   - Download the private key, X.509 certificate, and CSR individually by clicking on the provided links.

## Project Structure

- **app.py:** Main file of the Flask application.
- **utils.py:** Contains functions for certificate generation and user validation.
- **templates:** Folder with HTML templates.
  - **index.html:** Home page.
  - **login.html:** Login page.
  - **create_certificate.html:** Page for creating certificates.
- **uploads:** Folder to store generated certificates.

## Running the Application

1. Clone the repository.
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Open the application in a web browser at `http://localhost:5000`.

## Notes

- The application currently supports self-signed certificates.
- The application is a prototype and does not integrate with a certificate authority.
- Certificates are generated using OpenSSL.

## Future Improvements

- Integration with Let's Encrypt for CA-signed certificates.
- Enhanced user interface and error handling.
- Additional security features and certificate options.
