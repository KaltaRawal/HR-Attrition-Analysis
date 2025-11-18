import seaborn as sns
import matplotlib.pyplot as plt

def plot_heatmap(df):
    plt.figure(figsize=(12,8))
    sns.heatmap(df.corr(), cmap="coolwarm", annot=False)
    plt.title("Correlation Heatmap")
    plt.show()

def plot_distribution(df, col):
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.show()
