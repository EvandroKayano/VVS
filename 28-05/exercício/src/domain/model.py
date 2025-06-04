from dataclasses import dataclass, field
from enum import Enum
from src.domain.errors import DuplicateRoomName, DuplicateMovieName, DuplicateSession
from datetime import timedelta, datetime

class SeatStatus(Enum):
    AVAILABLE = "available"
    RESERVED = "reserved"
    OCCUPIED = "occupied"

@dataclass
class Seat:
    row: str
    number: int
    status: SeatStatus = SeatStatus.AVAILABLE

    @property
    def is_available(self):
        return self.status == SeatStatus.AVAILABLE
    
    def reserve(self):
        if self.status == SeatStatus.AVAILABLE:
            self.status = SeatStatus.RESERVED
            return True
        return False
    
    def confirm(self):
        if self.status == SeatStatus.RESERVED:
            self.status = SeatStatus.OCCUPIED
            return True
        return False
    
    def release(self):
        self.status = SeatStatus.AVAILABLE

    
@dataclass
class Room:
    name: str
    rows: list[list[Seat]]

    def __init__(self, name, seats=None):
        self.name = name
        self.rows = []
        if seats is None:
            self.create_list_of_seats()
            return
        i = 65
        for row in seats:
            row_seats = []
            row_name = chr(i)
            for j in range(row):
                seat = Seat(row=row_name, number=j+1)
                row_seats.append(seat)
            self.rows.append(row_seats)
            i += 1

    def create_list_of_seats(self):
        for i in range(10):
            row = chr(i + 65)
            row_seats = []
            for j in range(10):
                seat = Seat(row=row, number=j+1)
                row_seats.append(seat)
            self.rows.append(row_seats)

    def capacity(self):
        seats = 0
        for row in self.rows:
            seats += len(row)
        return seats
    
    def available_seats(self):
        available_seats = 0
        for row in self.rows:
            for seat in row:
                if seat.is_available:
                    available_seats += 1
        return available_seats
    
@dataclass
class Movie:
    title: str
    duration: int
    
    def __init__(self,title,duration):
        self.title = title
        self.duration = duration
        
    def get_duration(self):
        minutes = self.duration % 60
        hours = int(self.duration // 60)    
        result = f'{hours}h{minutes}min'
        return result
    
    def get_timedelta(self):
        return timedelta(minutes=self.duration)
    
 
@dataclass
class Session:
    room: Room
    movie: Movie
    id: int
    start_time: str
    
    def __init__(self, movie, room, start_time, id):
        self.room = room
        self.movie = movie
        self.start_time = start_time
        self.id = id
    
    def end_time(self):
        formatted_date = datetime.strptime(self.start_time, "%H:%M")
        end_dt = formatted_date + self.movie.get_timedelta()
        return end_dt.strftime("%H:%M")    
    
    def check_available_seat(self,seat_name):
        '''
        Transforma o nome da cadeira em inteiros: fileira e coluna.
        Assim acessamos a lista de cadeiras e verificamos se está
        ocupada ou não
        '''
        # seat_name = "B2", por exemplo
        seat_row = ord(seat_name[0]) - 65 # B -> 66
        seat_number = int(seat_name[1:]) # 2
        seat = self.room.rows[seat_row][seat_number]
        return (True if seat.status == SeatStatus.AVAILABLE else False)
        
    
@dataclass
class Theater:
    rooms: list[Room] = field(default_factory=list)
    movies: list[Movie] = field(default_factory=list)
    sessions: list[Session] = field(default_factory=list)
    n_sessions: int = 0

    def add(self, room):
        if self.duplicate_room_name(room):
            raise DuplicateRoomName()
        self.rooms.append(room)

    def remove(self, room):
        self.rooms.remove(room)

    def duplicate_room_name(self, room):
        return [theater_room for theater_room in self.rooms if theater_room.name == room.name]
    
    
    def addMovie(self, movie):
        if self.duplicate_movie_name(movie):
            raise DuplicateMovieName()
        self.movies.append(movie)

    def removeMovie(self, movie):
        self.movies.remove(movie)

    def duplicate_movie_name(self, movie):
        return [theater_movie for theater_movie in self.movies if theater_movie.title == movie.title]
    
    
    def create_session(self, movie, room, start_time):
        '''
        takes a movie and a room and creates a session
        '''
        session = Session(movie, room, start_time, self.n_sessions)
        self.n_sessions += 1
        self.add_session(session)
        
        return session
    
    def add_session(self, session):
        # checks if the object is duplicated
        if self.duplicate_session(session):
            raise DuplicateSession
        self.sessions.append(session)
        
    def remove_session(self, session):
        '''
        takes a session and remove
        '''
        self.sessions.remove(session)
        
    def duplicate_session(self, session):
        return [dup_session for dup_session in self.sessions if dup_session.id == session.id]