from flask import Flask
import mypy
from app import create_app

app: Flask = create_app()

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80, debug=True)


