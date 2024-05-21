# Room.py

class Room:
    def __init__(self, room_id, type, capacity):
        self.room_id = room_id
        self.type = type  # e.g., 'ICU', 'General', etc.
        self.capacity = capacity

    def display_info(self):
        print(f"Room ID: {self.room_id}")
        print(f"Type: {self.type}")
        print(f"Capacity: {self.capacity}")
