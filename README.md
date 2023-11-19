<h1 align="center">OpenCV Hand Gesture Control Things</h1>
<p align="center">
  <img src=".github/media/mediapipe.png" width="550"> 
  <img src=".github/media/PBLogo.png" width="210"> 
  &nbsp;&nbsp;&nbsp;
  <img src=".github/media/VLULogo.png" width="75">
</p>

<p align="center">
  <img src="https://visitor-badge.feriirawann.repl.co?username=pb3002&repo=hand-gesture-control-things-vn-vlu&style=for-the-badge&contentType=svg&color=brightgreen&logo=cbs" />
  
  <a href="https://www.linkedin.com/in/nguyenphuc-mrp/">
    <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white" alt="Linkedin"></a>
  
  <a href="https://www.facebook.com/phuc.2174802010773">
    <img src="https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white" alt="Facebook"></a>
    
  <a href="https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=GTvVlcSHvbQxNwkWrmstDrLfwbmwrCXwrRXtjZqKfkwSpmdJSzBKjlwQhJDNbRZvgskkCpXjnPgKq">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>
  
  <br>
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
  <img src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" />
</p>

## ✅About

This is a personal project and the final project for the Computer Vision course at Van Lang University, which I worked on alone. The project is a software that has 4 functions that can be controlled by hand gestures: light bulb, computer speaker, computer mouse, and fan. 

The project was written in Python language and uses Mediapipe to detect hand gestures.

Here are some important parameters of Mediapipe that we need to pay attention to:

<table>
  <tr>
    <td><code><b>max_num_hands</b></code>: The maximum number of hands can be detected by the GestureRecognizer.</td>
  </tr>
  <tr>
    <td><code><b>min_detection_confidence</b></code>: The minimum confidence score for the hand detection to be considered successful.</td>
  </tr>
  <tr>
    <td><code><b>min_tracking_confidence</b></code>: The minimum confidence score for the hand tracking to be considered successful.</td>
  </tr>
</table>

If you would like to learn more about this project, please refer to the following documents:

- [Vietnamese_Project_Explain]()
- English_Project_Explain

## 📌Requirements

Firstly, to ensure that the program can run smoothly, I recommend that you install these libraries before we begin.

And don’t forget that your computer needs a webcam to be able to use this program! 📷📷

```
pip install pillow 
pip install opencv-python 
pip install mediapipe 
pip install pycaw 
pip install comtypes 
pip install numpy 
pip install pyautogui
```

## 🛠️Installation

After you’ve installed the requirements, you can clone this repository or download it  [<u>here</u>](https://github.com/PB3002/CV-hand-gesture-house-control/archive/refs/heads/main.zip) to your local disk. Then, simply run the `main.py` file to enjoy the program experience. 🎉

## 📙How to use (Program Tutorial)

As you mentioned earlier above, this program includes 4 functions, and each function has a different usage.

### 💡Light Bulb Control (max_num_hands=1):

To control the light bulb function, you need to know that each light bulb corresponds to one of your fingers. When you raise a finger, the light bulb depends on it will turn on, and when you lower that finger, the light bulb will turn off.

**Quy định về đèn như sau:**

| Finger | Light color |
|:------ | -----------:|
| Thumb  | Yellow🟨    |
| Index  | Red 🟥      |
| Middle | Green 🟩    |
| Ring   | Blue 🟦     |
| Pinky  | Orange 🟧   |

📍Example:

<img title="" src="file:///C:/Users/ACER/Downloads/house.png" alt="" width="547" data-align="center">

### 🔊Volume Control (max_num_hands=2):

This function allows you to control the overall sound on your computer. By raising your thumb and index finger, you can increase or decrease the volume according to the distance you create between these two fingers. The farther apart your fingers are, the louder the volume will be, and vice versa.

📍Example:

<img title="" src="file:///C:/Users/ACER/Downloads/house.png" alt="" data-align="center" width="547">

### 🖱️Mouse Control (max_num_hands=1):

When you activate this function, a blue rectangle frame will appear on your webcam. This blue frame represents the resolution of the screen you are using. To control the mouse cursor, simply raise and move your index finger within the frame. And if you want to click the mouse, you can use your middle finger to quickly touch your index finger at the position where you want to click.

📍Example:

<p align="center">
  <img src=".github/media/dance_foot.gif" width="210">
  <img src=".github/media/dance_foot.gif" width="210">
  <br>
  <sup></sup>
</p>

### 𖣘 Fan Control (max_num_hands=1):

For the fan control function, all you need to do is clench your hand to turn off the fan and open all 5 fingers to turn on the fan. (Note: All 5 fingers must be open for the fan to turn on!)

📍Example:

<img title="" src="file:///C:/Users/ACER/Downloads/house.png" alt="" data-align="center" width="547">

## ✍️Author:

Nobody except me! Haha😆😆

As mentioned earlier, this is a project that I worked on alone and learned from many sources on the internet, even using AI. So if you want to support me in developing and creating projects like this, please help me buy some milk 🐮 (I am really addicted to Millo).



## 📝References:

- [Gesture recognition task guide  MediaPipe| Google for Developers|](https://developers.google.com/mediapipe/solutions/vision/gesture_recognizer)

- [mediapipe/docs/solutions/hands.md at master · google/mediapipe · GitHub](https://github.com/google/mediapipe/blob/master/docs/solutions/hands.md)

- [Nhận diện chuyển động cử chỉ bàn tay với OpenCV - Hand Tracking](https://ngoton.it/nhan-dien-chuyen-dong-cu-chi-ban-tay-voi-opencv-hand-tracking/)

- [AI Virtual Mouse](https://www.youtube.com/watch?v=8gPONnGIPgw&t=267s)

- [Mouse and keyboard automation using Python - GeeksforGeeks](https://www.geeksforgeeks.org/mouse-keyboard-automation-using-python/)

- [Distinguish Between Right and Left Hands in MediaPipe](https://toptechboy.com/distinguish-between-right-and-left-hands-in-mediapipe/)

- [How to show webcam in TkInter Window - Python - GeeksforGeeks](https://www.geeksforgeeks.org/how-to-show-webcam-in-tkinter-window-python/)

- [How to controll LED| OpenCV Python l](https://www.youtube.com/watch?v=fwMjVZhM08s&t=253s) 
