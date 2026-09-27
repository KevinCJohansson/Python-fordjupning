from datetime import date
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

def format_currency(value) -> str:
    return f"$ {value:,.0f}"

def format_number(value) -> str:
    return f"{value:,.0f}"

def generate_report(metrics: dict, chart_paths: dict, output_path: str = "report.pdf") -> None:
    env = Environment(loader=FileSystemLoader("."))
    env.filters["currency"] = format_currency
    env.filters["number"] = format_number
    template = env.get_template("report_template.html")

    html_out = template.render(
        generated_date=date.today().strftime("%Y-%m-%d"),
        start_date=metrics["start_date"].strftime("%Y-%m-%d"),
        end_date=metrics["end_date"].strftime("%Y-%m-%d"),
        total_sales=metrics["total_sales"],
        n_orders=metrics["n_orders"],
        avg_order_value=metrics["avg_order_value"],
        top_products=list(metrics["top_products"].items()),
        weekly_trend_img=Path(chart_paths["weekly_trend"]).resolve().as_uri(),
        category_img=Path(chart_paths["category"]).resolve().as_uri(),
        region_img=Path(chart_paths["region"]).resolve().as_uri(),
    )

    HTML(string=html_out).write_pdf(output_path),
    print(f"Report generated: {output_path}")