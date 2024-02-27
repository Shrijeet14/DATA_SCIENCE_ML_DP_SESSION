import streamlit as st

import pandas as pd

st.set_page_config(layout="wide",
                   page_title="Material web-app",
                   page_icon=":data:")

col1,col2=st.columns(2)

with col1 :
    st.image("images/banner.png",use_column_width="always")
with col2 :
    st.title("BOOTCAMP BY IOTA MATRIX AND EPOCH")
    information="""🚀 Welcome to the ultimate journey through Data Science, Machine Learning, and Deep Learning with BOOTCAMP BY IOTA MATRIX AND EPOCH!

In just three action-packed weeks, we'll equip you with the skills to conquer the digital frontier. Matrix Club kicks off Week 1 with Data Science essentials, followed by IOTA Club's deep dive into ML in Week 2. Finally, Week 3 sees EPOCH leading the charge into the world of Deep Learning.

Get ready to elevate your expertise and unleash your potential like never before! Join us for an adventure of learning and discovery. Let's ignite the spark of innovation together! 🔥📊🧠"""
    st.info(information)

    

st.write("Below you can find  the materials of our boot camp !!")


col3,empty_col,col4= st.columns([1.5,0.5,1.5])


df=pd.read_csv("data.csv",sep=";")

counter = 0
for index, row in df.iterrows():
    if counter % 2 == 0:
        with col3:
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
            st.write(f"[DATA SET]({row['dataset_url']})")
            st.write(f"[SLIDES]({row['slides_url']})")
            st.write(f"[NOTEBOOK]({row['notebook_url']})")
    else:
        with col4:
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
            st.write(f"[DATA SET]({row['dataset_url']})")
            st.write(f"[SLIDES]({row['slides_url']})")
            st.write(f"[NOTEBOOK]({row['notebook_url']})")
    counter += 1
