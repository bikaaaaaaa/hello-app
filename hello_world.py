import streamlit as st
import pandas as pd
import numpy as np
import datetime
 
def main():
    st.title('Whats uuuuuup')
    st.sidebar.title('sum motivation')
    st.sidebar.write('why be moody, when you can shake yo booty ;)')
 
    st.write('')
 
 
    st.subheader('Welcome to Theebikaas Streamlit with a divider', divider='rainbow')
    st.subheader('_Data elements_ :smile:')
    st.subheader(' ',divider='rainbow')
   
 
   
    df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))
   
    st.table(df)
    st.subheader('_Chart elements_ :smile:')
    st.subheader(' ',divider='rainbow')
   
 
    chart_data = pd.DataFrame(
    {
        "col1": np.random.randn(20),
        "col2": np.random.randn(20),
        "col3": np.random.choice(["A", "B", "C"], 20),
    }
    )
   
    st.line_chart(chart_data, x="col1", y="col2", color="col3")
   
    st.subheader('_Input Widgets_ :smile:')
    st.subheader(' ',divider='rainbow')
 
   
    d = st.date_input("When's your birthday", datetime.date(2002,12,30))
    st.write('Your birthday is:', d)
 
if __name__ == '__main__':
    main()


