for _ in range(100):
    templet = input("Enter a number up to 3: ")

    if templet == '1':
        number = input('Enter a number: ')
        measure_of_time = input("Enter a measurement of time: ")
        transport = input("Enter a mode of transportation: ")
        adjective = input("Enter an adjective: ")
        adjective2 = input("Enter an adjective: ")
        noun = input("Enter a noun: ")
        color = input("Enter a color: ")
        body_part = input("Enter a part of the body: ")
        verb = input("Enter a verb: ")
        number2 = input('Enter a number: ')
        noun2 = input("Enter a noun: ")
        noun3 = input("Enter a noun: ")
        body_part2 = input("Enter a part of the body: ")
        noun4 = input("Enter a noun: ")
        adjective3 = input("Enter an adjective: ")
        silly_word = input("Enter a silly word: ")

        mads1 = f"""It was about {number} {measure_of_time} ago when I arrived at the hospital in a {transport}.
        The hospital is a/an {adjective} place, there are a lot of {adjective2} {noun} here. There are nurses here who have {color} {body_part}.
        If someone wants to come into my room I told them that they have to {verb} first. I've decorated my room with {number2} {noun2}.
        Today I talked to a doctor and they were wearing a {noun3} on their {body_part2}. I heard that all doctors {verb} {noun4} every day for breakfast.
        The most {adjective3} thing about being in the hospital is the {silly_word} {noun}! """

        print(mads1)
        break

    elif templet == '2':
        name = input("Enter person's name: ")
        noun = input("Enter a noun: ")
        feeling = input("Enter an adjective (feeling): ")
        verb = input("Enter a verb: ")
        feeling2 = input("Enter an adjective (feeling): ")
        animal = input("Enter an animal: ")
        verb2 = input("Enter a verb: ")
        color = input("Enter a color: ")
        verbing = input("Enter a verb ending with -ing: ")
        adverb = input("Enter an adverb (ending with ly): ")
        number = input("Enter a number: ")
        measure_of_time = input("Enter a measurement of time: ")
        animal = input("Enter an animal: ")
        silly_word = input("Enter a silly word: ")
        noun2 = input("Enter a noun: ")

        mads2 = f"""This weekend I am going camping with {name}. I packed my lantern, sleeping bag, and {noun}. I am so {feeling} to {verb} in a tent.
        I am {feeling2} we might see a(n) {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb2}.
        I have heard that the {color} lake is great for {verbing}. Then we will {adverb} hike through the forest for {number} {measure_of_time}.
        If I see a {color} {animal} while hiking, I am going to bring it home as a pet! At night we will tell {number} {silly_word} stories and roast {noun2} around the campfire!!"""

        print(mads2)
        break

    elif templet == '3':
        name = input("Enter person's name: ")
        adjective = input("Enter an adjective: ")
        color = input("Enter a color: ")
        animal = input("Enter an animal: ")
        place = input("Enter a place: ")
        adjective2 = input("Enter an adjective: ")
        creature = input("Enter a magical creature (plural): ")
        adjective3 = input("Enter an adjective: ")
        creature2 = input("Enter a magical creature (plural): ")
        room = input("Enter a room of a house: ")
        noun = input("Enter a noun: ")
        noun2 = input("Enter a noun: ")
        plural = input("Enter a plural noun: ")
        adjective4 = input("Enter an adjective: ")
        plural2 = input("Enter a plural noun: ")
        number = input("Enter a number: ")
        measure_of_time = input("Enter a measurement of time: ")
        verbing = input("Enter a verb ending with -ing: ")
        adjective5 = input("Enter an adjective: ")
        noun3 = input("Enter a noun: ")

        mads3 = f"""Dear {name}, I am writing to you from a {adjective} castle in an enchanted forest. I found myself here one day after going for a ride on a {color} {animal} in {place}.
        There are {adjective2} {creature} and {adjective3} {creature} here! In the {room} there is a pool full of {noun}.
        I fall asleep each night on a {noun2} of {plural} and dream of {adjective4} {plural2}.
        It feels as though I have lived here for {number} {measure_of_time}. I hope one day you can visit, although the only way to get here now is {verbing} on a {adjective5} {noun3}!!"""

        print(mads3)
        break

    else:
        print("Invalid input. Please enter a number between 1 and 3.")
        templet = input("enter a number up to 3: ")