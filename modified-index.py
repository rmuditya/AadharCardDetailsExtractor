from pytesseract import Output
import pytesseract
import cv2
import os

path = os.path.join("./aadhar-img/3.jpg")
img = cv2.imread(path)
img2 = img.copy()
imageRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
results = pytesseract.image_to_data(imageRGB, output_type=Output.DICT)
for i in range(0, len(results["text"])):
	x = results["left"][i]
	y = results["top"][i]
	w = results["width"][i]
	h = results["height"][i]

	text = results["text"][i]
	conf = int(results["conf"][i])
	if conf > 80:
		print("Confidence: {}".format(conf))
		print("Text: {}".format(text))
		print("")
		# strip out non-ASCII text so we can draw the text on the image
		# using OpenCV, then draw a bounding box around the text along
		# with the text itself
		text = "".join([c if ord(c) < 128 else "" for c in text]).strip()

		cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
		
		cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
			0.4, (0, 0, 255), 2)

cv2.imshow("detecting", img)
# cv2.imshow("Original", img2)
cv2.waitKey(0)