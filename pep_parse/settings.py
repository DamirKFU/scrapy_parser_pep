from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'


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