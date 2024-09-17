import glob
import os
from threading import Thread,Event
import cv2
import time
from emailing import send_email

video = cv2.VideoCapture(0)

time.sleep(1)
first_frame = None
count = 1
status_list = []
email_send_event = Event()

def clean_folder():
    email_send_event.wait()
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)
while True:
    status = 0
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    cv2.imshow("My video", gray_frame_gau)
    if first_frame is None:
        first_frame = gray_frame_gau
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    thresh_frame = cv2.threshold(delta_frame, 70, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 25000:
            continue
        x, y, width, height = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 3)
        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/{count}.png",frame)
            count = count+1
    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[0] == 1 and status_list[1] == 0:
        all_images = glob.glob("images/*.png")
        index = int(len(all_images)/2)
        image_to_send = all_images[index]
        email_send_event.clear()
        email_thread = Thread(target=send_email,args=(image_to_send, ))
        email_thread.daemon = True
        email_thread.start()
        clean_thread = Thread(target=clean_folder,)
        clean_thread.daemon = True
        clean_thread.start()

        email_send_event.set()
        count = 1

    cv2.imshow("My video", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
