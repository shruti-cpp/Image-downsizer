import os
from tkinter import filedialog, Tk, Button, Label, Entry, StringVar, messagebox
from PIL import Image

MAX_SIZE = (800, 800)

def downsize_images(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    success_count = 0
    fail_list = []

    for filename in os.listdir(input_dir):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            try:
                with Image.open(input_path) as img:
                    img.thumbnail(MAX_SIZE)
                    img.save(output_path)
                success_count += 1
            except Exception as e:
                fail_list.append((filename, str(e)))

    return success_count, fail_list

def browse_input():
    path = filedialog.askdirectory()
    input_path.set(path)

def browse_output():
    path = filedialog.askdirectory()
    output_path.set(path)

def run_downsizer():
    inp = input_path.get()
    out = output_path.get()

    if not inp or not out:
        messagebox.showerror("Error", "Please select both input and output folders.")
        return

    success_count, fail_list = downsize_images(inp, out)

    if fail_list:
        error_message = "Failed to process these files:\n"
        error_message += "\n".join(f"{f[0]}: {f[1]}" for f in fail_list)
        messagebox.showerror("Processing Errors", error_message)

    messagebox.showinfo("Done", f"Processed {success_count} image(s) successfully.")

# === UI Setup ===
root = Tk()
root.title("Image Downsizer")
root.geometry("400x200")

input_path = StringVar()
output_path = StringVar()

Label(root, text="Input Folder").pack()
Entry(root, textvariable=input_path, width=50).pack()
Button(root, text="Browse", command=browse_input).pack()

Label(root, text="Output Folder").pack()
Entry(root, textvariable=output_path, width=50).pack()
Button(root, text="Browse", command=browse_output).pack()

Button(root, text="Downsize Images", command=run_downsizer).pack(pady=10)

root.mainloop()