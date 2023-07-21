import cv2
import os
import argparse
import numpy as np
import sys


def vid2frames(video, fps, start_time, end_time):
    # Create a VideoCapture object
    vidcap = cv2.VideoCapture(video)

    # Check if the video was opened successfully
    if not vidcap.isOpened():
        print("Error opening video file:", video)
        return
    
    video_fps = int(vidcap.get(cv2.CAP_PROP_FPS))
    max_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Set the starting and ending time if provided
    if start_time is not None and end_time is not None:
        # Calculate the frame indices corresponding to the start and end time
        start_frame = int(start_time * video_fps)
        end_frame = int(end_time * video_fps)
        max_frames = (end_time-start_time)*fps

        # Set the current frame position to the start frame
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    success, image = vidcap.read()

    # Check if the first frame was read successfully
    if not success:
        print("Error reading video frame")
        vidcap.release()
        return

    mask = np.zeros_like(image[:, :, 0])
    # Set non-zero pixels in the mask for the label region
    x1, y1 = 40, 30  # Left upper corner
    x2, y2 = 245, 30  # Right upper corner
    x3, y3 = 40, 75  # Left lower corner
    x4, y4 = 245, 75  # Right lower corner
    mask[y1:y3 + 1, x1:x2 + 1] = 255

    count = 0
    directory = './images'

    if not os.path.exists(directory):
        os.mkdir(directory)
    else:
        overwrite = input("The files in folder images will be overwritten. Do you want to continue? (y/n) ")
        if overwrite.lower() == 'n':
            sys.exit()
        if overwrite.lower() == 'y':
            # Get the list of files in the folder
            file_list = os.listdir(directory)
            # Iterate over the files and remove them
            for file_name in file_list:
                file_path = os.path.join(directory, file_name)
                os.remove(file_path)

    os.chdir(directory)

    frame_delay = int(video_fps / fps)
    frame_counter = 0

    while success:
        # If start_frame is provided, skip frames until reaching start_frame
        if start_time is not None and end_time is not None and frame_counter < start_frame:
            success, image = vidcap.read()

        # If end_frame is provided, break the loop if reached
        if end_time is not None and frame_counter > end_frame:
            break
        
        # Process frames at the specified fps
        if frame_counter % frame_delay == 0 and count <= max_frames:
            # Remove label through inpainting
            img_inpaint = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)

            # Apply unsharp mask filter
            blurred = cv2.GaussianBlur(img_inpaint, (0, 0), 2)
            sharpened_image = cv2.addWeighted(img_inpaint, 1.5, blurred, -0.5, 0)

            cv2.imwrite("frame%d.png" % count, sharpened_image)
            print('Read a new frame:', success)
            count += 1

        success, image = vidcap.read()
        frame_counter += 1

    # Release the VideoCapture object
    vidcap.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--video_path',
                        default=None,
                        type=str,
                        required=True,
                        help='Path to input video'
                        )

    parser.add_argument('--fps',
                        default=3,
                        type=int,
                        required=False,
                        help='How many frames per seconds are captured from the video'
                        )

    parser.add_argument('--start_time',
                        default=None,
                        type=int,
                        required=False,
                        help='Start point in seconds of the interval to be reconstructed'
                        )
    parser.add_argument('--end_time',
                        default=None,
                        type=int,
                        required=False,
                        help='End point in seconds of the interval to be reconstructed'
                        )

    parser.set_defaults(optimize=False)

    args = parser.parse_args()


    vid2frames(args.video_path, args.fps, args.start_time, args.end_time)
