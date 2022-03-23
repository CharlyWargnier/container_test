import streamlit as st
import pandas as pd

container = st.container()


with st.form("my_form"):

    container2 = st.container()

    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")

    if submitted:

        st.write("slider", slider_val, "checkbox", checkbox_val)

        thislist = ["apple", "banana", "cherry"]

        List = container2.selectbox("list", thislist)

        Drawing = container.image("Arrow2.png", width=700)

st.write("Outside the form")