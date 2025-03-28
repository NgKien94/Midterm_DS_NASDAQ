#After crawling data
import pandas as pd
import matplotlib.pyplot as plt

#Data từ file csv
data = pd.read_csv('nasdaq_stocks.csv')


df = pd.DataFrame(data)
# Hàm chuyển đổi chuỗi có đơn vị (B, M, K) thành số thực
def convert_to_float(x):
    if pd.isna(x):  # Giữ nguyên giá trị NaN
        return x
    x = str(x).replace(',', '')  # Loại bỏ dấu phẩy
    try:
        if 'B' in x:
            return float(x.replace('B', '')) * 1e9
        elif 'M' in x:
            return float(x.replace('M', '')) * 1e6
        elif 'K' in x:
            return float(x.replace('K', '')) * 1e3
        else:
            return float(x)  # Nếu không có đơn vị, chuyển thẳng thành float
    except ValueError:
        return None  # Trả về None nếu không chuyển đổi được (sẽ thành NaN trong DataFrame)

# Áp dụng chuyển đổi cho các cột số
for col in ['Market Cap', 'Revenue', 'FCF', 'Net Cash']:
    df[col] = df[col].apply(convert_to_float)

# Chuyển đổi cột Volume, xử lý giá trị '-' thành NaN
df['Volume'] = pd.to_numeric(df['Volume'].str.replace(',', ''), errors='coerce')  # Chuyển '-' hoặc giá trị không hợp lệ thành NaN

# Chọn các biến quan trọng
important_vars = ['Market Cap', 'FCF', 'Net Cash']

# 2. Vẽ histogram với thang log cho tất cả các biến
for var in important_vars:
    plt.figure(figsize=(10, 6))
    plt.hist(df[var].dropna(), bins=50, edgecolor='black', log=True)  # log=True cho trục Y
    plt.xscale('log')  # Thang log cho trục X
    plt.title(f'Histogram của {var} (Log Scale)')
    plt.xlabel(f'{var} (USD, log scale)')
    plt.ylabel('Tần suất (log scale)')
    plt.show()

# 3. Vẽ boxplot (giữ nguyên)
for var in important_vars:
    plt.figure(figsize=(8, 6))
    plt.boxplot(df[var].dropna())
    plt.title(f'Boxplot của {var}')
    plt.ylabel(var)
    plt.show()