from src.domain.model import Session, Booking, User, Theater, Room, Seat, SeatStatus
from test.builder.session_builder import SessionBuilder
from datetime import datetime

def test_booking_time_tracking():
    booking = Booking()
    assert booking.current == datetime.now()
    
def test_calculate_total_price():
    booking = Booking()
    session = SessionBuilder().aSession().build()
    session2 = SessionBuilder().aSession().with_room(Room("2")).build()
    booking.add_session(session)
    
    assert booking.total_price() == session.price
    
    booking.add_session(session2)
    
    assert booking.total_price() == session.price + session2.price
    
def test_can_add_booking_to_user_and_session():
    user = User("Evandro")
    session = SessionBuilder().aSession().build()
    
    user.add_booking(session, "B", 4)
    
    seat = session.room.get_seat("B",4)
    
    assert user in session.bookings
    assert session in user.bookings.tickets
    assert seat.status == SeatStatus.RESERVED
    
def test_can_confirm_booking():
    theater = Theater()
    user = User("Evandro")
    session:Session = SessionBuilder().aSession().build()
    seat_name = "B"
    seat_number = 4
    seat = session.room.get_seat(seat_name, seat_number)
    
    user.add_booking(session, seat_name, seat_number)
    user.confirm_booking(session,seat_name, seat_number)
    
    assert len(session.bookings) == 1
    assert seat.status == SeatStatus.OCCUPIED