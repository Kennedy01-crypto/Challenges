from flask import Blueprint, render_template, redirect, url_for, flash
from datetime import datetime

main_bp = Blueprint('main', __name__)

# Dummy data for now
DUMMY_CHALLENGES = [
    {'id': 1, 'title': 'Complete the Flask Tutorial', 'description': 'Read and implement the Flask mega-tutorial.', 'due_date': datetime(2024, 8, 1), 'status': 'In Progress'},
    {'id': 2, 'title': 'Build a REST API', 'description': 'Create a simple REST API for a blog.', 'due_date': datetime(2024, 8, 15), 'status': 'Not Started'},
    {'id': 3, 'title': 'Deploy to Production', 'description': 'Deploy this app to a cloud provider.', 'due_date': datetime(2024, 9, 1), 'status': 'Not Started'},
]

@main_bp.route('/')
@main_bp.route('/index')
def index():
    """Show all challenges."""
    return render_template('index.html', title='Home', challenges=DUMMY_CHALLENGES)

@main_bp.route('/challenge/<int:challenge_id>')
def challenge(challenge_id):
    """Show a single challenge."""
    chal = next((c for c in DUMMY_CHALLENGES if c['id'] == challenge_id), None)
    if chal is None:
        flash('Challenge not found!', 'error')
        return redirect(url_for('main.index'))
    return render_template('challenge.html', title=chal['title'], challenge=chal)

@main_bp.route('/create', methods=['GET', 'POST'])
def create_challenge():
    """Create a new challenge."""
    # We will add form handling logic here later
    # For now, just render the template
    return render_template('create_challenge.html', title='New Challenge')

@main_bp.route('/challenge/<int:challenge_id>/edit', methods=['GET', 'POST'])
def edit_challenge(challenge_id):
    """Edit an existing challenge."""
    chal = next((c for c in DUMMY_CHALLENGES if c['id'] == challenge_id), None)
    if chal is None:
        flash('Challenge not found!', 'error')
        return redirect(url_for('main.index'))
    # We will add form handling logic here later
    return render_template('edit_challenge.html', title='Edit Challenge', challenge=chal)

@main_bp.route('/challenge/<int:challenge_id>/delete', methods=['POST'])
def delete_challenge(challenge_id):
    """Delete a challenge."""
    # We will add deletion logic here later
    flash(f'Challenge {challenge_id} "deleted" (not really).', 'success')
    return redirect(url_for('main.index'))