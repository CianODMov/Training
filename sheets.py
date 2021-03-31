import gspread
from numpy.core.numeric import full
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from sprint_programmer import *
from gym_programmer import *
import time
import datetime

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

json = "C:\\Users\\HP\Desktop\\Python Projects\\Training\\creds.json"

creds = ServiceAccountCredentials.from_json_keyfile_name(json, scope)

client = gspread.authorize(creds)


def gym_programme_builder(name, programme):
    full_programme = gym_week_builder(programme, name)
    x = 0
    for i in full_programme:
        i['Date'] = programme[1][x]
        i['Gym'] = programme[0][x]
        i['extra1'] = 'extra1'
        i['extra2'] = 'extra2'
        x += 1
        # print(i)
    # dft = pd.DataFrame(full_programme)
    return full_programme


def track_programme_builder(name, programme):
    full_programme = sprint_week_builder(programme, name)
    # print(full_programme)
    x = 0
    for i in full_programme:
        i['Track'] = programme[0][x]
        i['extra1'] = 'extra1'
        i['extra2'] = 'extra2'
        x += 1
    # dft = pd.DataFrame(full_programme)
    return full_programme


def gym_track_merger(gym, track):
    merged = []
    for i, j in zip(gym, track):
        # print(len(i))
        # print('_________________')
        # print(len(j))
        # print('_________________')
        temp_merged = {}
        for (k, v), (k2, v2) in zip(i.items(), j.items()):
            # print(k, v)
            temp_merged[k] = v
            temp_merged[k2] = v2
        merged.append(temp_merged)
    dft = pd.DataFrame(merged)  # .set_index('Date')
    return merged


cian = Athlete(2.95, 4.01, 7.03, 10.86, 21.91,
               51.00, 137, 65.75, 100, 'Cian', 4)
charlie = Athlete(3.28, 4.29, 7.84, 12.36, 24.54,
                  53.67, 124, 49.64, 400, 'Charlie', 4)
inigo = Athlete(3.32, 4.44, 8.02, 12.54, 26.71,
                56.00, 120, 54.98, 100, 'Inigo', 4)
vlad = Athlete(3.14, 4.46, 7.87, 12.72, 25.17,
               53.00, 125, 51.61, 200, 'Vlad', 4)
ben = Athlete(3.29, 4.34, 7.79, 12.44, 25.17, 53.00, 121, 58.45, 400, 'Ben', 4)
jess = Athlete(3.87, 4.90, 8.92, 14.88, 29.28,
               60, 107.5, 58.45, 100, 'Jess', 4)

cian_gym = Gym(200, 200, 100, 110, 90, 60, 3, "Cian")
inigo_gym = Gym(170, 170, 95, 70, 100, 60, 3, "Inigo")
vlad_gym = Gym(150, 150, 90, 70, 80, 50, 3, "Vlad")
jess_gym = Gym(100, 110, 40, 40, 30, 30, 3, "Jess")
charlie_gym = Gym(135, 130, 85, 70, 85, 45, 3, "Charlie")
ben_gym = Gym(150, 150, 100, 100, 50, 50, 2, "Ben")

cian_programme = gym_track_merger(gym_programme_builder(cian_gym, programme_calculator(
    "2021-03-15", "2021-04-18")), track_programme_builder(cian, sprint_calculator(
        cian, "2021-03-15", "2021-04-18")))

charlie_programme = gym_track_merger(gym_programme_builder(charlie_gym, programme_calculator(
    "2021-03-15", "2021-04-18")), track_programme_builder(charlie, sprint_calculator(
        charlie, "2021-03-15", "2021-04-18")))

inigo_programme = gym_track_merger(gym_programme_builder(inigo_gym, programme_calculator(
    "2021-03-15", "2021-04-18")), track_programme_builder(inigo, sprint_calculator(
        inigo, "2021-03-15", "2021-04-18")))

vlad_programme = gym_track_merger(gym_programme_builder(vlad_gym, programme_calculator(
    "2021-03-15", "2021-04-18")), track_programme_builder(vlad, sprint_calculator(
        vlad, "2021-03-15", "2021-04-18")))

jess_programme = gym_track_merger(gym_programme_builder(jess_gym, programme_calculator(
    "2021-03-15", "2021-04-18")), track_programme_builder(jess, sprint_calculator(
        jess, "2021-03-15", "2021-04-18")))

ben_programme = gym_track_merger(gym_programme_builder(ben_gym, programme_calculator(
    "2021-03-15", "2021-04-18")), track_programme_builder(ben, sprint_calculator(
        ben, "2021-03-15", "2021-04-18")))


dft = pd.DataFrame(cian_programme)
# dft.to_csv('test_programme.csv', index=False)


def sheet_week(num):
    num1 = 4 + (num-1) * 11
    return num1


