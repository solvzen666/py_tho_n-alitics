import csv

funnel_by_device = {}
funnel_template = {'1_home_page': 0, '2_search_page': 0, '3_payment_page': 0, '4_payment_confirmation_page': 0}
with open(r'click_stream3.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, fieldnames=['ID', 'page', 'date', 'device', 'gender'])

    for row in csv_reader:

        page = list(row.items())[1][1]
        event_date = list(row.items())[2][1][:-3]
        device = list(row.items())[3][1]
        gender = list(row.items())[4][1]
        if device not in funnel_by_device:  # если нет
            funnel_by_device[device] = funnel_template.copy()
            if gender not in funnel_by_device[device]:
                funnel_by_device[gender] = funnel_by_device
                if event_date not in funnel_by_device[device]:
                    funnel_by_device[event_date] = funnel_by_device

        if page == '1_home_page':
            funnel_by_device[device]['1_home_page'] += 1
        elif page == '2_search_page':
            funnel_by_device[device]['2_search_page'] += 1
        elif page == '3_payment_page':
            funnel_by_device[device]['3_payment_page'] += 1
        elif page == '4_payment_confirmation_page':
            funnel_by_device[device]['4_payment_confirmation_page'] += 1

print(funnel_by_device)