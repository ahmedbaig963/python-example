Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import streamlit as st
... import pandas as pd
... st.title("Welcome Bano Qabil")
... 
... #creating dataset
... 
... df=pd.DataFrame({'first':[1,2,3,4,5,],'second':[6,7,8,9,10]})
... st.write(df)
... 
... # or
