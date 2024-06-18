from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from dbin import db
from models import Belonging, Sorcer, Technique

sorcers = Blueprint('sorcers', __name__)

@sorcers.route('/sorcers')
@login_required
def sorcer_list():
    sorcer_list = Sorcer.query.all()
    return render_template('sorcers.html', sorcers=sorcer_list)

@sorcers.route('/sorcers/add', methods=['GET', 'POST'])
@login_required
def add_sorcer():
    if request.method == 'POST':
        name = request.form.get('name')
        technique_name = request.form.get('technique_name')
        technique_description = request.form.get('technique_description')
        technique_rating = request.form.get('technique_rating')
        technique_strength = request.form.get('technique_strength')
        
        new_sorcer = Sorcer(
            name=name,
            technique_name=technique_name,
            technique_description=technique_description,
            technique_rating=int(technique_rating),
            technique_strength=int(technique_strength)
        )
        db.session.add(new_sorcer)
        db.session.commit()
        
        return redirect(url_for('sorcers.sorcer_list'))
    return render_template('add_sorcer.html')
