


sound_checks = {"consonant":0,"vowel":0}

vowels = ["a","e","i","o","u"]
consonants = ["p","t","k","m","n","s","r","l"]

while True:
    sound = input("Enter a sound (or 'quit' to quit): ")
    if sound == "quit":
        break
    print("You typed", sound)

    if sound in vowels:
        sound_checks ["vowel"]+=1
        print(sound,"is a vowel.") 
    elif sound in consonants:
        sound_checks["consonant"]+=1
        print(sound, "is a consonant.")
    else:
        print(sound,"is not valid")
    print(sound_checks)