# Anugya Website

## Overview
The **Anugya Website** is a responsive and feature-rich platform developed for a green energy services company. It is built using **Flask**, **HTML**, **CSS**, **JavaScript**, and Python. The website provides detailed information about services, projects, and sustainable energy initiatives, with features like a contact form and email functionality powered by Flask-Mail.

---

## Features
- **Responsive Design**: Optimized for all devices (desktop, tablet, mobile).
- **Dynamic Routing**: Flask framework handles various routes for rendering templates.
- **Email Integration**: Powered by Flask-Mail for user inquiries and communication.
- **Service Details**: Dedicated pages for each service with a clean UI.
- **Projects Page**: Showcases completed projects with a focus on green energy solutions.
- **Static Assets Management**: Organized structure for CSS, JS, and images.

---

## Project Structure

```
anugya-website/
│
├── app.py                # Main application script
├── requirements.txt      # Python dependencies
│
├── static/               # Static files (CSS, JS, Images, Videos)
│   ├── css/
│   │   ├── products.css
│   │   ├── services.css
│   │   ├── sustain.css
│   │   ├── styles.css
│   │   └── services-details.css
│   ├── js/
│   │   └── script.js
│   ├── images/
│   │   ├── geothermal.jpg
│   │   ├── solar.jpg
│   │   ├── sustainable-energy1.jpg
│   │   ├── sustainable-energy2.jpg
│   │   └── sustainable-energy3.jpg
│   └── logo1.png
│
├── templates/            # HTML templates
│   ├── about.html
│   ├── contact.html
│   ├── get-quote.html
│   ├── index.html
│   ├── projects.html
│   ├── services.html
│   ├── services-details.html
│   └── sustain.html
│
└── assets/               # Additional assets like downloadable files or extra images
```

---

## Installation

### Prerequisites
- Python 3.7 or higher
- Flask and its extensions (Flask-Mail)

### Setup Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository/anugya-website.git
   cd anugya-website
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure Flask-Mail in `app.py`:
   Replace the placeholders with your actual email credentials:
   ```python
   app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
   app.config['MAIL_PASSWORD'] = 'your-app-password'
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open the website in your browser:
   ```
   http://127.0.0.1:5000
   ```

---

## Usage
- Navigate to the homepage to explore services and projects.
- Use the **Contact Us** form to send inquiries.
- Browse service details and project showcases for more insights.

---

## Future Enhancements
- Add a real-time news feed for green energy updates.
- Integrate a CMS for easier content management.
- Improve SEO and accessibility features.

---

