# ===== Packages =====
import time

# ===== Initializations =====
score = 0

# ===== Functions =====
def sleep(x):
    time.sleep(x)

def title():
    print("\nWelcome to...")
    sleep(2)
    print("""
   ('-.                                                                    
  ( OO ).-.                                                                
  / . --. /                                                                
  | \-.  \                                                                 
.-'-'  |  |                                                                
 \| |_.'  |                                                                
  |  .-.  |                                                                
  |  | |  |  ('-. .-.               .-')    .-') _                         
  `--' `--' ( OO )  /              ( OO ). (  OO) )                        
  ,----.    ,--. ,--. .-'),-----. (_)---\_)/     '._ ,--.       ,--.   ,--.
 '  .-./-') |  | |  |( OO'  .-.  '/    _ | |'--...__)|  |.-')    \  `.'  / 
 |  |_( O- )|   .|  |/   |  | |  |\  :` `. '--.  .--'|  | OO ) .-')     /  
 |  | .--, \|       |\_) |  |\|  | '..`''.)   |  |   |  |`-' |(OO  \   /   
(|  | '. (_/|  .-.  |  \ |  | |  |.-._)   \   |  |  (|  '---.' |   /  /\_  
 |  '--'  | |  | |  |   `'  '-'  '\       /   |  |   |      |  `-./  /.__) 
  `------'  `--' `--'     `-----'  `-----'    `--'   `------'    `--'      
             _ .-') _                 .-')     .-')      ('-.              
            ( (  OO) )               ( OO ).  ( OO ).  _(  OO)             
 .-'),-----. \     .'_   ,--.   ,--.(_)---\_)(_)---\_)(,------. ,--.   ,--.
( OO'  .-.  ',`'--..._)   \  `.'  / /    _ | /    _ |  |  .---'  \  `.'  / 
/   |  | |  ||  |  \  ' .-')     /  \  :` `. \  :` `.  |  |    .-')     /  
\_) |  |\|  ||  |   ' |(OO  \   /    '..`''.) '..`''.)(|  '--.(OO  \   /   
  \ |  | |  ||  |   / : |   /  /\_  .-._)   \.-._)   \ |  .--' |   /  /\_  
   `'  '-'  '|  '--'  / `-./  /.__) \       /\       / |  `---.`-./  /.__) 
     `-----' `-------'    `--'       `-----'  `-----'  `------'  `--'      
""")
    sleep(2)
    
def rules():
    print("A Ghostly Odyssey is a text-based adventure game that is played entirely through the terminal.")
    sleep(2)
    print("To play this game, simply type the number that corresponds to the action that you wish to take.")
    sleep(2)
    print("If a bad input is entered, the game will immediately end.")
    sleep(4)
    print("\nNow, prepare to enter the world of....")
    sleep(4)
    print("\nA Ghostly Odyssey!\n")
    sleep(2)
    
def introduction():
    print("...")
    sleep(2)
    print("...")
    sleep(2)
    print("...\n")
    sleep(2)

def credits():
    print("\nThank you for playing this game!")
    print("This game was developed by Jayden Chan in collaboration with Adam Ahman, Jake Grigorian, and Max Smith.")

def main():
    choice = input("Type 'play to begin your adventure...\n")
    if (choice == "play"):
        title()
        rules()
        introduction()
        credits()
    else:
        print("Bad input detected.")
        print("Ending program...")
    
# ===== Main Game Code =====
main()