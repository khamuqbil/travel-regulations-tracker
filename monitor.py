import mechanicalsoup

browser = mechanicalsoup.Browser()
page = browser.get("https://www.saudia.com/before-flying/travel-information/travel-requirements-by-international-stations")
tag = page.soup.select("#ui-di-2")
result = tag.text

print(f"The result of your dice roll is: {result}")
