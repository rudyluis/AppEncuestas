import streamlit as st
import pandas as pd
import numpy as np
import pickle
import altair as alt
from sklearn.preprocessing import LabelEncoder
from pandas import set_option
from st_aggrid import AgGrid
import plotly.express as px
import pygwalker as pyg 
import streamlit.components.v1 as stc 
import seaborn as sns
import matplotlib.pyplot as plt
import random
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards
import SQL-Alchemy

def main():
	"""Simple Login App"""
	imagen = "logo.png"
	st.set_page_config(page_title="Encuestas Bienestar",
					page_icon=imagen,
					layout="wide",
					initial_sidebar_state="auto"
					)
	

	# Mostrar la imagen en la barra lateral
	st.sidebar.image(imagen,  width=200)	

if __name__ == '__main__':
    main()
