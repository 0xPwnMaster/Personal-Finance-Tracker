import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from pathlib import Path

def generate_finance_data():
    start_date = datetime(2024, 1, 1)
    dates = [start_date + timedelta(days=30 * i) for i in range(12)]
    categories = ['Salary', 'Rent', 'Groceries', 'Utilities', 'Entertainment', 'Savings']
    
    data = []
    for date in dates:
        for category in categories:
            if category == 'Salary':
                amount = random.uniform(3000, 5000)
            elif category == 'Savings':
                amount = random.uniform(500, 1500)
            else:
                amount = random.uniform(100, 1000)
            data.append({
                'Date': date.strftime('%Y-%m-%d'),
                'Category': category,
                'Amount': round(amount, 2),
                'Description': f"{category} expense"
            })
    
    # Resolve path relative to project root (../data/finance_data.csv)
    base_dir = Path(__file__).resolve().parent.parent
    des_path = base_dir / 'data' / 'finance_data.csv'

    df = pd.DataFrame(data)
    des_path.parent.mkdir(parents=True, exist_ok=True)  # Ensure directory exists
    df.to_csv(des_path, index=False)
    
    print(f"Synthetic data generated and saved to {des_path}")

if __name__ == "__main__":
    generate_finance_data()
