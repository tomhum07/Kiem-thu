class AirService:
	def __init__(self) -> None:
		self._airlines = {
			"VN": "Vietnam Airlines",
			"QH": "Bamboo Airways",
			"VJ": "VietJet Air",
		}
		self._bookings = {
			"BK001": {
				"email": "khach1@example.com",
				"confirmed": False,
				"origin": "SGN",
				"destination": "HAN",
			},
			"BK002": {
				"email": "khach2@example.com",
				"confirmed": True,
				"origin": "DAD",
				"destination": "SGN",
			},
		}
		self._flights = [
			{"id": "F001", "origin": "SGN", "destination": "HAN", "airline": "VN"},
			{"id": "F002", "origin": "SGN", "destination": "DAD", "airline": "VJ"},
			{"id": "F003", "origin": "DAD", "destination": "SGN", "airline": "QH"},
		]

	@staticmethod
	def _require_text(value: str, field_name: str) -> str:
		if not isinstance(value, str) or not value.strip():
			raise ValueError(f"{field_name} phai la chuoi khong rong")
		return value.strip()

	def confirm_booking(self, booking_id: str) -> bool:
		booking_id = self._require_text(booking_id, "booking_id")
		booking = self._bookings.get(booking_id)
		if booking is None:
			raise ValueError("khong tim thay booking")
		booking["confirmed"] = True
		return True

	def find_airline(self, code: str) -> str | None:
		code = self._require_text(code, "code").upper()
		return self._airlines.get(code)

	def search_flights_by_location(self, origin: str, destination: str) -> list[dict]:
		origin = self._require_text(origin, "origin").upper()
		destination = self._require_text(destination, "destination").upper()
		return [
			flight
			for flight in self._flights
			if flight["origin"] == origin and flight["destination"] == destination
		]

	def find_flights_by_location(self, origin: str, destination: str) -> list[dict]:
		return self.search_flights_by_location(origin, destination)

	def check_flight_time(self, departure_min: int, arrival_min: int) -> int:
		for name, value in ("departure_min", departure_min), ("arrival_min", arrival_min):
			if not isinstance(value, int):
				raise ValueError(f"{name} phai la so nguyen")
			if value < 0 or value > 1440:
				raise ValueError(f"{name} ngoai pham vi")
		if arrival_min < departure_min:
			raise ValueError("arrival_min khong duoc nho hon departure_min")
		return arrival_min - departure_min

	def send_checkin_reminder(self, booking_id: str, hours_before: int) -> str:
		booking_id = self._require_text(booking_id, "booking_id")
		if not isinstance(hours_before, int) or hours_before < 1 or hours_before > 48:
			raise ValueError("hours_before phai trong khoang 1..48")
		booking = self._bookings.get(booking_id)
		if booking is None:
			raise ValueError("khong tim thay booking")
		return f"Da gui nhac nho toi {booking['email']} ({hours_before}h)"


