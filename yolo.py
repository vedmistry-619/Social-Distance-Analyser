import cv2
import argparse
import numpy as np

# handle command line arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True,
                help = 'path to input image')
ap.add_argument('-c', '--config', required=True,
                help = 'path to yolo config file')
ap.add_argument('-w', '--weights', required=True,
                help = 'path to yolo pre-trained weights')
ap.add_argument('-cl', '--classes', required=True,
                help = 'path to text file containing class names')
args = ap.parse_args()

#READ INPUT
#image = cv2.imread(args.image)
vid = cv2.VideoCapture('video.mp4')
while vid.isOpened():
    (rval, image) = vid.read()

    Width = image.shape[1]
    Height = image.shape[0]
    scale = 0.00392

    # READ ALL OUTPUT CLASSES PREDICATBLE
    classes = None
    with open(args.classes, 'r') as f:
        classes = [line.strip() for line in f.readlines()]

    # GENERATE COLOR FOR CLASSES WE LATERON CHANGE THIS PIECE OF CODE 
    COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

    # read pre-trained model and config file
    net = cv2.dnn.readNet(args.weights, args.config)
    blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)
    net.setInput(blob)

    # function to get the output layer names 
    def get_output_layers(net):
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
        return output_layers

    # MAKE BOUNDING BOX
    def draw_bounding_box(img, class_id, confidence, x, y, x_plus_w, y_plus_h):
        label = str(classes[class_id])
        color = COLORS[class_id]
        cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)
        #cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    #RUN AND GET RESULTS
    outs = net.forward(get_output_layers(net))

    # initialization
    class_ids = []
    confidences = []
    boxes = []
    conf_threshold = 0.5 #CHANGE THIS IF TOO MANY DETECTIONS
    nms_threshold = 0.6 #BETTER UNCHANGED

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * Width)
                center_y = int(detection[1] * Height)
                w = int(detection[2] * Width)
                h = int(detection[3] * Height)
                x = center_x - w / 2
                y = center_y - h / 2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

    # go through the detections remaining
    # after nms and draw bounding box
    for i in indices:
        i = i[0]
        box = boxes[i]
        x = box[0]
        y = box[1]
        w = box[2]
        h = box[3]
        
        draw_bounding_box(image, class_ids[i], confidences[i], round(x), round(y), round(x+w), round(y+h))
    cv2.imshow("Results", image)
    if cv2.waitKey(1) == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
#python yolo.py --image video.mp4 --config yolov3.cfg --weights yolov3.weights --class yolov3.txt
#python yolo.py --image video.mp4 --config yolov3-tiny.cfg --weights yolov3-tiny.weights --class yolov3.txt