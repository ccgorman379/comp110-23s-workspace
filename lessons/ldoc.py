"""LDOC Practice Question."""

class PlaneTicket:

    departure_city: str
    arrival_city: str
    departure_time: int
    ticket_cost: float

    def __init__(self, city_a: str, city_b: str, depart: int, cost: float) -> None:
        """Create a new object of class PlaneTicket."""
        self.departure_city = city_a
        self.arrival_city = city_b
        self.departure_time = depart
        self.ticket_cost = cost
    
    def __str__(self) -> str:
        """Returns a readable ticket."""
        ticket_str: str = f"Flight from {self.departure_city} at {self.departure_time}"
        ticket_str += f"Arrive in {self.arrival_city}. Cost ${self.ticket_cost}."
        return ticket_str
    
    def delay(self, delay_hours: int) -> None:
        """Update departure time."""
        self.departure_time = self.departure_time + (delay_hours * 100)
        self.departure_time = self.departure_time % 2400
    
    def discount(self, discount: float) -> None:
        """Discount ticket cost by given discount amount."""
        self.ticket_cost = self.ticket_cost * (1-discount)

def compare_prices(ticket1: PlaneTicket, ticket2: PlaneTicket) -> PlaneTicket:
    """Compare prices of two tickets to see which is cheaper."""
    if ticket1.ticket_cost < ticket2.ticket_cost:
        return ticket1
    else:
        return ticket2


ticket: PlaneTicket = PlaneTicket("Raleigh", "New Orleans", 1000, 85.25)
print(ticket)
ticket.delay(2)
ticket.discount(0.10)

other_ticket: PlaneTicket = PlaneTicket("Orlando", "San Francisco", 1100, 100.50)
print(compare_prices(ticket, other_ticket))