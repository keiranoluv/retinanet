import os

BASE_DIR = "datasets/raccoon"
IMAGES_DIR = os.path.join(BASE_DIR, "images")

REQUIRED_FILES = [
    "train.csv",
    "val.csv",
    "classes.csv"
]

def check_structure():
    print("🔍 Checking dataset structure...\n")

    # 1. Check base directory
    if not os.path.isdir(BASE_DIR):
        print(f"❌ Missing directory: {BASE_DIR}")
        return
    print(f"✅ Found directory: {BASE_DIR}")

    # 2. Check images directory
    if not os.path.isdir(IMAGES_DIR):
        print(f"❌ Missing images directory: {IMAGES_DIR}")
        return
    print(f"✅ Found images directory: {IMAGES_DIR}")

    # 3. List a few images
    images = [f for f in os.listdir(IMAGES_DIR) if f.lower().endswith(".jpg")]

    if len(images) == 0:
        print("❌ No .jpg images found in images/")
    else:
        print(f"📸 Found {len(images)} image files")
        print("📸 Sample images:")
        for img in images[:5]:  # chỉ hiển thị 5 file
            print(f"   - {img}")

    print()

    # 4. Check required csv files
    for file in REQUIRED_FILES:
        path = os.path.join(BASE_DIR, file)
        if os.path.isfile(path):
            print(f"✅ Found file: {file}")
        else:
            print(f"❌ Missing file: {file}")

    print("\n✅ Structure check completed.")

if __name__ == "__main__":
    check_structure()
