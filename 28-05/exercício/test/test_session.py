from src.domain.model import Room, Movie, Session, Theater
from src.domain.errors import DuplicateSession
import pytest

def test_sucessfully_create_session():
    theater = Theater()
    room = Room("1")
    movie = Movie("MovieName", 90)
    session = theater.create_session(movie, room, "14:30")
    assert type(session) == Session
    assert session in theater.sessions
    assert session.movie == movie
    assert session.room == room
    
def test_can_create_session_with_unique_id():
    theater = Theater()
    room = Room("1")
    movie = Movie("MovieName", 90)
    session1 = theater.create_session(movie, room, "14:30") # id = 0
    session2 = theater.create_session(movie, room, "14:30") # id = 1
    session3 = session1  # id = 0
    
    with pytest.raises(DuplicateSession):
        theater.add_session(session3)
    
    assert session2 in theater.sessions
    
def test_can_calculate_end_time():
    theater = Theater()
    room = Room("1")
    movie = Movie("MovieName", 90)
    session = theater.create_session(movie, room, "14:30")
    assert session.end_time() == "16:00"
    
def test_can_check_if_seat_is_available():
    theater = Theater()
    room = Room("1")
    movie = Movie("MovieName", 90)
    session = theater.create_session(movie, room, "14:30")
    assert session.check_available_seat("B2") is True