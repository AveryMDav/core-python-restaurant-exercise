"""Restaurant rating lister."""


def start_up():
    scores = {}
    score = open('scores.txt')
    print("Select an option\n"
        "See all ratings: 1\n"
        "Add a new restaurant: 2\n"
        "Quit program: 3\n")
    options = int(input("Input option number to select\n"))

    if options == 1:
        get_scores(score, scores)

    elif options == 2:
            new_scores = add_restaurants()
            scores.update(new_scores)
            return start_up()

    elif options == 3:
        print('3')

    else:
        print("This is not a valid option")
        return start_up()



def get_scores(score, scores):
    for i in score:
        restaurant, score = i.split(':')
        scores[restaurant] = int(score)

    return display_restaurants(sorted(scores.items()))


def display_restaurants(scores):
    for i, x in scores:
        print(i,"has a score of", str(x)+".")
    return start_up()

def add_restaurants():
    new_scores = {}
    new = input("Would you like to add a new review? Yes or No:\n").lower()
    
    if new == "yes":
        new_name = input("What is the restaurants name?\n").capitalize()
        new_rating = rating()
        
        new_scores[new_name] = new_rating
    elif new == "no":
        pass
    else:
        print("Sorry I didn't quite understand that")
        return add_restaurants()
        
    return new_scores

def rating():
    new_rating = input("What would you rate this resaurant between 1-5?\n")
    if int(new_rating) <= 5 and int(new_rating) >= 1:
        return new_rating
    else:
        print("Please input a rating of 1-5")
        return rating()
        
start_up()