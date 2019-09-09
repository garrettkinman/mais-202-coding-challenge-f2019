import csv
import matplotlib.pyplot as plot

# TO USE THIS PROGRAM, NEED  matplotlib
# THEN JUST RUN `python loan-analyzer.py` IN THE TERMINAL
# AVERAGES WILL BE PRINTED TO CONSOLE
# AND GRAPH WILL POP OPEN

# AUTHOR: Garrett Kinman

class HomeOwner:
    def __init__(self, member_id):
        self.member_id = member_id
        self.loan_amnt = None

# each list represents all the people of each ownership type
mortgages = []
owns = []
rents = []

mortgages_sum = 0
owns_sum = 0
rents_sum = 0

# reads from home_ownership_data.csv and adds info to appropriate lists
# will ignore first line of data that just gives the column headers
with open('home_ownership_data.csv', 'rt') as home_ownership_file:
    home_ownership_reader = csv.reader(home_ownership_file)
    for row in home_ownership_reader:
        if row[1] == 'MORTGAGE':
            mortgages.append(HomeOwner(row[0]))
        elif row[1] == 'OWN':
            owns.append(HomeOwner(row[0]))
        elif row[1] == 'RENT':
            rents.append(HomeOwner(row[0]))
        else:
            continue

# reads from loan_data.csv and adds info to appropriate lists
# will ignore first line of data that just gives the column headers
with open('loan_data.csv', 'rt') as loan_data_file:
    loan_data_reader = csv.reader(loan_data_file)
    for row in loan_data_reader:
        is_found = False

        # don't need to check is_found before checking mortgages
        # since it can't have been found yet
        for member in mortgages:
            if member.member_id == row[0]:
                member.loan_amnt = float(row[1])
                mortgages_sum += float(row[1])
                is_found = True
                break

        # could have been found by now, so need to check
        if not is_found:
            for member in owns:
                if member.member_id == row[0]:
                    member.loan_amnt = float(row[1])
                    owns_sum += float(row[1])
                    is_found = True
                    break
        else:
            continue
        
        # could have been found by now, so need to check
        if not is_found:
            for member in rents:
                if member.member_id == row[0]:
                    member.loan_amnt = float(row[1])
                    rents_sum += float(row[1])
                    is_found = True
                    break
        else:
            continue

# now that all the data from the files is parsed, analyze the data

mortgages_avg = mortgages_sum / len(mortgages)
owns_avg = owns_sum / len(owns)
rents_avg = rents_sum / len(rents)

print('Avg mortgage: ' + str(mortgages_avg))
print('Avg own: ' + str(owns_avg))
print('Avg rent ' + str(rents_avg))

# for use in the bar chart
ownership_type = ['MORTGAGE', 'OWN', 'RENT']
avgs = [mortgages_avg, owns_avg, rents_avg]

def plot_bar_x():
    index = range(len(ownership_type))
    plot.bar(index, avgs)
    plot.xlabel('Home ownership', fontsize=10)
    plot.ylabel('Average loan amount ($)', fontsize=10)
    plot.xticks(index, ownership_type, fontsize=10)
    plot.title('Average loan amounts per home ownership')
    plot.show()

plot_bar_x()
