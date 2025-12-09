"""
Главное Flask приложение для системы управления продукцией мебельной компании
"""
from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from routes.products import products_bp
from routes.workshops import workshops_bp
from database import init_db


def create_app():
    """Создание и конфигурация Flask приложения"""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Включить CORS для всех маршрутов
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Инициализация БД
    init_db(app)

    # Регистрация blueprints
    app.register_blueprint(products_bp)
    app.register_blueprint(workshops_bp)

    # Главный роут
    @app.route('/')
    def index():
        return jsonify({
            'name': 'Furniture Company Management System',
            'version': '1.0.0',
            'api_endpoints': {
                'products': '/api/products',
                'workshops': '/api/workshops'
            }
        })

    # Обработка ошибок
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Ресурс не найден'}), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Внутренняя ошибка сервера'}), 500

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)