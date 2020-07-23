import cv2

path = "C:\\Users\\muhnu\\Documents\\python\\opencv\\minatbakat.jpeg"

img = cv2.imread(path)
cv2.imshow("minatbakat", img)
cv2.waitKey()
cv2.destroyAllWindows()
