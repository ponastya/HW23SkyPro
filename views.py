from typing import Union, Dict, Any

from flask import Blueprint, request, jsonify, Response

from marshmallow import ValidationError

from builders import build_query
from models import BatchRequestSchema

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query() -> Response | tuple[Response, int]:
    data: Union[Any, Dict] = request.json

    try:
        BatchRequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400

    result = None
    for query in data['queries']:
        result = build_query(
            cmd=query['cmd'],
            value=query['value'],
            file_name=data['file_name'],
            data=result,
        )

    return jsonify(result)
