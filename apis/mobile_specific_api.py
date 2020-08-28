from flask_jwt_extended import jwt_required
from flask_restplus import Resource

from core import success
from settings import app




def select_onboard_images ( ) :
	return [
		{
			'id':1,
			"image":app.config['BACK_END_URL']+'static/mobile_onboard_image_1.png',
			"description":"""Create Your profile
Create your InScholaris account, You could attach the digital copies of your educational transcripts, IELTS Score Card etc to your profile/account"""
		},
		{
			'id':2,
			"image" : app.config [ 'BACK_END_URL' ] + 'static/mobile_onboard_image_2.png',
			"description":"""One platform, Many countries, Every University"""
		},
		{
			'id':3,
			"image" : app.config [ 'BACK_END_URL' ] + 'static/mobile_onboard_image_3.png',
			"description":"""InScholar
InScholaris' conversational AI Chatbots and framework help you to compare and find the right programs & colleges matched with your profile, academics and interests"""
		}
	]



class MobileOnboardImage(Resource):

    def get(self):
        return success(data=select_onboard_images(),message='List of onboarding images')
