import argparse
import imutils
import time
import cv2
from scipy.misc import imsave

class Artwork:

	def __init__(self):
		pass

	def load_model(self, model_name):
		print("[INFO] Loading Model : {}".format(model_name))
		self.net = cv2.dnn.readNetFromTorch("models/instance_norm/" + model_name + ".t7")
		self.model_name = model_name

	def create_artwork(self, image_path):
		image_filename = image_path.split('.')[0]
		image = cv2.imread(image_path)
		image = imutils.resize(image, width=600)
		(h, w) = image.shape[:2]

		blob = cv2.dnn.blobFromImage(image, 1.0, (w, h),
			(103.939, 116.779, 123.680), swapRB=False, crop=False)
		self.net.setInput(blob)
		start = time.time()
		output = self.net.forward()
		end = time.time()

		output = output.reshape((3, output.shape[2], output.shape[3]))
		output[0] += 103.939
		output[1] += 116.779
		output[2] += 123.680
		output /= 255.0
		output = output.transpose(1, 2, 0)

		print("[INFO] neural style transfer took {:.4f} seconds".format(
			end - start))

		output_filename = "{}_{}.jpg".format(image_filename, self.model_name)
		output_file = cv2.imencode('.jpg', output*255)[1]

		return output_file