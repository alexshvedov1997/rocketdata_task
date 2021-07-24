# Rocketdata test

### Технические требования
* Python 3.8.10
* django 3.2.5
* django-seed 0.2.2
* celery 4.4.2
* djoser 2.1.0
* djangorestframework 3.12.4
* redis 3.5.3
* Установить redis-server

Вся разработка велась в ветке dev

### Примечания


>1.7 Все данные о сотрудниках одного уровня.
>> Фильтрация реализовалась по slug в url  
>>Пример: http://127.0.0.1:8000/rest_api/list_level/middle/  

>2.1 Заполните базу данных при помощи:  
• DB seeder для Django ORM  
• При помощи скрипта.
>> В company_employees/managment/commands была добавлена команда  
>> При вводе в terminal **python3 manage.py fill_db**, будет добавлено 
>> 10 записей в таблицу Other informations

>2.3 Пользователи могут получать доступ к API при помощи специального ключа.
>> Использовал djoser 





