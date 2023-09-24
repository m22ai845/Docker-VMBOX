# Core PKGS

import streamlit as st
import pandas as pd
import sqlite3

try:
    con = sqlite3.connect('data/world.sqlite')
    c = con.cursor()
except Exception as e:
    st.write(f"Error: {e}")

def sql_executor(raw_code):
    c.execute(raw_code)
    data = c.fetchall()
    return data

city = ['ID,', 'Name,', 'CountryCode,', 'District,', 'Population']
country = ['Code,', 'Name,', 'Continent,', 'Region,', 'SurfaceArea,', 'IndepYear,', 'Population,', 'LifeExpectancy,', 'GNP,', 'GNPOld,', 'LocalName,', 'GovernmentForm,', 'HeadOfState,', 'Capital,', 'Code2']
countrylanguage = ['CountryCode,', 'Language,', 'IsOfficial,', 'Percentage']



#DB Mgmt


def main():
    st.title("SQLPlayground")
    menu = ["Home","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("HomePage")
        col1,col2 = st.columns(2)
        with col1:
            with st.form(key='query_form'):
                raw_code = st.text_area("SQL Code Here")
                submit_code = st.form_submit_button("Execute")

                #Table of Info
                with st.expander("Table Info"):
                    t_info = {'city':city,'country':country,'countrylanguage':countrylanguage}
                    st.json(t_info)

            # Table
        #Result Layout
        with col2:
            if submit_code:
                st.info("Query Submitted")
                st.code(raw_code)
                # Table of info

                # Results
                query_results = sql_executor(raw_code)
                with st.expander("Result"):
                    st.write(query_results)
                with st.expander("Pretty Table"):
                    query_df = pd.DataFrame(query_results)
                    st.dataframe(query_df)
    else:
        st.subheader("About")


if __name__ == '__main__':
            main()