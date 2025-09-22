import sys
import importlib
import importlib.metadata

packages = [
    "numpy", "pandas", "matplotlib", "seaborn", "sklearn", "skfuzzy",
    "cv2", "jupyter", "jupyterlab", "ipykernel", "joblib", "dill",
    "nltk", "spacy", "tensorflow", "torch", "torchvision",
    "tensorflow_datasets", "transformers", "flask", "fastapi"
]

results = []
for pkg in packages:
    try:
        try:
            version = importlib.metadata.version(pkg)
        except importlib.metadata.PackageNotFoundError:
            m = importlib.import_module(pkg)
            version = getattr(m, "__version__", "unknown")
        results.append(f"{pkg}: OK, version = {version}")
    except Exception as e:
        results.append(f"{pkg}: ERROR → {e}")

results.append(f"Python: {sys.version}")

# simpan ke file
with open("verify_output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(results))

print("Hasil verifikasi sudah disimpan di verify_output.txt")
