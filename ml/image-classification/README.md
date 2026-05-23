# image-classification

YOLO26n-based home camera detection for people, pets, packages, and vehicles. Pretrained on COCO — no custom training yet.

## Setup

```bash
python -m venv yolo-env
source yolo-env/bin/activate
pip install ultralytics
```

## Usage

```bash
python detect.py          # single image
python summarize.py       # count detections across test_images/
```

## Roadmap

- [ ] Test against real camera footage
- [ ] Video/RTSP stream inference
- [ ] Export to NCNN for Raspberry Pi
- [ ] Deploy to Pi
- [ ] Alerting on detection
