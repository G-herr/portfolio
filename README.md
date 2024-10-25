# Portfolio

Developed a [portfolio website](https://gustavohr.pythonanywhere.com/) using a Flask with a 'Contact Me' form that saves submissions to a CSV file and sends automated email notifications. Website: [GustavoHR.pythonanywhere.com](https://gustavohr.pythonanywhere.com/)

* **Framework:** Built with [Flask](https://flask.palletsprojects.com/en/stable/) to create a lightweight, Python-based backend for serving dynamic content and handling form submissions.
* **Template Customization:** Modified an existing HTML/CSS template to create a clean, user-friendly portfolio showcasing my resume, projects, and contact details.
* **Contact Form with REST API:**
  * Developed a ['Contact Me'](https://gustavohr.pythonanywhere.com/contact.html) section with a REST API endpoint that handles user submissions.
  * On form submission, user information is securely saved to a database and simultaneously sent to my email for immediate notifications.
* **Data storage:**  User inquiry data is stored in a CSV file, providing a simple, flat-file storage solution without the need for a full relational database.
* **Email Notification:** Configured an [automated email system](https://docs.python.org/3/library/email.html#module-email) that sends notifications with user-submitted details upon each form submission.
* **Deployment:** Hosted the application on [Python Anywhere](https://www.pythonanywhere.com/) for reliable access and easy maintenance
