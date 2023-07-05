import pickle 
import cv2 
import numpy as np

with open("imgString.pickle", "rb") as f:
    data = pickle.load(f)


ListOfNumbers = data[2].split(",")


img = np.zeros((int(data[0]),int(data[1]),3), dtype=np.uint8)

print(img)

currRow = 0
currColumn = 0

for pixle in ListOfNumbers:
    
    if pixle == "N":
        currRow+=1
        currColumn = 0
        continue  
    img[currRow, currColumn] = pixle
    currColumn+=1

print("-------------------------")

print(img)


cv2.imshow("something", img)
cv2.waitKey(0)
