import cv2
import time
import numpy as np

confidence = 0.6
Nms= 0.3
class_names = []
with open("coco.names", "r") as f:
  class_names = [cname.strip() for cname in f.readlines()]

img = cv2.imread("image.jpg")

# Load model
net = cv2.dnn.readNet("yolov4.weights","yolov4.cfg")
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416,416), scale=1/255, swapRB=True)

start = time.time()
classes, scores, boxes = model.detect(img, confidence, Nms)
end = time.time()
fps = 1/(end-start)

for (classid, score, box) in zip(classes, scores, boxes):

  # Only keep detections with class person
  if classid == 0:

    if isinstance(score, (list, np.ndarray)):
      score_value = score[0]
    else:
      score_value = score

    label = "%s : %.2f" % (class_names[classid], score_value)

    cv2.rectangle(img,box,color=(0, 255, 0),thickness=2)
    cv2.putText(img, label, (box[0],box[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

cv2.putText(img, "FPS: %.2f" % fps, (20,25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

cv2.imshow("output", img)
cv2.waitKey(0)