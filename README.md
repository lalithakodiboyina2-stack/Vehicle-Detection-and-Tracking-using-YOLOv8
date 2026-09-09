# Vehicle Detection and Tracking using YOLOv8

Real-time Vehicle Detection, Tracking & Counting using YOLOv8 + ByteTrack for Intelligent Traffic Monitoring.

## Overview
This project detects vehicles from traffic videos and tracks them with unique IDs using YOLOv8 for detection and ByteTrack for tracking.

## Features
- Real-time detection (car, bike, bus, truck)
- Multi-object tracking with unique IDs
- Vehicle counting
- Saves tracked output video

## Tech Stack
- Python, Ultralytics YOLOv8, OpenCV, ByteTrack

## Installation
pip install -r requirements.txt

## Usage
python vehicle_detection.py

## How it Works
1. YOLOv8n detects vehicles (class IDs 2,3,5,7)
2. ByteTrack assigns unique ID to each vehicle
3. Counts total unique vehicles
4. Saves output to runs/detect/track/


