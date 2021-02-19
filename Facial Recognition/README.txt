Just for clarity, we are specifying the versions of each software in use here:
Spark - 2.2.1 running on Scala 2.11
Python - 3.7.4
Java 1.8.0_275

In order to install opencv and its associated libraries we faced quite a few issues. The following article was most helpful:
They are all pip installs and hence would download the latest versions by default.

https://www.pyimagesearch.com/2018/05/28/ubuntu-18-04-how-to-install-opencv/

We have run this project on a Virtual box VM running Ubuntu. Ideally it should work on Windows etc without any issues. 

If you plan to use Virtualbox, we should set up the following to attach your laptop's webcam to the image since by default it won't work:
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

NOTE: We could not get cheese working, but we have read its possible to test this via that too.

In order to run the project, we need to get the following setup correctly:
1. /known_people/ : folder parallel to the scripts which has the images of the people to be recognized. The name of the image files will be considered as the name of the people. 
2. update directory path in recognize_face_publish.py since this file takes the images of known people and stores the face embeddings as a Spark output.

