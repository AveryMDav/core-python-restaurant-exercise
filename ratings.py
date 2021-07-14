"""Restaurant rating lister."""


def get_scores():
    score = open('scores.txt')
    scores = {}
    for i in score:
        i = i.rstrip() 
        restaurant, score = i.split(':')
        scores[restaurant] = int(score)
    
    add_restaurants(scores)

    return display_restaurants(sorted(scores.items()))


def display_restaurants(scores):
    for i, x in scores:
        print(i,"has a score of", str(x)+"!")


def add_restaurants(scores):
    new_scores = scores
    new = input("Would you like to add a new review? Yes or No:\n")

    if new == "Yes":
        new_name = input("What is the restaurants name?\n")
        new_rating = input("What would you rate this resaurant between 1-5?\n")
        new_scores[new_name] = new_rating
    
    return new_scores


get_scores()