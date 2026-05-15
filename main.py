import cv2
from deepface import DeepFace
import os
import serial
import time
import pandas as pd
from datetime import datetime

# 1. Arduino Setup
try:
    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1, write_timeout=0)
    time.sleep(2)
    print("Arduino Connected!")
except:
    arduino = None
    print("Arduino Not Connected.")

# 2. Paths
db_path = "known_faces" 
log_dir = "logs"
if not os.path.exists(log_dir): os.makedirs(log_dir)

# 3. Master List (Saare students ke naam folder se nikalna)
all_students = [os.path.splitext(f)[0] for f in os.listdir(db_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
print(f"Total Students in Database: {len(all_students)}")

date_today = datetime.now().strftime("%Y-%m-%d")
log_file = os.path.join(log_dir, f"attendance_{date_today}.csv")

already_marked = {} 
cap = cv2.VideoCapture(0)

print("System Active! 's' for Scan | 'q' to Finish and mark Absents")

while True:
    ret, frame = cap.read()
    if not ret: break

    cv2.imshow("Smart Attendance System", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        print("Scanning...")
        try:
            results = DeepFace.find(img_path=frame, db_path=db_path, enforce_detection=False, model_name='VGG-Face', silent=True)
            
            if len(results) > 0 and not results[0].empty:
                full_path = results[0].iloc[0]['identity']
                user_name = os.path.splitext(os.path.basename(full_path))[0]
                
                current_time = time.time()
                if user_name not in already_marked:
                    now = datetime.now()
                    t_str = now.strftime("%H:%M:%S")
                    day_str = now.strftime("%A")

                    new_entry = pd.DataFrame([[user_name, date_today, day_str, t_str, "Present"]], 
                                            columns=['Name', 'Date', 'Day', 'Time', 'Status'])

                    if not os.path.isfile(log_file):
                        new_entry.to_csv(log_file, index=False)
                    else:
                        new_entry.to_csv(log_file, mode='a', header=False, index=False)

                    print(f"PRESENT: {user_name}")
                    already_marked[user_name] = current_time
                    if arduino: arduino.write(b'G')
                else:
                    print(f"{user_name} is already marked.")

            else:
                print("UNKNOWN!")
                if arduino: arduino.write(b'R')

        except Exception as e:
            print(f"Error: {e}")

    elif key == ord('q'):
        print("\nSystem Closing... Recording Absentees...")
        # 4. Absent Logic (Jo Master List mein hain magar already_marked mein nahi)
        absent_students = [s for s in all_students if s not in already_marked]
        
        if absent_students:
            now = datetime.now()
            day_str = now.strftime("%A")
            absent_data = []
            for student in absent_students:
                absent_data.append([student, date_today, day_str, "--:--:--", "Absent"])
            
            df_absent = pd.DataFrame(absent_data, columns=['Name', 'Date', 'Day', 'Time', 'Status'])
            df_absent.to_csv(log_file, mode='a', header=False, index=False)
            print(f"Marked {len(absent_students)} students as Absent.")
        
        break

cap.release()
cv2.destroyAllWindows()
if arduino: arduino.close()