import pyautogui
import time
import os

# --- ここを編集してください ---
# 撮影したい総ページ数を設定
TOTAL_PAGES = 1

# スクリーンショットを保存するフォルダ名
OUTPUT_FOLDER = "book_screenshots"

# 1ページあたりの待機時間（秒）。PCの動作が遅い場合は長めに設定
WAIT_TIME = 2.5
# -----------------------------

def create_dir(folder_name: str) -> str:
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    output_dir = os.path.join(desktop_path, folder_name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def screenshot(dir_path: str):
    for i in range(TOTAL_PAGES):
        page_num = i + 1
        print(f">>> {page_num} / {TOTAL_PAGES} ページ目を撮影中...")

        screenshot = pyautogui.screenshot()
        file_path = os.path.join(dir_path, f"page_{page_num:04d}.png")
        screenshot.save(file_path)

        pyautogui.press('left') 
        time.sleep(WAIT_TIME)

def main():
    # デスクトップに保存先フォルダを作成
    dir_path = create_dir(OUTPUT_FOLDER)

    # スクショ準備
    print(">>> 5秒後に自動撮影を開始します。")
    print(">>> Kindleアプリをフルスクリーンで最前面に表示してください。")
    time.sleep(5)

    # スクショ
    screenshot(dir_path)

    print(f">>> 撮影が完了しました。")
    print(f"デスクトップの '{OUTPUT_FOLDER}' フォルダに画像が保存されました。")

if __name__ == "__main__":
    main()