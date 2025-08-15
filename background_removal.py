from rembg import remove
from PIL import Image
import os

input_folder = "input"
output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}_nobg.png")

        with open(input_path, "rb") as inp_file:
            input_data = inp_file.read()
            output_data = remove(input_data)

        with open(output_path, "wb") as out_file:
            out_file.write(output_data)

        print(f"已處理: {filename}")
