# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Bangladeshi Railways.

class Train:
    def __init__(self, train_name, total_seats, fare_per_seat):
   
        """ Initializes a Train object with a name, total seats, and fare per seat.Also sets the available seats to the total number of seats initially."""
        self.train_name = train_name
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.fare_per_seat = fare_per_seat

    def book_ticket(self, num_tickets):

        """ Books a specified number of tickets if available. Updates the available seats accordingly. Returns a message indicating success or failure. """
        if num_tickets <= 0:
            return "Invalid number of tickets requested. Please enter a positive number."
        
        # Check if there are enough seats available to book
        if num_tickets > self.available_seats:
            return f"Only {self.available_seats} seats are available. Cannot book {num_tickets} tickets."
        
        # Deduct the booked tickets from available seats
        self.available_seats -= num_tickets
        return f"Successfully booked {num_tickets} tickets on {self.train_name}."

    def get_status(self):
        # Returns the current status of available seats for the train.
        return f"{self.available_seats} seats are available on {self.train_name}."

    def get_fare_info(self):
        # Returns the fare information for the train.
        return f"The fare per seat for {self.train_name} is {self.fare_per_seat} BDT."

if __name__ == "__main__":
    # Create a Train object with the name, total seats, and fare per seat
    Chattala_Express = Train("Chattala Express", 100, 250)

    # Print the fare information for the train
    print(Chattala_Express.get_fare_info())

    # Print the initial status of available seats
    print(Chattala_Express.get_status())

    # Attempt to book 5 tickets
    print(Chattala_Express.book_ticket(5))

    # Print the status of available seats after booking
    print(Chattala_Express.get_status())

    # Attempt to book 200 tickets, which is more than the available seats
    print(Chattala_Express.book_ticket(200))

