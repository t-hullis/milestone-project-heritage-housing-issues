import streamlit as st
from src.data_management import load_house_data

import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import ppscore as pps

sns.set_style("whitegrid")


def p2_sale_price_study():

    
    # load data
    df = load_house_data()

    # hard copied from churned customer study notebook
    vars_to_study = ['OverallQual', 'GrLivArea', 'YearBuilt', '1stFlrSF', 'GarageArea']

    st.write("### House Value Estimator")
    st.info(
        f"#### Business Requirement 1\n"
        f"""* 1 - The client is interested in discovering how the house attributes correlate 
         with the sale price. Therefore, the client expects data visualisations of the 
         correlated variables against the sale price to show that."""
    )

    # inspect data
    if st.checkbox("Inspect House Prices"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"printed below are the first 10 rows.")
        
        st.write(df.head(10))

    st.write("---")


    # Correlation Study Summary
    st.write(
        f"* A correlation study was conducted in the notebook to better understand how "
        f"the variables are correlated to sales price. \n"
        f"The most correlated variable are: **{vars_to_study}**"
    )

    # Text based on "02 - Churned Customer Study" notebook - "Conclusions and Next steps" section
    st.info(
        f"The correlation indications and plots below interpretation converge. "
        f"It is indicated that: \n"
        f"* A churned customer typically has a month-to-month contract \n"
        f"* A churned customer typically has fibre optic. \n"
        f"* A churned customer typically doesn't have tech support. \n"
        f"* A churned customer doesn't have online security. \n"
        f"* A churned customer typically has low tenure levels. \n"


        f"The correlation indications and plots in the noptebook are below. "
        f"It is indicated that: \n"
        f"* The sale price is generally higher for larger houses (`Ground Living Area`). \n"
        f"* The sale price is generally higher for homes of higher overall quality \n"
        f"* The sale price is sometimes higher if it was built recently. "
        f"This occurs due to the newer the house construction (`Year Built` or `Remodel`), "
        f"the higher generally in quality houses(`Overall Quality`). \n"
    )

    # Code copied from "02 - Churned Customer Study" notebook - "EDA on selected variables" section
    df_eda = df.filter(vars_to_study + ['SalePrice'])

    # Individual plots per variable
    if st.checkbox("Churn Levels per Variable"):
        churn_level_per_variable(df_eda)

    # Parallel plot
    if st.checkbox("Parallel Plot"):
        st.write(
            f"* Information in yellow indicates the profile from a churned customer")
        parallel_plot_churn(df_eda)


# function created using "02 - Churned Customer Study" notebook code - "Variables Distribution by Churn" section
def churn_level_per_variable(df_eda):
    target_var = 'Churn'

    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        if df_eda[col].dtype == 'object':
            plot_categorical(df_eda, col, target_var)
        else:
            plot_numerical(df_eda, col, target_var)




# code copied from "02 - Churned Customer Study" notebook - "Variables Distribution by Churn" section


def regr_level_per_variable(df_eda, target_var):
    
    for col in df_eda.drop([target_var], axis=1).columns.to_list():
            plot_numerical(df_eda, col, target_var)


def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    fig = sns.lmplot(data=df, x=col, y=target_var, ci=None) 
    plt.title(f"{col}", fontsize=20,y=1.05)
    st.pyplot(fig) # st.pyplot() renders image, in notebook is plt.show()