# Financial Forensics Project

This project focuses on analyzing financial data to predict stock price movements using machine learning techniques. The analysis includes data preprocessing, feature engineering, and model building to understand market behavior and potential investment opportunities.

## Project Structure

```
├── T1_data/               # Training data files
│   ├── Annual_P_L_1.csv
│   ├── Annual_P_L_2.csv
│   ├── Balance_Sheet.csv
│   ├── Quarter_P_L_1.csv
│   ├── Quarter_P_L_2.csv
│   ├── cash_flow_statments.csv
│   ├── other_metrics.csv
│   ├── price.csv
│   ├── ratios_1.csv
│   └── ratios_2.csv
├── T2_data/               # Testing/Validation data files
│   ├── Annual_P_L_1.csv
│   ├── Annual_P_L_2.csv
│   ├── Balance_Sheet.csv
│   ├── Quarter_P_L_1.csv
│   ├── Quarter_P_L_2.csv
│   ├── cash_flow_statements.csv
│   ├── other_metrics.csv
│   ├── price.csv
│   ├── ratios_1.csv
│   └── ratios_2.csv
├── analysis.ipynb         # Main analysis notebook
├── merged_output_T1.csv  # Merged training data
└── merged_output_T2.csv  # Merged testing data
```

## Features

The analysis includes various financial metrics and indicators:

- Technical Indicators: RSI, MACD
- Institutional Holdings: FII and DII holding changes
- Market Metrics: Market Capitalization (current and historical)
- Financial Ratios: Quick ratio, Current ratio, Interest Coverage Ratio
- Cash Flow Metrics: Operating and Free cash flow
- Valuation Metrics: Industry PE, Historical PE, Industry PBV
- Performance Metrics: Return over 1 year and 5 years

## Data Preprocessing

1. Data Merging: Multiple CSV files are merged based on company names
2. Missing Value Handling: Filled with zeros and converted to int64
3. Feature Normalization: MinMaxScaler applied to numeric features
4. Target Variable: Percentage increase from current price

## Model Development

- Train-Test Split: 80-20 split with random_state=42
- Features: Normalized financial metrics
- Target: Price movement prediction

## Usage

1. Clone the repository
2. Install required dependencies:
   ```
   pip install pandas numpy scikit-learn
   ```
3. Open and run `analysis.ipynb` in Jupyter Notebook

## Result

<img width="976" alt="image" src="https://github.com/user-attachments/assets/415d264a-04c2-4e07-9505-5b54c0a57fe9" />


