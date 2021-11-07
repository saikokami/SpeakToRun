import speech_recognition as sr
import configparser # ini file handling
import os
import time

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


#Initialize Config
cfg = configparser.ConfigParser()
cfg.read('C:/Users/benne/Documents/scripts/pyscripts/STR/wordlist.ini')
#End Ini


#cls
clear = lambda: os.system('cls')
#end cls

#Write to ini
def ini_close():
    with open('C:/Users/benne/Documents/scripts/pyscripts/STR/wordlist.ini', 'w') as f:
        cfg.write(f)





#ini set function
def ini_write(option,key,word):
    cfg[option][key] = word
    clear()


def add_word():
    clear()
    programm = input("Word: ").lower()
    path = input("Path: ")
    ini_write('word',programm,path)
    ini_close()
    menuhandler(menutexts,menufuncs)

def del_word():
    clear()
    programm = input("Word: ").lower()
    cfg.remove_option('word',programm)
    ini_close()
    menuhandler(menutexts,menufuncs)


def edit_word():
    clear()
    x = input("Word: ").lower()
    path = input("Path: ")
    ini_write('word',x,path)
    ini_close()
    menuhandler(menutexts,menufuncs)
    
def edit_trigger():
    clear()
    x = input("New trigger: ").lower()
    ini_write('trigger','tr',x)
    ini_close()
    menuhandler(menutexts,menufuncs)

def edit_startup():
    clear()
    startup = input("True/False: ").lower()
    ini_write('settings','startup',startup)
    ini_close()
    menuhandler(menutexts,menufuncs)

def list_words():
    clear()
    print("________LIST__________")
    for x in cfg['word']:
        print(x)
    print("______________________")
    wait=['seconds to continue']*5
    for i,value in enumerate(wait,1):
        print(i, value)
        time.sleep(1)

    menuhandler(menutexts,menufuncs)
    

def quitfnc():
    quit(0)





def main():
    clear()
    wordlist = []
    for x in cfg['word']:
        wordlist.append(x)     
    trigger = cfg['trigger']['tr']

    r = sr.Recognizer()

    with sr.Microphone() as source:
        while True:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio).lower()
                #print(text)
                if trigger in text:
                    if "close" in text:
                        return
                    elif "menu" in text:
                        menuhandler(menutexts,menufuncs)
                    else:
                        for x in wordlist:
                            if x in text:
                                print(x + " is launching!")
                                os.startfile(cfg['word'][x])
                                break
            except:
                print("Voice not found!")    


menutexts = [
    "Run script",
    "Add word",
    "Wordlist",
    "Delete word",
    "Edit word path",
    "Edit trigger",
    "Edit startup",
    "Exit"
]


menufuncs = [
    main,
    add_word,
    list_words,
    del_word,
    edit_word,
    edit_trigger,
    edit_startup,
    quitfnc
]

def menuhandler(texts, funcs):
    clear()
    print("Menu")
    for index, text in enumerate(texts, 1):
        print("{} {}".format(index, text))
    choice = int(input("Choose: ")) -1
    funcs[choice]()


def startup():
    if cfg['settings']['startup'] == "true":
        main()
    else:
        menuhandler(menutexts,menufuncs)

startup()

#cfg.remove_option('words','opera') # remove option | use remove_section to remove a whole section!






