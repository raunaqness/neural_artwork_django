import time
import cv2
import os
import numpy as np

class Artist:

	def create_artwork(self, pil_image, model_name):

		image = None
		
		try:
			image = cv2.cvtColor(np.asarray(pil_image), cv2.COLOR_RGB2BGR)
		except:
			print("CV2 : Error parsing file")

		net = cv2.dnn.readNetFromTorch(os.path.join(os.getcwd(), "utils/models/instance_norm/{}.t7".format(model_name)))
		model_name = model_name

		image_filename = "input_image"
		
		image = self.image_resize(image, width=600)
		(h, w) = image.shape[:2]

		blob = cv2.dnn.blobFromImage(image, 1.0, (w, h), (103.939, 116.779, 123.680), swapRB=False, crop=False)
		net.setInput(blob)
		start = time.time()
		output = net.forward()
		end = time.time()

		output = output.reshape((3, output.shape[2], output.shape[3]))
		output[0] += 103.939
		output[1] += 116.779
		output[2] += 123.680
		output /= 255.0
		output = output.transpose(1, 2, 0)

		print("[INFO] neural style transfer took {:.4f} seconds".format(
			end - start))

		output_filename = "{}_{}.jpg".format(image_filename, model_name)
		output_file = cv2.imencode('.jpg', output*255)[1]

		return output_file.tobytes()


	def image_resize(self, image, width = None, height = None, inter = cv2.INTER_AREA):
		
		dim = None
		(h, w) = image.shape[:2]

		if width is None and height is None:
			return image

		if width is None:
			r = height / float(h)
			dim = (int(w * r), height)

		else:
			r = width / float(w)
			dim = (width, int(h * r))

		resized = cv2.resize(image, dim, interpolation = inter)

		return resized
