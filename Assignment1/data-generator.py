import csv
import random
import decimal
import statistics
from statistics import mode, mean
import collections


def generateStudents():
    myData = ["Name", "Year", "Age", "Major", "Degree", "Living Condition", "GPA", "Passing"]
    names = ["Clayton", "Jacob", "Noah", "Hugh", "Jenna", "Liz", "Taylor", "Jeremiah", "Kim", "Daniel", "Tori", "Jeff",
             "Nick", "John", "Mary", "Ellie", "Joe", "Jared", "Gloria", "Emily"]
    years = ['Freshman', 'Sophomore', 'Junior', 'Senior']
    majors = ['Computer Science', 'Music Education', 'Graphic Design', 'Business', 'Nursing', 'Journalism', 'Spanish',
              'English', 'Math', 'Theatre', 'History Education']
    living_states = ['Dorm', 'Apartment', 'House', 'At home']
    degrees = ["BS", "BA"]
    all_names = []
    all_years = []
    all_ages = []
    all_majors = []
    all_degrees = []
    all_living_states = []
    all_gpas = []
    all_passing = []

    myFile = open('students.csv', 'w')
    with myFile:
        student_count = 1000
        writer = csv.writer(myFile)
        writer.writerow(myData)
        for i in range(student_count):
            name = random.choice(names)
            year = random.choice(years)  # ordinal
            age = random.randint(18, 65)  # numerical
            major = random.choice(majors)  # categorical
            degree = random.choice(degrees)  # boolean
            living_state = random.choice(living_states)  # categorical
            gpa = decimal.Decimal(random.randrange(155, 389)) / 100  # numerical
            if gpa < 2.0:  # boolean
                passing = "no"
            else:
                passing = "yes"
            all_names.append(name)
            all_years.append(year)  # ordinal
            all_ages.append(age)  # numerical
            all_majors.append(major)  # categorical
            all_degrees.append(degree)  # boolean
            all_living_states.append(living_state)  # categorical
            all_gpas.append(gpa)  # numerical
            all_passing.append(passing)  # boolean
            myData = [name, year, age, major, degree, living_state, gpa, passing]
            writer.writerow(myData)
        myFile.close()

    age_stats = ["Age Mean: " + str(mean(all_ages)), "Age Standard Deviation: " + str(statistics.stdev(all_ages)),
                 "Age Max: " + str(max(all_ages)), "Age Min: " + str(min(all_ages)), "Age Mode: " + str(mode(all_ages))]
    gpa_stats = ["GPA Mean: " + str(mean(all_gpas)), "GPA Standard Deviation: " + str(statistics.stdev(all_gpas)),
                 "GPA Max: " + str(max(all_gpas)), "GPA Min: " + str(min(all_gpas))]
    major_stats = collections.Counter(all_majors)
    living_stats = collections.Counter(all_living_states)
    passing_stats = collections.Counter(all_passing)
    degree_stats = collections.Counter(all_degrees)
    year_stats = collections.Counter(all_years)

    print("Student Passing rate: (Boolean Symmetric)")
    print("\t" + str((passing_stats["yes"] / student_count) * 100) + "% are passing\n")
    print("\t" + str((passing_stats["no"] / student_count) * 100) + "% are not passing\n")

    print("Degree (BS or BA): (Boolean Asymmetric)")
    print("\t" + str((degree_stats["BS"] / student_count) * 100) + "% are getting a BS\n")
    print("\t" + str((degree_stats["BA"] / student_count) * 100) + "% are getting a BA\n")

    print("Student Years: (Ordinal)")
    print("\t" + str((year_stats["Freshman"] / student_count) * 100) + "% are Freshman\n")
    print("\t" + str((year_stats["Sophomore"] / student_count) * 100) + "% are Sophomores\n")
    print("\t" + str((year_stats["Junior"] / student_count) * 100) + "% are Juniors\n")
    print("\t" + str((year_stats["Senior"] / student_count) * 100) + "% are Seniors\n")

    print("Major Frequencies: (Categorical)\n" + "\t" + str(major_stats) + "\n")
    print("Living Frequencies: (Categorical)\n" + "\t" + str(living_stats) + "\n")
    print("Age Statistics: (Numerical)\n" + "\t" + str(age_stats) + "\n")
    print("GPA Statistics: (Numerical)\n" + "\t" + str(gpa_stats) + "\n")


def generatecomputers():
    brands = ['HP', 'Apple', 'Dell', 'Acer', 'Lenovo', 'Microsoft', 'Asus', 'Samsung']
    RAMAmounts = ['4', '8', '16', '32', '64']
    ownerNames = ['Jenelle', 'Aniya', 'Arline', 'Florence', 'Ronnette', 'Frederick', 'Isidora', 'Augustine', 'Stacey']
    myFile = open('computers.csv', 'w')
    with myFile:
        for i in range(0, 200):
            brandchoice = random.choice(brands)
            RAMAmountschoice = random.choice(RAMAmounts)
            Owner = random.choice(ownerNames)
            Storageamounts = random.randint(16, 12000)

            OS = random.choice(['Mac', 'Windows'])
            processor = random.choice(["AMD", 'intel'])
            creationYears = random.randint(1981, 2019)
            myData = [Owner, brandchoice, RAMAmountschoice, Storageamounts, OS, processor, creationYears]
            writer = csv.writer(myFile)
            writer.writerow(myData)
        myFile.close()


generateStudents()
# generatecomputers()
