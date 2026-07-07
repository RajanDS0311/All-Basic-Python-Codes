alphabet =(input("enter an alphabet: "))
match alphabet.lower() :
    case "a" | "e" | "i" | "o" | "u" :
        print("It is a vovel")

    case _ :
        print("It is a consonant")