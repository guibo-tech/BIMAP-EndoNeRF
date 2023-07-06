import cv2
import os

def vid2frames(video,fps=3):
        
    vidcap = cv2.VideoCapture(video)
    success, image = vidcap.read()
    count = 0
    os.mkdir('./frames')
    os.chdir('./frames')


    frame_rate = vidcap.get(cv2.CAP_PROP_FPS)
    frame_delay = int(frame_rate / fps)
    frame_counter = 0

    while success:
        if frame_counter % frame_delay == 0:
            # Apply unsharp mask filter
            blurred = cv2.GaussianBlur(image, (0, 0), 2)
            sharpened_image = cv2.addWeighted(image, 1.5, blurred, -0.5, 0)

            cv2.imwrite("frame%d.jpg" % count, sharpened_image)
            print('Read a new frame:', success)
            count += 1

        success, image = vidcap.read()
        frame_counter += 1
