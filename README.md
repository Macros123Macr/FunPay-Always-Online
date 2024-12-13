# FunPay Always Online

![Funny GIF](https://ibb.co/1KZ0Z4F)

![GitHub Downloads](https://img.shields.io/github/downloads/Macros123Macr/FunPay-Always-Online/total?color=purple&logo=GitHub&style=for-the-badge) ![GitHub Stars](https://img.shields.io/github/stars/Macros123Macr/FunPay-Always-Online?color=purple&logo=GitHub&style=for-the-badge)

## Описание

**FunPay Always Online** — это проект, обеспечивающий автоматическое управление аккаунтом на платформе FunPay с функцией поддержания постоянного онлайна. 

## Особенности

1. **Постоянный онлайн** — поддерживает аккаунт всегда активным на FunPay.
2. **Логирование** — ведёт журнал работы в файле `funpay_online.log`.

## Установка

### Windows
1. Убедитесь, что Python 3.7 или выше установлен на вашем компьютере.
2. Скачайте проект и распакуйте архив.
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Запустите программу:
   ```bash
   python main.py
   ```

### Linux / Ubuntu
1. Убедитесь, что Python 3.7 или выше установлен на вашей системе.
2. Скачайте проект и распакуйте архив.
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Запустите программу:
   ```bash
   python main.py
   ```

## Логи
Файл `funpay_online.log` содержит журнал работы программы. Он создается автоматически и обновляется во время выполнения скрипта.

## Настройка

1. Откройте файл `usersINFO.txt` для настройки информации о пользователях.
2. Настройте необходимые параметры в `main.py` (если требуется).

## Лицензия

Проект распространяется под лицензией MIT. Подробнее читайте в файле `LICENSE`.
