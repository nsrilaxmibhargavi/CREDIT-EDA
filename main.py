import tkinter as tk
from tkinter import ttk
import pandas as pd
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# -------------------- GUI HELPERS --------------------
def add_plot(parent, fig):
    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()
    widget = canvas.get_tk_widget()
    widget.pack(fill="both", expand=True, padx=10, pady=15)


def log(text_widget, message):
    text_widget.insert(tk.END, message + "\n")
    text_widget.see(tk.END)


# -------------------- CREDIT CARD EDA --------------------
def credit_card_eda(plot_frame, log_box):
    log(log_box, "========== CREDIT CARD DATASET EDA ==========")

    df = pd.read_csv("credit_card_dataset.csv")
    df.drop(['Activation_30_Days', 'Client_Num'], axis=1, inplace=True, errors="ignore")

    log(log_box, f"Shape: {df.shape}")
    log(log_box, str(df.head()))
    log(log_box, "")

    for col in ['current_year', 'Qtr', 'Exp Type', 'Card_Category', 'Use Chip', 'Week_Num']:
        if col in df.columns:
            log(log_box, f"{col}: {df[col].unique()}")

    log(log_box, "\nMissing Values (%):")
    log(log_box, str(df.isnull().sum() / len(df) * 100))
    log(log_box, "")

    # ----------- GRAPHS -----------
    numeric_boxplots = [
        'Credit_Limit',
        'Total_Revolving_Bal',
        'Total_Trans_Amt',
        'Annual_Fees'
    ]

    for col in numeric_boxplots:
        fig = Figure(figsize=(8, 4))
        ax = fig.add_subplot(111)
        sns.boxplot(data=df, y=col, ax=ax)
        ax.set_title(f"{col} Distribution")
        add_plot(plot_frame, fig)

    # Scatter plots
    scatter_pairs = [
        ('Total_Trans_Amt', 'Credit_Limit'),
        ('Total_Trans_Amt', 'Total_Trans_Vol'),
        ('Annual_Fees', 'Credit_Limit')
    ]

    for x, y in scatter_pairs:
        fig = Figure(figsize=(8, 4))
        ax = fig.add_subplot(111)
        sns.scatterplot(data=df, x=x, y=y, ax=ax)
        ax.set_title(f"{x} vs {y}")
        add_plot(plot_frame, fig)

    log(log_box, "Credit Card EDA completed.\n")


# -------------------- CUSTOMER EDA --------------------
def customer_eda(plot_frame, log_box):
    log(log_box, "========== CUSTOMER DATASET EDA ==========")

    df = pd.read_csv("customer_dataset.csv")

    log(log_box, f"Shape: {df.shape}")
    log(log_box, str(df.head()))
    log(log_box, "")

    for col in ['Marital_Status', 'Education_Level', 'contact', 'Customer_Job']:
        log(log_box, f"{col}: {df[col].unique()}")

    log(log_box, "\nMissing Values (%):")
    log(log_box, str(df.isnull().sum() / len(df) * 100))

    log(log_box, "\nSatisfaction by Job:")
    log(
        log_box,
        str(
            df.groupby('Customer_Job')['Cust_Satisfaction_Score']
            .mean()
            .sort_values(ascending=False)
        )
    )

    # ----------- GRAPHS -----------
    fig = Figure(figsize=(8, 4))
    ax = fig.add_subplot(111)
    sns.histplot(data=df, x='Customer_Age', kde=True, ax=ax)
    ax.set_title("Customer Age Distribution")
    add_plot(plot_frame, fig)

    fig = Figure(figsize=(8, 4))
    ax = fig.add_subplot(111)
    sns.scatterplot(data=df, x='Income', y='Customer_Age', ax=ax)
    ax.set_title("Income vs Age")
    add_plot(plot_frame, fig)

    for col in ['Gender', 'Education_Level', 'Marital_Status', 'Customer_Job']:
        fig = Figure(figsize=(8, 4))
        ax = fig.add_subplot(111)
        sns.countplot(data=df, x=col, hue='Personal_loan', ax=ax)
        ax.set_title(f"{col} vs Personal Loan")
        ax.tick_params(axis='x', rotation=30)
        add_plot(plot_frame, fig)

    fig = Figure(figsize=(8, 4))
    ax = fig.add_subplot(111)
    sns.heatmap(df.corr(numeric_only=True), annot=False, cmap='coolwarm', ax=ax)
    ax.set_title("Correlation Heatmap")
    add_plot(plot_frame, fig)

    log(log_box, "Customer EDA completed.\n")


# -------------------- MAIN GUI --------------------
def main():
    root = tk.Tk()
    root.title("EDA Dashboard")
    root.geometry("1300x750")

    main_frame = ttk.Frame(root)
    main_frame.pack(fill="both", expand=True)

    # Left: plots
    plot_canvas = tk.Canvas(main_frame)
    plot_scroll = ttk.Scrollbar(main_frame, orient="vertical", command=plot_canvas.yview)
    plot_frame = ttk.Frame(plot_canvas)

    plot_canvas.create_window((0, 0), window=plot_frame, anchor="nw")
    plot_canvas.configure(yscrollcommand=plot_scroll.set)

    plot_frame.bind(
        "<Configure>",
        lambda e: plot_canvas.configure(scrollregion=plot_canvas.bbox("all"))
    )

    plot_canvas.pack(side="left", fill="both", expand=True)
    plot_scroll.pack(side="left", fill="y")

    # Right: output text
    log_box = tk.Text(main_frame, width=55, wrap="word", font=("Consolas", 10))
    log_box.pack(side="right", fill="y", padx=5)

    credit_card_eda(plot_frame, log_box)
    customer_eda(plot_frame, log_box)

    root.mainloop()


if __name__ == "__main__":
    main()