class HotelService:
	def __init__(self) -> None:
		self._hotels = {
			"H001": {"name": "Da Nang Beach Resort", "city": "Da Nang", "rating": 4.5, "price": 50},
			"H002": {"name": "Ha Noi Old Quarter", "city": "Ha Noi", "rating": 4.0, "price": 40},
			"H003": {"name": "Sai Gon Central", "city": "Ho Chi Minh", "rating": 3.8, "price": 35},
		}
		self._bookings: dict[str, dict] = {}
		self._next_booking = 1
		self._reviews: dict[str, list[dict]] = {}

	@staticmethod
	def _require_text(value: str, field_name: str) -> str:
		if not isinstance(value, str) or not value.strip():
			raise ValueError(f"{field_name} phai la chuoi khong rong")
		return value.strip()

	def search_hotels(self, city: str, min_rating: float = 0) -> list[dict]:
		city = self._require_text(city, "city").lower()
		if not isinstance(min_rating, (int, float)) or min_rating < 0 or min_rating > 5:
			raise ValueError("min_rating phai trong khoang 0..5")
		results = []
		for hotel_id, info in self._hotels.items():
			if info["city"].lower() == city and info["rating"] >= min_rating:
				results.append({"id": hotel_id, **info})
		return results

	def book_room(self, hotel_id: str, nights: int) -> str:
		hotel_id = self._require_text(hotel_id, "hotel_id")
		if hotel_id not in self._hotels:
			raise ValueError("khong tim thay khach san")
		if not isinstance(nights, int) or nights < 1 or nights > 30:
			raise ValueError("nights phai trong khoang 1..30")
		booking_id = f"HB{self._next_booking:03d}"
		self._next_booking += 1
		self._bookings[booking_id] = {"hotel_id": hotel_id, "nights": nights}
		return booking_id

	def cancel_booking(self, booking_id: str) -> bool:
		booking_id = self._require_text(booking_id, "booking_id")
		if booking_id not in self._bookings:
			raise ValueError("khong tim thay booking")
		del self._bookings[booking_id]
		return True

	def cancel_room(self, booking_id: str) -> bool:
		return self.cancel_booking(booking_id)

	def check_price(self, hotel_id: str, nights: int) -> float:
		hotel_id = self._require_text(hotel_id, "hotel_id")
		if hotel_id not in self._hotels:
			raise ValueError("khong tim thay khach san")
		if not isinstance(nights, int) or nights < 1 or nights > 30:
			raise ValueError("nights phai trong khoang 1..30")
		return self._hotels[hotel_id]["price"] * nights

	def review_hotel(self, hotel_id: str, rating: float, comment: str = "") -> bool:
		hotel_id = self._require_text(hotel_id, "hotel_id")
		if hotel_id not in self._hotels:
			raise ValueError("khong tim thay khach san")
		if not isinstance(rating, (int, float)) or rating < 1 or rating > 5:
			raise ValueError("rating phai trong khoang 1..5")
		if not isinstance(comment, str):
			raise ValueError("comment phai la chuoi")
		self._reviews.setdefault(hotel_id, []).append({"rating": float(rating), "comment": comment})
		return True

	def rate_hotel(self, hotel_id: str, rating: float, comment: str = "") -> bool:
		return self.review_hotel(hotel_id, rating, comment)


class SearchPlanService:
	def __init__(self) -> None:
		self._plans: dict[str, dict] = {}
		self._next_plan = 1
		self._catalog = [
			"flight: SGN->HAN",
			"flight: SGN->DAD",
			"hotel: Da Nang Beach Resort",
			"hotel: Ha Noi Old Quarter",
			"restaurant: Pho 24",
		]

	@staticmethod
	def _require_text(value: str, field_name: str) -> str:
		if not isinstance(value, str) or not value.strip():
			raise ValueError(f"{field_name} phai la chuoi khong rong")
		return value.strip()

	def search_all(self, query: str) -> list[str]:
		query = self._require_text(query, "query").lower()
		return [item for item in self._catalog if query in item.lower()]

	def filter_results(self, results: list[str], keyword: str) -> list[str]:
		if not isinstance(results, list):
			raise ValueError("results phai la list")
		keyword = self._require_text(keyword, "keyword").lower()
		return [item for item in results if keyword in item.lower()]

	def personalized_suggestions(self, user_profile: dict) -> list[str]:
		if not isinstance(user_profile, dict):
			raise ValueError("user_profile phai la dict")
		favorite_city = user_profile.get("favorite_city")
		if not favorite_city:
			raise ValueError("favorite_city la bat buoc")
		city = str(favorite_city).strip()
		if not city:
			raise ValueError("favorite_city la bat buoc")
		return [f"hotel: {city} budget", f"food: {city} local"]

	def personalized_suggestion(self, user_profile: dict) -> list[str]:
		return self.personalized_suggestions(user_profile)

	def save_plan(self, user_id: str, items: list[str]) -> str:
		user_id = self._require_text(user_id, "user_id")
		if not isinstance(items, list) or not items:
			raise ValueError("items phai la list khong rong")
		plan_id = f"PL{self._next_plan:03d}"
		self._next_plan += 1
		self._plans[plan_id] = {"user_id": user_id, "items": list(items)}
		return plan_id

	def optimize_itinerary(self, items: list) -> list:
		if not isinstance(items, list):
			raise ValueError("items phai la list")
		if items and isinstance(items[0], dict) and "priority" in items[0]:
			return sorted(items, key=lambda item: item.get("priority", 0))
		return sorted(items)
