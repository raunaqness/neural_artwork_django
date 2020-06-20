from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from PIL import Image

@api_view(('GET',))
def index(request):
	return Response('Hello world!')


@api_view(('GET', 'POST',))
def create_artwork(request):

	if request.method == 'GET':
		template = loader.get_template('index.html')
		context = {}
		return HttpResponse(template.render(context, request))

	if request.method == 'POST':

		if 'file' not in request.data:
			raise ParseError("Empty content")

		f = request.data['file']

		try:
			img = Image.open(f)
			img.verify()
		except:
			raise ParseError("Unsupported image type")



		template = loader.get_template('index.html')
		context = {}
		return HttpResponse(template.render(context, request))


