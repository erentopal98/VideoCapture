import cv2

# Get video duration in seconds from user
duration = int(input("Enter video duration (in seconds): "))

# Get video file name from user
file_name = input("Enter video file name (with extension): ")

# We use the VideoCapture class to turn on the camera. Start video capture
cap = cv2.VideoCapture(0)

# The VideoWriter class is used to save the file. Define the codec and create a video writer object
#The *'XVID' argument passed to the function is a shorthand for the string 'XVID', which is a specific codec that is supported by OpenCV.
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#It is the number of frames per second (FPS) for the video, which is set to 20.0.
#It is the size of the video frame, which is set to (640, 480), representing a width of 640 pixels and a height of 480 pixels
out = cv2.VideoWriter(file_name, fourcc, 20.0, (640, 480))

# Start capturing video

#is used to get the current time in "ticks" at the start of the video capture.
start_time = cv2.getTickCount()

#loop calculates the elapsed time in seconds by subtracting the start time from the current time and dividing by the number of ticks per second
while(int((cv2.getTickCount() - start_time)/cv2.getTickFrequency()) < duration):
    #captures a video frame from the camera
    ret, frame = cap.read()
    #The read() method returns a boolean value indicating whether the frame was successfully captured


    if ret==True:
        #If the frame was successfully captured, the code writes the frame to the video file using out.write(frame).
        out.write(frame)

        #It displays the frame in a window
        cv2.imshow('frame', frame)

        #If the user presses the 'q' key, the loop breaks and the video capture stops
        #If the ret value is false, meaning the frame is not captured, the loop also breaks
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# If job is finished, release everything
cap.release()
out.release()
cv2.destroyAllWindows()
#Your video file has been saved alongside your project files



