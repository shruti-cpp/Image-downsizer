import os
from PIL import Image


INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"
MAX_SIZE = (800, 800)  # Resize to fit in 800x800 box


os.makedirs(OUTPUT_FOLDER, exist_ok=True)

success_count = 0
fail_list = []
# resizing
for filename in os.listdir(INPUT_FOLDER):
    if filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, filename)
    try:
        with Image.open(input_path) as img:
            img.thumbnail(MAX_SIZE)
            img.save(output_path)

        # filesize
        original_size = os.path.getsize(input_path)
        new_size = os.path.getsize(output_path)

        # Kb
        original_kb = original_size / 1024
        new_kb = new_size / 1024

    
        print(f"{filename} downsized from {original_kb:.2f} KB to {new_kb:.2f} KB "
              f"({(new_kb / original_kb) * 100:.1f}% of original)")
        success_count += 1

    except Exception as e:
            fail_list.append((filename, str(e)))



print(f"\nProcessed {success_count} image(s) successfully.")

if fail_list:
    print("Failed to process these files:")
    for f, err in fail_list:
        print(f" - {f}: {err}")                
