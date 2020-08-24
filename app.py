
from settings import app
from apis import api, Signup, VerifyStudent, Login,RefreshTtoken,ListCountries,ListStates,ListCountryStates,ListCities,\
ListStatesCities,ListLanguages

# app = Flask(__name__)
api.init_app(app)

api.add_resource ( Signup, '/api/student/signup' )
api.add_resource(VerifyStudent,'/api/student/verify')
api.add_resource(Login,'/api/student/login')
api.add_resource(RefreshTtoken,'/api/student/refresh-token')
api.add_resource(ListCountries,'/api/v1/countries')
api.add_resource(ListStates,'/api/v1/states')
api.add_resource(ListCountryStates,'/api/v1/states/<country_id>')
api.add_resource(ListCities,'/api/v1/cities')
api.add_resource(ListStatesCities,'/api/v1/cities/<state_id>')
api.add_resource(ListLanguages,'/api/v1/languages')

if __name__ == '__main__':
    app.run(debug=True)
