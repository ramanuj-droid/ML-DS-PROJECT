import streamlit as st

#python declarative code is used in this framework
#html/css/js = no requirement

#BASIC UI TOOLS
st.title("My Restaurent")
st.subheader("Indian veg Non-veg Restaurent")
st.text("Welcome to the Restaurent:")
st.write("testing-1")

#TABLE ELEMENTS : SLIDER SELECTBOX,CHECKBOX,RADIO
Dinner = st.selectbox("Eating items", ["Paneer","Dal","Rice","bread"])
if st.button("Paneer"):
    st.success("Available")

    masala =st.checkbox("Add masala")
    
juice_type = st.radio("Pick up :",['Milk','Water','Lemon juice'])
st.write(f"Selected drink {juice_type}")

desert =st.selectbox("Dessert", ["ice cream","Cassata","Farerorosher"])
st.write(f"Selected desert {desert}")

price =st.slider("Price",0,500)
st.write(f"Selected price {price}")

items = st.number_input("total items",0,7)
st.write(f"Selected items {items}")

name = st.text_input("Enter your name :")
dob = st.date_input("Enter the birth date : ")
if name:
    st.write(f"Welcome to the table name {name}")
    st.write(f"your birth is {dob}")

#TABLE

st.subheader("Food Table")
col1, col2 =st.columns(2)
with col1:
    st.header("Bread")
    vote1 =st.button("Naan")
with col2:
    st.header("Rice")
    vote2 =st.button("Basmati")

if vote1:
    st.success("Thanks for Voting Naan")
elif vote2:
    st.success("Thanks for Choosing Naan")

#IMAGE PROCESSING
#st.image("C:\Users\salar\Desktop\Programming\PYTHON\heaveb.JPG")

st.sidebar.selectbox("Choose your snacks",["Doritoes","kURKURE","Flamgoes"])

with st.expander("Choose your snacks"):
    st.write("""1.A 2.B3.C""")

st.markdown("Enjoy")
st.markdown('> Blackquote ')

#DATAFRAME
import pandas as pd
file =st.file_uploader("Upload your file",type =["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data preview")
    st.dataframe(df)

#API REQUESTS
import requests as rq

st.title("Request handling")
amount =st.number_input("Enter INR",1)
currency = st.selectbox("Convert to :",["INR","USD","JPY"])

if st.button("Convert"):
    url ="https://api.exchangerate-api.com/v4/latest/inr"
    response = rq.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][currency]
        converted = rate * amount
        st.success(f"{amount} INR = {converted}{currency}")
    else:
        st.error("Failed")