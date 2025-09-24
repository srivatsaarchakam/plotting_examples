import ROOT as r
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def myplots(samples=10000):    
    rng = np.random.default_rng(42)
    data1 = rng.normal(100, 6, samples)
    
    # canvas 1
    plt.figure(figsize=(8, 6))
    counts1, bins1, _ = plt.hist(data1, bins=100, range=(50, 150), edgecolor='black', alpha=0.7)
    plt.clf()

    bin_centers = (bins1[:-1] + bins1[1:]) / 2
    errors = np.sqrt(counts1)

    plt.errorbar(bin_centers, counts1, yerr=errors, fmt='o', markersize=3, capsize=2, alpha=0.7, color='blue')

    plt.xlabel('x')
    plt.ylabel('Frequency')
    plt.title('Random Gauss')
    plt.grid(True, alpha=0.3)
    plt.savefig('canvas1_py.png')
    plt.show()
    
    # canvas 2
    fig = plt.figure(figsize=(12, 10))
    
    # panel # 1
    plt.subplot(2, 2, 1)

    counts1, bins1, _ = plt.hist(data1, bins=100, range=(50, 150), edgecolor='black', alpha=0.7)
    plt.errorbar(bin_centers, counts1, yerr=errors, fmt='o', markersize=2, capsize=1, alpha=0.5, color='blue')

    plt.xlabel('x')
    plt.ylabel('Frequency')
    plt.title('Random Gauss')
    plt.grid(True, alpha=0.3)
    
    # panel # 2
    plt.subplot(2, 2, 2)

    data2 = np.concatenate([data1, rng.uniform(50, 150, samples//3)])
    counts2, bins2, _ = plt.hist(data2, bins=100, range=(50, 150), edgecolor='black', alpha=0.7)
    bin_centers2 = (bins2[:-1] + bins2[1:]) / 2

    errors2 = np.sqrt(counts2)
    plt.errorbar(bin_centers2, counts2, yerr=errors2, fmt='o', markersize=2, capsize=1, alpha=0.5, color='blue')

    plt.xlabel('x')
    plt.ylabel('Frequency')
    plt.title('Gauss & Offset')
    plt.grid(True, alpha=0.3)
    
    # panel # 3
    plt.subplot(2, 2, 3)
    x_base = []
    while len(x_base) < samples * 30:
        x = rng.uniform(1, 11)
        y = rng.uniform(0, 1)
        if y < (1/x ** 2):
            x_base.append(x * 10 + 40)
    data3 = np.concatenate([data1, x_base[:samples*30]])
    
    counts3, bins3, _ = plt.hist(data3, bins=100, range=(50, 150), edgecolor='black', alpha=0.7)

    bin_centers3 = (bins3[:-1] + bins3[1:]) / 2
    errors3 = np.sqrt(counts3)

    plt.errorbar(bin_centers3, counts3, yerr=errors3, fmt='o', markersize=2, capsize=1, alpha=0.5, color='blue')

    plt.yscale('log')
    plt.xlabel('x')
    plt.ylabel('frequency')
    plt.title('Gauss & Offset 2')
    plt.grid(True, alpha=0.3)
    
    # panel # 4
    plt.subplot(2, 2, 4)
    data4a = rng.normal(100, 6, samples//2)
    data4b = rng.normal(100, 20, samples//2)
    data4 = np.concatenate([data4a, data4b])
    
    counts4, bins4, _ = plt.hist(data4, bins=100, range=(50, 150), edgecolor='black', alpha=0.7)
    bin_centers4 = (bins4[:-1] + bins4[1:]) / 2
    errors4 = np.sqrt(counts4)

    plt.errorbar(bin_centers4, counts4, yerr=errors4, fmt='o', markersize=2, capsize=1, alpha=0.5, color='blue')

    plt.xlabel('x')
    plt.ylabel('Frequency')
    plt.title('Double Gaussian')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('canvas2_py.pdf')
    plt.show()

if __name__ == "__main__":
    samples = 10000
    
    # Check if command line argument provided
    if len(sys.argv) > 1:
        try:
            samples = int(sys.argv[1])
        except ValueError:
            print(f"Invalid argument: {sys.argv[1]}. Using default samples={samples}")
    
    myplots(samples)