Motion Detection and Email Alert System

This project is a simple motion detection system that uses a webcam to capture video, detect motion, and send an email alert with an image when motion is detected. After the email is sent, the system automatically cleans up the saved images. The system runs smoothly without blocking the video feed by using multi-threading.

Features

	•	Detects motion using a webcam feed.
	•	Saves a snapshot when motion is detected.
	•	Sends an email alert with the captured image.
	•	Cleans up saved images after the email is sent.
	•	Uses multi-threading to avoid lag in video processing.

Prerequisites

To run this project, you need to have the following installed:

	•	Python 3.x
	•	OpenCV (cv2 module)
	•	Threading (part of the Python Standard Library)
	•	Glob (part of the Python Standard Library)

Installation

	1.	Clone this repository to your local machine:
    2.	Install the required Python packages:
	3.	Make sure the emailing.py module is correctly set up to handle sending emails using your preferred email service. This file should include your email credentials and any necessary configurations for sending emails.
    4.  Make sure images directory exist 
Usage

	1.	Run the script:
    2.	The program will:
        •	Start your webcam.
        •	Detect motion and highlight the moving objects.
        •	Save an image when motion is detected.
        •	Send an email with the saved image.
        •	Clean up the saved images after sending the email.
	3.	To stop the program, press the q key in the video window.

How It Works

	•	Motion Detection: The system captures frames from the webcam and converts them to grayscale. It applies Gaussian blur to reduce noise and detects changes in frames by comparing the current frame to the first frame.
	•	Email Alert: When motion is detected, an image is saved and sent as an email attachment.
	•	Threading: The email sending and folder cleaning processes are done in separate threads to ensure the video feed runs smoothly without lag.

Customization

	•	Adjust Motion Sensitivity: You can adjust the sensitivity of motion detection by changing the contour area threshold (currently set to 25000) in the code. Lower the value for higher sensitivity.
	•	Change Email Settings: Modify the send_email function in the emailing.py file to use your own email account for sending alerts.

Contributing

Feel free to submit issues or pull requests to improve the project.

