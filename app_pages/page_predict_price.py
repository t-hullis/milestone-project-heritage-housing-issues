import streamlit as st
import pandas as pd
from src.data_management import load_house_data, load_pkl_file, load_inherited_house_data
from src.machine_learning.predictive_analysis_ui import predict_sale_price
from datetime import date

def page_3_predict_body():
    # load predict sale_price files
    version = 'v1'
    sale_price_pipe = load_pkl_file(f"outputs/ml_pipeline/predict_sale_price/{version}/final_regressor_pipeline.pkl")
    sale_price_features = (pd.read_csv(f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
                                        .columns
                                        .to_list())

    st.write("### Predict House Sale Price")
    # display client's query and its data
    st.info(
        f"#### Business Requirement 2\n"
        f"* The client is interested to predict the house sale price for "
        f"her 4 inherited houses, and any other house in Ames, Iowa. ")

    st.write("---")
    st.write("The data of the houses you want an estimated price for can be entered below. "
			"If you are missing any values of the data set, they're set to median. ")
	
    # Generate Live Data
    X_live = DrawInputsWidgets()

    # Predict live data
    if st.button("Run Predictive Analysis"): 
        predict_sale_price(X_live, sale_price_features, sale_price_pipe)

    st.write("---")
    st.write("Here is the info for the key values of the clients inherited houses. ")
	
    in_df = load_inherited_house_data()
    filtered_df = in_df[["OverallQual", "GrLivArea", "TotalBsmtSF", "GarageArea", "YearBuilt", "YearRemodAdd"]]	
		
    st.write(filtered_df)

    st.write("After running them through the prediction app, their estimated prices are the following. \n\n "
			"* $ \n"
			"* $ \n"
			"* $ \n"
			"* $ ")
	
    st.write("---")







def DrawInputsWidgets():

	# Load the dataset
	df = load_house_data()
	percentageMin, percentageMax = 0.4, 2.0

    # Create input widgets for the most important features	
	col1, col2 = st.beta_columns(2)
	col3, col4 = st.beta_columns(2)
	col5, col6 = st.beta_columns(2)

	# Feed the ML pipeline by using these features
		
	# Create an empty DataFrame, to be displayed in the live data
	X_live = pd.DataFrame([], index=[0]) 
	
	# Then draw the widget based on the numerical or categorical type
	# and set initial values

	with col1:
		feature = "OverallQual"
		st_widget = st.number_input(
			label= feature,
			min_value= 0, 
			max_value= 10,
			value= int(df[feature].median()), 
            step = 1       
			)
	X_live[feature] = st_widget

	with col2:
		feature = "GrLivArea"
		st_widget = st.number_input(
			label= feature,
			min_value= int(df[feature].min()*percentageMin), 
			max_value= int(df[feature].max()*percentageMax),
			value= int(df[feature].median()), 
            step= 100
			)
	X_live[feature] = st_widget

	with col3:
		feature = "TotalBsmtSF"
		st_widget = st.number_input(
			label= feature,
			min_value= int(df[feature].min()*percentageMin), 
			max_value= int(df[feature].max()*percentageMax),
			value= int(df[feature].median()), 
            step= 50
			)
	X_live[feature] = st_widget

	with col4:
		feature = "GarageArea"
		st_widget = st.number_input(
			label= feature,
			min_value= int(df[feature].min()*percentageMin), 
			max_value= int(df[feature].max()*percentageMax),
			value= int(df[feature].median()), 
            step= 50
			)
	X_live[feature] = st_widget

	with col5:
		feature = "YearBuilt"
		st_widget = st.number_input(
			label= feature,
			min_value= int(df[feature].min()*percentageMin), 
			max_value= date.today().year,
			value= int(df[feature].median()), 
            step= 1
			)
	X_live[feature] = st_widget

	with col6:
		feature = "YearRemodAdd"
		st_widget = st.number_input(
			label= feature,
			min_value= int(df[feature].min()*percentageMin), 
			max_value= date.today().year,
			value= int(df[feature].median()), 
            step= 1
			)
	X_live[feature] = st_widget


	# st.write(X_live)

	return X_live
                    