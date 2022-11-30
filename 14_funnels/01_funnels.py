import csv
import json
from copy import deepcopy

funnel_template = {'1_home_page': 0, '2_search_page': 0, '3_payment_page': 0, '4_payment_confirmation_page': 0}
funnel_device = {}

with open('click_stream2.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, fieldnames=['user_id', 'page', 'event_date', 'device'])

    for row in csv_reader:
        funnel_device.setdefault(row['device'], {})
        funnel_device[row['device']].setdefault(row['event_date'], deepcopy(funnel_template))

        funnel_device[row['device']][row['event_date']][row['page']] += 1

with open('result.txt', mode='w') as result_file:
    result_file.write(json.dumps(funnel_device, sort_keys=True, indent=4))