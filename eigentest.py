import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Original grayscale image (5x5)
image_matrix = np.array([
    [100, 100, 10, 100, 100],
    [63, 120, 55, 120, 109],
    [85, 120, 117, 120, 120],
    [180, 115, 130, 135, 140],
    [180, 150, 160, 170, 180]
])

# Step 1: Center the data by subtracting column means
column_means = np.mean(image_matrix, axis=0)
centered_matrix = image_matrix - column_means

# Step 2: Calculate the covariance matrix
cov_matrix = np.cov(centered_matrix.T)

# Convert to DataFrame for better display
cov_df = pd.DataFrame(cov_matrix, 
                      columns=[f'Col{i+1}' for i in range(5)], 
                      index=[f'Col{i+1}' for i in range(5)])

# Display the image
plt.imshow(image_matrix, cmap='gray', interpolation='nearest')
plt.title("5x5 Grayscale Image")
plt.axis('off')  # Hide axis ticks
plt.colorbar(label='Pixel Intensity')  # Optional: shows intensity scale
plt.show()

# # Plot the covariance matrix as a heatmap
# plt.figure(figsize=(8, 6))
# sns.heatmap(cov_df, annot=True, fmt=".1f", cmap="coolwarm", cbar=True)
# plt.title("Covariance Matrix of Centered Grayscale Image")
# plt.tight_layout()
# plt.show()

#cov_df
