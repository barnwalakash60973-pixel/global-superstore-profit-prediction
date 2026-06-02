import streamlit as st
from prediction import predict_profit
from constants import SUB_CATEGORIES, CATEGORIES, SEGMENTS, REGIONS
import os

BASE_DIR = os.path.dirname(__file__)

dashboard_img = os.path.join(
    BASE_DIR,
    "Images",
    "dashboard.png"
)

rf_img = os.path.join(
    BASE_DIR,
    "Images",
    "rf_feature_importance.png"
)


st.set_page_config(
    page_title="Global Superstore Analytics",
    layout="wide"
)

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Home",
        "Dataset Overview",
        "EDA & Insights",
        "KPI Dashboard",
        "Profit Prediction",
        "About"
    ]
)

# 1. Home Page 
if menu == "Home":
    st.title("🏪 Global Superstore Analytics")

    st.image(dashboard_img)

    st.markdown("""
    ### Project Highlights

    - 51K+ Orders
    - 140+ Countries
    - Profit Prediction using ML
    - Ensemble Model (RF + GB)
    - R² ≈ 0.76
    - Business Intelligence Dashboard
    """)

# 2. Dataset Overview
elif menu == "Dataset Overview":

    st.header("📊 Dataset Overview")

    st.write("""
    The Global Superstore dataset contains:
    - 51,289 Orders
    - 140+ Countries
    - Sales, Profit, Discount
    - Shipping Cost
    - Category & Sub-Category
    - Region & Market
    """)

    


# 3. EDA Images
elif menu == "EDA & Insights":

    st.header("📈 EDA & Insights")

    st.subheader("Model Interpretation")

    st.image(rf_img)

    st.warning("""
Key Finding:
Sales and discount-related features are the most influential
factors in profit prediction. While higher sales generally
increase profit, extreme discounts often lead to reduced
profitability and loss-making orders.
""")
    

# 4. KPI Dashboard
elif menu == "KPI Dashboard":

    st.header("📋 KPI Dashboard")


    col1, col2, col3 = st.columns(3)

    col1.metric("Revenue", "$12.6M")
    col2.metric("Profit", "$1.47M")
    col3.metric("ROI", "11.6%")

    st.metric("Loss Making Orders", "24.5%")


# 5. Profit Prediction Inputs
elif menu == "Profit Prediction":

    st.header("Profit Prediction")

    sales = st.number_input(
    "Sales($)",
    min_value=0.0,
    value=0.0
)

    discount = st.number_input(
        "Discount",
        min_value=0.01,
        max_value=100.00
    )

    quantity = st.number_input(
        "Quantity",
        min_value=1
    )

    shipping_cost = st.number_input(
        "Shipping Cost($)"
    )

    sub_category = st.selectbox(
    "Sub-Category",
    SUB_CATEGORIES
    )

    category = st.selectbox(
    "Category",
    CATEGORIES
    )

    segment = st.selectbox(
    "Segment",
    SEGMENTS
    )

    region = st.selectbox(
    "Region",
    REGIONS
    )

    

    order_date = st.date_input(
    "Order Date"
    )

    # Button comes here
    if st.button("Predict Profit"):

        missing = []

        if sales <= 0:
            missing.append("Sales")

        if quantity <= 0:
            missing.append("Quantity")

        if shipping_cost <= 0:
            missing.append("Shipping Cost")

        # Discount can be 0, so check differently
        if discount is None:
            missing.append("Discount")

        if missing:
            st.warning(
            "Please fill the following required fields: "
            + ", ".join(missing)
        )

        else:
            pred = predict_profit(
            sales,
            discount,
            quantity,
            shipping_cost,
            category,
            segment,
            sub_category,
            region,
            order_date
        )

            if pred > 0:
                st.success(f"💰 Predicted Profit: ${pred:.2f}")
                st.info("This order is expected to be profitable.")
            else:
                st.error(f"📉 Predicted Loss: ${abs(pred):.2f}")
                st.warning("This order may result in a loss.")


# 6. About Project
elif menu == "About":

    st.header("👨‍💻 About Project")

    st.markdown("""
    ### Global Superstore Analytics & Profit Prediction

    Developed an end-to-end retail analytics and machine learning solution
    using the Global Superstore dataset.

    ### Dataset
    - 51K+ Orders
    - 140+ Countries
    - Multi-year retail transactions

    ### Project Components
    - Data Cleaning & Preprocessing
    - Feature Engineering
    - Exploratory Data Analysis (EDA)
    - Statistical Hypothesis Testing
    - Machine Learning Model Comparison
    - Ensemble Learning (RF + GB)
    - Interactive Streamlit Dashboard

    ### Hypothesis Testing
    - H1: Profit differs across customer segments
    - H2: Technology is more profitable than Furniture
    - H3: Discounts negatively impact profit
    - H4: Profit differs across global markets
    - H5: Same-Day shipping improves profitability

    ### Final Model
    - Ensemble (Random Forest + Gradient Boosting)
    - R² ≈ 0.76

    ### Key Business Findings
    - High discounts significantly reduce profitability
    - Technology is the most profitable category
    - APAC is the highest-profit market
    - Nearly 25% of orders are loss-making

    ### Technologies
    Python, Pandas, NumPy, Matplotlib,
    Scikit-Learn, Streamlit

    ### Author
    Akash Kumar
    """)