from pathlib import Path

from pep_parse.constants import SPIDER_MODULES


BOT_NAME = 'pep_parse'

SPIDER_MODULES = [SPIDER_MODULES]
NEWSPIDER_MODULE = SPIDER_MODULES


ROBOTSTXT_OBEY = True


BASE_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = BASE_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)

file_name = "pep_%(time)s.csv"

FEEDS = {
    f"{RESULTS_DIR.name}/{file_name}": {
        "format": "csv",
        "fields": ["number", "name", "status"],
        "encoding": "utf-8",
        'overwrite': True,
    }
}

ITEM_PIPELINES = {
    "pep_parse.pipelines.PepParsePipeline": 300,
}