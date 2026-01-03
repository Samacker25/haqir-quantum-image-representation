import os
from pathlib import Path

list_of_files = [

    "__init__.py",
    "classical_processing/__init__.py",
    "classical_processing/preprocess.py",  
    "classical_processing/block_segmentation.py",
    "classical_processing/importance_score.py",
    "qir_baselines/__init__.py",
    "qir_baselines/frqi.py",
    "haqir/__init__.py",
    "haqir/adaptive_selector.py",
    "haqir/haqir_circuit.py",
    "experiments/compare_methods.py",
    "docs/figures",
    "app.py",
    "requirements.txt",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")