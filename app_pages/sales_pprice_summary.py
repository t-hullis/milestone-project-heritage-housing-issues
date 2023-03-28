import streamlit as st
from src.data_management import load_house_data

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")



def p2_sale_price_study():

    
    # load data
    df = load_house_data()

    # hard copied from churned customer study notebook
    vars_to_study = ['OverallQual', 'GrLivArea', 'YearBuilt', '1stFlrSF', 'GarageArea']

    st.write("### House Value Estimator")
    st.info(
        f"#### Business Requirement 1\n"
        f"* The client is interested in understanding the patterns from the house sales data set, "
        f"so that the client can learn the most relevant variables correlated to **`SalePrice`**."
    )

    # inspect data
    if st.checkbox("Inspect Customer Base"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"printed below are the first 10 rows.")
        
        st.write(df.head(10))

    st.write("---")