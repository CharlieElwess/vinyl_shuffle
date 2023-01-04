###
### IMPORTS
###

import pandas as pd
import random
import streamlit as st
# import requests
# from io import BytesIO
from streamlit_design import get_css
import base64

###
### APP BACKGROUND & STYLE
###
def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.

    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "jpg"

    st.markdown(f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
                unsafe_allow_html=True)

# set_bg_hack('vinyl_shop_pexels-mick-haupt-5193731_lofi.jpeg')
set_bg_hack('record_shelf_edit.jpg')
st.markdown(get_css(), unsafe_allow_html=True)

###
###   IMPORT AND READ VINYL COLLECTION CSV
###

collection = pd.read_csv('vinyl_collection.csv')

###
### Functions to display and shuffle the vinyl
###


def show_vinyl(disc):
    cover = collection.loc[disc][6]
    # print(
    #     f"{collection.loc[disc][1]}\n{collection.loc[disc][2]} ({collection.loc[disc][3]})\n{collection.loc[disc][4]}"
    # )
    return st.markdown(
        f'{collection.loc[disc][1]} - {collection.loc[disc][2]} ({collection.loc[disc][3]})\n\n{collection.loc[disc][4]}\n\n<img src="{cover}" width=500 height=500>',
        unsafe_allow_html=True)


def shuffle():
    disc = random.choice(list(collection.index))
    return show_vinyl(disc)

###
### STREAMLIT
###

st.title("VINYL SHUFFLE")
st.markdown("SHUFFLE CHARLIE'S RECORD COLLECTION")
form = st.form(key="submit-form")
perform_shuffle = form.form_submit_button("SHUFFLE")

if perform_shuffle:
    shuffle()
