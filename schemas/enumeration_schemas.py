from models.enumeration_tables import Country,States,City,Language
from settings import app,db,ma

class CountrySchema(ma.Schema):
    class Meta:
        fields = ('id','country_name','country_code')

country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)

class StatesSchema(ma.Schema):
    class Meta:
        fields = ('id','state_name','country_id')
state_schema = StatesSchema()
states_schema = StatesSchema(many=True)

class CitiesSchema(ma.Schema):
    class Meta:
        fields = ('id','city_name','state_id')
city_schema = CitiesSchema()
cities_schema = CitiesSchema(many=True)

class LanguageSchema(ma.Schema):
    class Meta:
        fields = ('id','language')
language_schema = LanguageSchema()
languages_schema = LanguageSchema(many=True)
