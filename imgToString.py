import cv2
import pickle 

# reading as black and white
image = cv2.imread("img.jpg", cv2.IMREAD_GRAYSCALE)

finalString = ""
finalList = []

copyOfImage = image.copy()

height, width = copyOfImage.shape

# arr = np.array([None] * (height * width))

resizedImage = cv2.resize(image, (1000, int((height * 1000)/width)))

newHight, newWidth = resizedImage.shape


# looping through every pixle in the image and reading the value of it... then sava it to the String 
for i in range(0, newHight):             #looping at python speed...
   # adding all pixles values to the list 
   for j in range(0, newWidth):
      finalList.append(resizedImage[i, j])
      # finalString += str(resizedImage[i, j]) + "|"
   # adding a element to know when the row has ended and a new Line (N) has started
   finalList.append("N")


# print(",".join(str(v) for v in finalList))

print(type(",".join(str(v) for v in finalList)))

finalData = [newHight, newWidth, ",".join(str(v) for v in finalList)]

with open("imgString.pickle", "wb") as f:
   pickle.dump(finalData, f)

print("done")
cv2.imshow("somthing", resizedImage)
cv2.waitKey(0)

