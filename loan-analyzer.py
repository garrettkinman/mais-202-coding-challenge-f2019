import csv

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

# TODO: ignore first line of csv files

with open('home_ownership_data.csv', 'rt') as home_ownership_file:
    home_ownership_reader = csv.reader(home_ownership_file)
    for row in home_ownership_reader:
        print(row)
        if row[1] == 'MORTGAGE':
            mortgages.append(HomeOwner(row[0]))
        elif row[1] == 'OWN':
            owns.append(HomeOwner(row[0]))
        elif row[1] == 'RENT':
            rents.append(HomeOwner(row[0]))
        else:
            print('Yo, each duderino is supposed to be one of those three.')

with open('loan_data.csv', 'rt') as loan_data_file:
    loan_data_reader = csv.reader(loan_data_file)
    for row in loan_data_reader:
        print(row)
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
        
        if not is_found:
            print("Yo, member " + row[0] + " couldn't be found.")
        else:
            continue


mortgages_avg = mortgages_sum / len(mortgages)
owns_avg = owns_sum / len(owns)
rents_avg = rents_sum / len(rents)

print('Avg mortgage: ' + str(mortgages_avg))
print('Avg own: ' + str(owns_avg))
print('Avg rent ' + str(rents_avg))
