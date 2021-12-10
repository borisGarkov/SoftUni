def add(songs_data, song, composer, key):
    if song in songs_data:
        print(f"{song} is already in the collection!")
    else:
        songs_data[song] = {"Composer": composer, "Key": key}
        print(f"{song} by {composer} in {key} added to the collection!")
    return songs_data


def remove(songs_data, song):
    if song in songs_data:
        songs_data.pop(song)
        print(f"Successfully removed {song}!")
    else:
        print(f"Invalid operation! {song} does not exist in the collection.")
    return songs_data


def change_key(songs_data, song, key):
    if song in songs_data:
        songs_data[song]["Key"] = key
        print(f"Changed the key of {song} to {key}!")
    else:
        print(f"Invalid operation! {song} does not exist in the collection.")
    return songs_data


songs_number = int(input())
songs_data = {}

for _ in range(songs_number):
    song, composer, key = input().split("|")
    songs_data[song] = {"Composer": composer, "Key": key}

while True:
    command_data = input().split("|")
    command = command_data[0]
    if command == "Stop":
        break

    if command == "Add":
        song, composer, key = command_data[1:]
        songs_data = add(songs_data, song, composer, key)
    elif command == "Remove":
        song = command_data[1]
        songs_data = remove(songs_data, song)
    elif command == "ChangeKey":
        song, key = command_data[1:]
        songs_data = change_key(songs_data, song, key)

sorted_songs = sorted(songs_data.items(), key=lambda x: (x[0], x[1]["Composer"]))
for key,value in sorted_songs:
    print(f"{key} -> Composer: {value['Composer']}, Key: {value['Key']}")