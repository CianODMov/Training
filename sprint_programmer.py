import datetime
import math
import pandas as pd
from pprint import pprint


class Athlete:
    def __init__(self, fly, start, m60, m100, m200, m400, s15, vert, event, name, num_of_training_days):
        self.fly = fly
        self.start = start
        self.m60 = m60
        self.m100 = m100
        self.m200 = m200
        self.m400 = m400
        self.s15 = s15
        self.vert = vert
        self.t_fly = (start * 0.92) - 0.78
        self.t_100m = ((fly/3)*7) + start + 0.15
        self.expected_100m = m60 * 1.8151 - 1.965
        self.t_s15 = (15-start)*(30/fly)+30
        self.r60100 = m100 / m60
        self.r100200 = m200 / m100
        self.r200400 = m400 / m200
        self.r100400 = m400 / m100
        self.r60start = m60 / start
        self.r100fly = m100 / fly
        self.r100start = m100 / start
        self.rflystart = fly/start
        self.event = event
        self.name = name
        self.focus = self.focus_choice()
        self.training_days = num_of_training_days
        self.rm_distance = 300 if event == 400 else 150 if event == 200 else 80 if event == 100 else 50
        self.rm_reps = 2 if event == 400 else 3 if event == 200 else 4 if event == 100 else 6
        self.rm_rest = 40 if event == 400 else 18 if event == 200 else 10 if event == 100 else 6
        self.competition = self.event

        # Sessions
        self.lactic_150 = ["150m", "5 Reps", "4 min recovery",
                           "Target: " + str(round((m100 * 1.5) / 0.9, 2))]
        self.lactic_250 = ["250m", "4 Reps", "8 min recovery",
                           "Target: " + str(round((m100 * 2.5) / 0.9, 2))]
        self.lactic_rm = [str(self.rm_distance) +
                          'm', str(self.rm_reps * 2) +
                          " Reps", str(int(self.rm_rest/3)) + " min recovery",
                          "Target: " + str(round(0.8*m400, 2))]
        self.aerobic_200 = ["200m", "8 Reps", "2 min recovery",
                            "Target: " + str(round(m200/0.75, 2))]
        self.sleds_light = ["Light Sleds - 50m", "6 Reps", "6-8 min recovery",
                            "5-10kg", "Target: 7.0s"]
        self.sleds_heavy = ["Heavy Sleds - 30m", "6 Reps", "6-8 min recovery",
                            "30-60kg", "Target: 7.0s"]
        self.speed_fly4 = ["30m Flys", "4 Reps", "8 min recovery"]
        self.speed_fly6 = ["30m Flys", "6 Reps", "8 min recovery"]
        self.speed_fly8 = ["30m Flys", "6 Reps", "8 min recovery"]
        self.speed_15s3 = ["15s", "3 Reps", "18 min recovery"]
        self.speed_15s4 = ["15s", "4 Reps", "16 min recovery"]
        self.speed_15s5 = ["15s", "5 Reps", "16 min recovery"]
        self.speed_15s6 = ["15s", "6 Reps", "16 min recovery"]
        self.race_model = [str(self.rm_distance) +
                           'm', str(self.rm_reps) + " Reps", str(self.rm_rest) + " min recovery"]
        self.taper = ["40m", "3 Reps", "8 min recovery"]
        self.yoga = ["30 mins of Yoga"]
        self.competition = [str(event) + 'm', '2 reps', "40-60 min recovery"]

    def focus_choice(self):
        if self.event == 60:
            if self.fly / self.t_fly <= 0.99:
                programme = 'Acceleration'
            else:
                programme = 'TopSpeed'
        elif self.event == 100:
            if self.fly / self.t_fly <= 0.97:
                programme = 'Acceleration'
            elif self.t_s15 / self.s15 >= 1.05:
                programme = 'SpeedEndurance100'
            else:
                programme = 'TopSpeed'
        elif self.event == 200:
            if self.fly / self.t_fly <= 0.95:
                programme = 'Acceleration'
            elif self.t_s15 / self.s15 <= 1.03:
                programme = 'TopSpeed200'
            else:
                programme = 'SpeedEndurance200'
        elif self.event == 400:
            if self.fly / self.t_fly <= 0.9:
                programme = 'Acceleration'
            elif self.r200400 < 2.21 or self.t_s15 / self.s15 <= 1.03:
                programme = 'TopSpeed400'
            else:
                programme = 'SpeedEndurance400'
        else:
            programme = "N/A"
        return programme

    def intro_programmer(remaining_weeks):
        programme = ['Intro', 'Intro', 'Intro', 'Intro']
        return programme

    def acc_programmer(remaining_weeks):
        programme = ['Intro', 'Intro', 'Aerobic', 'Aerobic',
                     'Speed', 'Sleds', 'Sleds', 'Aerobic',
                     'Speed', 'Sleds', 'Sleds', 'Aerobic',
                     'Speed', 'Sleds', 'Sleds', 'Aerobic',
                     'Speed', 'Sleds', 'Race Model', 'Race Model 2',
                     'Taper']
        if remaining_weeks > 21:
            x = remaining_weeks - 21
            new_programme = programme[-x:]
            final_programme = programme + new_programme
            return final_programme
        else:
            return programme[-remaining_weeks:]

    def top_programmer(remaining_weeks):
        programme = ['Intro', 'Intro', 'Aerobic', 'Aerobic',
                     'Speed', 'Speed', 'Race Model', 'Aerobic',
                     'Speed', 'Speed', 'Race Model', 'Aerobic',
                     'Speed', 'Speed', 'Race Model', 'Aerobic',
                     'Speed', 'Speed', 'Race Model', 'Race Model 2',
                     'Taper']
        if remaining_weeks > 21:
            x = remaining_weeks - 21
            new_programme = programme[-x:]
            final_programme = programme + new_programme
            return final_programme
        else:
            return programme[-remaining_weeks:]

    def e100_programmer(remaining_weeks):
        programme = ['Intro', 'Intro', 'Aerobic', 'Aerobic',
                     'Speed', 'Endurance', 'Race Model', 'Aerobic',
                     'Speed', 'Endurance', 'Race Model', 'Aerobic',
                     'Speed', 'Endurance', 'Race Model', 'Aerobic',
                     'Endurance', 'Endurance', 'Race Model', 'Race Model 2',
                     'Taper']
        if remaining_weeks > 21:
            x = remaining_weeks - 21
            new_programme = programme[-x:]
            final_programme = programme + new_programme
            return final_programme
        else:
            return programme[-remaining_weeks:]

    def t200_programmer(remaining_weeks):
        programme = ['Intro', 'Intro', 'Aerobic', 'Aerobic',
                     'Speed', 'Endurance', 'Race Model', 'Aerobic',
                     'Speed', 'Endurance', 'Race Model', 'Aerobic',
                     'Speed', 'Endurance', 'Race Model', 'Aerobic',
                     'Speed', 'Speed', 'Race Model', 'Race Model 2',
                     'Taper']
        if remaining_weeks > 21:
            x = remaining_weeks - 21
            new_programme = programme[-x:]
            final_programme = programme + new_programme
            return final_programme
        else:
            return programme[-remaining_weeks:]

    def e200_programmer(remaining_weeks):
        programme = ['Intro', 'Intro', 'Aerobic', 'Aerobic',
                     'Speed', 'Endurance', 'Lactic', 'Aerobic',
                     'Speed', 'Endurance', 'Lactic', 'Aerobic',
                     'Speed', 'Endurance', 'Lactic', 'Aerobic',
                     'Endurance', 'Lactic', 'Race Model', 'Race Model 2',
                     'Taper']
        if remaining_weeks > 21:
            x = remaining_weeks - 21
            new_programme = programme[-x:]
            final_programme = programme + new_programme
            return final_programme
        else:
            return programme[-remaining_weeks:]

    def t400_programmer(remaining_weeks):
        programme = ['Intro', 'Intro', 'Aerobic', 'Aerobic',
                     'Speed', 'Lactic', 'Lactic', 'Aerobic',
                     'Speed', 'Lactic', 'Lactic', 'Aerobic',
                     'Speed', 'Lactic', 'Lactic', 'Aerobic',
                     'Endurance', 'Lactic', 'Race Model', 'Race Model 2',
                     'Taper']
        if remaining_weeks > 21:
            x = remaining_weeks - 21
            new_programme = programme[-x:]
            final_programme = programme + new_programme
            return final_programme
        else:
            return programme[-remaining_weeks:]

    def e400_programmer(remaining_weeks):
        programme = ['Intro', 'Intro', 'Aerobic', 'Aerobic',
                     'Endurance', 'Lactic', 'Lactic2', 'Aerobic',
                     'Speed', 'Lactic', 'Lactic2', 'Aerobic',
                     'Speed', 'Lactic', 'Lactic2', 'Aerobic',
                     'Endurance', 'Lactic2', 'Race Model', 'Race Model 2',
                     'Taper']
        if remaining_weeks > 21:
            x = remaining_weeks - 21
            new_programme = programme[-x:]
            final_programme = programme + new_programme
            return final_programme
        else:
            return programme[-remaining_weeks:]

    def intro(self):
        if self.training_days >= 3:
            Week = {
                "Tuesday": self.lactic_150,
                "Thursday": self.lactic_250,
                "Saturday": self.aerobic_200,
                "Sunday": self.sleds_light
            }
            return Week
        elif self.training_days <= 2:
            Week = {
                "Tuesday": self.lactic_150,
                "Thursday": self.lactic_250,
                "Sunday": self.sleds_light
            }
            return Week

    def aerobic(self):
        Week = {
            "Tuesday": self.speed_fly8,
            "Thursday": self.speed_15s3,
            "Saturday": self.yoga,
            "Sunday": self.aerobic_200,
        }
        return Week

    def lactic(self):
        if self.training_days >= 3:
            Week = {
                "Tuesday": self.speed_fly6,
                "Thursday": self.speed_15s5,
                "Saturday": self.race_model,
                "Sunday": self.lactic_rm,
            }
            return Week
        elif self.training_days <= 2:
            Week = {
                "Tuesday": self.speed_fly6,
                "Thursday": self.speed_15s5,
                "Sunday": self.lactic_rm,
            }
            return Week

    def lactic2(self):
        if self.training_days >= 3:
            Week = {
                "Tuesday": self.speed_fly6,
                "Thursday": self.lactic_250,
                "Saturday": self.race_model,
                "Sunday": self.lactic_rm,
            }
            return Week
        elif self.training_days <= 2:
            Week = {
                "Tuesday": self.speed_fly6,
                "Thursday": self.lactic_250,
                "Sunday": self.lactic_rm,
            }
            return Week

    def sleds(self):
        if self.training_days >= 3:
            Week = {
                "Tuesday": self.speed_fly6,
                "Thursday": self.sleds_light,
                "Saturday": self.speed_fly4,
                "Sunday": self.sleds_heavy,
            }
            return Week
        elif self.training_days <= 2:
            Week = {
                "Tuesday": self.speed_fly6,
                "Thursday": self.sleds_light,
                "Sunday": self.sleds_heavy,
            }
            return Week

    def speed(self):
        if self.training_days >= 3:
            Week = {
                "Tuesday": self.speed_fly6,
                "Thursday": self.speed_15s5,
                "Saturday": self.race_model,
                "Sunday": self.sleds_light,
            }
            return Week
        elif self.training_days <= 2:
            Week = {
                "Tuesday": self.speed_fly6,
                "Thursday": self.speed_15s5,
                "Sunday": self.sleds_light,
            }
            return Week

    def endurance(self):
        if self.training_days >= 3:
            Week = {
                "Tuesday": self.speed_fly6,
                "Thursday": self.speed_15s5,
                "Saturday": self.speed_15s5,
                "Sunday": self.sleds_heavy,
            }
            return Week
        elif self.training_days <= 2:
            Week = {
                "Tuesday": self.speed_fly6,
                "Thursday": self.speed_15s5,
                "Sunday": self.sleds_heavy,
            }
            return Week

    def race_modelling1(self):
        if self.training_days >= 3:
            Week = {
                "Tuesday": self.race_model,
                "Thursday": self.speed_15s3,
                "Saturday": self.speed_fly4,
                "Sunday": self.race_model,
            }
            return Week
        elif self.training_days <= 2:
            Week = {
                "Tuesday": self.speed_fly4,
                "Thursday": self.speed_15s3,
                "Sunday": self.race_model,
            }
            return Week

    def race_modelling2(self):
        if self.training_days >= 3:
            Week = {
                "Tuesday": self.speed_fly4,
                "Thursday": self.race_model,
                "Saturday": self.speed_fly4,
                "Sunday": self.taper,
            }
            return Week
        elif self.training_days <= 2:
            Week = {
                "Tuesday": self.speed_fly4,
                "Thursday": self.race_model,
                "Sunday": self.taper,
            }
            return Week

    def taper_week(self):
        Week = {
            "Tuesday": self.speed_fly4,
            "Thursday": self.taper,
            "Saturday": self.competition,
            "Sunday": self.competition,
        }
        return Week


