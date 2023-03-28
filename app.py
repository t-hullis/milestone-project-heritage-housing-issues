import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.page_summary import page_summary_body
from app_pages.page_sales_price_summary import p2_sale_price_study
from app_pages.page_predict import page_3_predict_body
from app_pages.page_hypothesis import p4_hypothesis_and_validation
from app_pages.page_ml_predict import page_5_ml_predict_body

app = MultiPage(app_name= "Heritage Housing")
app.add_page("Project Summary", page_summary_body)
app.add_page("Sale Price Correlation Study", p2_sale_price_study)
app.add_page("House Price Prediction", page_3_predict_body)
app.add_page("Hypothesis and Validation", p4_hypothesis_and_validation)
app.add_page("ML Model", p5_ml_predictor)

app.run() # Run the  app