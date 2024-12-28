import libcamera
import cv2
from picamera2 import Picamera2, Preview, Controls

from time import sleep

rotate180 = True
rotate90 = False

def main():
	cam = Picamera2()
	config = cam.create_preview_configuration()
	if rotate180:
		config["transform"] = libcamera.Transform(hflip=1, vflip=1)
	cam.configure(config)
	
	cam.start_preview(Preview.QTGL)
	cam.start()
	
	while True:
		try:
			frame = cam.capture_array()
			if rotate90:
				frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
			cv2.imshow("lol?", frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		except KeyboardInterrupt:
			break
	
	cam.stop()
	cam.stop_preview()
	cam.close()
	print("Closed.")
	
	
if __name__ == '__main__':
	main()
	
