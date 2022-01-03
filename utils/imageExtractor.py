## Importing libraries ##
from __future__ import print_function
import sys
import rclpy
import cv2
import os
import torch
import execnet
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class ImageExtractor(Node):

	def __init__(self):

		super().__init__('imageExtractor')

		self.cntr = 0

		self.bridge = CvBridge()

		self.subscription = self.create_subscription(Image, '/zed2i/zed_node/stereo/image_rect_color', self.listener_callback, 10)

		self.subscription

	def listener_callback(self, msg):

		try:
			image = self.bridge.imgmsg_to_cv2(msg, "bgr8")

			cvImage = cv2.imread(Image)

			filename = str(self.cntr) + ".jpg"

			cv2.imwrite(filename,cvImage)

		except CvBridgeError as e:
			print(e)

def main(args=None):

	rclpy.init(args=args)

	imageExtractor = ImageExtractor()

	rclpy.spin(imageExtractor)

	imageExtractor.destroy_node()

	rclpy.shutdown()


if __name__ == '__main__':
	main()
