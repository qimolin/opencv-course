import cv2 as cv

img = cv.imread('photos/cat_large.jpg')
cv.imshow('Cat', img)


def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

cv.waitKey(0)


def changeRes(width, height):
    # Live video res change
    capture.set(3, width)
    capture.set(4, height)


# Reading video
capture = cv.VideoCapture('videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    if isTrue:
        cv.imshow('Video', frame)
        cv.imshow('Video Resized', frame_resized)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    else:
        break
