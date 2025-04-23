# Gift-Recommendation-System
🎁 Gift Recommendation System
The Gift Recommendation System is a basic web application that helps users find suitable gifts by selecting an age group and an interest. It’s built using Python with Flask, HTML/CSS, and SQLite for the database. The system displays gift suggestions based on user choices, making the gift selection process faster and easier.
________________________________________
🎯 Purpose of the Project
This project was created to:
•	Help users choose gifts more easily
•	Learn and demonstrate basic full-stack web development
•	Practice working with forms, databases, and template rendering in Flask
________________________________________
📌 How It Works
1.	The user opens the homepage (index.html)
2.	They choose an age group (like "Kids", "18–25", etc.) and an interest (like "Books", "Technology", etc.)
3.	When they click Submit, the form data is sent to the Flask server
4.	Flask processes the input and searches the SQLite database for gifts that match
5.	Matching gifts are shown on the results page (result.html) with:
o	Image
o	Description
o	Price
o	A link to buy the gift
________________________________________
🛠️ Technologies Used
Tool	Purpose
Flask	Web server and routing (Python)
HTML/CSS	User interface
SQLite	Store gift information
Jinja2	Show results dynamically in HTML
________________________________________
📁 Project Files and Structure
gift-recommendation/
│
├── app.py                  # Flask application file
├── gifts.db                # SQLite database with gift data
├── insert_gifts.sql        # SQL file to insert sample gift entries
│
├── static/
│   └── styles.css          # CSS for styling the webpages
│
├── templates/
│   ├── index.html          # Homepage with the selection form
│   └── result.html         # Page showing gift recommendations
│
└── README.md               # Project description file (this one!)
________________________________________
🧪 How to Run the Project
1.	Clone the repository (or download the ZIP):
2.	git clone https://github.com/your-username/gift-recommendation.git
3.	cd gift-recommendation
4.	Install Flask:
5.	pip install flask
6.	Run the Flask app:
7.	python app.py
8.	Open your browser and visit:
9.	http://localhost:5000
________________________________________



OUTPUT:-

 ![image](https://github.com/user-attachments/assets/fd538790-13dc-4b0a-a4bf-f78030527889)

![image](https://github.com/user-attachments/assets/6cc144cd-7846-4153-8258-836d302b4851)

 ![image](https://github.com/user-attachments/assets/abe599d2-2302-47bd-bb40-ec18df3be8ab)

 ![image](https://github.com/user-attachments/assets/6d14798a-ad6f-4c5d-9ff0-bb988e178692)


