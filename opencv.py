font = cv2.FONT_HERSHEY_SIMPLEX
cam = cv2.VideoCapture(0)
cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
cv2.putText(frame, "Press 'C' -> capture image\n q -> Quit", (0, 35),
cv2.imshow("live", frame)
cv2.waitKey(100)
cv2.imwrite(dir_name + "/image," + str(student_id) + "," 