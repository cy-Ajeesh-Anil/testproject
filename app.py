
from settings import app
from apis import api, Signup, VerifyStudent, Login,RefreshTtoken

# app = Flask(__name__)
api.init_app(app)

api.add_resource ( Signup, '/signup' )
api.add_resource(VerifyStudent,'/verify')
api.add_resource(Login,'/login')
api.add_resource(RefreshTtoken,'/refresh-token')

if __name__ == '__main__':
    app.run(debug=True)
