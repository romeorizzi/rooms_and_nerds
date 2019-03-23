def shortest_play_length(num_rooms, num_nerds):
    n_nerds = 0
    max_in_a_room = 0
    for guests in num_nerds:
        n_nerds += guests
        if guests > max_in_a_room:
            max_in_a_room = guests
    return num_nerds - max_in_a_room

def longest_play_initial_disposition(num_rooms, num_nerds, num_in_room):
    for i in range(num_nerds):
        if i < num_nerds%num_rooms:
            num_in_room(i,1+num_nerds//num_rooms)
        else:
            num_in_room(i,num_nerds//num_rooms)

def max_num_moves(num_rooms, num_nerds):
    # TODO
    return 42

def longest_play(num_rooms, num_nerds, move):
    # TODO
    pass

def increasing_monovariant(num_rooms, num_nerds):
    monovariant = 0
    for i in range(num_rooms):
        monovariant += num_nerds[i]
    return monovariant//2

