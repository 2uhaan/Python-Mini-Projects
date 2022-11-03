print("Welcome to Xsos -- Two Worlds")
name = input("Enter your nickname : ").lower()
print("Hello", name, "Welcome to Wessex 2025......")
print("its 10:00 am , you just woke up but insted of your room ,you are in a grey room with no exit or window of any sort....")
print("a grim reaper appears...........")
choice_1 = input("He wants you to choose between a Dark orb / Light orb....enter Dark or Light : ").lower()
if choice_1 == "dark":
    print("you are a necromansor now.....you are immortal and have the ability to puppet a corpse")
    print("you are transported to your classroom.....12:30 pm")
    print("a classmate takes out an M4 and killed all 49 students but we cant kill you and he freaks out and drops the gun...he says..'what are you!")
    choice_2 = input("A - you pick up the M4 and finish him / B - you talk to him :").lower()
    if choice_2 == "a":
        print("after killing him you walk downstares and you see the police .. they think you are the school shooter...they tell you to surrender")
        choice_3 = input("A - you Surrender / B - you kill them all with the corpse in the classroom :").lower()
        if choice_3 == "a":
            print("you were arrested and found guilty..sentenced to life imprisonment")
        elif choice_3 == "b":
            print("you kill 7 police officers and back up arrives in 10min....50 cops 1 helicopter...you kill them all with your dead army of cops and students..")
            print("you keep killing and increasing the dead army")
            print("you become the most powerful individual on the planet.")
            print("you live forever with people who see you as the God of destruction...")
            print("You live forever in this pocket world which is an illution.......")
            print("THIS IS HELL")
        else:
            print("Invalid Choice")
    elif choice_2 == "b":
        print("you tell him to surrender himself.....you should him mercy...this was a test by the grim reaper")
        print("you Pass")
        print("You get reincarnated as a boy in 2013 to a family in berlin ." )
        print("The End.")
    else:
        print("Invalid Choice")
elif choice_1 == "light":
    print("you become the angle of light...your job is to show people the right track when they are lost.")
    print("you are in the classroom..12:30 pm...")
    print("the guy next to you was bullied by majority of the classmates.")
    print("he has a gun in his back")
    option_1 = input("A - convince him to change his mind / B - let him be :").lower()
    if option_1 == "a":
        print("you pass the test.")
        print("you are reincarnated as a boy in 2019 to a couple in Delhi,India .")
    elif option_1 == "b":
        print("your Heart stops.....you come back to life....your heart stops agian....the loop continues forever.")
        print("THIS IS HELL")
    else:
        print("Invalid Choice")
else:
    print("Invalid Choice.")
       
