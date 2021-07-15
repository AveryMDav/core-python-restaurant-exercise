"""Restaurant rating lister."""



def get_scores():
    scores = {}
    score = open('scores.txt')
    for i in score:
        restaurant, score = i.split(':')
        scores[restaurant] = int(score)
    
    new_scores = add_restaurants()
    scores.update(new_scores)

    return display_restaurants(sorted(scores.items()))


def display_restaurants(scores):
    for i, x in scores:
        print(i,"has a score of", str(x)+"!")


def add_restaurants():
    new_scores = []
    new = input("Would you like to add a new review? Yes or No:\n").lower()
    
    if new == "yes":
        new_scores = {}
        new_name = input("What is the restaurants name?\n").capitalize()
        new_rating = input("What would you rate this resaurant between 1-5?\n")
        new_scores[new_name] = new_rating
    elif new == "no":
        return new_scores
    else:
        print("Sorry I didn't quite understand that")
        return add_restaurants()
        
    return new_scores


get_scores()