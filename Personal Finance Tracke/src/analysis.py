import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def analyze_data(input_file, des=None):
    df = pd.read_csv(input_file)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Drop invalid dates
    if df['Date'].isna().any():
        print("Warning: Some dates could not be parsed and will be dropped.")
        df = df.dropna(subset=['Date'])

    # Metrics
    monthly_summary = df.groupby([df['Date'].dt.to_period('M'), 'Category'])['Amount'].sum().unstack()
    monthly_summary.index = monthly_summary.index.astype(str)
    
    savings_rate = monthly_summary['Savings'] / monthly_summary['Salary'] * 100
    savings_rate.index = savings_rate.index.astype(str)
    
    expense_ratios = monthly_summary.drop('Salary', axis=1).div(monthly_summary.sum(axis=1), axis=0) * 100
    expense_ratios.index = expense_ratios.index.astype(str)

    # Output directory
    output_dir = des if des else Path.cwd()
    output_dir.mkdir(parents=True, exist_ok=True)

    # Visualizations
    plt.figure(figsize=(10, 6))
    monthly_summary.plot(kind='line')
    plt.title('Monthly Income and Expenses')
    plt.ylabel('Amount ($)')
    plt.tight_layout()
    plt.savefig(output_dir / 'monthly_trends.png')
    plt.close()

    plt.figure(figsize=(8, 8))
    monthly_summary.mean().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Average Expense Breakdown')
    plt.tight_layout()
    plt.savefig(output_dir / 'expense_breakdown.png')
    plt.close()

    print("Savings Rate (%):", savings_rate.mean())
    print("Expense Ratios (%):", expense_ratios.mean())
    return monthly_summary, savings_rate, expense_ratios

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent
    input_file = base_dir / 'data' / 'finance_data_cleaned.csv'
    des = base_dir / 'data'  # or base_dir / 'output' if you want output folder

    analyze_data(input_file, des)
