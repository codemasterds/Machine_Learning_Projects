Diabetes Prediction Application using Flask and Random Forest Classifiers
Overview
This is a web application that predicts the likelihood of a person having diabetes based on their health information. The application uses a machine learning model, specifically a Random Forest Classifier, to make predictions. The model has been trained on a dataset of health information of individuals with and without diabetes. The application is built using Flask, a Python web framework, and is deployed on an EC2 server with Nginx and Gunicorn.

Features
User-friendly web interface that accepts user input for their health information
Predicts the likelihood of the user having diabetes based on the input provided
Displays the prediction result (either "Diabetes Risk: High" or "Diabetes Risk: Low") to the user
Provides a detailed explanation of how the prediction report is made
Provides an option for users to download the prediction report in PDF format
Technologies Used
Python
Flask
Random Forest Classifier
HTML/CSS/JavaScript
Bootstrap
Nginx
Gunicorn
Installation
To install and run the application, follow these steps:

Clone the repository: git clone https://github.com/<your-username>/diabetes-prediction-app.git
Navigate to the project directory: cd diabetes-prediction-app
Install the required packages: pip install -r requirements.txt
Run the application: python app.py
Usage
Open your web browser and go to http://<your-server-IP-address>
Fill in the health information form and submit
View the prediction result and explanation
Download the prediction report in PDF format
Future Improvements
Add more health information variables to improve the accuracy of the prediction model
Provide additional visualizations to enhance the user experience
Add a feature to allow users to save their prediction history
Allow users to customize the prediction threshold
License
This project is licensed under the MIT License. See the LICENSE file for more information.

Acknowledgments
This project was inspired by the need to provide a quick and easy way for individuals to check their risk of having diabetes. Thanks to the developers of Flask, Scikit-learn, and other open-source libraries that made this project possible.
