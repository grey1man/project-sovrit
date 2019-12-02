import time
import api_logic
import db_logic
import threading
import sqlite3

proxy = None
answer = None
prox1 = None
prox2 = None
flag = True
event = threading.Event()

#гоняем цикл пока не наступит нужный день
def loop_main() :
   global answer
   global proxy
   global prox1
   global prox2
   global flag
   print('#-----server started------#')
   while True :
      date = time.localtime()
      if answer == 'stop' :
         time.sleep(1)
         print('#--------server stopped--------#')
         event.wait()
         event.clear()
         time.sleep(1)
         print('#-----server started------#')
         answer = None
      if date.tm_wday == 1 and flag == True :
         conn = sqlite3.connect("mydatabase.db")
         db_logic.insert('matches', api_logic.load_matches(proxy), conn)
         db_logic.insert('players', api_logic.load_players(proxy), conn)
         
         #print(api_logic.load_matches(proxy))
         #print(api_logic.load_players(proxy))
         flag = False
         #позже надо добавить функции работы с бд

#цикл управления, считываем команды
def loop_control() :
   global answer
   global proxy
   global prox1
   global prox2
   global flag
   print('#-------control panel started--------#')
   while True :
      answer = input()
      if answer == 'start' :
         event.set()
         answer = None
      if answer == 'use proxy' :
         print('#-------stopping server--------#')
         answer = 'stop'
         time.sleep(1)
         print('please input ip address of http proxy')
         prox1 = input()
         print('please input ip address of https proxy')
         prox2 = input()
         proxy = { 'http' :prox1, 'https' : prox2}
         answer = None
         event.set()
      if answer == 'do not use proxy' :
         print('#-------stopping server--------#')
         answer = 'stop'
         time.sleep(1)
         proxy = None
         answer = None
         event.set()
      if answer == 'flag = true' :
         print('#-------stopping server--------#')
         answer = 'stop'
         time.sleep(1)
         flag = True
         event.set()
      if answer == 'flag = false' :
         print('#-------stopping server--------#')
         answer = 'stop'
         time.sleep(1)
         flag = False
         event.set()
         

thread_1 = threading.Thread(target = loop_main) 
thread_2 = threading.Thread(target = loop_control) 
thread_2.start()
thread_1.start()

   






    
    
