import os 
import csv
import sys

from helpers import Node,StackFrontier,QueueFrontier

movies = {}

people = {}

names = {}

def load_data(directory):

    """This function reads data from the csv files"""

    #creates a key value pair for people
    with open(f"{directory}/people.csv", mode="r") as people_file:
        reader = csv.DictReader(people_file)
        for row in reader:
            people[row["id"]] = {
                "name" : row["name"],
                "birth" : row["birth"],
                "movies" : set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])


    with open(f"{directory}/movies.csv", mode="r") as movie_file:
        reader = csv.DictReader(movie_file)
        for row in reader:
            movies[row["id"]] = {
                "title" : row["title"],
                "year" : row["year"],
                "stars" : set()
            }

    with open(f"{directory}/stars.csv", mode="r") as star_file:
        reader = csv.DictReader(star_file)
        for row in reader:
            people[row["person_id"]]["movies"].add(row["movie_id"])
            movies[row["movie_id"]]["stars"].add(row["person_id"])


def person_id_for_name(name):
    # name = name.lower()
    person_ids = list(names.get(name.lower()))
    person_ids_len = len(person_ids)
    if(person_ids_len == 0):
        return None
    elif(person_ids_len > 1):
        print(f"Which {name}?")
        for i in person_ids:
            name = people[i]["name"]
            p_id = i
            print(f"Name: {name} id: {p_id}")
        try:
            resp = input("Which id is intended? ")
            if resp in person_ids:
                return resp
        except:
            return None

    return person_ids[0]



def get_neighbours(person_id):

    movie_id = people[person_id]["movies"]
    neighbours = set()

    for m_id in movie_id:
        stars = movies[m_id]["stars"]
        for s_id in stars:
            neighbours.add((m_id, s_id))
    
    return neighbours


def shortest_path(source, goal):

    queue = QueueFrontier()
    source_movies = people[source]["movies"]


    for i in source_movies:
        temp_node = Node(source, None, i)
        queue.push(temp_node)

    while(queue.empty() != True):

        parent_node = queue.frontier[0]
        neighbours = get_neighbours(parent_node.state)
        answer = []
        push = answer.append

        for n in neighbours:
            temp_node = Node(n[1],parent_node,n[0])
            if temp_node.state == goal:
                while(temp_node.parent != None):
                    push((temp_node.action, temp_node.state))
                    temp_node = temp_node.parent
                return answer[::-1]
            else:
                response = any(x.state == temp_node.state for x in queue.frontier)
                if(response == False):
                    queue.push(temp_node)
        queue.remove()
    return None


def main():

    print("Loading data....")
    load_data("small")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")    
    
    path = shortest_path(source, target)

    if path != None:
        print(f"Degrees: {len(path)}")
        path = [(None, source)] + path
        for i in range(1,len(path)):
            source_star = people[path[i - 1][1]]["name"]
            star_movie = movies[path[i][0]]["title"]
            co_star = people[path[i][1]]["name"]
            print(f"{source_star} worked with {co_star} in {star_movie}")
    else:   
        print("There was no link")




if __name__ == "__main__":
    main()



# "Kevin Bacon"
# "Demi Moore"



# # print(get_neighbours("158"))
# print(shortest_path("158", "144"))

# print(get_neighbours("144"))
# print(movies)
# print()
# print(people)
# print()
# print(names)