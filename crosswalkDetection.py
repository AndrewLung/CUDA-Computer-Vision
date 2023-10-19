import cv2
import time

#print(cv2.__version__)
#print(cv2.getBuildInformation())

frameWidth = 1440
frameHeight = 900

#USED https://github.com/JetsonHacksNano/CSI-Camera AS REFERENCE
#Pipeline is necessary to boot up camera module using code for my SainSmart IMX219 Camera
#I tried accessing dev/0 to directly access my camera module and it does not work
#Depending on the camera module, you may have to take this approach w/ pipeline

def gstreamer_pipeline(
    #CHANGE VARIABLES DEPENDING ON YOUR CAMERA
    sensor_id=0,
    capture_width=1440,
    capture_height=900,
    display_width=1440,
    display_height=900,
    framerate=30,
    flip_method=0,
):
    return (
        "nvarguscamerasrc sensor-id=%d !"
        "video/x-raw(memory:NVMM), width=(int)%d, height=(int)%d, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            sensor_id,
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
cascade = cv2.cuda_CascadeClassifier.create("classifier/cascade.xml")

while True:
    #Converts to grayscale -- prerequisite to using Haar Cascades
    #Grayscale conversion done using GPU instead of CPU
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    start = time.time()
    cuFrame = cv2.cuda_GpuMat(gray)

    #Uses Haar Cascade to determine if object is detected
    crosswalkDetect = cascade.detectMultiScale(cuFrame).download()

    if crosswalkDetect is not None:
        for (x, y, w, h) in crosswalkDetect[0]:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    end = time.time()
    print(end - start)
    cv2.imshow("Result", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break