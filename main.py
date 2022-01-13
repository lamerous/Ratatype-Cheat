'''

Disclamer
The script was used by the creator only to test the security of the site.

For using this script, you should download HTML file of text from https://www.ratatype.ru/typing-test/test/
(Right Mouse Button -> Save As) and save them with text.html name

With love, your lamerous

----

Дисклеймер
Скрипт использовался создателем только для проверки защищенности сайта.

Чтобы использовать этот скрипт, загрузите HTML файл текста с https://www.ratatype.ru/typing-test/test/
(Правая кнопка мыши -> Сохранить Как) и сохранитеть его с именем text.html

С люблвью, ваш lamerous

'''

from bs4 import BeautifulSoup
import os
from pathlib import Path
import keyboard
import time

url = f'{os.getcwd()}\\text.html'
soup = BeautifulSoup(Path(url).read_text(encoding='utf-8'), 'lxml')
ans = soup.find_all(class_='mainTxt')

print(ans[0].text)

input('Press Enter to continue')

keyboard.send('Alt+Tab')
time.sleep(2)

for i in ans[0].text:
	keyboard.write(i, delay=0.047)
