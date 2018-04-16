import time
from scraper import StudentsScraper

# Start timer
start_time = time.time()
scraper = StudentsScraper();
scraper.scrape();
# Show elapsed time
end_time = time.time()
print ("\nelapsed time: " + \
			str(round(((end_time - start_time) / 60) , 2)) + " minutes")