def sheet_builder(name, programme):
    sheet = client.open("Sprint").worksheet(name.name)
    x = 15  # unsure how to make this date a variable
    mon_col = 4
    tue_col = 7
    wed_col = 10
    thu_col = 13
    fri_col = 16
    sat_col = 19
    sun_col = 22
    sheet.update_cell(2, 4, name.focus_choice())
    time.sleep(1)
    for row in programme:
        week_num = sheet_week(x)
        sheet.update_cell(week_num-1, 1, str(row.get('Date')))
        time.sleep(1)
        sheet.update_cell(week_num-1, 2, str(row.get('Gym')))
        time.sleep(1)
        sheet.update_cell(week_num-1, 3, str(row.get('Track')))
        time.sleep(1)
        sheet.update_cell(week_num-1, mon_col,
                          str(row.get('Date')+datetime.timedelta(days=0)))
        time.sleep(1)
        sheet.update_cell(week_num-1, tue_col,
                          str(row.get('Date')+datetime.timedelta(days=1)))
        time.sleep(1)
        sheet.update_cell(week_num-1, wed_col,
                          str(row.get('Date')+datetime.timedelta(days=2)))
        time.sleep(1)
        sheet.update_cell(week_num-1, thu_col,
                          str(row.get('Date')+datetime.timedelta(days=3)))
        time.sleep(1)
        sheet.update_cell(week_num-1, fri_col,
                          str(row.get('Date')+datetime.timedelta(days=4)))
        time.sleep(1)
        sheet.update_cell(week_num-1, sat_col,
                          str(row.get('Date')+datetime.timedelta(days=5)))
        time.sleep(1)
        sheet.update_cell(week_num-1, sun_col,
                          str(row.get('Date')+datetime.timedelta(days=6)))
        time.sleep(1)
        print(row.get('Date'))
        print(row.get('Gym'))
        print(row.get('Track'))
        for i in row.items():
            time.sleep(3)
            if i[0] == 'Monday':
                y = 0
                for item in i[1]:
                    if type(item) == list:
                        sheet.update_cell(week_num+y, mon_col, item[0])
                        time.sleep(1)
                        sheet.update_cell(week_num+y, mon_col+1, item[1])
                        time.sleep(1)
                        sheet.update_cell(week_num+y, mon_col+2, item[2])
                        time.sleep(1)
                        print(item)
                        y += 1
                    else:
                        print(item)
            elif i[0] == 'Tuesday':
                y = 0
                for item in i[1]:
                    if y <= 2:
                        sheet.update_cell(week_num, tue_col+y, item)
                    else:
                        sheet.update_cell(week_num+1, tue_col, item)
                    y += 1
                    time.sleep(1)
                    print(item)
            elif i[0] == 'Wednesday':
                y = 0
                for item in i[1]:
                    if type(item) == list:
                        sheet.update_cell(week_num+y, wed_col, item[0])
                        time.sleep(1)
                        sheet.update_cell(week_num+y, wed_col+1, item[1])
                        time.sleep(1)
                        sheet.update_cell(week_num+y, wed_col+2, item[2])
                        time.sleep(1)
                        print(item)
                        y += 1
                    else:
                        print(item)
            elif i[0] == 'Thursday':
                y = 0
                for item in i[1]:
                    if y <= 2:
                        sheet.update_cell(week_num, thu_col+y, item)
                    else:
                        sheet.update_cell(week_num+1, thu_col, item)
                    y += 1
                    time.sleep(1)
                    print(item)
            elif i[0] == 'Friday':
                y = 0
                for item in i[1]:
                    if type(item) == list:
                        sheet.update_cell(week_num+y, fri_col, item[0])
                        time.sleep(1)
                        sheet.update_cell(week_num+y, fri_col+1, item[1])
                        time.sleep(1)
                        sheet.update_cell(week_num+y, fri_col+2, item[2])
                        time.sleep(1)
                        print(item)
                        y += 1
                    else:
                        print(item)
            elif i[0] == 'Saturday':
                y = 0
                for item in i[1]:
                    if y <= 2:
                        sheet.update_cell(week_num, sat_col+y, item)
                    else:
                        sheet.update_cell(week_num+1, sat_col, item)
                    y += 1
                    time.sleep(1)
                    print(item)
            elif i[0] == 'Sunday':
                y = 0
                for item in i[1]:
                    if y <= 2:
                        sheet.update_cell(week_num, sun_col+y, item)
                    else:
                        sheet.update_cell(week_num+1, sun_col, item)
                    y += 1
                    time.sleep(1)
                    print(item)
            time.sleep(5)
        x += 1


sheet_builder(cian, cian_programme)
sheet_builder(jess, jess_programme)
sheet_builder(vlad, vlad_programme)
sheet_builder(inigo, inigo_programme)
sheet_builder(ben, ben_programme)
sheet_builder(charlie, charlie_programme)


# update_cell(row, col, value)
# sheet.update_cell(sheet_week(1), 3, 'Aerobic')


# =AVERAGE(INDIRECT(ADDRESS(ROW()-6,COLUMN())):INDIRECT(ADDRESS(ROW()-1,COLUMN())))
