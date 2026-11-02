# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-only
import unittest
from NBA import EAST, WEST, simulate

class NBATests(unittest.TestCase):
    def test_rosters(self):
        self.assertEqual(len(EAST), 15)
        self.assertEqual(len(WEST), 15)
        self.assertEqual(len(set(EAST + WEST)), 30)
    def test_deterministic(self):
        self.assertEqual(simulate(42), simulate(42))
    def test_champion(self):
        champion, lines = simulate(17)
        self.assertIn(champion, EAST + WEST)
        self.assertEqual(sum(" vs " in line for line in lines), 15)

if __name__ == "__main__":
    unittest.main()
