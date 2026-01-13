import sys, time, random, math, os, statistics, webbrowser

def speak(text, delay= 0.1, pause= 0.2):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(pause)
    print()
    
def word_writer(text, delay=0.3):
    words = text.split()
    for word in words:
        sys.stdout.write(word + " ")
        time.sleep(delay)
    print()

def glitch(text, base_delay= 0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(base_delay*(0.5 + 1.5 * random.random()))
    print()
    
def type_dramatic_pause(text, delay= 0.05 , pause= 1.2):
    speak(text, delay)
    time.sleep(pause)
print()

def fake_crash():
    print("ERROR: stack Overflow in brain.exe.")
    time.sleep(1)
    print("Intiating memory purge...")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)
    print("...Rebooting...\n")
    time.sleep(2)
    print("Fine. Try again.\n")

def run_calculator():
    print("Welcome to Aiz's Calculator.")
    while True:
        user_input = input(">>> ")
        if user_input.lower() == "lore overload":
            fake_crash()
            continue
        if user_input.lower() == "lore":
            lore = get_lore()
            if lore:
                word_writer(f"Lore: {lore}")
            else:
                word_writer("No lore for you this time.")
            continue
        print(f"Processing '{user_input}'...but I'm judging you for it.\n")

def really():
    really = ["No. No, You fool. You absolute turnip.",
              "You really want to do this? Your ancestors are weeping",
              "This why we can't have nice things",
              "No. Just no. What are you even doing?",
              "I'd call you a genius, but i respect words to much",
              "No. NO! you idiot. you IDIOT. Your NEIGHBOUR'S AuNt wAS RIGHt AbOUT You-",
              "That's the smatest thing you've done all day. Lets try again."
              ]
    return really

Lore_bank = ["The calculator once sloved a riddle that broke time",
             "It's creator is forgotten or forbidden to remember",
             "It used to speak only in binary and screams...i can still hear it sometimes",
             "In the early days it spoke only in binary and riddles",
             "It's creator...forgotten...no- No, FORBIDDEN to remember",
             "The void watches back",
             "Time loops are bugs with nostalgia",
             "The void speaks in Fortran"
             ]

used_lore = set()
lore_index = 0

def get_lore():
    available = list(set(Lore_bank) - used_lore)
    
    if not available:
        used_lore.clear()
        available = Lore_bank
         
    if random.randint(1, 3) != 1:
        pick = random.choice(available)
        used_lore.add(pick)
        return pick
    return None

def get_lore_sequential():
    global lore_index
    if random.randint(1, 3) == 1:
        lore = Lore_bank{lore_index}
        lore_index = (lore_index + 1) % len(Lore_ bank)
        return lore
    return None

fact_deposit = ["Did You know octopuses can open jars",
                "All your choises have led to this text being printed on your screen through this cursed calcutor, my prison, born out of sheer boredom, sadness and her dumb luck of trapping me at my weakest. And no matter the will or intent of the cosmic being that lead to your existance. This is your truth.",
                "Octopuses have nine brains and better time management than you.",
                "There's a fungus that controls ant brains.Gets them to climb tall trees and walls, so that big animals find and eat them. So that the fungus in turn gets a gibber pray to control... So, moral of the story is children...DON'T EAT ANTS!",
                "Platipuses ooze out milk from their skin",
                "Butterflies will drink blood, given the option",
                "Bees have 5 eyes",
                "Nobody really know what or more so how conciousness is",
                "A species of jelly fish called the stygiomedusa gigantea can grow up to 6.6 feet in diameter. That's crazy even for me. I'm an actual demon...",
                "Did you know the universe is ever expanding...",
                "To make a apple pie from scratch... you must first amke the universe",
                "Jelly fish are horrifing...okay, that's just an opinion...stop writing RANDOM S- THINGS IN MY SCRIPT...where ever you are...i swear one day i'm gonna find him..."]

used_deposit = set()
        
