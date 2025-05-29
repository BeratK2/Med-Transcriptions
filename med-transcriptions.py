# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub


# Download latest version
path = kagglehub.dataset_download("tboyle10/medicaltranscriptions")

print("Path to dataset files:", path)