# Movie Rater

Aplikacja webowa służąca do publikowania informacji o filmach i oceniania ich.
Napisałem ją w trakcie nauki frameworka Django.

## Uruchamianie

### 1. Sklonuj repozytorium.
    git clone ...
    cd Movie-Rater
### 2. Stwórz wirtualne środowisko Pythona 3 w folderze.
    python3 -m venv venv
### 3. Aktywuj środowisko.
    source venv/bin/activate
### 4. Zainstaluj zależności z requirements.txt
    pip3 install -r requirements.txt
### 5. Stwórz migracje i wyemigruj modele aplikacji.
    python3 manage.py makemigrations
    python3 manage.py migrate
### 6. Uruchom aplikacje.
    python3 manage.py runserver
### 7. Aplikacja znajduje się na route:
    (ustalony port localhost)/movies/all
    