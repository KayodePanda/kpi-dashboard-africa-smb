## Live App
You can try the dashboard here: https://kayodepanda-kpi-dashboard-africa-smb-dashboardapp-87v1wz.streamlit.app/

# KPI Dashboard for African Small Businesses

This project is a browser-based financial dashboard built with Python and Streamlit, designed to help small African businesses track key financial and customer performance indicators. It allows users to upload structured CSV files and automatically calculates KPIs including Profit, Customer Acquisition Cost (CAC), Lifetime Value (LTV), Churn Rate, and Revenue per Customer.

The dashboard is fully interactive and generates visual summaries such as revenue trends, expense tracking, and customer behavior patterns. Although the data used is simulated, the logic and layout are designed to reflect realistic SME financial performance.

The codebase is modular and extensible, making it suitable for adaptation to more complex or real-world datasets.

## Dashboard Preview
images/dashboard_preview.png

## About Me

My name is Kayode Olorunmaiye. I have an academic background in data science and economics, and I focus on solving real-world business problems through data. My interest lies in building tools that help businesses make smarter decisions, especially in environments where access to professional analytics is limited.This project reflects that goal. 
I designed and built this dashboard to give small African businesses better insight into their financial performance using metrics like profit, CAC, LTV, and churn. It’s a modular, browser-based tool that simplifies financial analysis without requiring technical expertise. I’m continuing to explore ways that data can support business growth at all levels.


## What This Dashboard Shows

- Revenue, Expenses, and Profit analysis
- CAC (Customer Acquisition Cost), LTV (Lifetime Value), Profit Margin
- Customer Growth Rate
- Easy-to-read charts + tables
- Interactive Streamlit web app

---

## 📁 Folder Structure

kpi-dashboard-africa-smb/
├── dashboard/               # Streamlit app (main script)
├── data/                    # Sample financial data (CSV)
├── notebooks/               # Jupyter notebooks for KPI logic and testing
├── scripts/                 # Optional helper scripts (modular codebase)
├── images/                  # All project screenshots
│   ├── dashboard_preview.png      # Main app layout preview
│   ├── revenue_expenses_chart.png # Revenue vs. Expenses chart
│   ├── profit_trend_chart.png     # Monthly profit trend chart
│   ├── cac_ltv_chart.png          # CAC vs. LTV comparison
│   ├── customer_growth_chart.png  # Customer growth over time
│   └── customer_churn_rate.png    # Monthly churn rate
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation




## KPI Preview

Here’s a snapshot of KPIs based on a sample dataset of monthly revenue and customer growth:

  Month	    Revenue	 Expenses  Profit  Total Customers	 CAC	    Revenue per Customer   LTV	    Churn Rate (%)
Jan 2023	10,000	 7,000	  3,000	    150	             140.00	       66.67	           800.00	      6.67
Feb 2023	12,000	 7,500	  4,500	    200	             125.00	       60.00	           720.00	      6.00
Mar 2023	15,000	 8,000	  7,000	    258	             114.29	       58.14	           697.67	      5.81
Apr 2023	17,000	 8,500	  8,500	    323	             106.25	       52.63	           631.58	      5.26
May 2023	20,000	 9,000	  11,000	396	             100.00	       50.51	           606.06	      5.01

##  Visual Output

The dashboard includes several visualizations to give users a quick overview of performance trends.
Here are some of the visual insights generated from this project:

###  Revenue vs Expenses Over Time  
Displays monthly revenue and expenses side-by-side to highlight profitability trends.
images/revenue_expenses_chart.png

### CAC vs LTV  
Visualizes the relationship between Customer Acquisition Cost and Lifetime Value to assess customer profitability.
images/cac_ltv_chart.png

## Profit Trend
Shows the progression of net profit over the selected time period.
images/profit_trend_chart.png

## Customer Growth Over Time
Tracks the number of total customers each month, reflecting business expansion.
images/customer_growth_chart.png

## Customer Churn Rate

Represents the monthly churn rate percentage, helping identify customer retention trends.
images/customer_churn_rate.png


---

##  Tools Used

- Python
- Pandas
- Jupyter Notebook
- Matplotlib
- Streamlit
- Git & GitHub

---

## How to Run the App

Make sure you have Python and streamlit installed (version 3.8 or above is recommended).
Clone the repository:

```bash
git clone https://github.com/KayodePanda/kpi-dashboard-africa-smb.git
cd kpi-dashboard-africa-smb

#Install the required packages 
pip install -r requirements.txt

#Run the streamlit app 
streamlit run dashboard/app.py




- Interactive Streamlit web app

