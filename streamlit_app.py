from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import time

##STEP 1
st.write("1. Load fine-tuned pretrained model YOLOx:")

# to insert model loading code in progress bar
my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)

##STEP 2    
st.write("2. Upload raw diving video:\n")

vid_file = st.file_uploader("Choose a file")

st.video(vid_file)


##STEP 3 
st.write("3. YOEO working its magic: ")

 
##STEP 4 display processed video and metrics
col1, col2, col3 = st.columns(3)
col1.metric("# Speciies Detected", "2")
col2.metric("Turtle", "1")
col3.metric("Fish", "23")
