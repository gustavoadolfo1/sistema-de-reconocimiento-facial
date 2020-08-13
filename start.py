def start():
    def save_att(student_id, name_student):
        d = datetime.date.today()
        now = datetime.datetime.utcnow()
        ids = []
        currentDT = datetime.datetime.now()
        dateshow = currentDT.strftime("%H")
        minuteshow = currentDT.strftime("%M")
        intdate = int(dateshow)
        date = currentDT.strftime("%I:%M:%S")

        event = ['morning','envening']
        """datefile =(int(d.strftime("%d")) - 1)
        d_m_file_name = d.strftime(datefile+"_%B_" + event[0] + ".csv")
        d_e_file_name = d.strftime(datefile + "_%B_" + event[1] + ".csv")
        print("d_m_file_name  " + d_m_file_name)
        print("d_m_file_name  " + d_e_file_name)"""
        #os.remove(d_m_file_name)
        #os.remove(d_e_file_name)
        if intdate < 14:
            file_name = d.strftime("%d_%B_" + event[0] + ".csv")
        elif(intdate >=14):
            file_name = d.strftime("%d_%B_" + event[1] + ".csv")
            try:
                with open(file_name, 'r+') as file_data:
                    file_data.seek(0)
                    for line in file_data:
                        id, name, state, dt = line.split(",")
                        ids.append(int(id))
                    if student_id not in ids:
                        print("not present")
                        update1 = currentDT.strftime('%H:%M:%S')
                        eveningtime = '00:00:00'
                        updateid=str(student_id)
                        updatedate=currentDT.strftime('%Y-%m-%d')
                        hk = mycourse.execute("SELECT name FROM students where id=%s and date=%s ",(updateid,updatedate))
                        if hk == 1:
                            mycourse.execute("UPDATE students SET evening=%s  WHERE evening =%s", (update1, eveningtime))
                            mydb.commit()
                            print(mycourse.rowcount, "record(s) affected")
                        else:
                            sql = "INSERT INTO students (id,name,present,date,morning,evening) VALUES (%s, %s, %s, %s, %s, %s)"
                            val = (str(student_id), name_student, "p", currentDT.strftime('%Y-%m-%d'), "00:00:00",
                                   currentDT.strftime('%H:%M:%S'))
                            mycourse.execute(sql, val)
                            mydb.commit()
                        file_data.write(str(student_id) + "," + name_student + ",p," + date + "\n")
                        file_data.seek(0)
                        playsound('audio.mp3')
                        print("marked", name_student, "present")
            except FileNotFoundError:
                with open(file_name, 'w') as file_data:
                    print(date)
                    update1 = currentDT.strftime('%H:%M:%S')
                    eveningtime = '00:00:00'
                    updateid = str(student_id)
                    updatedate = currentDT.strftime('%Y-%m-%d')
                    hk = mycourse.execute("SELECT name FROM students where id=%s and date=%s ", (updateid, updatedate))
                    if hk == 1:
                        mycourse.execute("UPDATE students SET evening=%s  WHERE evening =%s", (update1, eveningtime))
                        mydb.commit()
                        print(mycourse.rowcount, "record(s) affected")
                    else:
                        sql = "INSERT INTO students (id,name,present,date,morning,evening) VALUES (%s, %s, %s, %s, %s, %s)"
                        val = (str(student_id), name_student, "p", currentDT.strftime('%Y-%m-%d'), "00:00:00",
                               currentDT.strftime('%H:%M:%S'))
                        mycourse.execute(sql, val)
                        mydb.commit()
                    file_data.write(str(student_id) + "," + name_student + ",p," + date + "\n")
                    playsound('audio.mp3')
                    print("file created")
        try:
            with open(file_name, 'r+') as file_data:
                file_data.seek(0)
                for line in file_data:
                    id, name, state, dt = line.split(",")
                    ids.append(int(id))
                if student_id not in ids:
                    print("not present")
                    sql = "INSERT INTO students (id,name,present,date,morning,evening) VALUES (%s, %s, %s, %s, %s, %s)"
                    val = (str(student_id), name_student, "p",currentDT.strftime('%Y-%m-%d'), currentDT.strftime('%H:%M:%S'), "00:00:00")
                    mycourse.execute(sql,val)
                    mydb.commit()
                    print(mycourse.rowcount, "record inserted.")
                    file_data.write(str(student_id) + "," + name_student + ",p," + date + "\n")
                    file_data.seek(0)
                    playsound('audio.mp3')
                    print("marked", name_student, "present")
        except FileNotFoundError:
            with open(file_name, 'w') as file_data:
                print(date)
                sql = "INSERT INTO students (id,name,present,date,morning,evening) VALUES (%s, %s, %s, %s, %s,%s)"
                val = (str(student_id), name_student, "p",currentDT.strftime('%Y-%m-%d'), currentDT.strftime('%H:%M:%S'), "00:00:00")
                mycourse.execute(sql, val)
                mydb.commit()
                print(mycourse.rowcount, "record inserted.")
                file_data.write(str(student_id) + "," + name_student + ",p," + date + "\n")
                playsound('audio.mp3')
                print("file created")

    # setting font for puttext
    font = cv2.FONT_HERSHEY_SIMPLEX

    # laoding data files and storing in lists
    with open("encodings.txt", 'rb') as file_data:
        known_face_encodings = pickle.load(file_data)

    with open("name.txt", 'rb') as file_data:
        known_names = pickle.load(file_data)
        print(known_names)

    with open("ids.txt", 'rb') as file_data:
        student_ids = pickle.load(file_data)
        print(student_ids)
    if (k.get() == "cameraon"):
        cameraNumber = simpledialog.askstring("Input string", "Camera Number or ip:port")
        print(cameraNumber)
        print(type(cameraNumber))
        if cameraNumber == '0' or cameraNumber == '1':
            camera = int(cameraNumber)
            print(camera)
            cam = cv2.VideoCapture(camera)

        else:
            os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
            st = "rtsp://" + cameraNumber + ":554/onvif1"
            cam = cv2.VideoCapture(st)

    else:
        cam = cv2.VideoCapture(0)
    if (h.get() == "check"):
        playtime = simpledialog.askinteger("Input string", "Enter Time in Minutes")
        capture_duration = playtime * 60
        time=var
        start_time = time.time()
        timeplay = int(time.time() - start_time)
    else:
        timeplay = 1
        capture_duration = 2
    while (timeplay < capture_duration):
        frame = cam.read()[1]

        # converting BGR frame to RGB frame
        rgb_frame = frame[:, :, ::-1]

        # gettting face locations
        face_locations = face_recognition.face_locations(rgb_frame)

        # getting face encodings
        current_face_encoding = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, current_face_encoding):
            # compariong face with known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
            # print(matches)
            name = "unknown"

            if True in matches:
                # getting index for matched face
                match_index = matches.index(True)

                # getting name of the person
                name = known_names[match_index]
                student_id_det = student_ids[match_index]
                save_att(student_id_det, name)
            else:
                continue

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 1)
            if (h.get() == "check"):
                hk = int(time.time() - start_time)
                cv2.putText(frame, str(hk), (0, 35), font, 1.0, (255, 255, 255), 2)
                cv2.putText(frame, name, (left, top), font, 1.0, (255, 255, 255), 2)
            else:
                cv2.putText(frame, name, (left, top), font, 1.0, (255, 255, 255), 2)
        if (h.get() == "check"):
            timeplay = int(time.time() - start_time)

        cv2.imshow("Live", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()