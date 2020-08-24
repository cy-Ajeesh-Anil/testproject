from models import Country,States,City,Language
from settings import db

def select_countries() :
	countries= Country.query.all()
	if countries :
		return countries
	return None

def select_states():
	states = States.query.all()
	if states:
		return states
	return None

def select_country_states(cid=None):
	states = States.query.filter_by(country_id=cid)
	if states:
		return states
	return None

def select_cities():
	cities = City.query.all()
	if cities:
		return cities
	return None

def select_state_cities(sid=None):
	cities = City.query.filter_by(state_id=sid)
	if cities:
		return cities
	return None

def select_languages():
	languages = Language.query.all()
	if languages:
		return languages
	return None