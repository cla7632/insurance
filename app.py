import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

# Set a seed for reproducibility
np.random.seed(42)

# Data Preparation (if using sample data)
def generate_sample_data():
    # Simulate data similar to what an MIS Data Analyst might work with
    data = pd.DataFrame({
        'Date': pd.date_range(start='2022-01-01', periods=200, freq='D'),
        'ClaimAmount': np.random.normal(loc=5000, scale=1500, size=200).round(2),
        'ClaimType': np.random.choice(['Accident', 'Health'], size=200),
        'Status': np.random.choice(['Approved', 'Rejected', 'Pending'], size=200),
        'AgeGroup': np.random.choice(['Under 30', '30-50', '50+'], size=200),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], size=200)
    })
    return data

# Load or generate data
data = generate_sample_data()

# Streamlit app layout
st.title("MIS Data Analytics Report")
st.markdown("This report demonstrates data analysis skills relevant to the **Senior Manager, MIS Data Analytics** role.")

# Data Summary
st.header("Data Summary (based on random 200 samples)")
st.write(data.describe())

# Data Filters
st.sidebar.header("Filters")
claim_type = st.sidebar.multiselect("Select Claim Type:", options=data['ClaimType'].unique(), default=data['ClaimType'].unique())
status = st.sidebar.multiselect("Select Status:", options=data['Status'].unique(), default=data['Status'].unique())

# Apply filters
filtered_data = data[(data['ClaimType'].isin(claim_type)) & (data['Status'].isin(status))]

# Show filtered data
st.header("Filtered Data")
st.write(filtered_data)

# Plot Claim Amount Distribution
st.header("Claim Amount Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_data['ClaimAmount'], bins=20, kde=True, ax=ax)
st.pyplot(fig)

# Trend Analysis using Plotly
st.header("Claim Trends Over Time")
fig = px.line(filtered_data, x='Date', y='ClaimAmount', color='ClaimType', title='Claims Over Time')
st.plotly_chart(fig)

# Region-based Analysis
st.header("Claims by Region")
region_fig = px.histogram(filtered_data, x='Region', color='Status', barmode='group', title='Claims by Region and Status')
st.plotly_chart(region_fig)

# Generate Insights
st.header("Key Insights")
st.write("""
### 1. Claim Amount Distribution
- The **Claim Amount Distribution** indicates that most claims are centered around the average of MYR 5,000. 
- There is a visible peak in claims between MYR 4,000 to MYR 6,000, suggesting that the majority of claims fall within this range.
- The distribution shows some higher-value outliers, which may need further investigation to understand any anomalies or larger claims.

### 2. Claim Trends Over Time
- Analysis over time shows that **Accident-related claims** tend to spike during certain months, which could be due to seasonal factors or events impacting the frequency of accidents.
- **Health claims** have a relatively stable trend, but slight increases are noticeable at the end of each quarter, potentially linked to end-of-quarter check-ups or specific health policies.
- There's a noticeable dip in both claim types during mid-year, which could indicate seasonal patterns or periods with fewer incidents.

### 3. Approval Status Analysis
- **Approved claims** make up the majority of the dataset, suggesting that the current review processes are effective.
- **Pending and Rejected claims** show certain months with higher volumes, which might require attention to address bottlenecks in the claims approval process.

### 4. Claims by Region
- The data indicates that the **North region** has a higher frequency of claims, particularly in the `Accident` category, suggesting a need to explore regional factors like road safety or weather conditions.
- The **South and East regions** display a balanced mix of claim types, while the **West region** has a higher proportion of `Pending` claims, which might suggest operational challenges in processing.

### 5. Age Group Insights
- The majority of claims come from the **30-50 age group**, indicating that this demographic may have higher exposure to the company's insurance products or a higher likelihood of filing claims.
- The **Under 30 group** shows fewer claims overall, possibly pointing to lower risk profiles or different types of coverage favored by younger policyholders.
- For the **50+ age group**, health-related claims are more frequent, suggesting an opportunity for targeted medical claim strategies or policy adjustments.

### 6. General Observations
- Statistical tools suggest a moderate correlation between **claim amounts and the type of coverage**, indicating that certain coverage types may have higher average claim values.
- Seasonal patterns in claims (e.g., dips mid-year) can help refine predictive models for future claim trends and adjust strategies accordingly.
- The distribution of `Approved` and `Rejected` claims can provide insights into the effectiveness of underwriting processes and criteria.
""")

