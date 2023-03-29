import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.page_summary import page_summary_body
from app_pages.page_sales_price_summary import p2_sale_price_study
from app_pages.page_predict_price import page_3_predict_body
from app_pages.page_hypothesis import page_4_hypothesis_body
from app_pages.page_ml_predict import page_5_ml_predict_body

app = MultiPage(app_name= "Heritage Housing")
app.add_page("Project Summary", page_summary_body)
app.add_page("Sale Price Correlation Study", p2_sale_price_study)
app.add_page("House Price Prediction", page_3_predict_body)
app.add_page("Hypothesis and Validation", page_4_hypothesis_body)
app.add_page("ML Model", page_5_ml_predict_body)

app.run() # Run the  app