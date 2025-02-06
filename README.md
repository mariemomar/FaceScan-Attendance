# FaceTrack Attendance

## Overview
FaceTrack Attendance is a real-time facial recognition-based attendance system using OpenCV and the `face_recognition` library. The system detects and recognizes faces from a live camera feed and automatically marks attendance in a CSV file.

## Features
- Real-time face detection and recognition.
- Automatic attendance logging.
- Uses OpenCV for video processing.
- Utilizes the `face_recognition` library for facial recognition.
- Efficient and easy-to-use system for attendance tracking.

## Requirements
Ensure you have the following dependencies installed:
- Python 3.x
- OpenCV (`cv2`)
- NumPy
- `face_recognition` library

To install the dependencies, run:
```bash
pip install opencv-python numpy face-recognition
```

## How It Works
1. Store face images in the `Faces` directory.
2. The system encodes known faces and stores their encodings.
3. When the camera captures a face, it compares it with the known encodings.
4. If a match is found, it marks attendance in `Attendance.csv` with a timestamp.
5. The system runs continuously until the user presses 'q' to exit.

## Usage
Run the following command to start the attendance system:
```bash
python main.py
```

## File Structure
```
FaceTrack_Attendance/
│── Faces/               # Folder containing known face images
│── Attendance.csv       # File where attendance is logged
│── main.py              # Main script
│── README.md            # Project documentation
```

## Notes
- Ensure that images in the `Faces` folder are clear and well-lit for better recognition.
- The script uses Euclidean distance to determine face similarity, and the closest match is identified.

## License
This project is open-source and available for modification and distribution under the MIT License.

