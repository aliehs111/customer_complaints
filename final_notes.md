## Progress Notes (Updated 6-28-25)

### 1. Data & Exploration
- Loaded `banking_complaints.csv` and `dept_product.csv`; checked dtypes and missing values.
- Merged datasets on `Banking Product` to create `department` column; applied synonym map for variants (e.g., “Credit card” → “Credit Cards”).
- Filtered out `Others` department (1 sample) to avoid sampling errors.
- **Date range**: Jan 1, 2023, to Oct 21, 2023; plotted monthly complaint volumes.

### 2. Text Preprocessing
- Implemented `preprocess_text()`: lowercase, remove numbers/punctuation, drop stopwords, lemmatize.
- Created `clean_text` from `Complaint Description`.
- Fixed `KeyError: 'Complaint Text'` by using correct column name.
- Resolved `LookupError: punkt_tab` with `nltk.download('punkt_tab')`.

### 3. Department Routing Models
#### 3.1 Classical (TF-IDF + LogisticRegression)
- Tuned via grid search (`C=10`, `ngram_range=(1,2)`, `max_features=20,000`).
- **Accuracy**: 0.79
- **Macro F1**: 0.78
- Key confusions: *Remittance* vs. *Credit Reports*.

#### 3.2 Transformer (Zero-Shot BART-MNLI)
- Used `facebook/bart-large-mnli` on 100 test samples (after filtering `Others`).
- Simplified prompts, used 3 few-shot examples per department.
- Fixed `ValueError` in `train_test_split` by removing `stratify`.
- Fixed `SettingWithCopyWarning` with `df.loc`.
- **Accuracy**: 0.58 (up from 0.51, but below TF-IDF’s 0.79).
- **Macro F1**: 0.558 (up from 0.50).
- Misclassifications (e.g., CASA → Credit Cards) indicate domain mismatch; fine-tuning recommended.
- Attempted fine-tuning DistilBERT but hit `ValueError: fp16 mixed precision` on MPS; needs `fp16=False` or GPU.

### 4. Sentiment Analysis (VADER)
- Computed `vader_compound` scores and binned into:
  - Negative: 3,820
  - Positive: 2,873
  - Neutral: 318
- Plotted average monthly compound scores by department.

### 5. Business Recommendations
1. **Escalation Rules**: Flag complaints with `vader_compound` ≤ -0.5 for Compliance.
2. **Queue Prioritization**: Sort department queues by ascending `vader_compound`.
3. **Trend Monitoring**: Automate weekly sentiment dashboards; alert on dips.
4. **Agent KPIs**: Reward agents with high positive-sentiment resolutions.

### 6. Next Steps
- Fine-tune DistilBERT with `fp16=False` or on a GPU to exceed 79% accuracy.
- Analyze `zero_shot_predictions.csv` for misclassification patterns.
- Finalize write-up with zero-shot results (58% accuracy) and note fine-tuning potential.
- Complete automation pipeline for daily complaint processing.