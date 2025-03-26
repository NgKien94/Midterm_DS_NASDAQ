from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Cấu hình trình duyệt
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
driver = webdriver.Chrome(options=options)

URL = "https://stockanalysis.com/list/nasdaq-stocks/"
driver.get(URL)
time.sleep(5)  # Đợi trang load lần đầu

page = 1
all_data = []

try:
    # Đóng quảng cáo nếu có
    try:
        close_ad_button = WebDriverWait(driver, 25).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Close')]"))
        )
        close_ad_button.click()
        print("✅ Đã đóng quảng cáo!")
        time.sleep(2)  # Đợi trang ổn định sau khi đóng quảng cáo
    except:
        print("⚠ Không thấy quảng cáo hoặc đã tự động đóng.")

    while True:
        if page > 7 : 
            break
        print(f"📌 Đang lấy dữ liệu trang {page}...")

        # Chờ bảng xuất hiện
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table/tbody/tr")))

        # 🔴 TÌM LẠI DANH SÁCH ROWS SAU MỖI LẦN NHẤN "NEXT"
        rows = driver.find_elements(By.XPATH, "//table/tbody/tr")

        # Lưu dữ liệu từ bảng
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            all_data.append([col.text for col in columns])

        # Tìm nút "Next"
        try:
            # Tìm tất cả các nút có class 'controls-btn'
            buttons = driver.find_elements(By.XPATH, "//button[contains(@class, 'controls-btn')]")

            # Lọc ra nút có chữ "Next"
            next_button = None
            for button in buttons:
                if "Next" in button.text:
                    next_button = button
                    break

            if next_button:
                driver.execute_script("arguments[0].click();", next_button)
                time.sleep(5)  # Đợi trang mới load
                print("🌍 URL hiện tại:", driver.current_url)
            else:
                print("✅ Đã đến trang cuối cùng, dừng lại!")
                break

        except:
            print("❌ Không thể click nút Next, có thể đã hết trang!")
            break

        page += 1

except Exception as e:
    print("❌ Lỗi xảy ra:", e)

# Lưu dữ liệu vào file CSV
df = pd.DataFrame(all_data, columns=["No.", "Symbol", "Company Name", "Market Cap", "Stock Price", "% Change", "Revenue"])
df.to_csv("nasdaq_stocks.csv", index=False)
print("📂 Dữ liệu đã được lưu vào 'nasdaq_stocks.csv'!")

driver.quit()


#Phân tích dữ liệu trên có áp dụng được gì vào mô hình hay không, lợi ích là gì
