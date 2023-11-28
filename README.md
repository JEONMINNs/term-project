# [Project Overview] 👋

---
## "PUBLIC MASK (Public Mask) "
---




These days, video media such as YouTube and TikTok are very popular, there are many cases where passers-by are taken **recklessly.
In particular, in the case of outdoor filming, there are many cases where ordinary citizens are not mosaic, resulting in a series of damage.**

**In the end...**




## "We developed a mask that protects their faces."



#### [Order]
1. First, it senses the face and eyes through the camera.
2. After converting this to gray scale, face coordinates are calculated.
3. Mosaic the surrounding area of the face except for the eyes.
4. Display the results.
---




### Let's protect citizens' right to portrait through PUBLIC MASK!

---

![example](https://github.com/leeeul033/git-practice/assets/144300261/3932005a-32e5-4bcb-ab52-5c3f22dc4e14)

*Photographic sources : MOTIONLAB , (https://www.motionlab.co.kr/TUTORIAL/?q=YToyOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjtzOjQ6InBhZ2UiO2k6Mjt9&bmode=view&idx=12718622&t=board&category=0eC5Bl8r3K)*




### Let's protect citizens' right to portrait through PUBLIC MASK!

---
## How to implement it
---
#### 1. Install a library
 You must install the cv2 and dlib libraries used by the code. You can install it using the commands below.
> pip install opencv-python
> pip install dlib
#### 2. Download **shape_predictor_68_face_landmarks.dat**
 You can download it http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
 After downloading, unzip it, place it in the same directory as the script, or specify the file path directly to the script.  

#### 3. Check webcam
 The code uses the default camera (cv2.VideoCapture(0)). Make sure the webcam is working properly.
#### 4. Run code
Run code using idle. Running opens the opencv window and presses 'q' to end.

---
## Version Requirements(with versions we tested on)
---
 1. python(3,11)
 2. opencv(4.8.1)
 3. numpy(1.26.2)
