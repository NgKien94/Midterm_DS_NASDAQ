import requests
from bs4 import BeautifulSoup
import pandas as pd
import time



def scrape_coinmarketcap(pages=11):  # Đảm bảo lấy hơn 1000 records
    base_url = "https://coinmarketcap.com/"
    all_data = []
    
    for page in range(1, pages + 1):
        url = f"{base_url}?page={page}"
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        if response.status_code != 200:
            print(f"Failed to retrieve data from {url}")
            continue
        
        soup = BeautifulSoup(response.text, 'html.parser')
        table_rows = soup.select("table.cmc-table tbody tr")
        
        for row in table_rows:
            columns = row.find_all("td")
            if len(columns) < 10:
                continue
            
            name = columns[2].find("p", class_="coin-item-symbol").text.strip()
            price = columns[3].text.strip()
            market_cap = columns[7].text.strip()
            volume_data = columns[8].text.strip()
            supply = columns[9].text.strip()
            
            # Xử lý 24h Volume để thêm dấu +/-
            volume_parts = volume_data.split(" ")
            volume_value = volume_parts[0]
            if len(volume_parts) > 1 and ("+" in volume_parts[1] or "-" in volume_parts[1]):
                volume_change = volume_parts[1]
                volume = f"{volume_value} {volume_change}"
            else:
                volume = volume_value
            
            all_data.append([name, price, market_cap, volume, supply])
        
        time.sleep(2)  # Tránh bị chặn do gửi quá nhiều request
    
    return all_data

def save_to_csv(data, filename="coinmarketcap_data.csv"):
    df = pd.DataFrame(data, columns=["Name", "Price", "Market Cap", "24h Volume", "Circulating Supply"])
    df.to_csv(filename, index=False, sep=';')  # Xuất CSV với dấu phân cách là ;
    print(f"Data saved to {filename}")

 
records = scrape_coinmarketcap(11)  # Gọi hàm để lấy dữ liệu
save_to_csv(records)  # Gọi hàm để lưu file