import numpy as np
import matplotlib.pyplot as plt

# Define grid size
grid_size = (50, 50)
np.random.seed(42)  # Reproducibility

# Simulate data layers
magnetic_anomaly = np.random.normal(loc=0.0, scale=1.0, size=grid_size)
gravity_anomaly = np.random.normal(loc=0.0, scale=1.0, size=grid_size)
geochem = np.random.normal(loc=0.0, scale=1.0, size=grid_size)

# Inject synthetic geochemical anomaly
geochem[20:30, 20:30] += 3.0  # Simulated enrichment zone

# Compute composite prospectivity score (weighted logic)
prospectivity = (
    0.4 * (magnetic_anomaly < -1.0).astype(float) +   # magnetic lows
    0.3 * (gravity_anomaly > 1.0).astype(float) +     # gravity highs
    0.3 * (geochem > 2.0).astype(float)               # high geochemical values
)

# Plotting function
def plot_simulation():
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))

    axs[0, 0].imshow(magnetic_anomaly, cmap='coolwarm', interpolation='nearest')
    axs[0, 0].set_title('Simulated Magnetic Anomaly')

    axs[0, 1].imshow(gravity_anomaly, cmap='coolwarm', interpolation='nearest')
    axs[0, 1].set_title('Simulated Gravity Anomaly')

    axs[1, 0].imshow(geochem, cmap='YlGnBu', interpolation='nearest')
    axs[1, 0].set_title('Simulated Geochemical Enrichment')

    im = axs[1, 1].imshow(prospectivity, cmap='hot', interpolation='nearest')
    axs[1, 1].set_title('Composite Prospectivity Score')

    # Colorbar for prospectivity
    cbar = fig.colorbar(im, ax=axs[1, 1], fraction=0.046, pad=0.04)
    cbar.set_label('Prospectivity Score')

    for ax in axs.flat:
        ax.axis('off')

    plt.tight_layout()
    plt.savefig("prospectivity_demo.png", dpi=300)  # Save image
    plt.show()

# Run plot
if __name__ == "__main__":
    plot_simulation()
