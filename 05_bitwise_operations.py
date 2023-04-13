import cv2
import imutils

# wczytaj obraz
img = cv2.imread('/home/slavo/pythonProject/open_cv/venv/assets/bear.jpg')
logo = cv2.imread('/home/slavo/pythonProject/open_cv/venv/assets/python.png')
logo = imutils.resize(logo, height=150)

# wyświetl obraz
# cv2.imshow('bear', img)
# cv2.imshow('logo', logo)

# wyciecie obszaru z obrazu
rows, cols, channels = logo.shape
roi = img[:rows, :cols]
#cv2.imshow('roi', roi)

gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray', gray)

# maska
mask = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)[1]

# maska odwrotna
mask_inv = cv2.bitwise_not(mask)
#cv2.imshow('mask_inv', mask_inv)

# czarny obraz
black = cv2.bitwise_and(roi, roi, mask=mask_inv)
#cv2.imshow('black', black)

img_bg = cv2.bitwise_and(roi, roi, mask=mask)
logo_fg = cv2.bitwise_and(logo, logo, mask=mask_inv)
#cv2.imshow('img_bg', img_bg)
#cv2.imshow('logo_fg', logo_fg)

dst = cv2.add(img_bg, logo_fg)
img[:rows, :cols] = dst
cv2.imshow('bear', img) # wyświetl obraz

# czekaj na naciśnięcie klawisza
cv2.waitKey(0)