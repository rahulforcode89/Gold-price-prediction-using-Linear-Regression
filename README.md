Gold Price Prediction Using Multiple Linear Regression

Gold Price (GLD) prediction using Multiple Linear Regression on the Gold Price dataset.

This project analyzes how economic indicators such as S&P 500 (SPX), Crude Oil (USO), Silver (SLV), and EUR/USD exchange rates influence gold prices using Python libraries including "pandas", "numpy", "matplotlib", "seaborn", and "scikit-learn".

---

Team and Roles

Member| Entry No.| Role| GitHub Handle
Rahul Kumar| "2026AIB1071"| Documentation Lead| "@rahulforcode89" (https://github.com/rahulforcode89)
Vineet Singh Lodhi| "2026EEB1425"| Execution Lead| "@VINEETSINGHLODHI" (https://github.com/VINEETSINGHLODHI)
Member 3| "2026MCB1546"| PPT Lead| "@Manrojloveslemons" (https://github.com/Manrojloveslemons)
Member 4| "2026ESB1474"| Video Lead| "@2026esb1474-ui" (https://github.com/2026esb1474-ui)

All four members contributed code to this repository (see commit history).

---

Project Structure

Gold-price-prediction-using-Linear-Regression/
│
├── data/
│   └── gold_price_data.csv
│
├── codes/
│   ├── program.py
│   └── program.ipynb
│
├── outputs/
│   ├── gold_price_distribution.png
│   ├── feature_vs_gold_scatter.png
│   ├── correlation_heatmap.png
│   └── predicted_vs_actual.png
│
├── docs/
│   └── gold_price_data_ppt.pdf
│
├── requirements.txt
└── README.md

---

Requirements

- Python 3.10 or Python 3.11
- VS Code (recommended) or Jupyter Notebook
- Python extension for VS Code
- Jupyter extension for VS Code

---

Installation and Setup

1. Clone the repository

Open a terminal and execute:

git clone https://github.com/rahulforcode89/Gold-price-prediction-using-Linear-Regression.git

Navigate to the project directory:

cd Gold-price-prediction-using-Linear-Regression

2. Create a virtual environment

It is recommended to create a virtual environment to keep project dependencies separate.

python -m venv .venv

Activate the environment:

Windows:

.venv\Scripts\activate

macOS/Linux:

source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

Install Jupyter kernel support:

pip install ipykernel jupyter

---

How to Run the Project

Method 1: Using VS Code (Recommended)

1. Open the cloned project folder in VS Code.

2. Make sure the Python and Jupyter extensions are installed.

3. Navigate to:
   
   "codes/program.ipynb"

4. Open the notebook.

5. Click Select Kernel in the top-right corner.

6. Choose Python Environments.

7. Select the project's ".venv" environment.

8. Run the notebook cells individually using the play button or select Run All to execute the complete notebook.

Important: Open the repository's root folder in VS Code rather than opening only the "codes" folder. This helps maintain the correct relative paths to the dataset and output directory.

Method 2: Using Jupyter Notebook in a Browser

After activating the virtual environment and installing the dependencies, execute:

jupyter notebook

1. Jupyter will open in your browser.
2. Navigate to the "codes" folder.
3. Open "program.ipynb".
4. Execute the cells sequentially using Shift + Enter.

Method 3: Running the Python Script (Alternative)

The project also includes a standalone Python script.

From the repository's root directory, execute:

python codes/program.py

---

What Does the Project Do?

The notebook performs the following operations:

1. Data Loading: Loads the Kaggle Gold Price dataset containing 1,718 rows and 81 columns.
2. Data Cleaning: Removes duplicate entries and prepares the dataset for analysis.
3. Exploratory Data Analysis (EDA): Generates visualizations to understand gold price distributions and relationships with economic indicators.
4. Correlation Analysis: Examines relationships between gold prices and indicators such as:
   - S&P 500 ("SP_close")
   - Dow Jones ("DJ_close")
   - Crude Oil ("USO_Close")
   - Silver ("SF_Price")
   - US Dollar Index ("USDI_Price")
   - Gold Miners ETF ("GDX_Close")
5. Data Preprocessing: Uses "ColumnTransformer", "SimpleImputer", and "OneHotEncoder" to handle missing values and categorical features.
6. Model Training: Trains a Multiple Linear Regression model using an 80/20 train-test split with "random_state=42".
7. Model Evaluation: Evaluates the model using MAE, MSE, RMSE, and R².
8. Visualization: Generates actual-versus-predicted plots and correlation heatmaps.

---

Expected Output

Dataset shape (rows, columns): (1718, 81)
Training examples: 1374
Testing examples: 344

Model training completed!

MAE  : 1.747
MSE  : 4.865
RMSE : 2.206
R²   : 0.984

Correlation with Adj Close:
GDX_Close     0.98
SF_Price      0.95
USO_Close     0.64
USB_Price    -0.44
DJ_close     -0.59
SP_close     -0.68
USDI_Price   -0.72

Note: Actual output may vary slightly depending on the environment and library versions.

---

Generated Outputs

The project generates and saves the following visualizations in the "outputs/" directory:

File| Description
"gold_price_distribution.png"| Distribution of gold prices
"feature_vs_gold_scatter.png"| Relationship between gold price and GDX_Close
"correlation_heatmap.png"| Correlation between economic indicators
"predicted_vs_actual.png"| Comparison of actual and predicted gold prices

---

Troubleshooting

1. Kernel not found in VS Code

- Activate the project's ".venv" environment.
- Install "ipykernel" using "pip install ipykernel".
- Restart VS Code and select the correct Python kernel.

2. ModuleNotFoundError

Install the required packages:

pip install -r requirements.txt

3. Dataset or file not found

Make sure you have opened the repository's root directory in VS Code and that "gold_price_data.csv" exists inside the "data/" folder.

4. Plots are not appearing

Run the notebook cells sequentially and ensure that Matplotlib and Seaborn are installed.

---

Project Resources

- Presentation (PDF): ""docs/gold_price_data_ppt.pdf"" (docs/gold_price_data_ppt.pdf)
- Jupyter Notebook: ""codes/program.ipynb"" (codes/program.ipynb)
- Python Script: ""codes/program.py"" (codes/program.py)
- Video Demonstration: "Watch Project Demo on YouTube" (https://youtu.be/YOUR_VIDEO_ID_HERE)

---

AI-Use Disclosure

Gemini and Claude were used to assist in formatting the README documentation, structuring the project directory, and refining Matplotlib/Seaborn visualization snippets in the Python script and Jupyter Notebook.

All data preprocessing, feature selection, Multiple Linear Regression modeling, and evaluation metrics were reviewed, tested, and verified by the four team members and are explained in the video demonstration. No AI tools were used to fabricate the dataset or experimental results.
