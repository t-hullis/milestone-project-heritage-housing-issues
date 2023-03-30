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

    # Set dataframe filtered for only variables to study
    df_eda = df.filter(vars_to_study + ['SalePrice'])

    st.write("### House Value Estimator")
    st.info(
        f"#### Business Requirement 1\n"
        f"""* 1 - The client is interested in discovering how the house attributes correlate 
         with the sale price."""
    )

    # inspect data
    if st.checkbox("Inspect House Data"):
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
        f"The correlation indications and plots in the noptebook are below. "
        f"It is indicated that: \n"
        f"* The sale price is generally higher for larger houses. \n"
        f"* The sale price is generally higher for homes of higher overall quality \n"
        f"* The sale price is sometimes higher if it was built recently. "
       
    )

    

   # Code copied from "02 - Churned Customer Study" notebook - "EDA on selected variables" section

    if st.checkbox("Correlation of variable to Sale Price"):
        correlation_to_sale_price(df, vars_to_study)

    # if st.checkbox("Sales Price per Variable"):
    #     sale_price_per_variable(df_eda)


# Correlation heatmaps 

    if st.checkbox("Spearman Correlations"):
        
        df_corr_pearson, df_corr_spearman, pps_matrix = CalculateCorrAndPPS(df)
        heatmap_corr(df=df_corr_spearman, threshold=0.6, figsize=(20, 12), font_annot=15)

    # Checkbox widget to display the Pearson correlation information
    if st.checkbox("Peason Correlations"):
       
        df_corr_pearson, df_corr_spearman, pps_matrix = CalculateCorrAndPPS(df)
        heatmap_corr(df=df_corr_pearson, threshold=0.6, figsize=(20, 12), font_annot=15)

    # Checkbox widget to display the PPS information
    if st.checkbox("Predictive Power Score"):
        
        df_corr_pearson, df_corr_spearman, pps_matrix = CalculateCorrAndPPS(df)
        heatmap_pps(df=pps_matrix, threshold=0.15, figsize=(20, 12), font_annot=15)


# Copied from Data_cleaning notebook - correlation and pps analysis 

def sale_price_per_variable(df_eda):
    """  scatterplots vs SalePrice """
       # Set dataframe filtered for only variables to study
    target_var = 'SalePrice'
    for col in df_eda.drop([target_var], axis=1).columns.to_list():
        scatter_plot(df_eda, col, target_var)
        print("\n\n")

def scatter_plot(df, col, target_var):
    """ Plot scattergraphs vs target var"""
    fig, axes = plt.subplots(figsize=(12, 5))
    sns.scatterplot(data=df, x=col, y=target_var)
    plt.xticks(rotation=90)
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)

def plot_numerical(df, col, target_var):
    fig, axes = plt.subplots(figsize=(8, 5))
    sns.histplot(data=df, x=col, y=target_var)
    plt.title(f"{col}", fontsize=20, y=1.05)
    st.pyplot(fig)


def correlation_to_sale_price(df, vars_to_study):
    target_var = 'SalePrice'
    for col in ['GarageArea', 'GrLivArea', 'OverallQual', 'TotalBsmtSF', 'YearBuilt']:
        plot_numerical(df, col, target_var)
        st.write("\n\n")



def heatmap_corr(df,threshold, figsize=(20,12), font_annot = 8):
  if len(df.columns) > 1:
    mask = np.zeros_like(df, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    mask[abs(df) < threshold] = True

    fig, axes = plt.subplots(figsize=figsize)
    sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                mask=mask, cmap='viridis', annot_kws={"size": font_annot}, ax=axes,
                linewidth=0.5
                     )
    axes.set_yticklabels(df.columns, rotation = 0)
    plt.ylim(len(df.columns),0)
    st.pyplot(fig)


def heatmap_pps(df,threshold, figsize=(20,12), font_annot = 8):
    if len(df.columns) > 1:
      mask = np.zeros_like(df, dtype=np.bool)
      mask[abs(df) < threshold] = True

      fig, ax = plt.subplots(figsize=figsize)
      ax = sns.heatmap(df, annot=True, xticklabels=True,yticklabels=True,
                       mask=mask,cmap='rocket_r', annot_kws={"size": font_annot},
                       linewidth=0.05,linecolor='grey')
      
      plt.ylim(len(df.columns),0)
      st.pyplot(fig)

def CalculateCorrAndPPS(df):
    df_corr_spearman = df.corr(method="spearman")
    df_corr_pearson = df.corr(method="pearson")
    pps_matrix_raw = pps.matrix(df)
    pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']).pivot(columns='x', index='y', values='ppscore')

    return df_corr_pearson, df_corr_spearman, pps_matrix
