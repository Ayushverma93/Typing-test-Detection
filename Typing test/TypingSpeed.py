from time import *;
import random as r;
 
def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
                
        except :
            error = error + 1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/ time_R
    return round(speed)

while True:
    ck = input(" ready to test : yes / no: ")
    if ck == "yes":
        
        test =["Emma searched her entire house for the lost key. After hours of looking, she found it in the pocket of her winter coat.",
        "As she held it up, she remembered the adventures that awaited her in her grandmother's old house, where the key unlocked a treasure chest of memories.",
        "In a small town, a friendly ghost named Oliver haunted an old library"]

        test1 = r.choice(test)
        print("      ****** typing speed ****** ")
        print(test1)
        print()
        print()

        time_1 = time()
        testinput=input(" Enter : ")
        time_2 = time()

        print('Speed : ', speed_time(time_1, time_2, testinput),"w/sec")

        print("Error : ", mistake(test1,testinput))
    
    elif ck == 'no':
        print(" thankyou")
        break
    
    else:
        print(" wrong input")
    