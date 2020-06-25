def bmi(h, w):
    return w / ((h / 100) ** 2)


def calc_avg(people):
    sum = 0
    for person in people:
        sum += person[2]
    return sum / len(people)


def process(path):
    athletes = []
    normal_people = []
    with open(path, 'r+') as file:
        for line in file:
            height, weight, athlete_or_normal = line.split()
            height, weight = int(height), float(weight)
            if athlete_or_normal == "ATHLETE":
                athletes.append((height, weight, bmi(height, weight)))
            else:
                normal_people.append((height, weight, bmi(height, weight)))
    athletes_average_bmi = calc_avg(athletes)
    normal_average_bmi = calc_avg(normal_people)
    return athletes, athletes_average_bmi, normal_people, normal_average_bmi

# a,b,c,d = process("bmi2.txt")
# print(a, b)
# print(c, d)
