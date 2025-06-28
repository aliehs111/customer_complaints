## Progress Notes

- Project structure organized with separate folders for data, notebooks, and source code.  
- `banking_complaints.csv` loaded into a DataFrame after computing `project_root`.  
- Data types and missing values inspected via `df.info()` and `df.isna().sum()`.  
- `Date Received` converted to datetime and monthly complaint volumes plotted.  
- `preprocessing()` function implemented to lowercase text, remove numbers/punctuation, drop stopwords, and lemmatize.  
- `clean_text` column created from `Complaint Description`.  
- TF-IDF vectorization applied to `clean_text`; `LogisticRegression` trained on raw Banking Product labels.  
- Classification report showed strong results on major classes and zero recall on low-support products.  
- Model retrained using `department` as the target for better class balance.  
- VADER sentiment analysis performed, producing `vader_compound` scores and `vader_label` categories.  
- Conda environment confirmed as `nlp-dev`; kernel restarted and all cells ran without errors.  
- Final VADER label distribution:
```
negative 3820
positive 2873
neutral 318
```
## After last class clarifications on the department vs the product
 - Need to map the department column to the product column.
 - I hadn't noticed the tabs in the excel file when I downloaded it as a csv.  So I went ahead and downloaded each tab's sheet as it's own csv.
 - Current tree:
 - (base) sheilamcgovern@MacBook-Pro customer_grievance % tree -L 2
```
.
├── data
│   ├── banking_complaints.csv
│   ├── data_dictionary.csv
│   ├── dept_product.csv
│   └── issues.csv
├── instructions.md
├── notebooks
│   └── 01_data_analysis.ipynb
└── src
    ├── __pycache__
    ├── data_utils.py
    └── preprocess.py 
```
 - worked through the mapping code
 - Merged `dept_product.csv` with the complaints DataFrame on `Banking Product`, creating a new `department` column.  
- Printed unique departments and discovered a few NaN entries for variant product names.  
- Defined a small synonym map to catch unmapped product variants (e.g. “Credit card” → “Credit Cards”, “Bank account or service” → “CASA”).  
- Applied the synonym map to fill all remaining NaN values in `department`, then verified that every row now has one of the seven business departments.  
- Confirmed the merge by printing `df.columns` and `df['department'].unique()`, ensuring no more missing values.  
- Saved these changes and prepared the df for downstream transformer evaluation and VADER‐based sentiment plotting.  
    
# updates 6-29-25

## 1. Data & Exploration
- **Loaded** `banking_complaints.csv`; checked dtypes and missing values.  
- **Date range:** from *{min_date}* to *{max_date}*; complaints per month plotted to reveal seasonality.

## 2. Text Preprocessing
- Applied lowercase, number/punctuation removal, stop-word filtering, and lemmatization.
- Created `clean_text` for modeling.

## 3. Department Routing Models
### 3.1 Classical (TF-IDF + LogisticRegression)
- **Tuned** via grid search (`C=10`, `ngram_range=(1,2)`, `max_features=20 000`).  
- **Accuracy:** 0.79  
- **Macro F1:** 0.78  
- **Confusion matrix:** key confusions between *Remittance* and *Credit Reports*.

### 3.2 Transformer (Zero-Shot BART-MNLI)
- **Demo** on 100 test samples:  
  - **Accuracy:** ~0.51  
  - **Macro F1:** ~0.50  
- Shows proof-of-concept; fine-tuning would be next logical step for production.

## 4. Sentiment Analysis (VADER)
- Computed `vader_compound` and binned into negative/neutral/positive.  
- **Overall distribution:**  

- **Trend plot:** average monthly compound score by department (see chart).

## 5. Business Recommendations
1. **Escalation rules**  
 - Complaints with compound ≤ –0.5 → immediate compliance flag.  
2. **Queue prioritization**  
 - Sort each department’s queue by negativity (compound ascending).  
3. **Trend monitoring dashboards**  
 - Monthly sentiment KPIs per department; alert on sudden dips.  
4. **Agent KPIs & recognition**  
 - Use positive-sentiment tickets to highlight outstanding service.

## 6. Next Steps
- Fine-tune a transformer on `(clean_text, department)` to boost routing accuracy.  
- Integrate additional customer metadata for richer feature sets.  
- Automate daily scoring and reporting in a dashboard.
