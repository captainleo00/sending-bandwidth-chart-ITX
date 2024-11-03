# Base image với Python
FROM python:3.10-slim

# Cài đặt các dependencies cần thiết cho Chrome, ChromeDriver, và build các thư viện Python
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    xvfb \
    fonts-liberation \
    libappindicator3-1 \
    xdg-utils \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Thêm khóa và repo cho Chrome
RUN curl -sSL https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list

# Cài đặt Chrome
RUN apt-get update && apt-get install -y \
    google-chrome-stable \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Cài đặt ChromeDriver và ChromeDriverManager
RUN pip install --no-cache-dir selenium webdriver-manager

# Đặt biến môi trường để Selenium hoạt động với Chrome và Xvfb
ENV DISPLAY=:99

# Đặt thư mục làm việc
WORKDIR /app

# Sao chép file requirements.txt vào container để cài đặt các dependencies trước
COPY requirements.txt ./

# Cài đặt các thư viện Python từ requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY traffic_Viettel_collection.py ./

# Chạy Xvfb và ứng dụng
CMD ["sh", "-c", "Xvfb :99 -screen 0 1024x768x24 & python3 traffic_Viettel_collection.py"]
