import argparse

import pyautogui
import time
import os

# スクリーンショットを保存するフォルダ名
OUTPUT_FOLDER = "book_screenshots"

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--direction', '-d', default='left', choices=['left', 'right'], type=str)
    parser.add_argument('--pages', '-p', type=int, default=300)
    parser.add_argument('--wait', '-t', type=int, default=0.5)

    return parser.parse_args()

def create_dir(folder_name: str) -> str:
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    output_dir = os.path.join(desktop_path, folder_name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def screenshot(dir_path, direction: str, pages, wait: int):
    for i in range(pages):
        page = i + 1
        print(f">>> {page} / {pages} ページ目を撮影中...")

        screenshot = pyautogui.screenshot()
        file_path = os.path.join(dir_path, f"page_{page:04d}.png")
        screenshot.save(file_path)

        pyautogui.press(direction) 
        time.sleep(wait)

def main():
    # 引数の取得
    args = get_args()

    # デスクトップに保存先フォルダを作成
    dir_path = create_dir(OUTPUT_FOLDER)

    # スクショ準備
    print(">>> 5秒後に自動撮影を開始します。")
    print(">>> Kindleアプリをフルスクリーンで最前面に表示してください。")
    time.sleep(5)

    # スクショ
    screenshot(dir_path, args.direction, args.pages, args.wait)

    print(f">>> 撮影が完了しました。")
    print(f"デスクトップの '{OUTPUT_FOLDER}' フォルダに画像が保存されました。")

if __name__ == "__main__":
    main()