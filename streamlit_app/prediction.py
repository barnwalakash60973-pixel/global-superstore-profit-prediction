import os
import joblib
import pandas as pd
import numpy as np

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "ensemble_pipeline.pkl"
)

model = joblib.load(MODEL_PATH)


def disc_bucket(d):
    if d == 0:
        return "0_none"
    elif d <= 0.1:
        return "1_low"
    elif d <= 0.3:
        return "2_medium"
    elif d <= 0.5:
        return "3_high"
    return "4_extreme"


def feature_extraction(df):

    df = df.copy()

    df["discount_bucket"] = df["Discount"].apply(disc_bucket)

    df["has_discount"] = (df["Discount"] > 0).astype(int)
    df["high_discount"] = (df["Discount"] > 0.3).astype(int)

    df["log_sales"] = np.log1p(df["Sales"])
    df["log_shipping_cost"] = np.log1p(df["Shipping Cost"])

    # Category flags
    df['is_technology']      = (df['Category'] == 'Technology').astype(int)
    df['is_furniture']       = (df['Category'] == 'Furniture').astype(int)
    df['is_office_supplies'] = (df['Category'] == 'Office Supplies').astype(int)

    # Segment flags
    df['is_consumer']    = (df['Segment'] == 'Consumer').astype(int)
    df['is_corporate']   = (df['Segment'] == 'Corporate').astype(int)
    df['is_home_office'] = (df['Segment'] == 'Home Office').astype(int)


    return df

def predict_profit(
    sales,
    discount,
    quantity,
    shipping_cost,
    category,
    segment,
    sub_category,
    region,
    order_date
):

    year = order_date.year
    weeknum = order_date.isocalendar()[1]

    df = pd.DataFrame({
        "Sales":[sales],
        "Discount":[discount],
        "Quantity":[quantity],
        "Shipping Cost":[shipping_cost],
        "Category":[category],
        "Segment":[segment],
        "Sub-Category":[sub_category],
        "Region":[region],
        "Year":[year],
        "weeknum":[weeknum]
    })

    df = feature_extraction(df)

    prediction = model.predict(df)

    return prediction[0]