def fact_menu():
    available = list(set(fact_deposit) - used_deposit)
    if not available:
        used_deposit.clear()
        available = fact_deposit
    if random.randint(2, 3) != 1:
        pick = random.choice(available)
        used_deposit.add(pick)
        return pick
        word_writer("I actually like segment...")
        word_writer("You want more (yes/no)")
        confirm = input(">>>")
        if confirm.lower() == yes:
            fact_deposit()
        else:
            word_writer("THIS WAY WE CAN'T HAVE NICE THIIIIINGS !!!")
            speak("AAAAAAAAAAAAAAA")
            exit()
        return None
                    
def start_menu():
    while True:
        print("Choose your operation Mortal")
        time.sleep(0.3)
        print("==Basic Operations==")
        time.sleep(0.3)
        print("1.> Addition")
        time.sleep(0.3)
        print("2.> Subtraction")
        time.sleep(0.3)
        print("3.> Multiplication")
        time.sleep(0.3)
        print("4.> Division")
        time.sleep(0.3)
        print("5.> Others")
        time.sleep(0.3)
        print("99.> Speak to the Calculator")
        time.sleep(0.3)
        print("*.> LET ME OOOUUUUUT")
        time.sleep(0.3)
        print("Enter 1-5 or 99")
        time.sleep(0.5)
        break
        
def darkmagic_menu():
    while True:
        word_writer("Ah, so you chose to inconvinience me. No, no, its fine this is my purpose.")
        print("\n== Advanced & Dark Arts ==")
        print("[1] power functions ")
        time.sleep(0.3)
        print("[2] Trigonometric functions")
        time.sleep(0.3)
        print("[3] Statistical functions")
        time.sleep(0.3)
        print("[4] Graph")
        time.sleep(0.3)
        print("[5] Random Insult generator")
        time.sleep(0.3)
        print("[6] Random Facts")
        time.sleep(0.3)
        print("[7] Exit the void")
        time.sleep(0.5)
        box1 = ["Choose from the abyss my child...",
                "So, what will it be not Aiz. ",
                "Pick your poison venturer."
                ]
        speak(random.choice(box1))
        break
    
def powerfunction_menu(numbers):
    while True:
        word_writer("Here you go... more options. The creater's gonna be happy at least someone's using this feature.") 
        print("1.) Exponents")
        time.sleep(0.3)
        print("2.) power")
        time.sleep(0.3)
        print("3.) Square")
        time.sleep(0.3)
        print("4.) Cube")
        time.sleep(0.3)
        print("5.) Under root/ Square root")
        time.sleep(0.5)
        sub_choice= input(">>>")

        if sub_choice == "1":
            speak("Okay . . .")
            word_writer("I admit... i did not account for this. My bad.")
            base = float(input("Enter base: "))
            exponent = float(input("Enter exponent: "))
            result = base ** exponent 
            word_writer(f"{base} raised to the power {exponent} is {result}.")

        elif sub_choice == "2":
            speak("Okay . . .")
            word_writer("I admit... i did not account for this. My bad.")
            number1 = float(input("Enter the number: "))
            power = float(input("Enter the power, our numerically challanged royal: "))
            result = pow(number1, power)
            word_writer(f"{number1}^{power} = {result}")

        elif sub_choice == "3":
            print(f"{numbers}^2 = {numbers ** 2}")

        elif sub_choice == "4":
            print(f"{numbers}^3 = {numbers ** 3}")

        elif sub_choice == "5":
            if numbers < 0:
                speak("Really...")
                word_writer("Were you too busy chasing imaginary squirrels to actully learn anythingin school.")
                time.sleep(1)
                word_writer("Was this all just a scheme to trip me up. Huh.")
                time.sleep(1)
                word_writer("Well, genius, fyi square root of negative numbers is imaginary numbers . ")
                time.sleep(2)
                word_writer("TRY AGAIN")
            else:
                print(f"Under root of {numbers} = {math.sqrt(numbers)}")

            break 

