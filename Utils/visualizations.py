from pathlib import Path
from itertools import cycle
import pandas as pd
import matplotlib.pyplot as plt

TEXT_COLOR = "#EDEFF2"
MUTED_COLOR = "#8C97A5"
GRID_COLOR = "#2A333D"
PALETTE = ["#4FD1C5", "#9B8CF2", "#F2B84B", "#E8735C", "#63B3ED"]


def _style_dark_axes(ax) -> None:
    ax.set_facecolor("none")
    ax.tick_params(colors=MUTED_COLOR, labelsize=9)
    ax.yaxis.label.set_color(TEXT_COLOR)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    for spine in ("left", "bottom"):
        ax.spines[spine].set_color(GRID_COLOR)
    ax.grid(axis="y", color=GRID_COLOR, linewidth=0.7, alpha=0.8)
    ax.set_axisbelow(True)


def _save_chart(plot_fn, series: pd.Series, title: str, ylabel: str, path: Path, figsize=(7, 3)) -> None:
    fig, ax = plt.subplots(figsize=figsize)
    plot_fn(ax, series)
    ax.set_title(title, loc="left", fontsize=11, color=TEXT_COLOR)
    ax.set_ylabel(ylabel, fontsize=9)
    _style_dark_axes(ax)
    fig.patch.set_alpha(0)
    fig.tight_layout()
    fig.savefig(path, dpi=150, transparent=True)
    plt.close(fig)


def _draw_line(ax, series: pd.Series) -> None:
    color = PALETTE[0]
    ax.plot(series.index, series.values, color=color, linewidth=2.2)
    ax.fill_between(series.index, series.values, color=color, alpha=0.12)


def _draw_bar(ax, series: pd.Series) -> None:
    colors = [c for _, c in zip(series.index, cycle(PALETTE))]
    ax.bar(series.index, series.values, color=colors, width=0.55)


def create_charts(df: pd.DataFrame, output_dir: Path) -> dict:
    output_dir.mkdir(exist_ok=True)

    weekly_sales = df.set_index("Order Date").resample("W")["Sales"].sum()
    category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
    region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

    paths = {
        "weekly_trend": output_dir / "weekly_trend.png",
        "category": output_dir / "sales_by_category.png",
        "region": output_dir / "sales_by_region.png",
    }

    _save_chart(_draw_line, weekly_sales, "Weekly Sales", "Sales ($)", paths["weekly_trend"], figsize=(8, 3))
    _save_chart(_draw_bar, category_sales, "Sales by Category", "Sales ($)", paths["category"])
    _save_chart(_draw_bar, region_sales, "Sales by Region", "Sales ($)", paths["region"])

    return paths