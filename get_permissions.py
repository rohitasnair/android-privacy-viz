# Module to extract permissions and trackers list

from bs4 import BeautifulSoup
import csv

csv_file = open('privacy_concerns.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Application', 'Trackers', 'Permissions'])

count = 1
while True:
    str_count = str(count)

    try:
        with open('data/TRACK_' + str_count + '.html') as html_file:
            soup = BeautifulSoup(html_file, 'lxml')

            try:
                app_name = soup.find('div', class_='alert-heading').h2.b.text
                print(app_name)

                trackers = soup.find('div', class_='card-body').ul.text
                print(trackers)

                permissions = soup.find('table', class_='table table-sm').samp.text
                print(permissions)
                print('\n\n\n')

                count = count + 1

            except Exception as e:
                trackers = None
                print(trackers)

                permissions = None
                print(permissions)

                count = count + 1



    except Exception as e:
        print(e)
        count = count + 1

    csv_writer.writerow([app_name, trackers, permissions])

csv_file.close()



