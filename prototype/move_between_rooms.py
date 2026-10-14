"""Module Six Milestone starter for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Main lobby": {"south"},
    "Ventilation Shat": {"center"},
    "Security Substation": {"east"},
    "Server": {"west"}
    "executive lounge": {"north west"}
    "CEO's Panthouse": {"north east"
}
while True:
    print(f"You are in the {current_room}.")
    command = input("Enter a direction (north/south/east/west) or 'exit': ").strip().lower()
    if command == "exit":
        print("Goodbye!")
        break
    if command in rooms[current_room]:
        current_room = rooms[current_room][command]
    else:
        print("You can't go that way.")
