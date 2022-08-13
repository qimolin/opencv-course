import cv2 as cv

img = cv.imread('photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

treshold, thresh = cv.threshold(gray, 200, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

treshold, thresh_inv = cv.threshold(gray, 200, 255, cv.THRESH_BINARY_INV)
cv.imshow('Inverse Thresholded', thresh_inv)

adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('Adeptive Thresholded', adaptive_thresh)

cv.waitKey(0)
