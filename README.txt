1. В кореновата директория на проекта си създайте файла с requirements.txt и добавете следните зависимости:

selenium
webdriver_manager

2. Създайте файла .devcontainer/devcontainer.json в кореновата директория на проекта със следното съдържание:

{
  "image": "python:3.9",
  "extensions": [],
  "mounts": [],
  "remoteUser": "vscode",
  "settings": {
    "terminal.integrated.shell.linux": "/bin/bash"
  },
  "containerEnv": {
    "DISPLAY": "${localEnv:DISPLAY}"
  },
  "forwardPorts": [],
  "postCreateCommand": "pip install -r requirements.txt && apt-get update && apt-get install -y chromium-driver"
}

3. Отворете терминал в GitHub Codespaces и изпълнете следните команди, за да инсталирате ChromeDriver и зависимостите от requirements.txt:

sudo apt-get update
sudo apt-get install chromium-driver
pip install -r requirements.txt

4. pip install selenium

Инструкция за инсталиране на Chrome

1. Изпълнете следната команда, за да свалите последната версия на Google Chrome за Linux:

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

2. След като свалите пакета, изпълнете следната команда, за да инсталирате Google Chrome:

sudo dpkg -i google-chrome-stable_current_amd64.deb

Ако получите грешка за липсващи зависимости, изпълнете следната команда, за да поправите зависимостите:
sudo apt-get -f install


5. Отворете Python-файлът, съдържащ вашия код, и изпълнете го.