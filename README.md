<h2 align="center">Ninja assistant</h2>
Суть проекта в том, чтобы пользователь мог найти определение английских слов на русском. 

К примеру вы играете в rpg на английском и не можете перевести описание умения. Этот сервис поможет найти описание умения на русском (если оно есть). Или пользователь сам сможет добавить описание умения и т.д.
## Старт

##### 1) Клонировать репозиторий

#### 2) Создать .env.dev в корне проекта

    DEBUG=1
    SECRET_KEY=f244^w4HHGH6yfh)*dgLKJ3gshv$46tyftyTgfgF$$F$F
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] back
    
    # Data Base
    POSTGRES_DB=ninja_database
    POSTGRES_ENGINE=django.db.backends.postgresql
    POSTGRES_USER=user
    POSTGRES_PASSWORD=password
    POSTGRES_HOST=ninjadb
    POSTGRES_PORT=5432

##### 3) Запустить контейнер

    docker-compose up --build

#### 4) Демо
    uvicorn config.asgi:application --reload
    




