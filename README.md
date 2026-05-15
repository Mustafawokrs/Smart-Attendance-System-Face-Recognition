#  Smart Attendance System (AI + Hardware Integration)

[cite_start]This project provides a step-by-step implementation for building an automated Smart Attendance System[cite: 1, 4]. [cite_start]It uses computer vision to identify students and logs their presence in an Excel sheet while interacting with Arduino for real-time feedback[cite: 1, 5].

##  Key Features
* [cite_start]**Facial Recognition:** High-accuracy recognition using the **DeepFace** library[cite: 1, 10, 29].
* [cite_start]**Real-time Feedback:** Visual and audio confirmation via **LEDs and a Buzzer** connected to Arduino[cite: 1, 16, 27].
* [cite_start]**Automated Logging:** Attendance data is managed and saved in **Excel format** using Pandas[cite: 1, 11].
* [cite_start]**Optimized Accuracy:** Uses **Cosine Similarity** with a threshold of **0.40** for precise matching[cite: 1, 38, 39].

##  Requirements
### Software
* [cite_start]**Python 3.x:** Primary language[cite: 1, 8].
* [cite_start]**OpenCV:** For camera and image processing[cite: 1, 9].
* [cite_start]**DeepFace:** For facial recognition[cite: 1, 10].
* [cite_start]**Pandas:** For data logging[cite: 1, 11].
* [cite_start]**PySerial:** For Python-Arduino communication[cite: 1, 12].

### Hardware
* [cite_start]**Webcam:** For real-time video[cite: 1, 14].
* [cite_start]**Arduino Uno:** Microcontroller[cite: 1, 15].
* [cite_start]**LED (Green) & Buzzer:** For feedback on Pins 13 and 12[cite: 1, 27].

##  System Setup
1. [cite_start]**Database:** Create a `dataset` folder and save one clear image of each student named as their identity (e.g., `Mustafa.jpg`)[cite: 1, 23, 24, 25].
2. [cite_start]**Hardware:** Connect the Green LED to Pin 13 and the Buzzer to Pin 12 on the Arduino[cite: 1, 27].
3. **Execution:** Run the Python script. [cite_start]Ensure the Excel file is closed during operation[cite: 1, 29, 43].

##  Troubleshooting Tips
* [cite_start]**Lighting:** Ensure the room is well-lit for accurate feature detection[cite: 1, 41].
* [cite_start]**Serial Port:** Update the COM port in the Python code to match your Arduino[cite: 1, 42].
