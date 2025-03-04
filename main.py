import streamlit as st
import pandas as pd
import os

# Application title
st.title("Statistics and Probability Questions Based on Amazon Stock Data")

# Question instructions
st.markdown("""
---

1. Calculate the mean, median, and standard deviation of Amazon's closing price during 2024.

2. Calculate the range, variance, and standard deviation of Amazon's trading volume in 2024. What conclusions can be drawn from these results?

---

3. Categorize Amazon's 2024 closing prices into three groups:  
   - **Low:** Closing price < 1st Quartile (Q1)  
   - **Medium:** Closing price between 1st Quartile (Q1) and 3rd Quartile (Q3)  
   - **High:** Closing price > 3rd Quartile (Q3)  
   Determine the empirical probability for each category based on 2024 data.

4. Create a probability distribution for trading volume in 2024 by dividing it into discrete intervals (e.g., low, medium, high). Ensure the total probability equals 1.

---

5. Create the following visualizations:
   - Histogram of Amazon's 2024 closing prices
   - Boxplot to analyze the distribution of 2024 closing prices
   - Time Series Plot showing closing price trends from January 2024 to December 2024

---

6. Test whether Amazon's 2024 closing price data follows a normal distribution using:
   - Q-Q Plot
   - Normality test (e.g., Shapiro-Wilk test)

7. Provide conclusions based on the normality test results.

---

**Data:**  
Download Amazon stock data from:  
[Amazon Stock Data 2025 (Kaggle)](https://www.kaggle.com/datasets/umerhaddii/amazon-stock-data-2025/data)
""")

file_path = "AMZN_1997-05-15_2025-02-21.csv"

if os.path.exists(file_path):
    # Set pandas display precision
    pd.set_option('display.precision', 20)
    
    # Read CSV file
    df = pd.read_csv(file_path)
    
    st.subheader("Full Dataset")
    st.dataframe(df)  # Interactive table with scrollbar
    
    st.write(f"**Data Dimensions:** {df.shape[0]} rows x {df.shape[1]} columns")
else:
    st.error(f"File '{file_path}' not found in the current directory.")
    
st.markdown("""
### Column Descriptions

- **date**  
  Trading date
  
- **open**  
  Opening price
  
- **high**  
  Daily highest price
  
- **low**  
  Daily lowest price
  
- **close**  
  Adjusted closing price (accounting for splits)
  
- **adj_close**  
  CRSP-adjusted closing price (includes splits and dividends)
  
- **volume**  
  Number of shares traded daily
""")


st.title("Statistical Analysis Results for Amazon Stock in 2024")

st.markdown("""
### Closing Price Statistics
- **Mean:** 184.63  
- **Median:** 183.43  
- **Standard Deviation:** 17.43  

### Trading Volume Statistics
- **Range:** 126,440,900  
- **Variance:** 2.64 × 10¹⁴  
- **Standard Deviation:** 16,254,293.29  

### Conclusions

**Closing Price:**
- Average closing price: \$184.63
- Near-symmetric distribution (mean ≈ median)
- Significant price fluctuations (SD \$17.43)

**Trading Volume:**
- Extreme range (126 million shares)
- High variance indicates substantial daily trading volatility
- Demonstrates intense market activity fluctuations

---
""")

st.markdown("""
### Closing Price Categorization

**Quartile Values:**
- **1st Quartile (Q1):** 25th percentile closing price
- **3rd Quartile (Q3):** 75th percentile closing price

**Results:**
- **Low:** 63 days (25% of trading days)
- **Medium:** 126 days (50% of trading days)
- **High:** 63 days (25% of trading days)

**Conclusion:**  
50% of trading days fell into the *Medium* category, while 25% each were *Low* and *High*. Total probability sums to 1 (100%), satisfying probability distribution requirements.

---

### Trading Volume Probability Distribution

**Results:**
- **Medium Volume:** 50%
- **Low Volume:** 25%
- **High Volume:** 25%

**Conclusion:**  
Trading volume predominantly falls into the *Medium* category, with equal probabilities (25%) for *Low* and *High* volumes.

---

### Data Visualizations
""")

# Visualization images
image_files = ["histo ing.png", "boxxplot ing.png", "time ing.png"]

for img in image_files:
    if os.path.exists(img):
        st.image(img, caption=f"Visualization for Question 5: {img.split('.')[0]}", use_container_width=True)
    else:
        st.error(f"Image '{img}' not found in current directory.")

st.markdown("""
**Histogram:**  
- Displays frequency distribution of closing prices  
- Reveals price distribution across value ranges  

**Boxplot:**  
- Shows price distribution, median, and potential outliers  
- Highlights extreme fluctuations  

**Time Series Plot:**  
- Illustrates price trends throughout 2024  
- Helps identify upward/downward patterns  
""")


st.markdown("""
---
### Normality Test Results
""")

if os.path.exists("qq ing.png"):
    st.image("qq.png", caption="Q-Q Plot for Normality Test", use_container_width=True)
else:
    st.error("Q-Q Plot image not found.")

st.markdown("""
📌 **Q-Q Plot Interpretation**  
- Central data points align with the red line, suggesting near-normality  
- Deviations in lower/upper tails indicate skewness/outliers  
- Left tail: More low-price outliers than expected  
- Right tail: More high-price outliers than expected  

**Shapiro-Wilk Test Results**  
data: amazon_2024$close  
W = 0.94885, p-value = 9.915e-08  

📌 **Analysis**  
- p-value = 9.915e-08 (< 0.05) → ❌ Reject normality  
- W = 0.94885 suggests near-normal distribution with deviations  
- Combined with Q-Q Plot: Non-normal distribution with skewness  
""")


st.markdown("""
---
### Final Conclusions

1. **Shapiro-Wilk Test**  
   p-value < 0.05 → Strong evidence against normality  
   W value (0.94885) indicates slight proximity to normality but significant deviations  

2. **Q-Q Plot**  
- Tailed deviations confirm skewness  
- Central alignment cannot compensate for tail outliers  

📌 **Final Conclusion**  
Amazon's 2024 closing prices do NOT follow a normal distribution (p-value < 0.05). Observed skewness and outliers make parametric tests inappropriate for this dataset.
""")
