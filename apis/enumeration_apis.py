from models.enumeration_tables import Country,States,City,Language
from settings import app,db,marshmallow
from flask_restplus import Resource
from core import failure, success
from CRUD.enumeration_CRUD import select_countries,select_states,select_country_states,select_cities,\
    select_state_cities,select_languages
from schemas import enumeration_schemas
from flask_jwt_extended import jwt_required, get_jwt_identity


### Listing all countries
class ListCountries(Resource):
    @jwt_required
    def get(self):
        all_countries=select_countries()
        if all_countries:
            countries = enumeration_schemas.countries_schema.dump(all_countries)
            return success(data=countries)
        return success(data=[])

### Listing all states
class ListStates(Resource):
    @jwt_required
    def get(self):
        all_states=select_states()
        if all_states:
            states = enumeration_schemas.states_schema.dump(all_states)
            return success(data=states)
        return success(data=[])

### Listing all states based on countries
class ListCountryStates(Resource):
    @jwt_required
    def get(self, country_id):
        all_states=select_country_states(country_id)
        if all_states:
            states = enumeration_schemas.states_schema.dump(all_states)
            return success(data=states)
        return success(data=[])

### Listing all cities in country
class ListCities(Resource):
    @jwt_required
    def get(self):
        all_cities = select_cities()
        if all_cities:
            cities = enumeration_schemas.cities_schema.dump(all_cities)
            return success(data=cities)
        return success(data=[])

### Listing all cities based on states
class ListStatesCities(Resource):
    @jwt_required
    def get(self,state_id):
        all_cities = select_state_cities(state_id)
        if all_cities:
            cities = enumeration_schemas.cities_schema.dump(all_cities)
            return success(data=cities)
        return success(data=[])

##### Listing all languages
class ListLanguages(Resource):
    @jwt_required
    def get(self):
        all_languages = select_languages()
        if all_languages:
            languages = enumeration_schemas.languages_schema.dump(all_languages)
            return success(data=languages)
        return success(data=[])