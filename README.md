# Feature Engineering Healthcare

Notebook-based feature engineering workflows for hospital admissions data to support healthcare analytics and predictive modeling.

## Notebooks

- `Pandas.ipynb`: pandas fundamentals and tabular manipulation practice.
- `FEATURE ENGINEERING.ipynb`: healthcare feature engineering workflow.

## Quick Start

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter notebook
```

Open `Pandas.ipynb` first if you want a pandas refresher, then continue with `FEATURE ENGINEERING.ipynb`.

## Healthcare Data Privacy

Do not commit protected health information (PHI), patient identifiers, raw hospital exports, or re-identifiable data. Use synthetic, public, anonymized, or approved teaching datasets only.

Before sharing derived features, confirm they do not encode direct identifiers such as names, phone numbers, medical record numbers, precise addresses, or full dates of birth.

## Reproducibility Notes

- Document the source and privacy status of any dataset used with the notebooks.
- Record missing-value, encoding, scaling, and train/test split choices.
- Keep raw data separate from generated outputs.
