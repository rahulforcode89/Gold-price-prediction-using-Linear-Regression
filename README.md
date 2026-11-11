<div align="center">

#  Gold Price Prediction Using Multiple Linear Regression

Predicting Gold Price (GLD) from economic indicators using Python and scikit-learn.

![Python](https://img.shields.io/badge/Python-3.10%20|%203.11-3776AB?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikit-learn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![R²](https://img.shields.io/badge/R²-0.984-success)

</div>

---

##  Overview

This project analyzes how economic indicators such as **S&P 500 (SPX)**, **Crude Oil (USO)**, **Silver (SLV)**, and **EUR/USD exchange rates** influence gold prices. It uses `pandas`, `numpy`, `matplotlib`, `seaborn`, and `scikit-learn`.

## 📑 Table of Contents

- [Team and Roles](#-team-and-roles)
- [Project Structure](#-project-structure)
- [Requirements](#-requirements)
- [Installation and Setup](#-installation-and-setup)
- [How to Run](#-how-to-run-the-project)
- [Project Workflow](#-project-workflow)
- [Features Used](#-important-features-used)
- [Expected Output](#-expected-output)
- [Visualizations](#-generated-visualizations)
- [Troubleshooting](#-troubleshooting)
- [Project Resources](#-project-resources)
- [AI-Use Disclosure](#-ai-use-disclosure)

---

##  Team and Roles

| Member | Entry No. | Role | GitHub |
|--------|-----------|------|--------|
| Rahul Kumar | `2026AIB1071` | Documentation Lead | [@rahulforcode89](https://github.com/rahulforcode89) |
| Vineet Singh Lodhi | `2026EEB1425` | Execution Lead | [@VINEETSINGHLODHI](https://github.com/VINEETSINGHLODHI) |
| Member 3 | `2026MCB1546` | PPT Lead | [@Manrojloveslemons](https://github.com/Manrojloveslemons) |
| Member 4 | `2026ESB1474` | Video Lead | [@2026esb1474-ui](https://github.com/2026esb1474-ui) |

> All four members contributed code to this repository (see commit history).

---

##  Project Structure

```text
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
```

---

## Requirements

| Requirement | Version / Details |
|-------------|-------------------|
| Python | 3.10 or 3.11 |
| Code Editor | VS Code (recommended) |
| Python Extension | Required for Python support |
| Jupyter Extension | Required for notebook support |
| Jupyter Kernel | `ipykernel` |

---

##  Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/rahulforcode89/Gold-price-prediction-using-Linear-Regression.git
cd Gold-price-prediction-using-Linear-Regression
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt)**

```bat
.venv\Scripts\activate.bat
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
or try
```bash
python -m pip install -r requirements.txt
```


Install Jupyter kernel support:

```bash
pip install ipykernel jupyter
```
or try
```bash
python -m pip install --upgrade pip setuptools wheel
```

---

## ▶️ How to Run the Project

### Method 1: VS Code (Recommended)

1. Open the cloned repository folder in VS Code.
2. Install the **Python** and **Jupyter** extensions if needed.
3. Open `codes/program.ipynb`.
4. Click **Select Kernel** in the top-right corner.
5. Select **Python Environments**.
6. Choose the interpreter from the project's `.venv` environment.
7. Click **Run All**, or run individual cells with the play button.

> [!IMPORTANT]
> Open the repository's **root folder** in VS Code, not just the `codes` folder. This keeps the relative paths to the dataset and output directory working correctly.

### Method 2: Jupyter Notebook

With the virtual environment activated:

```bash
jupyter notebook
```

1. Open the `codes` folder in the Jupyter interface.
2. Select `program.ipynb`.
3. Run cells sequentially with `Shift + Enter`.

### Method 3: Python Script

From the repository root:

```bash
python codes/program.py
```

---

## Project Workflow

| Step | Operation | Description |
|:----:|-----------|-------------|
| 1 | Data Loading | Loads the Gold Price dataset (1,718 rows × 81 columns) |
| 2 | Data Cleaning | Removes duplicate entries and prepares the dataset |
| 3 | Exploratory Data Analysis | Analyzes distributions and relationships between indicators |
| 4 | Correlation Analysis | Examines correlations between gold prices and other indicators |
| 5 | Data Preprocessing | Handles missing values and categorical features using scikit-learn transformers |
| 6 | Model Training | Trains a Multiple Linear Regression model (80/20 train-test split) |
| 7 | Model Evaluation | Evaluates with MAE, MSE, RMSE, and R² |
| 8 | Visualization | Generates actual-vs-predicted plots and correlation heatmaps |

---

##  Important Features Used

| Feature | Column |
|---------|--------|
| S&P 500 | `SP_close` |
| Dow Jones | `DJ_close` |
| Crude Oil | `USO_Close` |
| Silver | `SF_Price` |
| US Dollar Index | `USDI_Price` |
| Gold Miners ETF | `GDX_Close` |

**Target variable:** Gold Price (`Adj Close`)

---

## Expected Output

```text
Dataset shape (rows, columns): (1718, 81)

Training examples: 1374
Testing examples: 344

Model training completed!

MAE  : 1.747
MSE  : 4.865
RMSE : 2.206
R²   : 0.984
```

### Correlation with Gold Price

| Feature | Correlation |
|---------|:-----------:|
| `GDX_Close` | 0.98 |
| `SF_Price` | 0.95 |
| `USO_Close` | 0.64 |
| `USB_Price` | -0.44 |
| `DJ_close` | -0.59 |
| `SP_close` | -0.68 |
| `USDI_Price` | -0.72 |

> [!NOTE]
> Actual output may vary slightly depending on the environment and library versions.

---

##  Generated Visualizations

All plots are saved in the `outputs/` directory.

| File | Description |
|------|-------------|
| `gold_price_distribution.png` | Distribution of gold prices |
| `feature_vs_gold_scatter.png` | Relationship between gold prices and `GDX_Close` |
| `correlation_heatmap.png` | Correlation between economic indicators |
| `predicted_vs_actual.png` | Comparison of actual and predicted gold prices |

---

## Troubleshooting

<details>
<summary><b>Kernel not found in VS Code</b></summary>

<br>

```bash
pip install ipykernel
```

Restart VS Code and select the `.venv` Python interpreter as the notebook kernel.

</details>

<details>
<summary><b>ModuleNotFoundError</b></summary>

<br>

```bash
pip install -r requirements.txt
```

</details>

<details>
<summary><b>Dataset not found</b></summary>

<br>

Make sure that:

- The repository root folder is open in VS Code.
- The dataset exists at `data/gold_price_data.csv`.
- The notebook uses the correct relative dataset path.

</details>

<details>
<summary><b>Plots not appearing</b></summary>

<br>

Run the notebook cells sequentially and make sure Matplotlib and Seaborn are installed.

</details>

---

##  Project Resources

| Resource | Link |
|----------|------|
| Presentation | [gold_price_data_ppt.pdf](docs/gold_price_data_ppt.pdf) |
| Jupyter Notebook | [program.ipynb](codes/program.ipynb) |
| Python Script | [program.py](codes/program.py) |
| Project Demo | [Watch on YouTube](https://youtu.be/YOUR_VIDEO_ID_HERE) |

---

## AI-Use Disclosure

Gemini and Claude were used to assist in formatting the README documentation, structuring the project directory, and refining Matplotlib/Seaborn visualization snippets in the Python script and Jupyter Notebook.

All data preprocessing, feature selection, Multiple Linear Regression modeling, and evaluation metrics were reviewed, tested, and verified by the four team members and are explained in the video demonstration. No AI tools were used to fabricate the dataset or experimental results.
