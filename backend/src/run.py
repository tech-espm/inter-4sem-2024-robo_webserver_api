from app import create_app
from flask_cors import CORS
run = create_app()

CORS(run, origins=["http://localhost:8080"])

if __name__ == '__main__':
    run.run(host='0.0.0.0', port=5000)


