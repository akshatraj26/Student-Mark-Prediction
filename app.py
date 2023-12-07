import numpy as np
import pandas as pd
from flask import Flask, request, render_template, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import joblib
import pytz

app = Flask(__name__)


# Configure the Alchemy Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'studentmarkpredictions'
db = SQLAlchemy(app)

app.app_context().push()


class User(db.Model):
    __tablename__ = 'client'
    
    id = db.Column(db.Integer, primary_key =True)
    number_courses = db.Column(db.Integer, nullable=False)
    study_hours = db.Column(db.Float, nullable =False)
    predicted_output = db.Column(db.Integer, nullable =False)
    indian_time = pytz.timezone('Asia/Kolkata')
    created = db.Column(db.DateTime, default = datetime.now(indian_time))
    
    def __repr__(self):
        return f"<Student {self.study_hours}>"

# Load the model
model = joblib.load("multiple_student_mark_prediction.pkl")


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/predict", methods=["POST", "GET"])
def predict():
    if request.method == 'POST':
        number_of_courses = int(request.form['NumofCourses'])
        study_hour = float(request.form['Study_Hour'])
        
        if number_of_courses> 8:
            flash("Don't take to many courses in a college or Your mind will start to hank")
            return redirect(url_for('home'))
        # input_features = [int(x) for x in request.form.values()]
        
        print("Number of Courses: ", number_of_courses)
        print('Study Hours :', study_hour)

        # validate input hour
        if study_hour < 0 or study_hour > 24:
            flash('Please enter the valid hour between 1 - 24', 'danger')
            return redirect(url_for('home'))
        elif study_hour > 18:
            flash('You are not a human. Get some rest man or you will get sick.', 'danger')
            return redirect(url_for('home'))

        if study_hour.is_integer():
            study_hour = int(study_hour)
        else:
            study_hour = study_hour
        # Prepare feature array
        input_features = np.array([number_of_courses, study_hour])
        # print("Features Value: ", input_features)
        
        prediction = model.predict([input_features])[0].round(2)
        # print("Predicted Text: ", prediction)
        
        
     
 
        
        new_entry = User(number_courses = number_of_courses, study_hours = study_hour, predicted_output = prediction)
        try:
            
            db.session.add(new_entry)
            db.session.commit()
            return render_template('index.html', message = "Based on our prediction, if you study for  {}  hours per day, you might achieve   {}% marks.".format(str(study_hour), float(prediction)))
        except Exception as e:
            flash('There was some problem showing or saving your results', 'danger')
            print(str(e))
       
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run( port=5000, debug=True)
   
