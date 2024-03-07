import sys
sys.path.append('..')

from flask import Flask, request
from infrastructure.user_repository import UserRepository
from domain.user_service import UserService

app = Flask(__name__)

# Configura la URL de conexión a MySQL
#mysql_db_url = 'mysql+mysqlconnector://user:password@host/database'
mysql_db_url = 'mysql+mysqlconnector://root:13960@localhost/prueba'
# Crea instancias de servicios y repositorios con la URL de conexión
user_repo = UserRepository(mysql_db_url)
user_service = UserService(user_repo)

@app.route('/', methods=['GET'])
def index():
    return 'Hello, World!'

@app.route('/users', methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    return {'users': users}

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.get_user(user_id)
    return {'user': user}

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = user_service.create_user(data)
    return {'user': new_user}, 201

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    result = user_service.delete_user(user_id)
    if result:
        return {'message': 'User deleted'}
    else:
        return {'message': 'User not found'}, 404
    
if __name__ == '__main__':
    while True:
        try:
            app.run(debug=True, port=8000)
        except Exception as e:
            print(f"Error occurred: {e}")
