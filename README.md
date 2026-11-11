# Gold Price Prediction using Linear Regression

**Gold Price (GLD) prediction using Multiple Linear Regression on the Gold Price dataset.**  
Analyzes how S&P 500 (SPX), Crude Oil (USO), Silver (SLV), and EUR/USD exchange rates impact gold prices using Python (`pandas`, `numpy`, `matplotlib`, `seaborn`, and `scikit-learn`).

---

## Team and Roles

| Member | Entry No. | Role | GitHub Handle |
| :--- | :--- | :--- | :--- |
| Rahul Kumar | `2026AIB1071` | Documentation Lead | [@rahulforcode89](https://github.com/rahulforcode89) |
| Vineet Singh Lodhi | `2026EEB1425` | Execution Lead | [@VINEETSINGHLODHI](https://github.com/VINEETSINGHLODHI) |
| Member 3 | `2026MCB1546` | PPT Lead | [@Manrojloveslemons](https://github.com/Manrojloveslemons) |
| Member 4 | `2026ESB1474` | Video Lead | [@2026esb1474-ui](https://github.com/2026esb1474-ui) |

*All four members contributed code to this repository (see commit history).*

---

## Project Structure

```text
Gold-price-prediction-using-Linear-Regression/
├── data/
│   └── gold_price_data.csv              # Kaggle Gold Price dataset (1,718 rows, 81 columns)
├── codes/
│   ├── program.py                       # Main entry-point Python script
│   └── program.ipynb                    # Jupyter Notebook showcasing inline outputs & plots
├── outputs/                             # Saved exploratory & regression plots
│   ├── gold_price_distribution.png      # Distribution of Gold ETF (Adj Close) prices
│   ├── feature_vs_gold_scatter.png      # Gold Price vs Gold Miners ETF (GDX_Close)
│   ├── correlation_heatmap.png          # Correlation heatmap across key economic indicators
│   └── predicted_vs_actual.png          # Actual vs Predicted Gold Prices scatter plot
├── docs/
│   ├── Team_Slides.pdf                  # 5-slide project presentation (PDF)
├── requirements.txt                     # Pinned Python package dependencies
└── README.md                            # Project documentation
```

---

## Setup

Tested on Python 3.10 and Python 3.11 (Windows, macOS, and Linux).

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/rahulforcode89/Gold-price-prediction-using-Linear-Regression.git](https://github.com/rahulforcode89/Gold-price-prediction-using-Linear-Regression.git)
   cd Gold-price-prediction-using-Linear-Regression
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## How to Run

1. **Run the Python script from the root of the repository:**
   ```bash
   python codes/program.py
   ```
   *(Alternatively, open `codes/program.ipynb` in VS Code or Jupyter Notebook to view interactive cell-by-cell outputs and plots.)*

2. **What the script does:**
   - Loads `data/gold_price_data.csv` and removes duplicate entries.
   - Generates exploratory visualizations and a correlation heatmap analyzing how S&P 500 (`SP_close`), Dow Jones (`DJ_close`), Crude Oil (`USO_Close`), Silver (`SF_Price`), US Dollar Index (`USDI_Price`), and Gold Miners ETF (`GDX_Close`) correlate with Gold prices (`Adj Close`).
   - Preprocesses numeric and categorical features using Scikit-Learn's `ColumnTransformer`, `SimpleImputer`, and `OneHotEncoder` inside a `Pipeline` (preventing target leakage).
   - Trains a Multiple `LinearRegression` model on an 80/20 train-test split (`random_state=42`).
   - Prints evaluation metrics (`MAE`, `MSE`, `RMSE`, `R²`) and saves all diagnostic plots to `outputs/`.

### Expected Output

```text
Dataset shape (rows, columns): (1718, 81)
Saved outputs/gold_price_distribution.png
Saved outputs/feature_vs_gold_scatter.png
Training examples: 1374
Testing examples: 344
Model training completed!
MAE  : 1.747
MSE  : 4.865
RMSE : 2.206
R²   : 0.984
Saved outputs/predicted_vs_actual.png
Saved outputs/correlation_heatmap.png
Correlation with Adj Close:
GDX_Close     0.98
SF_Price      0.95
USO_Close     0.64
USB_Price    -0.44
DJ_close     -0.59
SP_close     -0.68
USDI_Price   -0.72
Name: Adj Close, dtype: float64
```

---

## Links

- **Presentation Slides (5 Slides):** [`docs/Team_Slides.pdf`](docs/Team_Slides.pdf)
- **YouTube Video Demonstration (Max 5:00):** [Watch Project Demo on YouTube](https://youtu.be/YOUR_VIDEO_ID_HERE)

---

## AI-Use Disclosure

Gemini and Claude were used to assist in formatting the `README.md` documentation template, structuring the project directory tree, and refining the Matplotlib/Seaborn visualization snippets in `codes/program.py` and `codes/program.ipynb`. All data preprocessing, feature selection, Multiple Linear Regression modeling, and evaluation metrics were thoroughly reviewed, tested, and verified by all four team members and are explained in the video demonstration. No AI tools were used to fabricate the dataset or the experimental results.
