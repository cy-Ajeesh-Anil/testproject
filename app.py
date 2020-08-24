
from settings import app
from apis import api, Signup, VerifyStudent, Login,RefreshTtoken,ListCountries,ListStates,ListCountryStates,ListCities,\
ListStatesCities,ListLanguages

# app = Flask(__name__)
api.init_app(app)

api.add_resource ( Signup, '/signup' )
api.add_resource(VerifyStudent,'/verify')
api.add_resource(Login,'/login')
api.add_resource(RefreshTtoken,'/refresh-token')
api.add_resource(ListCountries,'/countries')
api.add_resource(ListStates,'/states')
api.add_resource(ListCountryStates,'/states/<cid>')
api.add_resource(ListCities,'/cities')
api.add_resource(ListStatesCities,'/cities/<sid>')
api.add_resource(ListLanguages,'/languages')

if __name__ == '__main__':
    app.run(debug=True)
