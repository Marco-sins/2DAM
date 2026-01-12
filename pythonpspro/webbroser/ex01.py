import webbrowser

chrome = webbrowser.get(using='google-chrome')  # get a specific browser
chrome.open('http://www.python.org', new=1)  # open in a new tab, if possible