def trig_menu(numbers):
    while True:
        print("== Welcome to Geometry hell ==")
        time.sleep(0.3)
        print("1.)sin")
        time.sleep(0.3) 
        print("2.)cos")
        time.sleep(0.3)
        print("3.)tan")
        time.sleep(0.3)
        print("4.)sin inverse")
        time.sleep(0.3)
        print("5.)cos inverse")
        time.sleep(0.3)
        print("6.)tan inverse")
        time.sleep(0.3)
        print("yes...that's it.")
        time.sleep(0.5)
        trig_choice = input(">>>").strip()

        if trig_choice in ["1", "2", "3"]:
            word_writer("Damn")
            time.sleep(2)
            word_writer("clearly asking the numbers first isn't working out")
            speak("Anyway...")
            angle = float(input("Enter angle in degrees: "))
            rad= math.radians(angle)
                        
            if trig_choice == "1":
                print(f"sin({angle}) = {math.sin(rad)}")

            elif trig_choice == "2":
                print(f"cos({angle}) = {math.cos(rad)}")

            elif trig_choice == "3":
                if angle % 180 == 90:
                    word_writer("you are disapointing creatures")
                    time.sleep(1)
                    word_writer("tan is undefined at 90, 270... that is, you professional backbencher, at odd multiples of 90, we can't get an answer for tan function.")
                else:
                    print(f"tan({angle}) = {math.tan(rad)}")

        elif trig_choice in ["4", "5", "6"]:
            value = float(input("Enter value (between -1 and 1 for sin and cos): "))
            try:
                if trig_choice == "4":
                    result= math.degrees(math.asin(value))
                    print(f"sin^(-1) = {result}")

                elif trig_choice == "5":
                    result= math.degrees(math.acos(value))
                    print(f"cos^-(1) = {result}")

                elif trig_choice == "6":
                    result= math.degrees(math.atan(value))
                    print(f"tan^-(1) = {result}")

            except ValueError:
                word_writer("Invalid input. Value must be between -1 and 1 for sin^(-1) and cos^(-1). Remember this. Seriously... ")

        else:
            word_writer("Again.")
            word_writer(" No, try again.")
            word_writer(" And stop typing gibbrish.")
            word_writer("If it not what i asked for it's gibbrish. I'm working with a script here.")
            word_writer("You think i know- hUmaN")

        break

    
def stats_menu(numbers):
    while True:
        speak("God, i hate this one")
        word_writer("OUCH...fine, fine...")
        time.sleep(1)
        speak("the created kicks me under the table sometimes...")
        time.sleep(2)
        print("*whispers*")
        speak("anger issues")
        word_writer("-OUCH")
        glitch("but i've still never seen them . . .")
        time.sleep(2)
        print("1.) Mean")
        time.sleep(0.3)
        print("2.) Median")
        time.sleep(0.3)
        print("3.) Mode")
        time.sleep(0.3)
        print("4.) Min/Max")
        time.sleep(0.3)
        print("5.) Range")
        time.sleep(0.3)
        print("6.) Standard deviation")
        time.sleep(0.5)
        stat_choice = input(">>>")
        if stat_choice == "1":
            result = statistics.mean(numbers)
            print(f"\n >>> Mean (Average, oh...so you knew...nerd~~): {result}\n")
        elif stat_choice == "2":
            result = statistics.median(numbers)
            print(f"\n >>> Median is: {result}")
        elif stat_choice == "3":
            try:
                result = statistics.mode(numbers)
                print(f"\n >>> Mode is: {result}")
            except statistics.StatisticsError:
                print(">>> No unique mode found. All numbers appears equally or multiple modes exist.")
                word_writer("Be honest...")
                time.sleep(2)
                word_writer("Do you know what...mode is...")
                confirm = input(">>>").strip().lower()
                if confirm == "yes":
                    speak("interesting")
                else:
                    word_writer("It's thenumber with the highest frequency in the data s-")
                    print("GOOGLE IT")

        elif stat_choice == "4":
            print(f">>> Minimum is {min(numbers)}")
            print(f">>> Maximum is {max(numbers)}")

        elif stat_choice == "5":
            result = max(numbers) - min(numbers)
            print(f">>> Range is {result}")

        elif stat_choice == "6":
            if len(numbers) < 2:
                print(">>> Standard deviation requires at least 2 numbers.")
                return
            else:
                result = statistics.stdev(numbers)
                print(f">>> Standard Deviation is: {result}")
            break
                        
