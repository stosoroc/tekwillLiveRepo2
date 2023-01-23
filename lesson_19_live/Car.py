class Car:

    def __init__(self, make, model, vin, plate, color, year):
        self.make = make
        self.model = model
        self.vin = vin
        self.plate = plate
        self.color = color
        self.year = year

        self.rental_history = []
        self.rental_count = 0

    def rent(self, idnp, date):
        self.rental_history.append((date, idnp))
        self.rental_count += 1


class Cust:
    def __init__(self, first_name, last_name, idnp, dob, total_rentals):
        self.first_name = first_name
        self.last_name = last_name
        self.idnp = idnp
        self.dob = dob
        self.total_rentals = total_rentals
        self.rental_history = []
        self.rental_count = 0

    def rent(self, car_plate, date):
        self.rental_history.append((date, car_plate))
        self.rental_count += 1


class ReservationService:

    def __init__(self, car, customer, date):
        self.car = car
        self.customer = customer
        self.date = date

    def check_can_reserve(self):
        """Verifica daca poate fi creata reservatia"""
        if self.car.rental_history:
            pass

    def reserve(self):
        """Creaza si salveaza rezervatia"""


class FileReservationService:

    def __init__(self, file):
        self._file = file
        self._reservtaions = []
        self._reservations_count_today = 0

    def add_reservation(self, reservation_info):
        pass

    def _save_reservation_to_file(self):
        pass

    def _check_reservation_possible(self, reservation_info):
        pass


class TravelAgency:

    def get_best_offer(self):
        pass

    def get_offer_in_budget_range(self):
        pass

    def get_offer_for_country(self):
        pass


ta = TravelAgency()
ta.get_best_offer()
