Version of software used:
Spark - 2.2.1 running on Scala 2.11
Python - 3.7.4
Java 1.8.0_275


This project was run on Virtual box VM running Ubuntu. However, you should be able to work with it on Windows as well without issues.

If you're using Virtualbox, please follow the steps enlisted below to attach your laptop's webcam to the image:
1. Download the virtualbox extension pack for the virtual box version you are using.
2. Click Preferances on Virtualbox window and browse to the folder where the downloaded file is present. Installation proceeds after that.
3. On your VM image, click Settings -> USB -> USB 2.0 -> Add a filter for the webcam device on your machine
4. Launch the VM and click Devices->Webcams->Integrated Camera. If this does not show up, there was something wrong in your setup and needs to be corrected. Another thing you can try is going to command line and typing:
	cd <Path to Oracle/VirtualBox/ folder>
	VBoxManage list webcams
	VBoxManage controlvm <VM_IMAGE_NAME> webcam attach <ALIAS NUMBER FOR WEBCAM>
Details are at: https://docs.oracle.com/en/virtualization/virtualbox/6.0/admin/webcam-passthrough.html

Test with following:
sudo apt-get install luvcview
sudo apt-get install guvcview

sudo apt-get install guvcview

To test webcam:
fswebcam <filename.jpg>
eog <filename.jpg>

This should show you the webcam image captured. 

In order to run this project, the following must be set up correctly:
1. /known_people/ : folder parallel to the scripts which has the images of the people to be recognized. The name of the image files will be considered as the name of the people. 
2. update directory path in recognize_face_publish.py since this file takes the images of known people and stores the face embeddings as a Spark output.

