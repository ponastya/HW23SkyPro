from flask import Blueprint, request, jsonify

from functions import filter_query

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    data = request.json
    with open(data['file_name']) as f:
        result = filter_query(
            value = data['value1'],
            data = f.readlines()
        )
    return jsonify(list(result))