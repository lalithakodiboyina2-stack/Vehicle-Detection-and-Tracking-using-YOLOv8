# ============================================
# VEHICLE DETECTION AND COUNTING
# Using YOLO + ByteTrack
# ============================================

# 1. Install Ultralytics YOLO
# !pip install -q ultralytics

# 2. Import libraries
from ultralytics import YOLO
from collections import defaultdict

# 3. Load pretrained YOLO model
model = YOLO("yolov8n.pt")

# 4. Vehicle class IDs from COCO
# 2 = car, 3 = motorcycle, 5 = bus, 7 = truck
vehicle_classes = [2, 3, 5, 7]

# 5. Detect, track and count vehicles
def detect_and_count(video_path="traffic.mp4"):
    track_history = defaultdict(list)
    results = model.track(
        source=video_path,
        classes=vehicle_classes,
        conf=0.4,
        tracker="bytetrack.yaml",
        save=True,
        verbose=False
    )
    
    # Count unique vehicle IDs
    vehicle_count = len(track_history)
    print(f"Total Vehicles Detected: {vehicle_count}")
    print("Vehicle detection completed!")

# Run
# detect_and_count("your_video.mp4")
