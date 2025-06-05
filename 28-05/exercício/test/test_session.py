from src.domain.model import Room, Movie, Session, Theater, SeatStatus, Seat
from src.domain.errors import DuplicateSession, OverlapSessionRoom, OverlapSessionStartTime
import pytest
from test.builder.session_builder import SessionBuilder
from test.builder.room_builder import RoomBuilder
from datetime import datetime

def test_sucessfully_create_session():
    theater = Theater()
    room = Room("1")
    movie = Movie("MovieName", 90)
    session = theater.create_session(movie, room, "14:30")
    assert type(session) == Session
    assert session in theater.sessions
    assert session.movie == movie
    assert session.room == room
    
def test_can_calculate_end_time():
    theater = Theater()
    room = Room("1")
    movie = Movie("MovieName", 90)
    session = theater.create_session(movie, room, "14:30")
    assert session.end_time().strftime("%H:%M") == "16:00"
    
def test_can_check_if_seat_is_available():
    session = SessionBuilder().aSession().build()
    assert session.check_available_seat("B2") is True
    
def test_can_get_all_available_seats():
    reserved_room = RoomBuilder().aReserved_room().build()
    # 4x4, primeira fileira está ocupada
    session = SessionBuilder().aSession().with_room(reserved_room).build()
    available_seats = []
    for row in session.room.rows:
        for seat in row:
            if seat.status == SeatStatus.AVAILABLE:
                available_seats.append(seat)
    
    assert len(available_seats) == 12
    assert available_seats[0].row == "B"
    assert available_seats[0].number == 1
    
def test_session_room_overlap_detection():
    theater = Theater()
    room1 = Room("1")
    movie = Movie("MovieName", 90)
    session1 = theater.create_session(movie, room1, "16:30")
    session2 = SessionBuilder().aSession().build()
         
    # same room and time, different movie
    with pytest.raises(OverlapSessionRoom):
        theater.add_session(session2)
        
    # same room, dif time
    session3 = SessionBuilder().aSession().with_start_time("21:00").build()
    theater.add_session(session3)   
    assert session3 in theater.sessions
    
    # dif room, same time
    session4 = SessionBuilder().aSession().with_room(Room("2")).build()
    theater.add_session(session4)   
    assert session4 in theater.sessions
    
def test_detect_overlap_in_sessions_starting_time():
    '''
    Testar se o filme anterior já acabou, para começar o próximo
    '''
    theater = Theater() 
    session1 = SessionBuilder().aSession().build()
    session2 = SessionBuilder().aSession().with_start_time("18:33").build()
    theater.add_session(session1)   
    with pytest.raises(OverlapSessionStartTime):
        theater.add_session(session2)  