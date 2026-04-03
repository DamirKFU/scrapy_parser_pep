import csv
from collections import defaultdict
from datetime import datetime

from pep_parse.settings import RESULTS_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.counter = defaultdict(int)

    def process_item(self, item, spider):
        self.counter[item["status"]] += 1
        return item

    def close_spider(self, spider):
        total = sum(self.counter.values())
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"status_summary_{timestamp}.csv"
        file_dir = RESULTS_DIR / file_name

        with open(file_dir, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Статус", "Количество"])
            writer.writeheader()
            for status, count in self.counter.items():
                writer.writerow({"Статус": status, "Количество": count})
            writer.writerow({"Статус": "Total", "Количество": total})
