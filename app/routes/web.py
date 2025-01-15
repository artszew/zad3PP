from flask import Blueprint, render_template, request, redirect, url_for
from app.models import DataPoints, db

web_bp = Blueprint('web', __name__)


@web_bp.route('/')
def home():
    data_points = DataPoints.query.all()
    return render_template('index.html', data_points=data_points)


@web_bp.route('/add', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        try:
            width = float(request.form.get('width'))
            height = float(request.form.get('height'))
            species = int(request.form.get('species'))

            if width <= 0 or height <= 0 or species < 0:
                raise ValueError("Invalid data values")

            new_point = DataPoints(width=width, height=height, species=species)
            db.session.add(new_point)
            db.session.commit()
            return redirect(url_for('web.home'))
        except (ValueError, TypeError):
            return render_template('add.html', error="Invalid data"), 400

    return render_template('add.html')


@web_bp.route('/delete/<int:record_id>', methods=['POST'])
def delete_data(record_id):
    point = DataPoints.query.get(record_id)
    if not point:
        return render_template('error.html', message="Data point not found"), 404

    db.session.delete(point)
    db.session.commit()
    return redirect(url_for('web.home'))
