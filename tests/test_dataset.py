import csv
import unittest
from pathlib import Path


DATASET_PATH = (
    Path(__file__).resolve().parent.parent
    / "examples"
    / "sample-competitor-data.csv"
)


class TestCompetitorDataset(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with DATASET_PATH.open(
            mode="r", encoding="utf-8-sig", newline=""
        ) as file:
            reader = csv.DictReader(file)
            cls.headers = reader.fieldnames
            cls.rows = list(reader)

    def test_required_columns(self):
        self.assertEqual(
            self.headers,
            ["company", "market", "feature", "value", "evidence_status"],
        )

    def test_record_count(self):
        self.assertEqual(len(self.rows), 12)

    def test_competitors(self):
        companies = {row["company"] for row in self.rows}
        self.assertEqual(
            companies, {"Northstar", "TaskPilot", "FlowDesk"}
        )

    def test_features(self):
        features = {row["feature"] for row in self.rows}
        self.assertEqual(
            features,
            {
                "Free Plan",
                "Arabic Support",
                "Monthly Price",
                "API Integration",
            },
        )

    def test_unknown_values_are_preserved(self):
        unknown_rows = [
            row for row in self.rows
            if row["value"] == "Unknown"
        ]

        self.assertEqual(len(unknown_rows), 3)
        self.assertTrue(
            all(row["evidence_status"] == "Unknown"
                for row in unknown_rows)
        )

    def test_prices(self):
        prices = {
            row["company"]: int(row["value"].split()[0].replace("$", ""))
            for row in self.rows
            if row["feature"] == "Monthly Price"
            and row["value"] != "Unknown"
        }

        self.assertEqual(prices["Northstar"], 12)
        self.assertEqual(prices["TaskPilot"], 9)
        self.assertEqual(prices["Northstar"] - prices["TaskPilot"], 3)
        self.assertEqual((12 - 9) * 12, 36)
        self.assertAlmostEqual((12 - 9) / 9 * 100, 33.333333, places=4)


if __name__ == "__main__":
    unittest.main()
