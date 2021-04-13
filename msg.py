import random

neutral_paths=['messages/amelka_mess.txt',
               'messages/default_mess.txt',
               'messages/papiez_mess.txt',
               'messages/pogoda_mess.txt',
               'messages/hour_mess.txt',
               'messages/hania_mess.txt',
               'messages/gra_mess.txt']

class Msg:
    def __init__(self,file):
        with open(file,encoding='utf-8') as f:
            self.__arr=[line[:-1] for line in f]
        if file not in neutral_paths:
            with open('messages/default_mess.txt',encoding='utf-8') as f:
                arr2=[line[:-1] for line in f]
                self.__arr+=arr2
        self.__const_arr = self.__arr.copy()
    def get_arr(self):
        return self.__arr
    def choose_message(self):
        msg=random.choice(self.__arr)
        self.__arr.remove(msg)
        if len(self.__arr)==0:
            self.__arr=self.__const_arr.copy()
        return msg
    def join_arr(self,arr):
        self.__arr+=arr