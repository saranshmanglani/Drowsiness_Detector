# Drowsiness_Detector
A system that can automatically detect driver drowsiness in a real-time video stream and then trigger an alarm if the driver appears to be drowsy.

## Proposed Work
->A device with a video camera placed inside the car is continuously filming the driver’s face during the ride.  
->A detection system analyses the video frame by frame and determines whether the driver’s eyes are open or shut.  
->If the eyes are shut for more than 1/4 a second (longer than a normal blink period) then the system sets the alarm on to alert the
driver.

## Implementation
->A frame is extracted from the video.  
->It is then converted to gray scale.  
->A face is detected in the frame.  
->The facial landmarks are predicted on the detected face.  
->A threshold value is set to 20 for consecutive frames and 6.5 for average distance.  
->The Euclidean Distance is calculated between the 4 landmark points of the eyes.  
->Average Distance is Calculated.  
->If the average distance is less than the threshold value i.e. 6.5, for more than 20 consecutive frames, the alarm is triggered.

## Tools Required
->Arduino  
->Camera  
->Buzzer/Alarm  
->MicroSD Card  

### Note:
->Download "shape_predictor_68_face_landmarks.dat" and put it in the main directory which contains the code file. 
->Wearing glasses (of any kind) cause the system to fail.
