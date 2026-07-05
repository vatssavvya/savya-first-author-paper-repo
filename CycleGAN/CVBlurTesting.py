import cv2

image = cv2.imread("blur_testing.jpg")

final_Result = cv2.GaussianBlur(image, (15,15),0)

cv2.imwrite('blurred-cancerimage.jpg', final_Result)