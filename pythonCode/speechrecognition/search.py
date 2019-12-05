import webbrowser
import subprocess
# Copy and paste the path of your chrome browser installed in your system
acrobatPath = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
searchQuery = "Bhankas Bhankas"
finalUrl = "google.co.in/search?q="+searchQuery
finalUrl = finalUrl.replace(" ", "", 1)
finalUrl = finalUrl.replace(" ", "+")
subprocess.Popen("%s %s" % (acrobatPath, finalUrl))