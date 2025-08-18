import argparse
import os
from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- Plot defaults (cleaner images) ---
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["axes.grid"] = True
plt.rcParams["figure.autolayout"] = True

def summarize_dataframe(df: pd.DataFrame) -> str:
    lines = []
    lines.append("# Dataset Summary")
    lines.append(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    lines.append("")

    # dtypes
    lines.append("## Dtypes")
    dtypes_str = df.dtypes.astype(str).to_string()
    lines.append(dtypes_str)
    lines.append("")

    # missing values
    lines.append("## Missing Values (per column)")
    na = df.isna().sum()
    if (na > 0).any():
        lines.append(na[na > 0].to_string())
    else:
        lines.append("No missing values.")
    lines.append("")

    # basic stats
    lines.append("## Numerical Summary (describe)")
    if len(df.select_dtypes(include=np.number).columns) > 0:
        lines.append(df.describe().to_string())
    else:
        lines.append("No numeric columns.")
    lines.append("")

    # categorical overview
    cat_cols = df.select_dtypes(exclude=np.number).columns.tolist()
    lines.append("## Categorical Columns")
    if cat_cols:
        lines.append(", ".join(cat_cols))
    else:
        lines.append("No categorical columns.")
    lines.append("")
    return "\n".join(lines)

def plot_numeric_histograms(df: pd.DataFrame, out_dir: Path):
    num_cols = df.select_dtypes(include=np.number).columns.tolist()
    for col in num_cols:
        plt.figure()
        df[col].dropna().hist(bins=30)
        plt.title(f"Histogram - {col}")
        plt.xlabel(col); plt.ylabel("Count")
        plt.savefig(out_dir / f"hist_{col}.png", dpi=150)
        plt.close()

def plot_categorical_bars(df: pd.DataFrame, out_dir: Path, top_k: int = 20):
    cat_cols = df.select_dtypes(exclude=np.number).columns.tolist()
    for col in cat_cols:
        vc = df[col].astype("string").str.strip().replace({"": pd.NA}).dropna().value_counts().head(top_k)
        if vc.empty:
            continue
        plt.figure()
        vc.plot(kind="bar")
        plt.title(f"Top {min(top_k, len(vc))} Categories - {col}")
        plt.xlabel(col); plt.ylabel("Frequency")
        plt.xticks(rotation=45, ha="right")
        plt.savefig(out_dir / f"bar_{col}.png", dpi=150, bbox_inches="tight")
        plt.close()

def plot_corr_heatmap(df: pd.DataFrame, out_dir: Path):
    num_df = df.select_dtypes(include=np.number)
    if num_df.shape[1] < 2:
        return
    corr = num_df.corr(numeric_only=True)
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=False, cmap="vlag", center=0)
    plt.title("Correlation Heatmap (numeric features)")
    plt.savefig(out_dir / "correlation_heatmap.png", dpi=150, bbox_inches="tight")
    plt.close()

def run_eda(file_path: str, sep: str = ",", encoding: str = "utf-8", na_values: str | None = None, limit_rows: int | None = None):
    # prepare outputs
    out_dir = Path("outputs")
    out_dir.mkdir(parents=True, exist_ok=True)

    # read
    df = pd.read_csv(file_path, sep=sep, encoding=encoding, na_values=na_values)
    if limit_rows:
        df = df.head(limit_rows)

    # save head preview for quick check
    df.head(20).to_csv(out_dir / "sample_head.csv", index=False)

    # write text summary
    summary = summarize_dataframe(df)
    (out_dir / "summary.txt").write_text(summary, encoding="utf-8")

    # plots
    plot_numeric_histograms(df, out_dir)
    plot_categorical_bars(df, out_dir)
    plot_corr_heatmap(df, out_dir)

    print("✅ EDA complete.")
    print(f"- Text summary: {out_dir / 'summary.txt'}")
    print(f"- Sample head:  {out_dir / 'sample_head.csv'}")
    print(f"- Charts saved in: {out_dir.resolve()}")

def parse_args():
    p = argparse.ArgumentParser(description="Minimal Auto-EDA (Phase 1 MVP)")
    p.add_argument("--file", required=True, help="Path to CSV file")
    p.add_argument("--sep", default=",", help="CSV separator (default ,)")
    p.add_argument("--encoding", default="utf-8", help="File encoding (default utf-8)")
    p.add_argument("--na-values", default=None, help="Additional strings to treat as NA, e.g. 'NA;None'")
    p.add_argument("--limit-rows", type=int, default=None, help="Process only first N rows (speed/debug)")
    return p.parse_args()

if __name__ == "__main__":
    args = parse_args()
    na_values = args.na_values.split(";") if args.na_values else None
    run_eda(file_path=args.file, sep=args.sep, encoding=args.encoding, na_values=na_values, limit_rows=args.limit_rows)
