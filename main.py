from pathlib import Path
from Utils.data_loader import load_data
from Utils.metrics import compute_metrics
from Utils.visualizations import create_charts
from Utils.report_generator import generate_report

DATA_PATH = "Data/sales_2018_Q1.csv"
OUTPUT_DIR = Path("report_assets")


def main() -> None:
    df = load_data(DATA_PATH)
    metrics = compute_metrics(df)
    chart_paths = create_charts(df, OUTPUT_DIR)
    generate_report(metrics, chart_paths)


if __name__ == "__main__":
    main()