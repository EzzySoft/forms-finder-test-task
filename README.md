## Описание
Используется фреймворк [FastApi](https://fastapi.tiangolo.com) и Docker контейнер с MongoDB

## Запуск
Для запуска приложения необходимо выполнить команду:
```bash
docker compose up
```
При старте в базу будут загружены подготовленные тестовые данные.


## Тестирование 
Для тестирования есть скрипт `test_requests.py` который выводит какие данные отправляются приложению и какие приходят в виде ответа

```bash
python test_requests.py
```
