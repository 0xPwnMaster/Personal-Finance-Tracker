Personal Finance Tracker and Budget Analysis
A Python-based dashboard to track and analyze personal income, expenses, and savings goals using a synthetic dataset. Built with Pandas, Matplotlib, Seaborn, and Plotly, this project showcases data cleaning, analysis, and interactive visualization skills.
Features

Data Generation: Creates a synthetic dataset with monthly income, expenses, and savings.
Data Cleaning: Handles missing values, standardizes formats, and removes outliers.
Analysis: Calculates savings rate and expense ratios.
Visualizations: Includes line charts for trends, pie charts for expense breakdown, and an interactive Plotly dashboard.
Insights: Provides actionable insights, e.g., "20% of income goes to discretionary spending."

Dataset
The synthetic dataset (data/finance_data.csv) includes:

Date: Monthly timestamp
Category: Salary, Rent, Groceries, Utilities, Entertainment, Savings
Amount: Dollar amount
Description: Brief note

Setup Instructions

Clone the Repository:git clone https://github.com/your-username/PersonalFinanceTracker.git
cd PersonalFinanceTracker


Set Up Virtual Environment:python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate


Install Dependencies:pip install -r requirements.txt


Generate Data:python src/data_generator.py


Run Analysis and Dashboard:python src/dashboard.py

This generates visualizations (monthly_trends.png, expense_breakdown.png) and an interactive dashboard (dashboard.html).

Insights

Savings Rate: On average, ~20% of income is saved monthly.
Expense Breakdown: Discretionary spending (e.g., Entertainment) accounts for ~20% of total expenses.
Trends: Utilities and Rent are consistent, while Entertainment varies significantly.

Screenshots
View Interactive Dashboard
Technologies Used

Python (Pandas, Matplotlib, Seaborn, Plotly)
Git for version control

Future Improvements

Add user input for custom data.
Integrate with real financial APIs.
Enhance dashboard with filters for specific categories.
