# ATM Cash Withdrawal Forecasting

This repository contains experiments on forecasting daily ATM cash withdrawals using machine learning and deep learning models.  
The work is based on the paper *"Calendar, Holiday, and Temporal Features for ATM Demand: Modeling, Zero Handling, and Clustering Effects"*.

## 📁 Repository Structure
```markdown
├── environment.yml
├── LICENSE
├── README.md
├── notebooks/
│   ├── preliminary_data_analysis.ipynb
│   ├── models_with_zero_handling.ipynb
│   └── models_without_zero_handling.ipynb
├── results/
│   └── standardized_models_results.xlsx
```

## 📌 Motivation
Efficient ATM cash management is critical for banks. Overstocking increases idle cash, insurance, and transportation costs, while understocking leads to service failures and emergency replenishments. Accurate short-term forecasting helps banks balance these trade-offs.

## 📂 Contents
- `environment.yml` — Conda environment specification (Python 3.12.10, PyTorch 2.6.0 with CUDA 12.1, XGBoost, scikit-learn, Optuna).
- `preliminary_data_analysis.ipynb` — Exploratory data analysis of ATM withdrawal data.
- `models_with_zero_handling.ipynb` — Notebook with models trained after removing zero-withdrawal sequences.
- `models_without_zero_handling.ipynb` — Notebook with models trained on raw data including zeros.
- `standardized_models_results.xlsx` — Collected model results in a standardized format for easier comparison.
- `LICENSE` — Open-source license for the codebase.

> 📌 The research paper describing methodology and results is **submitted separately by email**.

## 🗂 Dataset
- 31 ATMs from a large Turkish city.  
- Time span: 2 years and 2 months.  
- Some ATMs activated late → zero periods (due to outages, pre-activation, or stock-outs).  
- Features engineered:
  - **Calendar effects**: day of week, day of month, month, holidays, half-days.  
  - **Temporal effects**: lagged values (1, 2, 3, 7, 14, 28 days), rolling mean/std.  
  - **Clusters**: ATMs grouped into 2–4 demand-level clusters using k-means.  

## 🤖 Models
Four model families were tested under identical splits:
- **Linear Regression** — baseline, transparent and interpretable.  
- **XGBoost** — gradient-boosted trees for structured tabular features.  
- **LSTM** — sequence model for capturing temporal dependencies.  
- **N-BEATS** — neural architecture for time-series forecasting.  

Hyperparameters for all models were tuned with **Optuna**.

## 🔬 Experiments
The notebooks test different design choices:
- **Feature sets**: raw values, calendar features, temporal features, combined features.  
- **Sequence lengths**: 7, 14, 28, 84 (depending on feature set).  
- **Zero handling**: keeping vs. excluding zero-withdrawal periods.  
- **Clustering**: global models vs. cluster-based models (k=2, 3, 4).  

Evaluation metrics:
- **SMAPE** (Symmetric Mean Absolute Percentage Error)  
- **MAE** (Mean Absolute Error)  

## 🚀 Setup

Create and activate the environment:
```bash
conda env create -f environment.yml
conda activate ml-gpu-env
```

Start Jupyter:
```bash
jupyter notebook
```

## ▶️ How to Run

Run the notebooks in the following order:

1. **Preliminary Analysis**  
   - Open `preliminary_data_analysis.ipynb`  
   - Explore the dataset  
   - Check ATM-level differences and calendar/holiday effects  

2. **Models With Zero Handling**  
   - Open `models_with_zero_handling.ipynb`  
   - Train and evaluate models with zero sequences removed  

3. **Models Without Zero Handling**  
   - Open `models_without_zero_handling.ipynb`  
   - Train and evaluate models using raw data including zeros  

4. **Standardized Results**  
   - Review `standardized_models_results.xlsx`  
   - Contains organized performance metrics from all tested models  
   - Makes it easier to compare across feature sets, clustering, and zero handling  

⚠️ **Note:** Training with Optuna can take a long time since it runs multiple trials.  
For quick code tryouts, reduce the number of Optuna trials (e.g., set trials to 5 instead of 100).  


> 🔁 Each notebook is self-contained: rerun all cells from top to bottom to reproduce results.





