import pyautogui
import time
import os

# --- ここを編集してください ---
# 撮影したい総ページ数を設定
TOTAL_PAGES = 10

# スクリーンショットを保存するフォルダ名
OUTPUT_FOLDER = "book_screenshots"

# 1ページあたりの待機時間（秒）。PCの動作が遅い場合は長めに設定
WAIT_TIME = 2.5
# -----------------------------

# デスクトップに保存先フォルダを作成
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
output_dir = os.path.join(desktop_path, OUTPUT_FOLDER)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print(">>> 5秒後に自動撮影を開始します。")
print(">>> Kindleアプリをフルスクリーンで最前面に表示してください。")
time.sleep(5)

for i in range(TOTAL_PAGES):
    page_num = i + 1
    print(f">>> {page_num} / {TOTAL_PAGES} ページ目を撮影中...")

    screenshot = pyautogui.screenshot()
    file_path = os.path.join(output_dir, f"page_{page_num:04d}.png")
    screenshot.save(file_path)

    # left or right
    pyautogui.press('left') 
    time.sleep(WAIT_TIME)

print(f">>> 撮影が完了しました。")
print(f"デスクトップの '{OUTPUT_FOLDER}' フォルダに画像が保存されました。")
