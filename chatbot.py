import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {"beaches" : ["Bali", "Maldives", "Phuket"], "mountains" : ["Swiss Alps", " Rocky mountains", "Himalayas"], "cities" : ["Tokyo", "Paris", "New York"]}

jokes = ["Why don't programmers like nature? Too many bugs!", "Why did the computer go to the doctor? Because it had a virus!", " Why do travelers always feel warm? Because of all their hot spots!"]

def normalise_input(text):

    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():

    print(Fore.CYAN + "Travelbot: Beaches, mountains, or cities?")
    preference = normalise_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"Travelbot: How about {suggestion}")
        print(Fore.CYAN + "Travelbot: Do you like it?(Y/N)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "Y":
            print(Fore.GREEN + f"Travelbot: Awesome! Enjoy the {suggestion}!")
        elif answer == "N":
            print(Fore.RED + "Lets try another!")
            recommend()
        else:
            print(Fore.RED + "I'll suggest again!")
            recommend()
    else:
        print(Fore.RED + "Sorry! I don't have information on that type of destination!")
        recommend()

    show_help()

def packing_tips():
    print(Fore.CYAN + "Travelbot: Where to?")
    location = normalise_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "Travelbot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN +f"Travelbot: Packing tips for {days} days in {location}")
    print(Fore.GREEN + "Make sure you pack versatile clothes")
    print(Fore.GREEN + " Bring chargers and adapters")
    print(Fore.GREEN + "Check the weather forecast before you pack")

def tell_joke():
    print(Fore.YELLOW + f"Travelbot: {random.choice(jokes)}")

def show_help():
    print(Fore.MAGENTA + "\nI can: ")
    print(Fore.GREEN + "Suggest travel spots")
    print(Fore.GREEN + "Offer packing tips ")
    print(Fore.GREEN + "Tell a joke ")
    print(Fore.CYAN + "Type 'exit' to end\n")

def chat():

    print(Fore.CYAN + "Hello! I'm Travelbot")
    name = input(Fore.YELLOW + "Your name: ")
    print(Fore.GREEN + f"Nice to meet you {name}")
    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalise_input(user_input)
        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "pack" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input:
            print(Fore.CYAN + "Travelbot: Safe travels! Bye for now!")
            break
        else:
            print(Fore.RED + "Travelbot: I didn't understand? Could you rephrase?")

if __name__ == "__main__":
     chat()

