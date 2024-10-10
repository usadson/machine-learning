FROM tensorflow/tensorflow:latest-gpu-jupyter
WORKDIR "/tmp"

ENV TF_USE_LEGACY_KERAS=1

RUN pip install --upgrade pip

RUN pip install --upgrade pandas\
    scikit-learn\
    matplotlib\
    scipy\
    seaborn \
    tensorflow \
    keras_nlp \
    xgboost \
    statsmodels \
    torch \
    transformers \
    tf-keras \
    accelerate \
    chromadb \
    python-docx \
    requests \
    bitsandbytes \
    langchain_community \
    scikit-image \
    ipywidgets \ 
    plotly \
    openpyxl \
    historicdutchweather \
    pvlib \
    peft \
    Pillow \
    opencv-python-headless

# Install Pandoc
RUN apt-get update && apt-get install -y pandoc

# Install LaTeX (minimal install)
RUN apt-get install -y texlive-xetex texlive-fonts-recommended texlive-plain-generic

# Clean up to reduce image size
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*