def sprint_calculator(name, start_date_entry, *arg):
    start_year, start_month, start_day = map(int, start_date_entry.split('-'))
    start_date = datetime.date(start_year, start_month, start_day)
    start = start_date - datetime.timedelta(days=start_date.weekday())
    race_date = start_date  # assigned correctly below in for loop
    programme = []
    prog = 'None'
    weeks = []
    for extra_race1 in arg:
        start_date = race_date
        race_year, race_month, race_day = map(int, extra_race1.split('-'))
        race_date = datetime.date(race_year, race_month, race_day)
        num_of_weeks = math.ceil((race_date - start_date).days / 7.0)
        # if intro == "y":
        #     for focus in Athlete.intro_programmer(range(4)):
        #         programme.append(focus)
        #     num_of_weeks -= 4
        if Athlete.focus_choice(name) == 'Acceleration':
            for focus in Athlete.acc_programmer(num_of_weeks):
                programme.append(focus)
                weeks = list(range(1, len(programme)+1))
        elif Athlete.focus_choice(name) == 'TopSpeed':
            for focus in Athlete.top_programmer(num_of_weeks):
                programme.append(focus)
                weeks = list(range(1, len(programme)+1))
        elif Athlete.focus_choice(name) == 'SpeedEndurance100':
            for focus in Athlete.e100_programmer(num_of_weeks):
                programme.append(focus)
                weeks = list(range(1, len(programme)+1))
        elif Athlete.focus_choice(name) == 'TopSpeed200':
            for focus in Athlete.t200_programmer(num_of_weeks):
                programme.append(focus)
                weeks = list(range(1, len(programme)+1))
        elif Athlete.focus_choice(name) == 'SpeedEndurance200':
            for focus in Athlete.e200_programmer(num_of_weeks):
                programme.append(focus)
                weeks = list(range(1, len(programme)+1))
        elif Athlete.focus_choice(name) == 'TopSpeed400':
            for focus in Athlete.t400_programmer(num_of_weeks):
                programme.append(focus)
                weeks = list(range(1, len(programme)+1))
        elif Athlete.focus_choice(name) == 'SpeedEndurance400':
            for focus in Athlete.e400_programmer(num_of_weeks):
                programme.append(focus)
                weeks = list(range(1, len(programme)+1))

        else:
            return "None"
    week = [start]
    for i in range(len(weeks)-1):
        week.append(start + datetime.timedelta(days=7))
        start = week[-1]
    return programme, week


def sprint_week_builder(programme, name):
    final_programme = []
    for week in programme[0]:
        if week == 'Intro':

            final_programme.append(name.intro())
        elif week == 'Aerobic':
            final_programme.append(name.aerobic())
        elif week == 'Lactic':
            final_programme.append(name.lactic())
        elif week == 'Lactic2':
            final_programme.append(name.lactic2())
        elif week == 'Sleds':
            final_programme.append(name.sleds())
        elif week == 'Speed':
            final_programme.append(name.speed())
        elif week == 'Endurance':
            final_programme.append(name.endurance())
        elif week == 'Race Model':
            final_programme.append(name.race_modelling1())
        elif week == 'Race Model 2':
            final_programme.append(name.race_modelling2())
        elif week == 'Taper':
            final_programme.append(name.taper_week())
    return final_programme
