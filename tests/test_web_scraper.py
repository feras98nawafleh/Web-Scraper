from web_scraper import __version__
from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report

def test_version():
    assert __version__ == '0.1.0'

def test_count():
    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    actual = get_citations_needed_count(URL)
    expected = 5

    assert actual == expected

def test_report():
    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    actual = get_citations_needed_report(URL)
    expected = '[{"title": "citation needed", "citation number": 1}, {"title": "citation needed", "citation number": 2}, {"title": "citation needed", "citation number": 3}, {"title": "citation needed", "citation number": 4}, {"title": "citation needed", "citation number": 5}]'

    assert actual == expected