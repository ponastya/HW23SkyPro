from flask import Blueprint

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/perform_query', methods=['GET', 'POST'])
def perform_query():
    return f"Я страничкв профиля пользователя "