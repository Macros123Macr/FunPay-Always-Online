# FunPay Always Online

![GitHub Downloads](https://img.shields.io/github/downloads/Macros123Macr/FunPay-Always-Online/total?color=purple&logo=GitHub&style=for-the-badge) ![GitHub Stars](https://img.shields.io/github/stars/Macros123Macr/FunPay-Always-Online?color=purple&logo=GitHub&style=for-the-badge)

## Описание

**FunPay Always Online** — это проект, поддерживающий ваш аккаунт на FunPay в состоянии постоянного онлайна. Скрипт периодически отправляет запросы к домену FunPay, используя вашу cookie `golden_key`, чтобы имитировать постоянное присутствие.

## Особенности

1. **Постоянный онлайн**: Скрипт отправляет запросы каждые 10 секунд, поддерживая активность аккаунта.
2. **Логирование**: Все действия записываются в файл `funpay_online.log`.
3. **Автоматическое обновление сессии**: Каждые 3 часа сессия пересоздаётся для имитации нового подключения.

## Подготовка

1. Получите значение вашей cookie `golden_key` с сайта FunPay (через инструменты разработчика в браузере или расширения для работы с cookie).
2. В файле `usersINFO.txt` пропишите:
   ```txt
   COOKIE_golden_key=ВАШЕ_ЗНАЧЕНИЕ
