from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, FileResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from PIL import Image

from utils.Artist import Artist

@api_view(('GET',))
def index(request):
	return Response('Hello world!')


@api_view(('GET', 'POST',))
def create_artwork(request):

	if request.method == 'POST':

		if 'file' not in request.data:
			raise ParseError("Empty content")

		print("request.data")
		print(request.data)


		f = request.data['file']
		file_bytes = f.read()

		print("file")
		print(f)

		try:
			pil_image = Image.open(f)
			pil_image.verify()
		except:
			raise ParseError("Unsupported image type")

		new_artwork = Artist().create_artwork(Image.open(f), "starry_night")

		return HttpResponse(new_artwork, content_type="image/jpeg")

	if request.method == 'GET':
		template = loader.get_template('index.html')
		context = {}
		return HttpResponse(template.render(context, request))
