import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.write("lets print a tale")

#CREATE A DATA FRAME 


# df = pd.DataFrame({
#     "id" : [1,2,3,4,5,6],
#     "name" : ["sujay", "binod","eela","rani","sanju","bidi"],
#     "salary in lakhs " : [10,20,30,40,50,60]
# })

# st.write(df)


#HOW ST.WRITE FUNCTIONS 

# st.write("befor", df , "after" ,452313*345678 )


#LETS BUILD A GRAPH

df = pd.DataFrame(
    np.random.randn(100, 3),
    columns=["a", "b" , "c"]
)

st.write(df)

c = alt.Chart(df).mark_circle().encode(
    x="a", y="b" ,size ="c",color ="c",)
st.write(c)
