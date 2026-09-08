# Biomedical Image Analysis of Hand Kinematics

This repository contains the codebase and simulation files for a low-cost, offline computer vision pipeline designed to extract and simulate high-fidelity fine-motor kinematics. By utilizing standard 2D smartphone video and optical markers, this project provides a highly accessible alternative to the expensive, hardware-intensive motion-capture setups traditionally used in biomechanics.

## Overview

The system captures the complex hand movements of a high-dexterity piano performance (specifically Chopin's Waltz in C-sharp minor, Op. 64, No. 2). Recorded at 30 fps via a standard Pixel 9 smartphone camera, the computer vision pipeline extracts precise spatiotemporal coordinates and distance measurements between the thumb and fifth digit (pinky). 

This empirical visual data is integrated into a dynamic bond graph model to mathematically simulate the resulting biomechanical forces. The physics model successfully replicates the physiological stretch and mechanical stress of human tendons, validating the application of Hooke's Law by demonstrating a strictly proportional relationship between kinematic displacement and internal tendon effort.

## Key Features

* **Interactive HSV Color Picker:** A dedicated calibration interface that allows users to dynamically adjust Hue, Saturation, and Value thresholds to isolate markers perfectly under varying environmental lighting.
* **Offline Kinematic Tracking:** Extracts continuous coordinates using dynamic area-thresholding to mitigate environmental optical noise.
* **Automated Data Filtering:** Systematically detects marker occlusion and motion blur, rejecting false positives and filtering null values.
* **Anthropometric Mass Estimation:** Calculates the independent mass of individual digits utilizing 2D planar projections.
* **Dynamic Physics Simulation:** Translates pixel-based optical data into proportional mechanical stress via parameterized 20-sim bond graphs.

## Tech Stack and Tools

* **Computer Vision:** Python, OpenCV
* **Physics Simulation:** 20-sim (Dynamic Bond Graph Modeling)
* **Data Processing:** Python (Dataset structuring and mathematical scaling)
* **Academic Documentation:** LaTeX (IEEEtran standard)

## Repository Structure

```text
├── colour picker.py    # GUI for dynamic HSV threshold calibration
├── Right Hand Tracker.py         # Main OpenCV pipeline for extracting coordinates for the right hand
├── Left Hand Tracker.py         # Main OpenCV pipeline for extracting coordinates for the left hand
├── right_hand_data.csv         # Raw data from the right hand tracker
├── right_hand_distance.csv         # Filtered data from the right hand tracker 
├── left_hand_data.csv         # Raw data from the left hand tracker
├── left_hand_distance.csv         # Filtered data from the left hand tracker 
└── README.md
