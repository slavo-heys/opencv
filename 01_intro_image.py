import cv2
import numpy as np

# wczytaj obraz
orginal_img = cv2.imread('/home/slavo/pythonProject/open_cv/venv/assets/python.png')
img = orginal_img.copy()

#cv2.imshow('bear', img) # wyświetl obraz
#cv2.waitKey(0) # czekaj na naciśnięcie klawisza

# zapisz obraz
# cv2.imwrite('/home/slavo/Pobrane/bear_copy.jpg', img)

height, width = img.shape[:2]
print(f'wysokosc: {height}, szerokosc: {width}')

# rysowanie linii
# cv2.line(img, (0, 0), (width, height), (0, 255, 0), 5)
# cv2.imshow('bear', img) # wyświetl obraz
# cv2.waitKey(0) # czekaj na naciśnięcie klawisza

# # rysowanie prostokąta
# img = orginal_img.copy()
# cv2.rectangle(img, (200, 50), (400, 230), (255, 0, 0), 3)
# cv2.imshow('bear', img) # wyświetl obraz
# cv2.waitKey(0) # czekaj na naciśnięcie klawisza

# rusowanie koła
img = orginal_img.copy()
cv2.circle(img, (300, 140), 90, (0, 0, 255), 3)
cv2.imshow('bear', img) # wyświetl obraz
cv2.waitKey(0) # czekaj na naciśnięcie klawisza