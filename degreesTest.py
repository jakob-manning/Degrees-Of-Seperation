#degressTest

import csv
import sys

from util import Node, StackFrontier, QueueFrontier


# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}

def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass

def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors

def search(start, destination):
    load_data("small")

    startingID = start
    p = people

    destinationID = destination

    # initialize an empty explored set
    explored = set()

    #Initialize starting frontier
    ##create root node
    rootNode = Node(star = startingID, parentNode = None, film = None)
    ##create frontier
    frontier = QueueFrontier()
    frontier.add(node = rootNode)

    def searchLoop():
        while not frontier.empty():
            #remove an item from the frontier
            currentNode = frontier.remove()

            #add the item to the explored list
            explored.add(currentNode.star)

            #find neighbours for that current node
            currentID = currentNode.star

            currentNeighbourSet =  neighbors_for_person(currentID)

            # Add neighbors to frontier
            for film, star in currentNeighbourSet:
                if not frontier.contains_state(star) and star not in explored: 
                    child = Node(star=star, parentNode=currentNode, film=film)
                    #check if we are at the final location
                    if star == destinationID:
                        return child
                    frontier.add(child)
        return None
    result = searchLoop()
    
    #check if there are no nodes
    if result == None:
        return result
    
    #if there is a solution, build the list
    currentNode = result
    path = list()
    while True:
        if currentNode.parentNode == None:
            break
        path.append((currentNode.film, currentNode.star))
        currentNode = currentNode.parentNode
    path.reverse()
    return path


result = search("102", "398")
