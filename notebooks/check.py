import os
import shutil
import random
from pathlib import Path

def create_validation_split(dataset_path, val_split=0.2):
    """
    Split training data to create validation set
    
    Args:
        dataset_path: Path to your dataset root
        val_split: Fraction of data to use for validation (0.2 = 20%)
    """
    dataset_path = Path(dataset_path)
    train_images = dataset_path / "train" / "images"
    train_labels = dataset_path / "train" / "labels"
    
    # Create validation directories
    val_images = dataset_path / "valid" / "images"
    val_labels = dataset_path / "valid" / "labels"
    
    val_images.mkdir(parents=True, exist_ok=True)
    val_labels.mkdir(parents=True, exist_ok=True)
    
    # Get all image files
    if not train_images.exists():
        print(f"❌ Training images directory not found: {train_images}")
        return
    
    image_files = list(train_images.glob("*.jpg")) + list(train_images.glob("*.png"))
    
    if not image_files:
        print("❌ No image files found in training directory")
        return
    
    print(f"Found {len(image_files)} images")
    
    # Randomly select files for validation
    random.shuffle(image_files)
    val_count = int(len(image_files) * val_split)
    val_files = image_files[:val_count]
    
    print(f"Moving {val_count} images to validation set...")
    
    # Move images and corresponding labels
    for img_file in val_files:
        # Move image
        shutil.move(str(img_file), str(val_images / img_file.name))
        
        # Move corresponding label file
        label_name = img_file.stem + ".txt"  # assuming .txt labels
        label_file = train_labels / label_name
        
        if label_file.exists():
            shutil.move(str(label_file), str(val_labels / label_name))
        else:
            print(f"⚠️ Warning: Label file not found for {img_file.name}")
    
    print(f"✅ Validation split complete!")
    print(f"Training set: {len(list(train_images.glob('*.jpg')) + list(train_images.glob('*.png')))} images")
    print(f"Validation set: {len(list(val_images.glob('*.jpg')) + list(val_images.glob('*.png')))} images")

# Usage
dataset_path = "../data/processed/snapcal-1"
create_validation_split(dataset_path)