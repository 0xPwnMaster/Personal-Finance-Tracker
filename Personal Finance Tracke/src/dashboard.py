import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
from pathlib import Path
from analysis import analyze_data

def create_dashboard(input_file, output_file):
    # Check if input file exists
    if not input_file.exists():
        print(f"Error: Input file {input_file} not found.")
        return

    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error reading {input_file}: {e}")
        return

    # Validate DataFrame
    required_columns = ['Date', 'Category', 'Amount']
    if not all(col in df.columns for col in required_columns):
        print(f"Error: Input file missing required columns: {required_columns}")
        return
    if df.empty:
        print("Error: Input file is empty.")
        return

    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Run analysis
    try:
        monthly_summary, savings_rate, expense_ratios = analyze_data(input_file)
    except Exception as e:
        print(f"Error in analysis: {e}")
        return

    # Convert Period indices to strings for Plotly compatibility
    monthly_summary.index = monthly_summary.index.astype(str)
    savings_rate.index = savings_rate.index.astype(str)
    expense_ratios.index = expense_ratios.index.astype(str)

    # Define custom dark theme
    dark_theme = {
        'layout': {
            'paper_bgcolor': '#1f1f1f',
            'plot_bgcolor': '#2c2c2c',
            'font': {'color': '#ffffff', 'family': 'Roboto, sans-serif', 'size': 14},
            'title': {'x': 0.5, 'xanchor': 'center', 'font': {'size': 24, 'color': '#ffffff'}},
            'margin': {'l': 60, 'r': 60, 't': 120, 'b': 60},
            'showlegend': True,
            'legend': {'bgcolor': 'rgba(0,0,0,0.7)', 'bordercolor': '#ffffff', 'borderwidth': 1},
        },
        'data': {
            'scatter': [{'line': {'width': 3}, 'marker': {'size': 8}}],
            'pie': [{'textinfo': 'percent+label', 'hoverinfo': 'label+percent+value'}]
        }
    }

    # Create subplot layout
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Monthly Trends', 'Expense Breakdown', 'Savings Rate', 'Expense Ratios'),
        specs=[[{"type": "xy"}, {"type": "pie"}],
               [{"type": "xy"}, {"type": "xy"}]],
        vertical_spacing=0.12,
        horizontal_spacing=0.15
    )

    # Update subplot titles font
    for i, annotation in enumerate(fig['layout']['annotations']):
        if 'text' in annotation:
            annotation.update(font={'size': 18, 'color': '#ffffff'})

    # Monthly Trends
    colors = px.colors.qualitative.Bold
    for i, col in enumerate(monthly_summary.columns):
        if monthly_summary[col].notna().any():  # Check for valid data
            fig.add_trace(
                go.Scatter(
                    x=monthly_summary.index,
                    y=monthly_summary[col],
                    name=col,
                    line=dict(width=3, color=colors[i % len(colors)]),
                    hovertemplate='%{x}: $%{y:.2f}<extra></extra>'
                ),
                row=1, col=1
            )

    # Expense Breakdown (Pie)
    pie_data = monthly_summary.mean()
    if not pie_data.empty and pie_data.notna().any():
        fig.add_trace(
            go.Pie(
                labels=pie_data.index,
                values=pie_data,
                textinfo='percent+label',
                hoverinfo='label+percent+value',
                marker=dict(colors=px.colors.qualitative.Bold, line=dict(color='#ffffff', width=1)),
                textfont={'size': 14, 'color': '#ffffff'}
            ),
            row=1, col=2
        )

    # Savings Rate (Line)
    if not savings_rate.empty and savings_rate.notna().any():
        fig.add_trace(
            go.Scatter(
                x=savings_rate.index,
                y=savings_rate,
                name='Savings Rate (%)',
                line=dict(color='#00cc96', width=3),
                hovertemplate='%{x}: %{y:.1f}%<extra></extra>'
            ),
            row=2, col=1
        )

    # Expense Ratios
    for i, col in enumerate(expense_ratios.columns):
        if expense_ratios[col].notna().any():
            fig.add_trace(
                go.Scatter(
                    x=expense_ratios.index,
                    y=expense_ratios[col],
                    name=f'{col} Ratio (%)',
                    line=dict(width=3, color=colors[i % len(colors)]),
                    hovertemplate=f'{col}: %{{y:.1f}}%' + '<extra></extra>'
                ),
                row=2, col=2
            )

    # Dropdown menu
    buttons = [
        dict(
            label="All Categories",
            method="update",
            args=[{"visible": [True] * len(monthly_summary.columns) + [True] + [True] * len(expense_ratios.columns)}]
        )
    ]
    for i, col in enumerate(monthly_summary.columns):
        visible = [False] * len(monthly_summary.columns) + [True] + [True] * len(expense_ratios.columns)
        visible[i] = True
        buttons.append(
            dict(
                label=col,
                method="update",
                args=[{"visible": visible}]
            )
        )

    # Update layout with dark theme and alignment
    fig.update_layout(
        title_text="Personal Finance Dashboard",
        title_x=0.5,
        height=1000,
        width=1400,
        showlegend=True,
        template=dark_theme,
        updatemenus=[
            dict(
                buttons=buttons,
                direction="down",
                showactive=True,
                x=0.05,
                xanchor="left",
                y=1.15,
                yanchor="top",
                active=0,
                font={'color': '#ffffff'},
                bgcolor='#3a3a3a',
                bordercolor='#ffffff'
            )
        ],
        hoverlabel={'bgcolor': '#3a3a3a', 'font': {'color': '#ffffff'}},
        xaxis={'gridcolor': '#444444'},
        yaxis={'gridcolor': '#444444'},
        xaxis3={'gridcolor': '#444444'},
        yaxis3={'gridcolor': '#444444'},
        xaxis4={'gridcolor': '#444444'},
        yaxis4={'gridcolor': '#444444'}
    )

    # Axes labels with consistent styling
    fig.update_xaxes(title_text="Month", row=1, col=1, title_font={'color': '#ffffff'}, tickfont={'color': '#ffffff'})
    fig.update_yaxes(title_text="Amount ($)", row=1, col=1, title_font={'color': '#ffffff'}, tickfont={'color': '#ffffff'})
    fig.update_xaxes(title_text="Month", row=2, col=1, title_font={'color': '#ffffff'}, tickfont={'color': '#ffffff'})
    fig.update_yaxes(title_text="Savings Rate (%)", row=2, col=1, title_font={'color': '#ffffff'}, tickfont={'color': '#ffffff'})
    fig.update_xaxes(title_text="Month", row=2, col=2, title_font={'color': '#ffffff'}, tickfont={'color': '#ffffff'})
    fig.update_yaxes(title_text="Expense Ratio (%)", row=2, col=2, title_font={'color': '#ffffff'}, tickfont={'color': '#ffffff'})

    # Ensure output directory exists
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Custom CSS for HTML output
    custom_css = """
    body {
        background-color: #1f1f1f;
        font-family: 'Roboto', sans-serif;
        color: #ffffff;
        margin: 0;
        padding: 20px;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .js-plotly-plot {
        border: 2px solid #ffffff;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
        background-color: #2c2c2c;
    }
    .plotly-graph-div {
        width: 100%;
        max-width: 1400px;
    }
    h1 {
        text-align: center;
        color: #ffffff;
        font-size: 36px;
        margin-bottom: 20px;
    }
    .modebar {
        background-color: #3a3a3a !important;
    }
    .modebar-group a {
        color: #ffffff !important;
    }
    """

    # Custom HTML template to include CSS and font in <head>
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Personal Finance Dashboard</title>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
        <style>
            {css}
        </style>
        {plotly_js}
    </head>
    <body>
        <h1>Personal Finance Dashboard</h1>
        {plot_div}
    </body>
    </html>
    """

    # Generate Plotly HTML content
    try:
        plot_html = pio.to_html(
            fig,
            include_plotlyjs='cdn',
            full_html=False,
            config={'displayModeBar': True, 'responsive': True}
        )
        # Combine with custom HTML template
        final_html = html_template.format(
            css=custom_css,
            plotly_js='<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>',
            plot_div=plot_html
        )
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_html)
        print(f"Interactive dashboard saved as {output_file}")
    except Exception as e:
        print(f"Error saving dashboard: {e}")

if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent.parent
    input_file = base_dir / 'data' / 'finance_data_cleaned.csv'
    output_file = base_dir / 'data' / 'dashboard.html'

    create_dashboard(input_file, output_file)