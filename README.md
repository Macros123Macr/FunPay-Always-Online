# FunPay Always Online

![GitHub Downloads](https://img.shields.io/github/downloads/Macros123Macr/FunPay-Always-Online/total?color=purple&logo=GitHub&style=for-the-badge) ![GitHub Stars](https://img.shields.io/github/stars/Macros123Macr/FunPay-Always-Online?color=purple&logo=GitHub&style=for-the-badge)

## Описание

**FunPay Always Online** — это скрипт для поддержания вашего аккаунта FunPay в состоянии постоянного онлайна. Он периодически отправляет запросы к домену FunPay, используя значение cookie `golden_key` для имитации активности.

## Особенности

1. **Постоянный онлайн:** Скрипт отправляет запросы каждые 10 секунд.
2. **Логирование:** Все действия записываются в файл `funpay_online.log`.
3. **Обновление сессии:** Сессия пересоздаётся каждые 3 часа для имитации нового подключения.

## Установка

### Подготовка

1. **Получение значения `golden_key`:**
   - Используйте инструменты разработчика браузера или расширения, такие как EditThisCookie, для получения значения `golden_key`.

2. **Создание файла `usersINFO.txt`:**
   В корне проекта создайте файл `usersINFO.txt` со следующим содержимым:
   ```txt
   COOKIE_golden_key=ВАШЕ_ЗНАЧЕНИЕ
   ```
   Замените `ВАШЕ_ЗНАЧЕНИЕ` на реальное значение cookie `golden_key`.

### Запуск без Docker

1. Убедитесь, что Python 3.7 или выше установлен.
2. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Macros123Macr/FunPay-Always-Online.git
   cd FunPay-Always-Online
   ```
3. Установите зависимости:
   ```bash
   pip install requests
   ```
4. Запустите скрипт:
   ```bash
   python main.py
   ```

### Запуск с помощью Docker

1. Установите Docker на вашем сервере:
   ```bash
   sudo apt update
   sudo apt install -y docker.io
   ```
2. Соберите Docker-образ:
   ```bash
   docker build -t funpay_online .
   ```
3. Запустите контейнер:
   ```bash
   docker run -d --name funpay_online --restart=always funpay_online
   ```

## Настройка

- **Параметры скрипта:**
  - `CHECK_INTERVAL` — интервал между запросами (по умолчанию 10 секунд).
  - `RECONNECT_INTERVAL` — интервал для пересоздания сессии (по умолчанию 3 часа).

Вы можете изменить эти параметры, отредактировав `main.py`.

## Логи

Файл `funpay_online.log` создаётся автоматически и содержит всю информацию о работе скрипта. Для просмотра логов контейнера используйте:
```bash
docker logs -f funpay_online
```

## Автозапуск скрипта на Linux

Вы можете настроить службу systemd для автоматического запуска скрипта при старте системы:

1. Создайте файл службы:
   ```bash
   sudo nano /etc/systemd/system/funpay_online.service
   ```
2. Добавьте следующее содержимое:
   ```ini
   [Unit]
   Description=FunPay Always Online Service
   After=network.target

   [Service]
   User=your_username
   WorkingDirectory=/path/to/FunPay-Always-Online
   ExecStart=/usr/bin/python3 main.py
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```
3. Перезагрузите конфигурацию systemd и запустите службу:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl start funpay_online
   sudo systemctl enable funpay_online
   ```

## Структура проекта

```plaintext
FunPay-Always-Online/
├── Dockerfile
├── LICENSE
├── README.md
├── main.py
└── usersINFO.txt
```

## Лицензия

Проект распространяется под лицензией MIT. Полный текст лицензии доступен в файле `LICENSE`.
