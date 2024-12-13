import time
import logging
import requests
import os

# Настраиваем логирование
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("funpay_online.log"),
        logging.StreamHandler()
    ]
)

FUNPAY_URL = "https://funpay.com/"   # Теперь отправляем запросы к главной странице домена
CHECK_INTERVAL = 10                  # Интервал между запросами (10 секунд)
RECONNECT_INTERVAL = 3 * 3600        # Пересоздание сессии каждые 3 часа

def load_config():
    """Загружаем данные из usersINFO.txt и возвращаем словарь."""
    config = {}
    if not os.path.exists("usersINFO.txt"):
        logging.error("Файл usersINFO.txt не найден!")
        return config
    
    with open("usersINFO.txt", "r", encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            if "=" in line:
                key, val = line.split("=", 1)
                key = key.strip()
                val = val.strip()
                config[key] = val
    return config

def configure_session(session, config):
    # Добавляем только COOKIE_golden_key, если он есть
    for k, v in config.items():
        if k == "COOKIE_golden_key":
            session.cookies.set("golden_key", v)

def main():
    config = load_config()
    if "COOKIE_golden_key" not in config:
        logging.error("COOKIE_golden_key не найден в файле usersINFO.txt!")
        return

    while True:
        with requests.Session() as session:
            configure_session(session, config)

            start_time = time.time()
            while (time.time() - start_time) < RECONNECT_INTERVAL:
                try:
                    response = session.get(FUNPAY_URL, timeout=10)
                    if response.status_code == 200:
                        logging.info("Онлайн статус успешно поддержан (200 OK) на домене FunPay")
                    else:
                        logging.warning(f"Неожиданный статус: {response.status_code}")
                except requests.RequestException as e:
                    logging.error(f"Ошибка при запросе к FunPay: {e}")
                
                time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
