**Personal Finance Tracker and Budget Analysis**

A Python-based dashboard for tracking and analyzing personal income, expenses, and savings goals. Built with Pandas, Matplotlib, Seaborn, and Plotly, this project demonstrates skills in data cleaning, statistical analysis, and interactive data visualization. It provides actionable insights into financial habits, making it a practical tool for personal budgeting.
**Table of Contents**

Project Overview
Features
Dataset
Setup Instructions
Insights
Visualizations
Technologies Used
Future Improvements
License

**Project Overview**
This project simulates a real-world personal finance tool, enabling users to monitor income, expenses, and savings through an interactive dashboard. It processes a synthetic dataset, performs data cleaning, calculates key financial metrics (e.g., savings rate, expense ratios), and visualizes results using charts and an interactive Plotly dashboard. The repository is structured for clarity and reproducibility, making it ideal for showcasing on GitHub and resumes.
**Features**

Synthetic Data Generation: Creates a realistic dataset with monthly income, expenses, and savings.
Data Cleaning: Handles missing values, standardizes formats, and removes outliers.
Financial Analysis: Computes metrics like savings rate and expense ratios.
Visualizations: Generates line charts for trends, pie charts for expense breakdowns, and an interactive Plotly dashboard.
Insights: Provides actionable recommendations, e.g., identifying high discretionary spending.

**Dataset**
The synthetic dataset (data/finance_data.csv) includes:

Date: Monthly timestamp (e.g., 2024-01-01)
Category: Salary, Rent, Groceries, Utilities, Entertainment, Savings
Amount: Dollar amount (e.g., $500.23)
Description: Brief note (e.g., "Groceries expense")

**Setup Instructions**
1. Clone the Repo :
Clone the Repository:git clone https://github.com/your-username/PersonalFinanceTracker.git
cd PersonalFinanceTracker

2. Set Up Virtual Environment (Optional) :
Set Up Virtual Environment:python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. Install Dependencies :
Install Dependencies:pip install -r requirements.txt

4. Generate Synthetic Data :
Generate Synthetic Data:python src/data_generator.py

5. Run Analysis and Dashboard : 
Run Analysis and Dashboard:python src/dashboard.py

This generates visualizations (monthly_trends.png, expense_breakdown.png) and an interactive dashboard (dashboard.html) viewable in any browser.

**Insights**

Savings Rate: Approximately 20% of monthly income is allocated to savings, indicating a healthy savings habit.
Expense Breakdown: Discretionary spending (e.g., Entertainment) accounts for ~20% of total expenses, suggesting potential for optimization.
Trends: Rent and Utilities remain consistent, while Entertainment expenses fluctuate, highlighting areas for budget control.

**Visualizations**

Monthly Trends: Line chart showing income and expense trends over time.
Expense Breakdown: Pie chart illustrating the average distribution of expenses.
Interactive Dashboard: A Plotly dashboard combining all metrics, accessible via dashboard.html.View Dashboard Locally

**Technologies Used**

Python: Core programming language
Pandas: Data manipulation and analysis
Matplotlib/Seaborn: Static visualizations
Plotly: Interactive dashboard
Git: Version control

**Future Improvements**

Add support for user-uploaded financial data.
Integrate with APIs for real-time bank data (e.g., Plaid).
Enhance dashboard with filters for specific categories or date ranges.
Deploy dashboard to a public platform like Heroku or Tableau Public.

**License**
This project is licensed under the MIT License - see the LICENSE file for details.

Built by [Om Kadam]