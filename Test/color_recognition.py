#https://pysource.com/2021/10/19/simple-color-recognition-with-opencv-and-python/
import cv2


img = cv2.imread('red.jpg')
print(img)
cv2.imshow("img", img)
cv2.waitKey(0)

# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


# _, frame = img.read()
# hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# height, width, _ = frame.shape

# cx = int(width / 2)
# cy = int(height / 2)

# # Pick pixel value
# pixel_center = hsv_frame[cx, cy]

# h_value = pixel_center[0]
# s_value = pixel_center[1]
# v_value = pixel_center[2]
# # print(h_value, s_value, v_value)
# print(pixel_center)

# color = "Undefined"

# if s_value < 30:
#     color = "WHITE"
# elif v_value < 20:
#     color = "BLACK"
# elif h_value < 5:
#     color = "RED"
# elif h_value < 22:
#     color = "ORANGE"
# elif h_value < 33:
#     color = "YELLOW"
# elif h_value < 78:
#     color = "GREEN"
# elif h_value < 131:
#     color = "BLUE"
# elif h_value < 170:
#     color = "VIOLET"
# else:
#     color = "RED"
    
# print(color)
    

# pixel_center_bgr = frame[cy, cx]
# b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

# cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
# cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
# cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

# cv2.imshow("Frame", frame)
# key = cv2.waitKey(1)

# cap.release()
# cv2.destroyAllWindows()