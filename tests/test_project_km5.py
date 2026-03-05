import unittest
from project_km5 import *


class TestProjectKM5(unittest.TestCase):
    def test_segment_distances(self):
        # Simple 2D path
        self.assertEqual(
            segment_distances(
                [
                    [0, 0],
                    [3, 4],
                ]
            ),
            [5.0],
        )

        # 3D path with two segments
        self.assertEqual(
            segment_distances(
                [
                    [0, 0, 0],
                    [0, 0, 6],
                    [0, 8, 6],
                ]
            ),
            [6.0, 8.0],
        )

    def test_window_sums(self):
        # Window of 2 over small list
        # [1, 2] -> 3
        # [2, 3] -> 5
        # [3, 4] -> 7
        self.assertEqual(
            window_sums([1, 2, 3, 4], 2),
            [3, 5, 7],
        )

        # Window of 3 with positive and negative values
        # [10, -10, 10]   -> 10
        # [-10, 10, -10]  -> -10
        # [10, -10, 10]   -> 10
        self.assertEqual(
            window_sums([10, -10, 10, -10, 10], 3),
            [10, -10, 10],
        )

    def test_spam_filter_stats(self):
        stats = spam_filter_stats(0.2, 0.9, 0.8)
        # Expected values for a single email "population"
        # tp = 0.2 * 0.9  = 0.18
        # fn = 0.2 * 0.1  = 0.02
        # tn = 0.8 * 0.8  = 0.64
        # fp = 0.8 * 0.2  = 0.16
        # ppv = 0.18 / (0.18 + 0.16) ≈ 0.529
        self.assertAlmostEqual(stats["tp"], 0.18, places=3)
        self.assertAlmostEqual(stats["fn"], 0.02, places=3)
        self.assertAlmostEqual(stats["tn"], 0.64, places=3)
        self.assertAlmostEqual(stats["fp"], 0.16, places=3)
        self.assertAlmostEqual(stats["ppv"], 0.529, places=3)

        # Rare spam scenario
        stats_rare = spam_filter_stats(0.01, 0.99, 0.9)
        # Here ppv is about 0.091 (9.1%)
        self.assertAlmostEqual(stats_rare["ppv"], 0.091, places=3)

    def test_shared_items(self):
        # Overlapping shopping lists, with duplicates in one list
        result = shared_items(
            ["milk", "eggs", "bread", "eggs"],
            ["bread", "cereal", "milk"],
        )
        self.assertEqual(set(result), {"milk", "bread"})

        # Completely disjoint lists
        self.assertEqual(
            shared_items(
                ["apples", "bananas"],
                ["coffee", "tea"],
            ),
            [],
        )

    def test_max_temperature_rise(self):
        # Temperatures rise and fall; best increase is 7 -> 15 (8 degrees)
        self.assertEqual(
            max_temperature_rise([10, 7, 12, 8, 15]),
            8,
        )

        # Always decreasing: no positive rise
        self.assertEqual(
            max_temperature_rise([30, 28, 25, 20]),
            0,
        )

        # Flat then jump
        self.assertEqual(
            max_temperature_rise([5, 5, 5, 10]),
            5,
        )

    def test_population_projection(self):
        # 50% growth per year for 2 years: 100 * 1.5^2 = 225
        self.assertEqual(
            population_projection(100, 0.5, 2),
            225,
        )

        # Zero growth leaves population unchanged
        self.assertEqual(
            population_projection(1000, 0.0, 10),
            1000,
        )

    def test_months_to_repay_loan(self):
        # Exact multiple of monthly payment
        self.assertEqual(
            months_to_repay_loan(1000, 250),
            4,
        )

        # Not an exact multiple; should round up
        self.assertEqual(
            months_to_repay_loan(1000, 300),
            4,
        )

    def test_validate_schedule(self):
        # Total time 3 hours, total energy 4.5 -> within limits
        self.assertIs(
            validate_schedule(
                [
                    (2, 3.0),
                    (1, 1.5),
                ],
                4,
                5.0,
            ),
            True,
        )

        # Time exceeds the daily limit even though energy is fine
        self.assertIs(
            validate_schedule(
                [
                    (2, 3.0),
                    (1, 1.5),
                ],
                2,
                10.0,
            ),
            False,
        )


if __name__ == "__main__":
    unittest.main()