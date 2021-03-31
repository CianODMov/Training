class Athlete:
    def __init__(self, fly, start, m60, m100, m200, m400, vert, event, training_days):
        self.fly = fly
        self.start = start
        self.m60 = m60
        self.m100 = m100
        self.m200 = m200
        self.m400 = m400
        self.vert = vert
        self.r60100 = m100 / m60
        self.r100200 = m200 / m100
        self.r200400 = m400 / m200
        self.r100400 = m400 / m100
        self.r60start = m60 / start
        self.r100fly = m100 / fly
        self.r100start = m100 / start
        self.rflystart = fly/start
        self.event = event
        self.training_days = training_days


class Acceleration:
    pass


class TopSpeed:
    pass


class SpeedEndurance100:
    pass


class TopSpeed200:
    pass


class SpeedEndurance200:
    pass


class TopSpeed400:
    pass


class Endurance400:
    pass


def programme_choice(name):
    if name.event == 60:
        if name.r60start < 1.789:
            programme = Acceleration
        else:
            programme = TopSpeed
    elif name.event == 100:
        if name.r60start < 1.68 or name.r100start < 3.42:
            programme = Acceleration
        elif name.r100fly < 3.80:
            programme = TopSpeed
        else:
            programme = SpeedEndurance100
    elif name.event == 200:
        if name.r60start < 1.65 or name.r100start < 2.54:
            programme = Acceleration
        elif name.r100200 < 2.025:
            programme = TopSpeed200
        else:
            programme = SpeedEndurance200
    elif name.event == 400:
        if name.r60start < 1.6 or name.r100start < 2.48:
            programme = Acceleration
        elif name.r200400 < 2.21:
            programme = TopSpeed400
        else:
            programme = Endurance400
    else:
        programme = "N/A"
    return programme


cian = Athlete(2.89, 4.01, 7.03, 10.86, 21.91, 51.00, 65.75, 60)
charlie = Athlete(3.28, 4.35, 7.65, 12.00, 24.54, 53.65, 49.64, 200)
vlad = Athlete(3.14, 4.46, 7.87, 12.72, 25.17, 53.00, 51.61, 200)
# inigo = Athlete(3.14, )
# jess = Athlete(3.69, )
# ben = Athlete(3.14, )
# carlos = Athlete(3.92, )


# print(cian.r60start)
# print(programme_choice(cian))


