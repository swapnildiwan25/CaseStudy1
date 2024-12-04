import streamlit as st
import pickle

st.set_page_config(page_title="Diamond price prediction", page_icon=" :money_with_wings:",layout="wide")
st.title(" Diamond price prediction ")

model1=pickle.load(open('gbr1.pkl','rb'))
model2=pickle.load(open('adr1.pkl','rb'))

c1,c2=st.columns(2)

n1=c1.number_input("Carat?")
n2=int(c2.number_input("Cut?"))
n3=int(c1.number_input("Color?"))
n4=int(c2.number_input("Clarity?"))
n5=c1.number_input("Depth?")
n6=c2.number_input("Table?")
n7=c1.number_input("x?")
n8=c2.number_input("y?")
n9=c2.number_input("z?")

new_feature=[[n1,n2,n3,n4,n5,n6,n7,n8,n9]]

c3,c4=st.columns(2)

if c3.button("GBR Model prediction"):
    t1=model1.predict(new_feature)
    c3.subheader(t1)
    
if c4.button("ADR Model prediction"):
    t2=model2.predict(new_feature)
    c4.subheader(t2)
