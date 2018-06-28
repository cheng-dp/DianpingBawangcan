1. install python

sudo apt-get install python2.7 python-dev pip

sudo ln /usr/bin/python2.7 /usr/bin/python

2. install selenium

pip install selenium

3. download and install Chrome

4. download chromedriver and put into PATH

wget -c https://chromedriver.storage.googleapis.com/2.40/chromedriver_linux64.zip

unzip chromedriver_linux64.zip

sudo cp chromedriver /usr/bin

5. run python Main.py, the program will start.

6. use crontab to set schedule start to run.sh so that it will run everyday.
