from flask import Blueprint, request, jsonify

from marshmallow import ValidationError

from builders import build_query
from models import RequestSchema


main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    data = request.json

    try:
        RequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400

    # return ""

    first_result = build_query(
        cmd = data['cmd1'],
        value = data['value1'],
        data = None,
        file_name = data['file_name']
    )

    result = build_query(
        cmd=data['cmd2'],
        value=data['value2'],
        data=first_result,
        file_name=data['file_name']
    )

    return jsonify(result)