class Programme:
    def rnd5(self, x, base=5):
        return base * round(x/base)

    def lactate(self):
        if self.num_of_gym_days >= 3:
            Week = {
                "Monday": {"Deadlift": [self.rnd5(self.deadlift * 0.6), "3x10"],
                           "Clean": [self.rnd5(self.clean * 0.6), "3x6"],
                           "Military Press": [self.rnd5(self.mil_press * 0.7), "3x10"],
                           "Leg Raises": [0.0, "3x6"],
                           "Calf Raises": [self.rnd5(self.squat * 0.3), "3x8"]},
                "Wednesday": {"Squat": [self.rnd5(self.squat * 0.6), "3x8"],
                              "Power Squat": [self.rnd5(self.squat * 0.5), "2x4"],
                              "Bench Press": [self.rnd5(self.bench * 0.7), "3x8"],
                              "Knee Pull": ["Band", "3x6"],
                              "Ankle Push": [0.0, "4x2x10s"]},
                "Friday": {"Lunge": [self.rnd5(self.squat * 0.4), "3x12"],
                           "Power Lunge": [self.rnd5(self.squat * 0.3), "3x6"],
                           "Bent Over Row": [self.rnd5(self.bent_row * 0.65), "3x12"],
                           "Aleknas": [5.0, "3x12"],
                           "Knee Push": [0.0, "3x3x10s"]}
            }
            return Week
        elif self.num_of_gym_days <= 2:
            Week = {
                "Wednesday": {"Squat": [self.rnd5(self.squat * 0.6), "3x8"],
                              "Clean": [self.rnd5(self.clean * 0.6), "3x6"],
                              "Bench Press": [self.rnd5(self.bench * 0.7), "3x8"],
                              "Knee Pull": ["Band", "3x6"],
                              "Ankle Push": [0.0, "4x2x10s"]},
                "Friday": {"Deadlift": [self.rnd5(self.deadlift * 0.6), "3x10"],
                           "Power Lunge": [self.rnd5(self.squat * 0.4), "4x4"],
                           "Bent Over Row": [self.rnd5(self.bent_row * 0.65), "3x12"],
                           "Aleknas": [5.0, "3x12"],
                           "Knee Push": [0.0, "3x3x10s"]}
            }
            return Week

    def lactic(self):
        if self.num_of_gym_days >= 3:
            Week = {
                "Monday": {"Deadlift": [self.rnd5(self.deadlift * 0.85), "4x3"],
                           "Clean": [self.rnd5(self.clean * 0.85), "4x3"],
                           "Military Press": [self.rnd5(self.mil_press * 0.85), "4x3"],
                           "Leg Raises": [0.0, "3x6"],
                           "Calf Raises": [self.rnd5(self.squat * 0.3), "3x5"]},
                "Wednesday": {"Squat": [self.rnd5(self.squat * 0.9), "5x2"],
                              "Power Squat": [self.rnd5(self.squat * 0.6), "3x2"],
                              "Bench Press": [self.rnd5(self.bench * 0.9), "5x2"],
                              "Knee Pull": ["Band", "3x6"],
                              "Ankle Push": [0.0, "4x2x10s"]},
                "Friday": {"Lunge": [self.rnd5(self.squat * 0.6), "3x4"],
                           "Power Lunge": [self.rnd5(self.squat * 0.4), "2x4"],
                           "Bent Over Row": [self.rnd5(self.bent_row * 0.8), "3x4"],
                           "Aleknas": [5.0, "3x12"],
                           "Knee Push": [0.0, "3x3x10s"]}
            }
            return Week
        elif self.num_of_gym_days <= 2:
            Week = {
                "Wednesday": {"Squat": [self.rnd5(self.squat * 0.9), "5x2"],
                              "Clean": [self.rnd5(self.clean * 0.85), "4x3"],
                              "Bench Press": [self.rnd5(self.bench * 0.9), "5x2"],
                              "Knee Pull": ["Band", "3x6"],
                              "Ankle Push": [0.0, "4x2x10s"]},
                "Friday": {"Deadlift": [self.rnd5(self.deadlift * 0.8), "3x4"],
                           "Power Lunge": [self.rnd5(self.squat * 0.4), "3x4"],
                           "Bent Over Row": [self.rnd5(self.bent_row * 0.8), "3x4"],
                           "Aleknas": [15.0, "3x12"],
                           "Knee Push": [0.0, "3x3x10s"]}
            }
            return Week

    def eccentric(self):
        if self.num_of_gym_days >= 3:
            Week = {
                "Monday": {"Deadlift": [self.rnd5(self.deadlift * 0.85), "3x3x8s"],
                           "Clean": [self.rnd5(self.clean * 0.80), "4x4"],
                           "Military Press": [self.rnd5(self.mil_press * 0.85), "3x3x8s"],
                           "Leg Raises": [0.0, "3x6"],
                           "Calf Raises": [self.rnd5(self.squat * 0.3), "3x3x8s"]},
                "Wednesday": {"Half Squat": [self.rnd5(self.squat * 0.9), "4x2x10s"],
                              "Power Squat": [self.rnd5(self.squat * 0.7), "4x4"],
                              "Bench Press": [self.rnd5(self.bench * 0.9), "4x2x10s"],
                              "Knee Pull": ["Band", "3x6"],
                              "Ankle Push": [0.0, "4x2x10s"]},
                "Friday": {"Lunge": [self.rnd5(self.squat * 0.6), "3x3x10s"],
                           "Power Lunge": [self.rnd5(self.squat * 0.4), "4x4"],
                           "Bent Over Row": [self.rnd5(self.bent_row * 0.8), "3x3x10s"],
                           "Aleknas": [10.0, "3x3x10s"],
                           "Knee Push": [0.0, "3x3x10s"],
                           "Nordic Curls": [0.0, "3x3x10s"]}
            }
            return Week
        elif self.num_of_gym_days <= 2:
            Week = {
                "Wednesday": {"Half Squat": [self.rnd5(self.squat * 0.9), "4x2x10s"],
                              "Clean": [self.rnd5(self.clean * 0.80), "4x4"],
                              "Bench Press": [self.rnd5(self.bench * 0.9), "4x2x10s"],
                              "Knee Pull": ["Band", "3x6"],
                              "Ankle Push": [0.0, "4x2x10s"]},
                "Friday": {"Deadlift": [self.rnd5(self.deadlift * 0.85), "3x3x8s"],
                           "Power Lunge": [self.rnd5(self.squat * 0.4), "4x4"],
                           "Bent Over Row": [self.rnd5(self.bent_row * 0.8), "3x3x10s"],
                           "Aleknas": [10.0, "3x3x10s"],
                           "Knee Push": [0.0, "3x3x10s"],
                           "Nordic Curls": [0.0, "3x3x10s"]}
            }
            return Week

    def isometric(self):
        if self.num_of_gym_days >= 3:
            Week = {
                "Monday": {"Deadlift": [self.rnd5(self.deadlift * 0.85), "3x3x8s"],
                           "Clean": [self.rnd5(self.clean * 0.80), "4x4"],
                           "Military Press": [self.rnd5(self.mil_press * 0.85), "3x3x8s"],
                           "Leg Raises": [0.0, "3x6"],
                           "Calf Raises": [self.rnd5(self.squat * 0.3), "3x3x8s"]},
                "Wednesday": {"Half Squat": [self.rnd5(self.squat * 0.9), "4x2x10s"],
                              "Power Squat": [self.rnd5(self.squat * 0.7), "4x4"],
                              "Bench Press": [self.rnd5(self.bench * 0.9), "4x2x10s"],
                              "Knee Pull": ["Band", "3x6"],
                              "Ankle Push": [0.0, "4x2x10s"]},
                "Friday": {"Lunge": [self.rnd5(self.squat * 0.6), "3x3x10s"],
                           "Power Lunge": [self.rnd5(self.squat * 0.4), "4x4"],
                           "Bent Over Row": [self.rnd5(self.bent_row * 0.8), "3x3x10s"],
                           "Aleknas": [10.0, "3x3x10s"],
                           "Knee Push": [0.0, "3x3x10s"],
                           "Nordic Curls": [0.0, "3x3x10s"]}
            }
            return Week
        elif self.num_of_gym_days <= 2:
            Week = {
                "Wednesday": {"Half Squat": [self.rnd5(self.squat * 0.9), "4x2x10s"],
                              "Clean": [self.rnd5(self.clean * 0.80), "4x4"],
                              "Bench Press": [self.rnd5(self.bench * 0.9), "4x2x10s"],
                              "Knee Pull": ["Band", "3x6"],
                              "Ankle Push": [0.0, "4x2x10s"]},
                "Friday": {"Deadlift": [self.rnd5(self.deadlift * 0.85), "3x3x8s"],
                           "Power Lunge": [self.rnd5(self.squat * 0.4), "4x4"],
                           "Bent Over Row": [self.rnd5(self.bent_row * 0.8), "3x3x10s"],
                           "Aleknas": [10.0, "3x3x10s"],
                           "Knee Push": [0.0, "3x3x10s"],
                           "Nordic Curls": [0.0, "3x3x10s"]}
            }
            return Week

    def concentric(self):
        if self.num_of_gym_days >= 3:
            Week = {
                "Monday": {"Deadlift": [self.rnd5(self.deadlift * 0.85), "4x3"],
                           "Clean": [self.rnd5(self.clean * 0.85), "4x3"],
                           "Military Press": [self.rnd5(self.mil_press * 0.85), "4x3"],
                           "Leg Raises": [0.0, "3x6"],
                           "Calf Raises": [self.rnd5(self.squat * 0.3), "3x5"]},
                "Wednesday": {"Squat": [self.rnd5(self.squat * 0.9), "5x2"],
                              "Power Squat": [self.rnd5(self.squat * 0.6), "3x2"],
                              "Bench Press": [self.rnd5(self.bench * 0.9), "5x2"],
                              "Knee Pull": ["Band", "3x6"],
                              "Ankle Push": [0.0, "4x2x10s"]},
                "Friday": {"Lunge": [self.rnd5(self.squat * 0.6), "3x4"],
                           "Power Lunge": [self.rnd5(self.squat * 0.4), "2x4"],
                           "Bent Over Row": [self.rnd5(self.bent_row * 0.8), "3x4"],
                           "Aleknas": [15.0, "3x12"],
                           "Knee Push": [0.0, "3x3x10s"]}
            }
            return Week
        elif self.num_of_gym_days <= 2:
            Week = {
                "Wednesday": {"Squat": [self.rnd5(self.squat * 0.9), "5x2"],
                              "Clean": [self.rnd5(self.clean * 0.85), "4x3"],
                              "Bench Press": [self.rnd5(self.bench * 0.9), "5x2"],
                              "Knee Pull": ["Band", "3x6"],
                              "Ankle Push": [0.0, "4x2x10s"]},
                "Friday": {"Deadlift": [self.rnd5(self.deadlift * 0.8), "3x4"],
                           "Power Lunge": [self.rnd5(self.squat * 0.4), "3x4"],
                           "Bent Over Row": [self.rnd5(self.bent_row * 0.8), "3x4"],
                           "Aleknas": [15.0, "3x12"],
                           "Knee Push": [0.0, "3x3x10s"]}
            }
            return Week

    def power(self):
        if self.num_of_gym_days >= 3:
            Week = {
                "Monday": {"Deadlift": [self.rnd5(self.deadlift * 0.7), "4x4"],
                           "Clean": [self.rnd5(self.clean * 0.8), "4x4"],
                           "Military Press": [self.rnd5(self.mil_press * 0.7), "4x4"],
                           "Leg Raises": [0.0, "3x6"],
                           "Calf Raises": [self.rnd5(self.squat * 0.3), "3x5"]},
                "Wednesday": {"Squat": [self.rnd5(self.squat * 0.75), "5x3"],
                              "Power Squat": [self.rnd5(self.squat * 0.4), "3x3"],
                              "Bench Press": [self.rnd5(self.bench * 0.75), "5x3"],
                              "Knee Pull": ["Band", "3x6"],
                              "Ankle Push": [0.0, "4x2x10s"]},
                "Friday": {"Lunge": [self.rnd5(self.squat * 0.5), "3x5"],
                           "Power Lunge": [self.rnd5(self.squat * 0.3), "2x5"],
                           "Bent Over Row": [self.rnd5(self.bent_row * 0.8), "3x5"],
                           "Aleknas": [15.0, "3x5"],
                           "Knee Push": [0.0, "3x3x10s"]}
            }
            return Week
        elif self.num_of_gym_days <= 2:
            Week = {
                "Wednesday": {"Squat": [self.rnd5(self.squat * 0.75), "5x3"],
                              "Clean": [self.rnd5(self.clean * 0.8), "4x4"],
                              "Bench Press": [self.rnd5(self.bench * 0.75), "5x3"],
                              "Knee Pull": ["Band", "3x6"],
                              "Ankle Push": [0.0, "4x2x10s"]},
                "Friday": {"Deadlift": [self.rnd5(self.deadlift * 0.5), "4x4"],
                           "Power Lunge": [self.rnd5(self.squat * 0.3), "3x4"],
                           "Bent Over Row": [self.rnd5(self.bent_row * 0.8), "3x4"],
                           "Aleknas": [15.0, "3x12"],
                           "Knee Push": [0.0, "3x3x10s"]}
            }
            return Week

    def peaking(self):
        if self.num_of_gym_days >= 3:
            Week = {
                "Monday": {"Deadlift": [self.rnd5(self.deadlift * 0.5), "4x5"],
                           "Snatch": [self.rnd5(self.clean * 0.4), "4x5"],
                           "Military Press": [self.rnd5(self.mil_press * 0.5), "4x5"],
                           "Leg Raises": [0.0, "3x6"]},
                "Wednesday": {"Squat": [self.rnd5(self.squat * 0.55), "5x4"],
                              "Bench Press": [self.rnd5(self.bench * 0.55), "5x4"],
                              "Knee Pull": ["Band", "3x6"],
                              "Ankle Push": [0.0, "4x2x10s"]},
                "Friday": {"Lunge": [self.rnd5(self.squat * 0.6 * 0.45), "3x6"],
                           "Bent Over Row": [self.rnd5(self.bent_row * 0.45), "3x6"],
                           "Aleknas": [15.0, "3x6"],
                           "Knee Push": [0.0, "3x3x10s"]}
            }
            return Week
        elif self.num_of_gym_days <= 2:
            Week = {
                "Wednesday": {"Squat": [self.rnd5(self.squat * 0.55), "5x4"],
                              "Snatch": [self.rnd5(self.clean * 0.4), "4x5"],
                              "Bench Press": [self.rnd5(self.bench * 0.55), "5x4"],
                              "Knee Pull": ["Band", "3x6"],
                              "Ankle Push": [0.0, "4x2x10s"]},
                "Friday": {"Deadlift": [self.rnd5(self.deadlift * 0.5), "4x4"],
                           "Power Lunge": [self.rnd5(self.squat * 0.3), "3x4"],
                           "Bent Over Row": [self.rnd5(self.bent_row * 0.8), "3x4"],
                           "Aleknas": [15.0, "3x12"],
                           "Knee Push": [0.0, "3x3x10s"]}
            }
            return Week

    def taper(self):
        if self.num_of_gym_days >= 3:
            Week = {
                "Monday": {"Deadlift": [self.rnd5(self.deadlift * 0.5), "4x5"],
                           "Snatch": [self.rnd5(self.clean * 0.4), "4x5"],
                           "Military Press": [self.rnd5(self.mil_press * 0.5), "4x5"],
                           "Leg Raises": [0.0, "3x6"]},
                "Wednesday": {"Squat": [self.rnd5(self.squat * 0.55), "5x4"],
                              "Bench Press": [self.rnd5(self.bench * 0.55), "5x4"],
                              "Knee Pull": ["Band", "3x6"],
                              "Ankle Push": [0.0, "4x2x10s"]}
            }
            return Week
        elif self.num_of_gym_days <= 2:
            Week = {
                "Wednesday": {"Squat": [self.rnd5(self.squat * 0.55), "5x4"],
                              "Snatch": [self.rnd5(self.clean * 0.4), "4x5"],
                              "Bench Press": [self.rnd5(self.bench * 0.55), "5x4"],
                              "Knee Pull": ["Band", "3x6"],
                              "Ankle Push": [0.0, "4x2x10s"]}
            }
            return Week

    def aerobic(self):
        if self.num_of_gym_days >= 3:
            Week = {
                "Monday": {"Deadlift": [self.rnd5(self.deadlift * 0.5), "3x20"],
                           "Clean": [self.rnd5(self.clean * 0.4), "3x12"],
                           "Military Press": [self.rnd5(self.mil_press * 0.5), "3x20"],
                           "Knee Raises": [0.0, "3x15"]},
                "Wednesday": {"Squat": [self.rnd5(self.squat * 0.55), "5x4"],
                              "Bench Press": [self.rnd5(self.bench * 0.55), "5x4"],
                              "Knee Pull": ["Band", "3x6"],
                              "Ankle Push": [0.0, "4x2x30s"]},
                "Friday": {"Lunge": [self.rnd5(self.squat * 0.6 * 0.45), "3x20"],
                           "Bent Over Row": [self.rnd5(self.bent_row * 0.45), "3x20"],
                           "Aleknas": [15.0, "3x6"],
                           "Knee Push": [0.0, "3x3x10s"]}
            }
            return Week
        elif self.num_of_gym_days <= 2:
            Week = {
                "Wednesday": {"Squat": [self.rnd5(self.squat * 0.55), "5x4"],
                              "Snatch": [self.rnd5(self.clean * 0.4), "4x5"],
                              "Bench Press": [self.rnd5(self.bench * 0.55), "5x4"],
                              "Knee Pull": ["Band", "3x6"],
                              "Ankle Push": [0.0, "4x2x10s"]},
                "Friday": {"Deadlift": [self.rnd5(self.deadlift * 0.5), "4x4"],
                           "Power Lunge": [self.rnd5(self.squat * 0.3), "3x4"],
                           "Bent Over Row": [self.rnd5(self.bent_row * 0.8), "3x4"],
                           "Aleknas": [15.0, "3x12"],
                           "Knee Push": [0.0, "3x3x10s"]}
            }
            return Week


