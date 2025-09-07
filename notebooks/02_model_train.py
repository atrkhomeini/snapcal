import os
from dotenv import load_dotenv
from roboflow import Roboflow
import yaml
import mlflow
from ultralytics import YOLO, settings
import torch
import gc

# === MEMORY OPTIMIZATION SETTINGS ===
# Clear any existing CUDA cache
if torch.cuda.is_available():
    torch.cuda.empty_cache()

# Force garbage collection
gc.collect()

# Set environment variables for memory optimization
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:128'

# === Configuration ===
settings.update({'mlflow':True})
DATASET_DIR = os.path.abspath('../data/processed/snapcal-1')
DATASET_YAML_PATH = os.path.join(DATASET_DIR, 'data.yaml')
print(f"YAML path: {DATASET_YAML_PATH}")
print(f"YAML exists: {os.path.exists(DATASET_YAML_PATH)}")
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB")
# Verify directories exist
train_dir = os.path.join(DATASET_DIR, 'train', 'images')
val_dir = os.path.join(DATASET_DIR, 'valid', 'images')
print(f"Train dir exists: {os.path.exists(train_dir)}")
print(f"Valid dir exists: {os.path.exists(val_dir)}")

# === TRAINING WITH REDUCED PARAMETERS ===
mlflow.set_experiment("SnapCal Component Detection")

with mlflow.start_run() as run:
    run_id = run.info.run_id
    print(f"Starting memory-optimized training - Run ID: {run_id}")

    # REDUCED PARAMETERS FOR STABILITY
    params = {
        "epochs": 10,           # Reduced from 50
        "batch_size": 4,        # Reduced from 16 
        "image_size": 416,      # Reduced from 640
        "model_type": "yolov8n.pt",  # Keep nano (smallest)
        "workers": 2,           # Limit data loading workers
        "patience": 5           # Early stopping
    }
    mlflow.log_params(params)
    print(f"Memory-optimized parameters: {params}")

    try:
        # Load model
        model = YOLO(params["model_type"])
        
        # Train with memory optimizations
        results = model.train(
            data=DATASET_YAML_PATH,
            epochs=params["epochs"],
            batch=params["batch_size"],
            imgsz=params["image_size"],
            workers=params["workers"],
            patience=params["patience"],
            project="training_runs",
            name=run_id,
            # Additional memory optimizations
            cache=False,        # Don't cache images in RAM
            device=0 if torch.cuda.is_available() else 'cpu',
            amp=True,          # Automatic Mixed Precision (saves memory)
            fraction=0.8       # Use only 80% of available GPU memory
        )

        # Log metrics
        if hasattr(results, 'box') and results.box is not None:
            final_metrics = {
                "mAP50-95": results.box.map if results.box.map is not None else 0,
                "mAP50": results.box.map50 if results.box.map50 is not None else 0,
                "precision": results.box.mp if results.box.mp is not None else 0,
                "recall": results.box.mr if results.box.mr is not None else 0
            }
            mlflow.log_metrics(final_metrics)
            print(f"Final metrics: {final_metrics}")
        else:
            print("⚠️ No box metrics available")

        # Log model
        mlflow.pytorch.log_model(model, "model")
        print("✅ Training completed successfully!")
        
    except Exception as e:
        print(f"❌ Training failed: {str(e)}")
        raise
    
    finally:
        # Clean up memory
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        gc.collect()
        print("🧹 Memory cleaned up")