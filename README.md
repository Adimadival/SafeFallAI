# SafeFall AI — Fall Detection and Elder Care

## Overview
SafeFall AI is a prototype designed to detect potential falls using a webcam-based computer vision pipeline and provide an audible alert.

## Problem Statement
Older adults who live alone may need timely assistance after a fall. SafeFall AI explores how computer vision and temporal analysis can help identify potential fall events.

## Current Features
- Webcam-based person and pose analysis
- Fall scoring using movement and posture-related features
- Temporal confirmation to reduce false alarms
- Audible alert when a fall is detected
- Fall-event logging, where configured

## Technology Stack
- Python
- OpenCV
- Computer vision and pose estimation
- Weighted scoring and temporal state machine

## Requirements
- Windows 11 or another compatible Python environment
- Python version compatible with the project dependencies
- Webcam
- Project dependencies listed in `requirements.txt`

## Installation
Clone the repository:

```bash
git clone https://github.com/Adimadival/SafeFallAI.git
cd SafeFallAI
```

Create and activate a virtual environment on Windows:

```powershell
py -3.12 -m venv .venv312
.\.venv312\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run
Start webcam-based detection:

```powershell
python main.py --source 0
```

If your Python version or dependency requirements differ, follow the versions supported by the project.

## Testing
Test in a safe, controlled environment:
- Normal standing and walking
- Sitting and slowly lying down
- Controlled movement resembling a potential fall
- Audible alert behaviour

Do not intentionally fall to test the system.

## Hackathon Integration Status
The local Python prototype is available for development and testing. PipeGen integration, NVIDIA GPU execution, TensorRT engine generation, performance reporting and required pipeline evidence must be verified separately before claiming completion.

## Limitations
- This is a prototype, not a certified medical or emergency-response system.
- Detection may produce false positives or miss falls.
- A webcam may not cover every room or movement.
- Local testing on AMD graphics does not demonstrate NVIDIA TensorRT compatibility.

## Privacy and Safety
Use the camera only with appropriate consent. Protect recorded video and event logs. Do not rely on this prototype as the sole method of emergency monitoring.

## Future Improvements
- Validate performance using representative test data
- Integrate with the required PipeGen workflow
- Evaluate on compatible NVIDIA hardware
- Measure detection latency and false-positive rates
- Add privacy-preserving and caregiver-notification options

## Repository
https://github.com/Adimadival/SafeFallAI
