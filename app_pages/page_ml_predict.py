import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_house_data, load_pkl_file
from src.machine_learning.evaluate_regression import regression_performance


def page_5_ml_predict_body():

    # Load sale price pipeline files
    version = 'v1'
    sale_price_pipe = load_pkl_file(f"outputs/ml_pipeline/predict_sale_price/{version}/final_regressor_pipeline.pkl")
    sale_price_features = pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
    sale_price_importance = plt.imread(f"outputs/ml_pipeline/predict_sale_price/{version}/features_importance.png")
    X_train = pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
    X_test = pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_test.csv")
    y_train =  pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/y_train.csv")
    y_test =  pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/y_test.csv")

    
    st.write("### ML Pipeline: Predict House Price")
    # Display pipeline training summary conclusions
    st.info(
        f"* We wanted a **Regressor** model to predict the **`Sale Price`** for the houses. "
        f"Our target **R2 score was above 0.7**, and we tried improving "
        f"the score using a **PCA Regressor** model but with no success.\n"

        f"* The data for the pipeline was tuned by taking several steps "
        f"to clean and engineer it. The highest performing steps "
        f"and hyperparameters on the most critical features "
        f"are listed below: ")
    st.write("---")

    # Show pipeline steps
    st.write("* ML Pipeline To Predict Sale Price")
    st.code(sale_price_pipe)
    st.write("---")

    # Show best features
    st.write("* The Features The Model Was Trained And Their Importance")
    st.write(X_train.columns.to_list())
    st.image(sale_price_importance)
    st.write("---")

    # evaluate performance on both sets
    
    st.write("### Pipeline Performance")
    regression_performance(X_train=X_train, y_train=y_train,
                        X_test=X_test, y_test=y_test,
                        pipeline=sale_price_pipe)



# This code isfrom the churnometer project from Code Institute with  adjustments