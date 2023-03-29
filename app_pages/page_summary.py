import streamlit as st

def page_summary_body():

    st.write("### Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Terms & Jargon**\n"
        f"* A **Client** is a person who consumes your service or product.\n"
        f"* A **SalePrice** is the amount of money the house cost to buy, when they sold thier house.\n"
        f"**Project Dataset**\n"
        f"* The dataset represents a **Housing Market** in Iowa, USA, "
        f"containing individual data on the local houses "
        f"(1stFlrSF(first floor square footage), 2ndFlrSF (second floor square footage), bedroom above grade), "
        f"other information like (Overall Condition,	Overall Quality, Wood Deck Size) "
        f"To see it you can click **[HERE](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data)**.\n\n"
        )

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project file](https://github.com/t-hullis/milestone-project-heritage-housing-issues).")
    

    # copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in discovering how the house attributes correlate with"
        f"the sale price. Therefore, the client expects data visualisations of the correlated "
        f"variables against the sale price to show that.\n "


        f"""* 2 - The client is interested in predicting the house sale price from her four
         inherited houses and any other house in Ames, Iowa. """
       
        )
