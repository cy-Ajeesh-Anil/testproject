
from settings import app
from apis import api, Signup, VerifyStudent, Login,RefreshTtoken,ListCountries,ListStates,ListCountryStates,ListCities,\
ListStatesCities,ListLanguages

# app = Flask(__name__)
api.init_app(app)

api.add_resource ( Signup, '/api/v1/student/signup' )
api.add_resource(VerifyStudent,'/api/v1/student/verify')
api.add_resource(Login,'/api/v1/student/login')
api.add_resource(RefreshTtoken,'/api/v1/student/refresh-token')
api.add_resource(ListCountries,'/api/v1/countries')
api.add_resource(ListStates,'/api/v1/states')
api.add_resource(ListCountryStates,'/api/v1/states/<country_id>')
api.add_resource(ListCities,'/api/v1/cities')
api.add_resource(ListStatesCities,'/api/v1/cities/<state_id>')
api.add_resource(ListLanguages,'/api/v1/languages')

if __name__ == '__main__':
    app.run(debug=True)
