# Sports Analytics
# Task 1: Deep-SORT (40 points)

## 1. (10 poiints) Draw the architecture of the tracking solution using a diagraming tool of your choice that is compatible to Github rendering.
<img src="https://github.com/ahhyun-moon/cs-gy-6613-assignments/blob/main/sports-analytics/sports_analytics_diagram.drawio.png">

## 2. (30 points) Write a summary of key components of the architecture above including the equations of the Kalman filter and explain what the Hungarian Algorithm will do .

### **Faster RCNN (Detection):**

Pretrained with COCO dataset, Faster R-CNN model finds bounding boxes containing objects such that each bounding box has only one object. Then, it classifies the image inside each bounding box and assign it a label with confidence score.

### **Kalman Filter (Estimation):**

The Kalman Filter operates in a “predict-correct” loop.  It estimates/predicts the position of the target in the next frame using a constant velocity model. When a detection is associated with a target, the detected bounding box is used to update/correct the target state.
<img src="https://github.com/ahhyun-moon/cs-gy-6613-assignments/blob/main/sports-analytics/sports_analytics_kalman.drawio.png" width=700>

### **Deep SORT:**

Deep SORT tracks objects based on the velocity and motion of the object, plus the appearance of the object. 
Appearance is a single feature vector, waiting to be classified. This feature vector is known as the appearance descriptor. 
We use Mahalanobis distance for Measurement-to-track association, which is the process of determining the relation between a measurement and an existing track.  

### **Hungarian Algorithm (Association):**
The Hungarian Algorithm is a solution for the assignment problem, or maximum/minimum-weighted bipartite matching problem.
A cost matrix is computed as the intersection-over-union (IOU) distance between each detection and all predicted bounding boxes from the existing targets. The assignment is solved optimally using the Hungarian algorithm. If the IOU of detection and target is less than a certain threshold value called IOUmin then that assignment is rejected. This technique solves the occlusion problem and helps maintain the IDs.


# Task2: Deep-SORT Implementation (50 points)
## Source Code in Colab: 
https://colab.research.google.com/drive/1SqbJs_lGJBwzQR-f22RfsNh5Vy-JtFw2?usp=sharing
## Result video is available online via G-Drive: 
https://drive.google.com/file/d/1FNqUBFfYgpNjSzb6y55O9TISjCfiuhkd/view?usp=sharing
## Or can be downloaded from the github page: 
https://github.com/ahhyun-moon/cs-gy-6613-assignments/blob/main/sports-analytics/result_video.mp4


# Task 3: Critique (10 points)
