import os
import time 
import sys

"""
  *
 ***
*****
*****
Function For rotate cursor "\\|/-" like msfconsole
*****
*****
 ***
  *
"""

def rotate(Massage="Massage",Time=0.2,Repeat=5):
	Cursor_R="\\|/-";
	while(Repeat>=0):
		for charactors in Cursor_R:
			time.sleep(Time);
			sys.stdout.write("\r{}{}".format(Massage,charactors));
			sys.stdout.flush();
		Repeat=Repeat-1;


"""
  *
 ***
*****
*****
Function to Home option here
*****
*****
 ***
  *
"""

def Homeoption():
    print("\033[32m")
    os.system("figlet -w 100 Wi-Fi  Jammer !")
    print("\t\033[33");
    print('\033[33m       .-        -.');
    print("\033[31m      /            \ ");
    print("");
    print("\033[32m     |,  .-.  .-.  ,|  ");
    print("\033[31m     | )(_ /  \_ )( |  ");
    print("     |/     /\     \|       ");
    print('\033[32m     <__    ^^    __>');
    print("\033[32m      \__|IIIIII|__/");
    print("");
    print("\033[31m        \ IIIIII / ");
    print("\033[31m         -------- " );
    print("\033[31m            _ ");
    print("\n\n\n\033[33m");
    rotate("continue...",0.2,2);
    print("\n")
    print("\033[33m::::::::::::"*5);
    print("\033[33m::::::::::::"*5);
    print("\033[32m:::[!]\033[31m ");
    print("\033[32m:::[2]\033[31m wlan0")
    print("\033[32m:::[3]\033[31m wlan1")
    print("\033[33m::::::::::::"*5);
    print("\033[33m::::::::::::"*5);



print("selerct the interface")
os.system("airmon-ng")
print("wlan0")
print("wlan1")

if __name__=="__main__":
    Homeoption()