# cian = Athlete(200, 200, 100, 110, 90, 60, 3)
# inigo = Athlete(170, 170, 95, 70, 100, 60, 3)
# vlad = Athlete(150, 150, 90, 70, 80, 50, 3)
# jess = Athlete(100, 110, 40, 40, 30, 30, 3)
# charlie = Athlete(135, 130, 85, 70, 85, 45, 2)
# ben = Athlete(150, 150, 100, 100, 50, 50, 2)


# cian_dft = pd.DataFrame(cian.eccentric())
# print("Cian Eccentric:")
# print(cian_dft)

# inigo_dft = pd.DataFrame(inigo.eccentric())
# print(" ")
# print("Inigo Eccentric:")
# print(inigo_dft)

# vlad_dft = pd.DataFrame(vlad.eccentric())
# print(" ")
# print("Vlad Eccentric:")
# print(vlad_dft)

# jess_dft = pd.DataFrame(jess.eccentric())
# print(" ")
# print("Jess Eccentric:")
# print(jess_dft)

# charlie_dft = pd.DataFrame(charlie.eccentric())
# print(" ")
# print("Charlie Eccentric:")
# print(charlie_dft)

# ben_dft = pd.DataFrame(ben.lactate())
# print(" ")
# print("Ben Lactate:")
# print(ben_dft)
