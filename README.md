\# SafeFall AI — Fall Detection and Elder Care



\## Problem

Elderly people who fall while alone may not receive timely assistance.



\## Proposed Solution

SafeFall AI is a computer-vision prototype that analyses a webcam feed, estimates body pose, identifies potential fall-like movements and triggers an audible alert.



\## Current Features

\- Webcam-based pose estimation

\- Fall scoring using body movement and posture features

\- Temporal confirmation to reduce false alerts

\- Audible alert for detected fall-like events



\## Technology Stack

\- Python

\- OpenCV

\- Pose estimation

\- Weighted scoring and temporal state machine



\## Run Locally

Create and activate a Python virtual environment, install the dependencies from `requirements.txt`, then run:



`python main.py --source 0`



\## Testing

Test cases include standing, sitting, slowly lying down and controlled fall-like movements performed safely. Record the observed results rather than claiming unverified accuracy.



\## Current Limitations

This is a prototype, not a certified medical or emergency-response system. The local Windows AMD setup has not yet demonstrated the mandatory NVIDIA TensorRT and DeepStream deployment required for PipeGen Track A.



\## Hackathon Integration

PipeGen pipeline stages, TensorRT engine, speed report and NVIDIA live-run evidence must be added after successful execution in a supported environment.



\## Privacy

Avoid saving identifiable video unless necessary and consented to. Apply privacy blur before saving any frames.



\## Future Work

\- JSON or MQTT incident notifications

\- Privacy-preserving video processing

\- Evaluation on diverse fall and non-fall scenarios

\- Edge deployment and performance benchmarking

