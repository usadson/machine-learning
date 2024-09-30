FROM tensorflow/tensorflow:latest-gpu-jupyter
WORKDIR "/tmp"

RUN apt-get install ffmpeg libsm6 libxext6  -y; pip install pandas\
    scikit-learn\
    seaborn\
    opencv-python-headless\
    tqdm