#By TheUnix
#Simple
import sys,os,time
print("\033[92mGetHash ,Developed by The Unix")
time.sleep(2)
print("\033[92mAnything\'s Have A Hash , The Unix")
time.sleep(1)
def plain():
    try:
        ask=input("\033[93mGetHash(>>\033[0m ")
        if ask=="help":
            print("\033[92mHey .\nDo : hash(SOMETHING_YOU_WANT_HASH) . i.e hash(\"hello\")\tfor get hash of a word or text\nDo : print(SOMETHING_YOU_WANT_WRITE) .i.e print(\"hello\")\tfor write somthing\nDo : input(INPUT) . i.e input(\"what\'s your name? : \")\tfor input somthing\nso exit() for exit")
            plain()
        elif ask=="hash":
            print("\033[91mdid you mean hash() ?")
            plain()
        elif ask=="print":
            print("\033[91mdid you mean print() ?")
            plain()
        elif ask=="input":
            print("\033[91mdid you mean input() ?")
            plain()
        elif ask=="hash()":
            print("\033[91mPlease do hash(\"YOUR TEXT\")")
            plain()
        elif ask=="print()":
            print("\033[91mPlease do print(\"YOUR TEXT\")")
            plain()
        elif ask=="input()":
            print("\033[91mPlease do input(\"YOUR TEXT\")")
            plain()
        elif "input(\""+ask.replace("input(\"","") in ask:
            askyourself=input(ask.replace("input(\"","").replace("\")","")+": ")
            plain()
        elif ask=="exit()":
            print("\033[91mGetHash, a simple project by The Unix\033[0m")
        elif "print(\""+ask.replace("print(\"","") in ask:
            print(ask.replace("print(\"","").replace("\")",""))
            plain()
        elif "hash(\""+ask.replace("hash(\"","") in ask:
            print(hash(ask.replace("hash(\"","").replace("\")","")))
            plain()
        else:
            print("\033[91mIllegal Command")
            plain()
    except(Exception,KeyboardInterrupt,SystemExit,SystemError):
        print("There\'s an error occured.we can\'t do this operation")
        plain()
plain()
