from dataclasses import dataclass, field
from enum import Enum
from src.domain.errors import DuplicateRoomName, DuplicateMovieName, DuplicateSession, OverlapSessionRoom, OverlapSessionStartTime
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
 
    def get_seat(self, seat_name, seat_number):
        seat_name = ord(seat_name) - 65
        return self.rows[seat_name][seat_number]
    
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
        return (f'{minutes}min' if hours == 0 else f'{hours}h{minutes}min' if minutes>0 else f'{hours}h')
    
    def get_timedelta(self):
        return timedelta(minutes=self.duration)
    
 
@dataclass
class Session:
    room: Room
    movie: Movie
    start_time: datetime
    price: float
    bookings: list
    
    def __init__(self, movie, room, start_time, price= 10.0, bookings=[]):
        self.room = room
        self.movie = movie
        self.start_time = datetime.strptime(start_time, "%H:%M")
        self.price = price
        self.bookings = bookings
    
    def end_time(self):
        return self.start_time + self.movie.get_timedelta()
    
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
        takes a movie, a room, a datetime and creates a session
        '''
        session = Session(movie, room, start_time)
        self.add_session(session)
        
        return session
    
    def add_session(self, session):
        # checks if the object is duplicated
        if not self.raise_Exception(session):
            self.sessions.append(session)
        
    def raise_Exception(self, session):
        # adicionando sessão igual
        if [dup_session for dup_session in self.sessions if dup_session == session]:
            raise DuplicateSession
        
        for s in self.sessions:
            # adicionando uma sessão na mesma sala e horário
            if s.room == session.room and s.start_time == session.start_time:
                raise OverlapSessionRoom    
            # adicionando uma sessão na mesma sala, enquanto o filme ainda não acabou
            if s.room == session.room and s.end_time() > session.start_time:
                raise OverlapSessionStartTime

    def remove_session(self, session):
        '''
        takes a session and remove
        '''
        self.sessions.remove(session)
         
            
@dataclass
class Booking:
    tickets: list[Session] = field(default_factory=list)       
    current: datetime = field(default_factory=datetime.now)
 
    def add_session(self,session):
        if [dup_session for dup_session in self.tickets if dup_session == session]:
            raise DuplicateSession(session)
        self.tickets.append(session)
            
    def remove_session(self, session):
        '''
        takes a session and remove
        '''
        self.tickets.remove(session)
        
    def total_price(self):
        sum = 0
        for s in self.tickets:
            sum += s.price
            
        return sum
        
    def reserve_seat(self, session:Session, seat_name, seat_number):
        to_reserve:Seat = session.room.get_seat(seat_name, seat_number)
        if to_reserve.status == SeatStatus.AVAILABLE:
            to_reserve.status = SeatStatus.RESERVED
        else:
            raise Exception()
            
    def confirm_seat(self, session: Session, seat_name, seat_number):
        to_confirm:Seat = session.room.get_seat(seat_name, seat_number)
        if to_confirm.status == SeatStatus.RESERVED:
            to_confirm.status = SeatStatus.OCCUPIED
        else:
            raise Exception()
  
            
            
@dataclass
class User:
    name: str
    bookings: Booking
    
    def __init__(self, name, booking=Booking()):
        self.name = name
        self.bookings = booking
        
        
    def add_booking(self, session:Session, seat_name, seat_number):
        self.bookings.tickets.append(session)
        session.bookings.append(self)
        
        self.bookings.reserve_seat(session, seat_name, seat_number)
        
    def confirm_booking(self, session:Session, seat_name, seat_number):
        sessao:list[Session] = [sess for sess in self.bookings.tickets if session.room == sess.room and sess.start_time == session.start_time]
        sessao[0].bookings.remove(self)
        
        self.bookings.confirm_seat(session, seat_name, seat_number)
        
    def cancel_booking(self, session, seat_name, seat_number):
        sessao:list[Session] = [sess for sess in self.bookings.tickets if session.room == sess.room and sess.start_time == session.start_time]
        sessao[0].bookings.remove(self)
                
        for s in self.bookings.tickets:
            if s.room == sessao[0].room and s.start_time == sessao[0].start_time:
                self.bookings.tickets.remove(s)
                
        seat:Seat = sessao[0].room.get_seat(seat_name,seat_number)
        seat.status = SeatStatus.AVAILABLE