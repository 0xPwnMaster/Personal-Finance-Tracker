import pandas as pd
import numpy as np
from pathlib import Path

def clean_data(input_file, output_file):
    df = pd.read_csv(input_file)

    # Handle missing values
    df['Amount'] = df['Amount'].fillna(df['Amount'].mean())

    # Standardize formats
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Category'] = df['Category'].str.title()
    df['Amount'] = df['Amount'].round(2)

    # Remove outliers
    df = df[np.abs(df['Amount'] - df['Amount'].mean()) <= (3 * df['Amount'].std())]

    # Drop invalid dates
    df = df.dropna(subset=['Date'])

    # Ensure output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_file, index=False, date_format='%Y-%m-%d')
    print("Data cleaned and saved to", output_file)
    return df

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent  # Go to project root
    input_file = base_dir / 'data' / 'finance_data.csv'
    output_file = base_dir / 'data' / 'finance_data_cleaned.csv'

    clean_data(input_file, output_file)
