#visualisation.py
#This file is responsible to visualise all the data

import matplotlib.pyplot as plt
import pandas as pd


def plot_over_time(data, metric="polarity", moving_average_window=5, save_path=None):
    # Convert data to DataFrame
    df = pd.DataFrame(data)
    df['date'] = pd.to_datetime(df['publicationDate'])
    df = df.sort_values('date')

    # Select metric and compute moving average
    df[metric] = df['sentiment'].apply(lambda x: x[metric]) if metric == "polarity" else df['subjectivity']
    df['moving_average'] = df[metric].rolling(window=moving_average_window).mean()

    # Plot the metric over time
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df[metric], label=f"{metric.capitalize()} Over Time", marker='o', linestyle='-', alpha=0.6)
    plt.plot(df['date'], df['moving_average'], label=f"Moving Average (Window={moving_average_window})", color='red',
             linewidth=2)
    plt.title(f"{metric.capitalize()} Over Time", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel(metric.capitalize(), fontsize=12)
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()


def plot_distribution(data, metric="polarity", bins=20, save_path=None):
    # Convert data to DataFrame
    df = pd.DataFrame(data)
    df[metric] = df['sentiment'].apply(lambda x: x[metric]) if metric == "polarity" else df['subjectivity']

    # Plot the histogram
    plt.figure(figsize=(12, 6))
    plt.hist(df[metric], bins=bins, color='blue' if metric == "polarity" else 'green', alpha=0.7, edgecolor='black')
    plt.title(f"{metric.capitalize()} Distribution", fontsize=16)
    plt.xlabel(metric.capitalize(), fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()


def plot_polarity_vs_subjectivity(data, x_range=None, y_range=None, x_label="Polarity", y_label="Subjectivity", save_path=None):
    # Convert data to DataFrame
    df = pd.DataFrame(data)

    # Extract polarity and subjectivity
    df['polarity'] = df['sentiment'].apply(lambda x: x['polarity'])
    df['subjectivity'] = df['subjectivity']

    # Plot the scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['polarity'], df['subjectivity'], alpha=0.7, c='purple', edgecolor='black')

    # Set axis limits if provided
    if x_range:
        plt.xlim(x_range)
    if y_range:
        plt.ylim(y_range)

    # Add labels and title
    plt.title("Polarity vs Subjectivity", fontsize=16)
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
