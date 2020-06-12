from room import Room
from player import Player
from world import World
from util import Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
def another_direction(direction):
    if direction == 'n':
        return 's'
    elif direction == 's':
        return 'n'  
    elif direction == 'e':
        return 'w'  
    elif direction == 'w':
        return 'e'  

# def search_rooms(self, starting_room):
# q = Queue()
# create stack (tried queues, couldn't get to work)
stack = Stack()
# create set like normal
visited = set()
# Only loop through the 500 rooms once, then stop
while len(visited) < len(world.rooms):
    # empty array to capture directions
    route = [] 
    # available exits
    dirs = player.current_room.get_exits()
    room_direction = player.current_room.get_room_in_direction
    # if not in visited, add to visited
    for vertex in dirs:
        if vertex != None and room_direction(vertex) not in visited:
            route.append(vertex)
    visited.add(player.current_room)
    # If we have already visited a room, choose another random room
    if len(route) > 0:
        random_room = random.randint(0, len(route) -1)
        stack.push(route[random_room])
        player.travel(route[random_room])
        traversal_path.append(route[random_room])
    # end of rooms
    else:
        x = stack.pop()
        traversal_path.append(another_direction(x))
        player.travel(another_direction(x))
   
#  route.append(vertex)
    # visited.add(player.current_room)
    # v = q.pop()
    # if len(route) > 0:
    #     
    #     player.travel(route[starting_room])
    #     q.push(route[starting_room])
    #     for direction in another_direction(v):
    #         q.push(direction)
    # else:
    #     p = q.pop()
    #     player.travel(another_direction(p))



# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
