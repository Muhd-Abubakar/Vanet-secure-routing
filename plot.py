import pandas as pd
import matplotlib.pyplot as plt

def plot_hash_times():
    df = pd.read_csv("results/hash_times.csv")
    plt.figure(figsize=(8, 5))
    plt.plot(df["hash_time"], marker='o', label="SHA256 Time")
    plt.title("Hash Generation Time per Message")
    plt.xlabel("Message Step")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("results/hash_plot.png")
    plt.show()

if __name__ == "__main__":
    plot_hash_times()
