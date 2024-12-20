from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from flask import send_from_directory

app = Flask(__name__, static_folder='static')

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Your Gmail address
app.config['MAIL_PASSWORD'] = 'your-app-password'      # Your App Password
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'
app.secret_key = 'your_secret_key'  # Change to a random secret key

mail = Mail(app)

@app.route('/services-details')
def services_details():
    return render_template('services-details.html')

@app.route('/assets/<path:filename>')
def assets_static(filename):
    return send_from_directory('assets', filename)

@app.route('/projects')
def projects():
    return render_template('projects.html')  # This renders the 'projects.html' template

@app.route('/sustain')
def sustain():
    return render_template('sustain.html')  # This renders the 'projects.html' template




@app.route('/services')
def services():
    return render_template('services.html')  # This renders the 'reviews.html' template


@app.route('/contact')
def contact():
    return render_template('contact.html')  # This renders the 'contact.html' template


# Homepage route
@app.route('/')
def index():
    return render_template('index.html')  # Renders the main homepage

# Route for the About page
@app.route('/about')
def about():
    return render_template('about.html')  # Renders the About Us page

# Route for the quote form (GET method)
@app.route('/get-quote')
def get_quote_form():
    return render_template('get-quote.html')  # Renders the Get Quote form page

# Route for the quote form submission (POST method)
@app.route('/get-quote', methods=['POST'])
def get_quote():
    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')
    project_name = request.form.get('project_name')
    project_description = request.form.get('project_description')
    phone_number = request.form.get('phone_number')

    # Form validation
    if not name or not email or not project_name or not project_description or not phone_number:
        flash('All fields are required!', 'warning')
        return redirect(url_for('get_quote_form'))

    # Create the email message
    msg = Message("New Quote Request", recipients=['receiver-email@example.com'])
    msg.body = f"""
    Name: {name}
    Email: {email}
    Project Name: {project_name}
    Project Description: {project_description}
    Phone Number: {phone_number}
    """

    # Send the email
    try:
        mail.send(msg)
        flash('Quote request sent successfully!', 'success')
    except Exception as e:
        flash(f'Failed to send email: {str(e)}', 'danger')

    # After submission, redirect to the homepage to refresh the form
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