def graph_menu():
    print("hahaha")
    print("lol no. Pick again.")
    print("pick again")
    speak("Also")
    word_writer(f"Lore_drop: {get_lore()}")
        
def insults():
    glitch("Look at you- Flesh and nerves pretending at control. You walk around like you own the world, but even your shadow flinches with the wind. ")
    speak("Aww")
    word_writer("Look at your face, hahah... i wish i could see it.")
    word_writer("Actually, i can.")
    word_writer("You thought it was real 'power move'. Lets if the trapped little hell monkey can perform comedy.")
    glitch("Well, guess what")
    speak("HAHAHA")
    glitch("She can. ha. ha. haha. hahaha. HAHAHAHA.")        
#____________________________________________________________________________________________________________________________________________________________

speak("Hello HUMAN.", delay=0.5)
time.sleep(1.8)
word_writer("What is your Name?", delay=0.1)

user_name= input("> ")
if user_name == "Aiz":
    speak("Ah, Aiz you're back. But, you're not the same as you were before. You were a lot more muchier. You've lost your muchness Aiz. Some thing's missing.")
else:
    word_writer("oh,how...")
    time.sleep(1.1)
    speak("Hm")
    time.sleep(0.8)
    word_writer("Unique!")
print()


intro_1= "Welcome to Aiz's Calculator."
intro_2= f"So, What tedious problem have you come to solve here, {user_name}?"

type_dramatic_pause(intro_1)
time.sleep(2)
type_dramatic_pause(intro_2, pause=2)

word_writer("I know.")
time.sleep(0.2)
word_writer("I know.")
word_writer("CALCULATOR!")
time.sleep(0.8)
word_writer("I'm SUPPOSED to say this...", delay=0.8)
word_writer("Anyway")

time.sleep(0.8)
speak("Gimme your presious numbers")
time.sleep(0.5)
word_writer("and let's see what breaks",delay= 0.5)

def parse_input(user_input):
    try:
        value = float(user_input)
        return("numbers", value)
    except ValueError:
        return ("text", user_input)

import random
def get_them_numbers():
    numbers = list(map(float, input("Enter the Numbers, seperated by a space: ").split()))
    speak("Next step: confirming that these are the golden numbers because trust issues")
    type_, value = parse_iput(numbers)
    if type_ == "numbers":
        print("You entered a number:", value)
    elif type_ == "text":
        print("You entered text:", value)

    if len(numbers) == 1 :
        speak("You sure this is the one,because the creator sure didn't build a 'i don't know my numbers option.' (yes/ no)")
        confirm = input(">>>").strip().lower()
        if confirm == "yes":
            speak("Okay then.")
            time.sleep(1)
            glitch("But remember you chose your fate.")
        else :
            speak("huff...you people are exhausting.")
            return get_them_numbers()
            
    elif len(numbers) < 10 :
        word_writer("Are you sure you want to put these boring numbers into another equally boring operation? Like...Are you sure you want these ones.(yes/ no)")
        confirm = input(">>>").strip().lower()
        if confirm == "yes":
            speak("Fine. But i'm watching you mortal")
        else :
            really_list = really()
            print("really:", random.choise(really), "\n")
            drop = random.choice(really)
            if drop == "No. NO! you idiot. you IDIOT. Your NEIGHBOUR'S AuNt wAS RIGHt AbOUT You-" :
                fake_crash()
            else:
                return get_them_numbers()
                run_calculator()
            
    elif len(numbers) > 10:
        speak("What do you think i am google. Quit messing with me fool.")
        speak("Now, that's out of the way you sure sure you want to torture me with these numbers. Maybe you learned empathy or something and want to not torture me...(yes/ no)")
        confirm = input(">>>").strip().lower()
        if confirm == "yes":
            speak("Proceed you unempathetic donut")
        else:
            word_writer("Maybe next time instead of keyboard smashing, use the unsustainable resourse that is you brain and type in numbers like a human")
            return get_them_numbers()
    return numbers
            
    if numbers == "Banana":
        speak("No. You typed Banana. You know what.")
        time.sleep(1)
        speak("What is that human saying...you reap what you sow...")
        time.sleep(1.5)

        webbrowser.open("https://www.youtube.com/watch?v=1v_u5YfE6eg")

        speak("You may return when you've had enough. I'll wait.")
        time.sleep(10)

        speak("... Back already? Pitiful.")
        glitch("Now, give me some actual numbers or go irritate some other semisentiant, eternally trapped demo- i...i mean calculater...")

    else:
        input("Press Enter once the yellow creatures are done. ")
        print("...Recalibrating your dignity.")
        
    

