from flask import render_template, redirect, url_for, request
from datetime import datetime

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    try:
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        date = request.form.get('date')
        rating = request.form.get('rating')
        comments = request.form.get('comments')
        
        # Convert date string to datetime object if needed
        feedback_date = datetime.strptime(date, '%Y-%m-%d') if date else None
        
        # Add to database (adjust according to your database setup)
        # Example using SQLAlchemy:
        # new_feedback = Feedback(
        #     name=name,
        #     email=email,
        #     date=feedback_date,
        #     rating=rating,
        #     comments=comments
        # )
        # db.session.add(new_feedback)
        # db.session.commit()
        
        return redirect(url_for('thank_you'))
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred while submitting feedback", 500

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html') 