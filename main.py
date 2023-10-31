import streamlit as st
import pandas as pd
import numpy as np
import json


df = pd.DataFrame(json.load(open("data/purdue.json")))

st.title('NCAA Basketball Dashboard')