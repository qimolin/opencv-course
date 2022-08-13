import cv2 as cv

# Reading image
img = cv.imread('photos/cat_large.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)

# Reading video
capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    if isTrue:
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()
