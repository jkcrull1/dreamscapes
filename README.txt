Dreamscapes Landscaping Service
Dreamscapes is a Flask-based web application for a fictitious landscaping service company. This interactive application allows customers to browse the company's services, make service requests, and get in contact with the management.

Features
The application includes the following main features:

Home Page: This page displays a carousel of images showcasing various landscaping projects completed by the company.

Contact Page: Allows visitors to send a message to the company. The form collects the user's name, email, and message.

Manager Page: A page accessible only by the company's management team. It provides a list of customers who have contacted the company.


Technology Stack
The application uses the following technologies:

Python: The backend is written in Python.
Flask: The web framework used is Flask 
HTML/CSS: Frontend is designed using HTML and styled with CSS.
MySQL: Used as the database to store customer information.
Jinja2: A templating engine for Python, used in Flask to generate dynamic HTML content.
Gunicorn: A WSGI HTTP server to serves the Flask application in production.

The devlopment server is 127.0.0.1:5000 using flask
The production server is 127.0.0.1:8000 using Gunicorn

The application is configured to be deployed easily using Gunicorn.

*NOTE* As Security was not the focus of our projct the manager page is easily accesible 
