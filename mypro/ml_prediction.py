import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
from sklearn.preprocessing import LabelEncoder
import pickle


df = pd.read_csv("mypro/test_Data0.csv")
df.head()


def preprocessing_steps(df):
  def preprocess_data(df, feature):
    df.drop(['id', 'recipient_age_below_10',
            'recipient_age_int'], axis=1, inplace=True)
    cat_col = [col for col in df.columns if df[col].dtype == 'object']
    num_col = [col for col in df.columns if df[col].dtype != 'object']
    cat_col, num_col = extract_cat_num(df)
    df[feature] = pd.to_numeric(df[feature], errors='coerce')

  def convert_dtype(df, feature):
    df[feature] = pd.to_numeric(df[feature], errors='coerce')
    features = ['CD3_x1e8_per_kg', 'CD3_to_CD34_ratio', 'CD3_x1e8_per_kg',
                'recipient_body_mass', 'CD3_to_CD34_ratio', 'survival_status']
    for feature in features:
        convert_dtype(df, feature)

  return (df)


def extract_cat_num(df):
    cat_col = [col for col in df.columns if df[col].dtype == 'object']
    num_col = [col for col in df.columns if df[col].dtype != 'object']
    # num_col=[col for col in df.columns if df[col].dtype=='float64']
    return cat_col, num_col


le = LabelEncoder()
cat_col, num_col = extract_cat_num(df)
for col in cat_col:
    df[col] = le.fit_transform(df[col])
selected_feat = ['donor_age', 'donor_age_below_35', 'donor_ABO', 'donor_CMV', 'recipient_age',
                 'recipient_gender', 'recipient_body_mass', 'recipient_ABO', 'recipient_rh',
                 'recipient_CMV', 'disease', 'disease_group', 'ABO_match', 'CMV_status',
                 'HLA_match', 'allel', 'HLA_group_1', 'risk_group', 'stem_cell_source',
                  
                 'tx_post_relapse', 'CD34_x1e6_per_kg', 'CD3_x1e8_per_kg',
                 'CD3_to_CD34_ratio', 'extensive_chronic_GvHD', 'relapse', 'survival_time']
df = df[selected_feat]
with open('mypro/model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
predictions = loaded_model.predict(df)
print(predictions)
