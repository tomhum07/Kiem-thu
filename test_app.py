import os
import sys
import time
import unittest

sys.path.append(os.path.dirname(__file__))

from app import AirService, HotelService, SearchPlanService


class TestAirService(unittest.TestCase):
    def setUp(self) -> None:
        self.service = AirService()

    def test_functional_confirm_booking_success(self) -> None:
        self.assertTrue(self.service.confirm_booking("BK001"))

    def test_negative_confirm_booking_invalid(self) -> None:
        with self.assertRaises(ValueError):
            self.service.confirm_booking("BK999")

    def test_boundary_check_flight_time_zero_duration(self) -> None:
        self.assertEqual(0, self.service.check_flight_time(600, 600))

    def test_boundary_send_checkin_reminder_min_hours(self) -> None:
        message = self.service.send_checkin_reminder("BK001", 1)
        self.assertIn("Da gui nhac nho", message)

    def test_negative_find_airline_unknown(self) -> None:
        self.assertIsNone(self.service.find_airline("ZZ"))

    def test_performance_search_flights(self) -> None:
        start = time.perf_counter()
        for _ in range(2000):
            self.service.search_flights_by_location("SGN", "HAN")
        duration = time.perf_counter() - start
        self.assertLess(duration, 0.2)

    # @unittest.expectedFailure
    def test_expected_failure_find_flights_mismatch(self) -> None:
        results = self.service.find_flights_by_location("SGN", "HAN")
        self.assertEqual(len(results), 0)


class TestHotelService(unittest.TestCase):
    def setUp(self) -> None:
        self.service = HotelService()

    def test_functional_search_hotels_city(self) -> None:
        results = self.service.search_hotels("Da Nang", min_rating=4.0)
        self.assertGreaterEqual(len(results), 1)
        self.assertEqual(results[0]["city"], "Da Nang")

    def test_boundary_book_room_min_nights(self) -> None:
        booking_id = self.service.book_room("H001", 1)
        self.assertTrue(booking_id.startswith("HB"))

    def test_negative_book_room_invalid_nights(self) -> None:
        with self.assertRaises(ValueError):
            self.service.book_room("H001", 0)

    def test_functional_cancel_room(self) -> None:
        booking_id = self.service.book_room("H001", 2)
        self.assertTrue(self.service.cancel_room(booking_id))

    def test_performance_check_price(self) -> None:
        start = time.perf_counter()
        for _ in range(2000):
            self.service.check_price("H001", 2)
        duration = time.perf_counter() - start
        self.assertLess(duration, 0.2)

    def test_functional_rate_hotel(self) -> None:
        self.assertTrue(self.service.rate_hotel("H001", 4.0, "tot"))

    # @unittest.expectedFailure
    def test_expected_failure_price_mismatch(self) -> None:
        self.assertEqual(self.service.check_price("H001", 2), 1)


class TestSearchPlanService(unittest.TestCase):
    def setUp(self) -> None:
        self.service = SearchPlanService()

    def test_functional_search_all(self) -> None:
        results = self.service.search_all("flight")
        self.assertGreaterEqual(len(results), 1)

    def test_negative_search_all_empty_query(self) -> None:
        with self.assertRaises(ValueError):
            self.service.search_all(" ")

    def test_boundary_save_plan_single_item(self) -> None:
        plan_id = self.service.save_plan("user01", ["flight: SGN->HAN"])
        self.assertTrue(plan_id.startswith("PL"))

    def test_functional_filter_results(self) -> None:
        results = self.service.search_all("hotel")
        filtered = self.service.filter_results(results, "Da Nang")
        self.assertGreaterEqual(len(filtered), 1)

    def test_performance_optimize_itinerary(self) -> None:
        items = [5, 3, 2, 4, 1]
        start = time.perf_counter()
        for _ in range(2000):
            self.service.optimize_itinerary(items)
        duration = time.perf_counter() - start
        self.assertLess(duration, 0.2)

    def test_negative_personalized_suggestion_missing_profile(self) -> None:
        with self.assertRaises(ValueError):
            self.service.personalized_suggestion({})

    # @unittest.expectedFailure
    def test_expected_failure_missing_suggestion(self) -> None:
        suggestions = self.service.personalized_suggestions({"favorite_city": "Hue"})
        self.assertIn("hotel: Ha Noi budget", suggestions)


if __name__ == "__main__":
    unittest.main()
