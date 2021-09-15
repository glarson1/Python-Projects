import webbrowser





f = open("basic.html", "w")
f.write("<html><body><h1>Stay tuned for our amazing summer sale!</h1>{}</body></html>")
f.close()





basicHTML = 'C:/Users/gabri/OneDrive/Documents/GitHub/Python-Projects/basic.html'

webbrowser.open_new_tab(basicHTML)
