from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, Job, Application
from forms import RegistrationForm, LoginForm, JobForm, ApplicationForm, JobSearchForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-dev-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///job_portal.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create database tables
with app.app_context():
    db.create_all()

# Home route
@app.route('/')
def index():
    recent_jobs = Job.query.order_by(Job.posted_date.desc()).limit(5).all()
    return render_template('index.html', jobs=recent_jobs)

# Auth routes
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, role=form.role.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('auth/register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        else:
            flash('Invalid email or password', 'danger')
    
    return render_template('auth/login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Job routes
@app.route('/jobs')
def jobs():
    form = JobSearchForm()
    page = request.args.get('page', 1, type=int)
    
    # Filter jobs based on search parameters
    keyword = request.args.get('keyword', '')
    location = request.args.get('location', '')
    category = request.args.get('category', '')
    
    jobs_query = Job.query
    
    if keyword:
        jobs_query = jobs_query.filter(Job.title.contains(keyword) | Job.description.contains(keyword))
    if location:
        jobs_query = jobs_query.filter(Job.location.contains(location))
    if category and category != '':
        jobs_query = jobs_query.filter(Job.category == category)
    
    jobs = jobs_query.order_by(Job.posted_date.desc()).paginate(page=page, per_page=10)
    
    return render_template('jobs/search.html', jobs=jobs, form=form)

@app.route('/jobs/create', methods=['GET', 'POST'])
@login_required
def create_job():
    if current_user.role != 'employer' and current_user.role != 'admin':
        flash('Only employers can post jobs', 'danger')
        return redirect(url_for('index'))
    
    form = JobForm()
    if form.validate_on_submit():
        job = Job(
            title=form.title.data,
            description=form.description.data,
            company=form.company.data,
            location=form.location.data,
            salary=form.salary.data,
            category=form.category.data,
            employer_id=current_user.id
        )
        db.session.add(job)
        db.session.commit()
        flash('Job posted successfully!', 'success')
        return redirect(url_for('jobs'))
    
    return render_template('jobs/create.html', form=form)

@app.route('/jobs/<int:job_id>')
def job_detail(job_id):
    job = Job.query.get_or_404(job_id)
    form = ApplicationForm()
    return render_template('jobs/detail.html', job=job, form=form)

@app.route('/jobs/<int:job_id>/apply', methods=['POST'])
@login_required
def apply_job(job_id):
    if current_user.role != 'job_seeker':
        flash('Only job seekers can apply for jobs', 'danger')
        return redirect(url_for('job_detail', job_id=job_id))
    
    job = Job.query.get_or_404(job_id)
    
    # Check if already applied
    existing_application = Application.query.filter_by(
        job_id=job_id, user_id=current_user.id
    ).first()
    
    if existing_application:
        flash('You have already applied for this job', 'info')
        return redirect(url_for('job_detail', job_id=job_id))
    
    form = ApplicationForm()
    if form.validate_on_submit():
        application = Application(
            job_id=job_id,
            user_id=current_user.id,
            resume=form.resume.data,
            cover_letter=form.cover_letter.data
        )
        db.session.add(application)
        db.session.commit()
        flash('Application submitted successfully!', 'success')
    
    return redirect(url_for('job_detail', job_id=job_id))

# Profile routes
@app.route('/profile')
@login_required
def profile():
    if current_user.role == 'job_seeker':
        applications = Application.query.filter_by(user_id=current_user.id).all()
        return render_template('profile/job_seeker.html', applications=applications)
    elif current_user.role == 'employer':
        jobs = Job.query.filter_by(employer_id=current_user.id).all()
        return render_template('profile/employer.html', jobs=jobs)
    else:  # Admin
        return redirect(url_for('admin_dashboard'))

@app.route('/profile/jobs/<int:job_id>/applications')
@login_required
def job_applications(job_id):
    job = Job.query.get_or_404(job_id)
    
    if current_user.id != job.employer_id and current_user.role != 'admin':
        abort(403)
    
    applications = Application.query.filter_by(job_id=job_id).all()
    return render_template('profile/applications.html', job=job, applications=applications)

# Admin routes
@app.route('/admin')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        abort(403)
    
    users = User.query.all()
    jobs = Job.query.all()
    applications = Application.query.all()
    
    return render_template('admin/dashboard.html', users=users, jobs=jobs, applications=applications)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
