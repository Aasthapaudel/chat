# Chat App Using Flask-SocketIO

## Introduction
This is a chat application implemented using Flask-SocketIO. It includes user registration and authentication functionalities.

## Demo
[![Chat App Demo](https://your-image-link.com)](https://your-app-link.com)

## Files in the Program
- **application.py**: Main app file containing registration/login page logic and Flask-SocketIO backend.
- **models.py**: Flask-SQLAlchemy models for user registration and login.
- **wtform_fields.py**: Classes for WTForms/Flask-WTF and custom validators.
- **create.py**: Optional file only required if the repo is to be cloned.
- **Procfile**: File required for deployment (e.g., on Heroku).
- **requirements.txt**: List of Python packages installed.
- **templates/**: Folder with all HTML files.
- **static/**: Folder with all JS scripts and CSS files.

## Usage
### Run the App
Use [the link to the production server](https://your-app-link.com) directly.

### Clone/Modify the App
1. Modify `application.py` to replace the secret key and the database link with your own values.

    The lines to be edited in `application.py` are shown below:
    ```python
    app.secret_key = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_url'
    ```

2. Edit `create.py` to replace the database link with your own.

3. Run `create.py` from the terminal to create the table to hold user credentials.
    
    ```bash
    python create.py
    ```

## Roadmap
Add security features related to Input Validation, Cross-Domain, Secure Transmission, and Logging.

*See [OWASP Cheat Sheet Series](https://www.owasp.org/index.php/OWASP_Cheat_Sheet_Series#tab=Main).*


