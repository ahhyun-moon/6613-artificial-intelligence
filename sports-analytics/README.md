# Sports Analytics
# Task 1: Deep-SORT (40 points)

## 1. (10 poiints) Draw the architecture of the tracking solution using a diagraming tool of your choice that is compatible to Github rendering.
<img src="https://github.com/ahhyun-moon/cs-gy-6613-assignments/blob/main/sports-analytics/sports_analytics_diagram.drawio.png">

## 2. (30 points) Write a summary of key components of the architecture above including the equations of the Kalman filter and explain what the Hungarian Algorithm will do .

### **Faster RCNN (Detection):**

In this assignment, we adopt Faster RCNN pretrained with COCO dataset. Faster R-CNN model finds bounding boxes containing objects such that each bounding box has only one object. Then, it classifies the image inside each bounding box and assign it a label with confidence score.

### **Kalman Filter (Estimation):**

The Kalman Filter operates in a “predict-correct” loop.  It estimates/predicts the position of the target in the next frame using a constant velocity model. When a detection is associated with a target, the detected bounding box is used to update/correct the target state. If no detection is associated with the target, its state is simply predicted without correct using the Linear velocity model.

The equations of Kalman filter are divided into two groups: the time update equations also called the prediction equations and measurement update equations can be thought of also as the correction equations.

The time update equations are responsible for projecting forward the current state and error covariance estimates to obtain the a priori estimates for the next time step. The measurement update equations are responsible for improving the a posteriori estimate by incorporating a new measurement into the a priori estimate.

<img src="https://github.com/ahhyun-moon/cs-gy-6613-assignments/blob/main/sports-analytics/sports_analytics_kalman.drawio.png" width=700>

### **Deep SORT:**

Deep SORT tracks objects based on the velocity and motion of the object, plus the appearance of the object. 
Appearance is a single feature vector, waiting to be classified. This feature vector is known as the appearance descriptor. 
We use Mahalanobis distance for Measurement-to-track association, which is the process of determining the relation between a measurement and an existing track.  

### **Hungarian Algorithm (Association):**
The Hungarian Algorithm is a solution for the assignment problem, or maximum/minimum-weighted bipartite matching problem.
In assigning detections to existing targets, each target’s bounding box geometry is estimated by predicting its new location in the latest frame. The assignment cost matrix is then computed as the intersection-over-union (IOU) distance between each detection and all predicted bounding boxes from the existing targets. If the IOU of detection and target is less than a certain threshold value called IOUmin then that assignment is rejected. This technique solves the occlusion problem and helps maintain the IDs.


# Task2: Deep-SORT Implementation (50 points)
## Source Code in Colab: 
https://colab.research.google.com/drive/1SqbJs_lGJBwzQR-f22RfsNh5Vy-JtFw2?usp=sharing
## Result video is available online via G-Drive: 
https://drive.google.com/file/d/1FNqUBFfYgpNjSzb6y55O9TISjCfiuhkd/view?usp=sharing
## Or can be downloaded from the github page: 
https://github.com/ahhyun-moon/cs-gy-6613-assignments/blob/main/sports-analytics/result_video.mp4


# Task 3: Critique (10 points)
There are three possible improvements to the solution. 

**1. Overlapping Issue**

<img src="https://github.com/ahhyun-moon/cs-gy-6613-assignments/blob/main/sports-analytics/critique1.png" width=600>
- When two objects are overlapped (in this case the soccer players), currrent solution mistakenly detects and tracks as a single person. 

**2. ID Update** 

<img src="https://github.com/ahhyun-moon/cs-gy-6613-assignments/blob/main/sports-analytics/critique2.png" width=600>
- In one of the later frames, we can see the IDs are much larger numbers compared to the beginning. We can assume that the solution could be losing objects' identities in the process of tracking and generating new IDs for the objects.
- This is possibly due to the camera angles keep zooming in/out and changing angles. 

**3. Ball Tracking**

<img src="https://github.com/ahhyun-moon/cs-gy-6613-assignments/blob/main/sports-analytics/critique4.png" width=600>
<img src="https://github.com/ahhyun-moon/cs-gy-6613-assignments/blob/main/sports-analytics/critique3.png" width=600>
- Compared to the detection when camera is zoomed in (shown in the first screenshot above), ball detecting and tracking is not consistant when zoomed out(shown in the second screenshot above).  
