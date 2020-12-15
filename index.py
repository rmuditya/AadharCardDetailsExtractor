import numpy as np
import cv2
import pytesseract
font = cv2.FONT_HERSHEY_PLAIN
# reading the path
path = "./aadhar-img/3.jpg"
# read the img
img = cv2.imread(path)
img2 = img.copy()
# convert to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Configuration for tesseract
configr = ('-l eng --oem 1 --psm 3')
text_aadhar =  pytesseract.image_to_string(imgGray, config = configr)

# Validations and checking
if 'Name' and 'DOB' in text_aadhar:
	print('[SUCCESS] Aadhar Card is Valid')
	res = text_aadhar.split()
	
	
	# print(res)
	if 'Name' in text_aadhar:
		index = res.index('Name:')
		name = "Name : " + res[index + 1] + " " + res[index + 2]
		# print(name)
		if 'DOB:' in text_aadhar:
			index = res.index('DOB:')
			DOB = "Date of birth: " + res[index + 1]
			if 'Female' in text_aadhar:
				index = res.index('Female')
				aadhar_no = 'Aadhar Number : ' + res[index + 1] + res[index + 2] + res[index + 3]
				# print(aadhar_no)
				print(name)
				print(DOB)
				print(aadhar_no)
				cv2.putText(img, name,(20,20),font,1,(0,255,128),2)
				cv2.putText(img, DOB,(230,20),font,1,(0,255,128),2)
				cv2.putText(img, aadhar_no,(160,445),font,1,(0,255,128),2)
			else:
				if 'Male' in text_aadhar:
					index = res.index('Male')
					aadhar_no = 'Aadhar Number : ' + res[index + 1] + res[index + 2] + res[index + 3]
					# print(aadhar_no)

					# print(DOB)
					# print(name)
					# print(aadhar_no)
			
			

# print(DOB)
# print(name)
# print(aadhar_no)
		# pass
else:
	print('[ERROR] Aadhar Card is Invalid')
	print('[INFO] TRY WITH CLEAR IMAGE')
# print(text_no)
# output
cv2.imwrite('detected/' + name +'.jpg', img)
cv2.imshow("Detected Details", img)
# cv2.imshow("Original", img2)c
# cv2.imshow("imgGray", imgGray)
cv2.waitKey(0)