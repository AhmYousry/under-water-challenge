import cv2
import numpy as np

video = cv2.VideoCapture('line tracking.mp4')

flag = 0
count = 0
#img = cv2.imread("1.jpg")
while True:
    ret, img = video.read()

    kernal = np.ones((5, 5), "uint8")
    #gaussianBlurKernel = np.array(([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]), np.float32)
    gaussianBlurKernel = np.array(([[1, 2, 1], [2, 3, 4], [1, 2, 3]]), np.float32) / 9
    #gaussianBlurKernel = np.array([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]])

    gaussianBlur = cv2.filter2D(src=img, kernel=gaussianBlurKernel, ddepth=-1)

    sepia_img = cv2.transform(img, gaussianBlurKernel)



    normalizedImg = np.zeros((img.shape[0], img.shape[1]))
    normalizedImg = cv2.normalize(gaussianBlur,  normalizedImg, 0, 50, cv2.NORM_MINMAX)

    img_hsv = cv2.cvtColor(normalizedImg, cv2.COLOR_RGB2HSV)

    lower_blue = np.array([30, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(img_hsv, lower_blue, upper_blue)

    #blue_mask = cv2.dilate(mask, kernal)

    thresh = cv2.threshold(mask, 20, 250, cv2.THRESH_BINARY_INV)[1]

    blue_mask = cv2.dilate(thresh, kernal)

    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 12))

    detect_vertical = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, vertical_kernel, iterations=2)

    lines = cv2.HoughLinesP(detect_vertical, 2, np.pi / 180, 100, minLineLength=210, maxLineGap=20)


    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            




    #cv2.imshow('dst_rt', normalizedImg)
    cv2.imshow("image", img)
    #cv2.imshow("dilate", blue_mask)
    #cv2.imshow("thresh", thresh)
    #cv2.imshow("mask", mask)
    key = cv2.waitKey(10)
    if key == 27:
        break
        video.release()
        cv2.destroyAllWindows()