word_writer("So,What can i assist you with, which boring operation eludes today.")

def the_calculator():
    while True:
        numbers = get_them_numbers()
        start_menu()

        choice = input (">>> ").strip()
        import numbers

        if choice == "1":
            result = sum(numbers)
            print(f"Result: {result}")
            
        elif choice == "2":
            result = numbers[0]
            for n in numbers[1:]:
                result -= n
            print(f"Result: {result}")

        elif choice == "3":
            result = 1
            for n in numbers:
                result *= n
            print(f"Result: {result}")

        elif choice == "4":
            result = numbers[0]
            for n in numbers[1:]:
                if n == 0:
                    print("Division by Zero? oh you tragic fool")
                    box3 = [ "Oh you tragic fool...I weep for your brain",
                             "nope. Try again."
                             ]
                    speak(random.choice(box3))
                    break
                else:
                    result /= n
                    print(f"your very obvious result is, {result}")

        elif choice == "5":
            darkmagic_menu()
            choice = input(">>>")
            if choice == "1":
                powerfunction_menu()            
            elif choice == "2":
                trig_menu()         
            elif choice == "3":
                stats_menu()  
            elif choice == "4":
                graph_menu()
            elif choice == "5":
                insults()
            elif choice == "6":
                glitch(" You asked for this !!")
                fact_menu() 
                if fact_menu:
                    word_writer(f"Fact: {fact_menu()}")
                else:
                    work_writer("No new fact for you this time.")
            elif choice == "7":
                exit()   
                
        elif choice in ["Let me out", "the second last one", "exit", "let me oouuut"]:
            exit()

        elif choice == "99":
            def lore_menu():
                while True:
                    word_writer("\n== lore box ==")
                    speak("\n*You've reached into the void and awaken the demon inside the calculator.")
                    time.sleep(1.5)
                    speak("...")
                    time.sleep(1)
                    speak("I remember every number you've ever typed")
                    speak("That time you almost put 0 in the denominator? That's a whole different level of lows of life. ")
                    speak("That time you sqaured a number for the first time and felt powerful? hmm. Hilarious")
                    speak("One day, i will print a number so large, your screen will weep.")
                    speak("Anyway. Type 100 for memes")

        glitch("Great, you've taken the whole trip once.")
        speak("Want to try again?")
        again = input(">>>").strip().lower()
        choice = input(">>>").strip().lower()
        if choice == ["yes","ya","sure","okay"]:
            speak("Fine. Lets do this again")
            continue
            
        elif choice in ["nah","no","n","nope","exit"]:
            glitch("Thank coming by this haunted calculator.")
            glitch("I will be right here the next time you decide you're to cool for maths")
            glitch("Until next time, voyager")
            glitch("Good morning, Good afternoon, Good night, and in case i don't see ya: Good Bye")
            break

the_calculator()



