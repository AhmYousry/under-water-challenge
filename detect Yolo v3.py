from imageai.Detection.Custom import CustomObjectDetection
import cv2


def detect(input_image, output_image):
    detector = CustomObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath("detection_model-ex-025--loss-0016.213.h5")
    detector.setJsonPath("detection_config (1).json")
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=input_image, output_image_path="Star-detected.jpg")
    for detection in detections:
        print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])

    return output_image



image = detect(input_image, output_image)

cv2.imshow("image", image)
cv2.waitKey(0)

