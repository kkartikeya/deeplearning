List all USB cameras: 
ioreg -p IOUSB| grep -i camera

install opencv for python:
pip3 install opencv-python

Play Live single camera:
python livecamera.py

Play Live two cameras concatenated horizontally:
python livecamera1.py
