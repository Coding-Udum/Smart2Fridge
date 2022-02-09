# import libraries
import cv2
import numpy
import time 
import os 

pictureTaken = False 



def openedBehavior(): #Methode definiert Verhalten wenn Kühlschrank geöffnet. 
    global pictureTaken
    print("Fridge is open")
    time.sleep(3) # this line creates a 5 second delay before repeating the loop
    if not pictureTaken:
        os.system('fswebcam -r 1280x720 -S 3 --jpeg 50 --save /home/pi/tflite1/content.jpg') # uses Fswebcam to take picture
        os.system('fswebcam -r 1280x720 -S 3 --jpeg 50 --save /var/www/html/content.jpg') # uses Fswebcam to take picture
        os.system('python3 TFLite_detection_image.py --modeldir=Sample_TF_Lite_Model')
        pictureTaken = True


def closedBehavior(): #Methode definiert Verhalten wenn Kühlschrank geschlossen. 
    global pictureTaken
    print("Fridge is closed")
   
    time.sleep(1) # this line creates a 1 second delay before repeating the loop
    pictureTaken = False

def checkOpen(): #Metode prüft ob Kühlschrank geöffnet
    print("checking open")
    os.system('fswebcam -r 320x240 -S 3 --jpeg 50 --save /home/pi/tflite1/status.jpg') # uses Fswebcam to take small picture
    myimg1 = cv2.imread('status.jpg')
    avg_color_per_row1 = numpy.average(myimg1, axis=0)
    avg_color1 = numpy.average(avg_color_per_row1, axis=0)
    statusOpen = (numpy.sum(avg_color1)>150) #Wenn durchschnittlicher RGB Wert summiert kleiner als 150 ist, ist der Kühlschrank geschlossen. Also statusOpen = false. Wenn über 150 statusOpen = true
    
    return statusOpen





while True: # Dauerschleife
    
    
    if checkOpen(): openedBehavior()
    else: closedBehavior()
        
    

   

 
    


