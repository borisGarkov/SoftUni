rooms_number = int(input())
free_chairs = 0
is_game_one = True
for number_of_room in range(1, rooms_number + 1):
    room = input().split()
    chairs_number = int(room[0].count("X"))
    taken_places = int(room[-1])
    difference = taken_places - chairs_number

    if difference > 0:
        print(f"{abs(difference)} more chairs needed in room {number_of_room}")
        is_game_one = False
    else:
        free_chairs += difference

if is_game_one:
    print(f"Game On, {abs(free_chairs)} free chairs left")