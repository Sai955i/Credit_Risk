from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///candidates.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    interview_date = db.Column(db.String(20), nullable=False)
    documents_submitted = db.Column(db.String(200), nullable=False)
    candidate_name = db.Column(db.String(100), nullable=False)

# Home route
@app.route('/')
def index():
    candidates = Candidate.query.all()
    return render_template('index.html', candidates=candidates)

# Add candidate route
@app.route('/add', methods=['GET', 'POST'])
def add_candidate():
    if request.method == 'POST':
        company_name = request.form['company_name']
        interview_date = request.form['interview_date']
        documents_submitted = request.form['documents_submitted']
        candidate_name = request.form['candidate_name']

        new_candidate = Candidate(
            company_name=company_name,
            interview_date=interview_date,
            documents_submitted=documents_submitted,
            candidate_name=candidate_name
        )
        db.session.add(new_candidate)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_candidate.html')

# Run the app
if __name__ == '__main__':
    with app.app_context():  # Ensure application context is active
        db.create_all()  # Create database tables
    app.run(debug=True)