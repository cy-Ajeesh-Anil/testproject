import json

from flask import jsonify, Response


def failure ( errors=None, message=None ) :
	from werkzeug.exceptions import BadRequest
	e = BadRequest ( 'My custom message' )
	e.data = ({'errors' : errors, 'message' : message, 'status' : 'Failed'})
	raise e


def success ( data=None, message=None ) :
	value={
		"message":message,
		"data":data,
		"status":'Success'
	}
	return Response ( json.dumps(value), status=201, mimetype='application/json' )