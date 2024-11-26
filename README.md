This project focuses on the object detection task to identify video frames where a name tag is present. The goal was to draw bounding boxes around the name tags using the YOLOv5 model, which is well-suited for detecting small objects.

The dataset used in this project was annotated and generated using Roboflow, which can be accessed in the following link:

[Roboflow dataset](https://app.roboflow.com/testing-zbrbk/aaa-mtikj/2)

The PyTorch-YOLOv5 model was implemented based on the official YOLOv5 repository. For more information on how to use and implement YOLOv5, visit the official GitHub:

[YOLOv5](https://github.com/ultralytics/yolov5)

Here are some examples of the detection predictions using YOLOv5:

<img src="https://github.com/MPYong/object_detection/blob/main/Sample/Sample_1.jpg?raw=true" width="600" />

<img src="https://github.com/MPYong/object_detection/blob/main/Sample/Sample_2.jpg?raw=true" width="600" />

Through this project, I gained a better understanding of object detection tasks, particularly:

* Labeling and annotating datasets for object detection.
* Understanding the requirements for training models on specific tasks.
* Identifying suitable models for small object detection, such as YOLOv5.
