from src.domain.model import Room, Seat

class RoomBuilder:
    room: Room
    
    def aRoom(self):
        self.room = Room("1")
        return self
    
    def aReserved_room(self):
        self.room = Room(name="1",seats=[4,4,4,4])
        for i in range(4):
            self.room.rows[0][i].reserve()
        return self
    
    def build(self):
        return self.room
   