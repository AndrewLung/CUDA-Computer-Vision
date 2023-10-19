In this project, I made a crosswalk button identifier using Haar Cascades by manually collecting hundreds of samples, using a Haar Cascade Trainer GUI, and referring to various resources that I list below to help me set up my image classifiers. I then added cuda acceleration and reported results.

My Youtube Link: https://www.youtube.com/watch?v=_SDN7dNdWJg

Slides: https://docs.google.com/presentation/d/10J6PlTE6XnXadmw0pnQP6C1tOqoNkMiAhJyBqFEAqnc/edit?usp=sharing

Project report included in files.








CREDITS:

Credit for camera module code is found in the .py file. I used various resources for writing the logic for crosswalkDetection.py.

On YouTube, Murtaza's Workshop is a fantastic resource and by far the most helpful to the completion of the project. JetsonHacks is great for learning hardware setup and I also used the videos to help me get image detection rolling when Murtaza's videos weren't enough. I used multiple videos as resources from these creators, so I am crediting their channels as a whole.

For understanding Haar Cascades, I used these videos:
https://www.youtube.com/watch?v=88HdqNDQsEk
https://www.youtube.com/watch?v=ZSqg-fZJ9tQ

Here is the Haar Cascade Trainer GUI I used:
https://amin-ahmadi.com/cascade-trainer-gui/

For porting to GPU, it is a matter of reading existing cuda documentation for C++ then porting it to Python; Python documentation on OpenCV 2 is scarce, so it is better to understand the C++ implementation first. Check this link:
https://learnopencv.com/getting-started-opencv-cuda-module/

For the Python specific functions, check out the official OpenCV website for the Python function equivalents of these C++ implementations.
