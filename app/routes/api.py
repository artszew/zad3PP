from flask import Blueprint, jsonify, request
from app.models import DataPoints, db

api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route('/data', methods=['GET'])
def get_all_data():
    data_points = DataPoints.query.all()
    data = [{"id": dp.id, "width": dp.width, "height": dp.height, "species": dp.species} for dp in data_points]
    return jsonify(data), 200


@api_bp.route('/data', methods=['POST'])
def add_data():
    try:
        data = request.get_json()
        width = float(data['width'])
        height = float(data['height'])
        species = int(data['species'])

        if width <= 0 or height <= 0 or species < 0:
            raise ValueError("Invalid data values")
        new_point = DataPoints(width=width, height=height, species=species)
        db.session.add(new_point)
        db.session.commit()
        return jsonify({"id": new_point.id}), 201
    except (ValueError, TypeError, KeyError):
        return jsonify({"error": "Invalid data"}), 400


@api_bp.route('/data/<int:record_id>', methods=['DELETE'])
def delete_data(record_id):
    point = DataPoints.query.get(record_id)
    if not point:
        return jsonify({"error": "Data point not found"}), 404

    db.session.delete(point)
    db.session.commit()
    return jsonify({"id": point.id}), 200
