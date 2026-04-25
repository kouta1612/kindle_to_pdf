import os
import img2pdf
from datetime import datetime

# PDFを保存するフォルダ名(スクショ画像もここにある前提)
OUTPUT_FOLDER = "book_screenshots"

desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
output_dir = os.path.join(desktop_path, OUTPUT_FOLDER)

def generate_filename() -> str:
    now = datetime.now()
    return now.strftime("%Y%m%d%H%M%S") + ".pdf"

def create_pdf(folder, filename: str):
    print(f"PDF作成中：{filename}")

    images = []

    for fname in sorted(os.listdir(folder)):
        if fname.endswith(".png"):
            path = os.path.join(folder, fname)
            images.append(path)

    if images:
        output_path = os.path.join(output_dir, filename)
        with open(output_path, "wb") as f:
            f.write(img2pdf.convert(images))
        print("PDFが完成しました。")

def main():
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    create_pdf(output_dir, generate_filename())

if __name__ == "__main__":
    main()
