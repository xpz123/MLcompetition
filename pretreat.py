import csv
def loadCsv(filename):
    lines = csv.reader(open(filename, "r"))
    dataset = list(lines);
    return dataset

def date_account_pro(time):
    res += 31 * (int(time[5]) - 7)
    if len(time) == 8:
        res += (int(time[7]) - 1)
    else:
        res += (int(time[7]+time[8]) - 1)
    return res

def gender_pro(gender):
    if gender == 'FEMALE':
        return -1
    elif gender == 'MALE':
        return 1
    else:
        return 0

def age_pro(age):
    if age == '':
        return 0
    else:
        return int(age)

def hamming_dist(str1, str2):
    diffs = 0
    if len(str1) != len(str2):
        return 'Length of two strings must be equal'
    else:
        for ch1, ch2 in zip(str1, str2):
            if ch1 != ch2:
                diffs += 1
    return diffs

#facebook(001), basic(010), google(100)
def sign_method_pro(method):
    if method == 'facebook':
        return '001'
    elif method == 'basic':
        return '010'
    else:
        return '100'

def sign_flow_pro(num):
    return int(num)

def find_element(dataset, pos):
    eles = set()
    for i in range(len(dataset)):
        name = dataset[i][pos]
        eles.add(name)
    eles.remove(dataset[0][pos])
    return eles

def content_pro(dataset, lan, pos):
    lans = list(find_element(dataset, pos))
    if lan == '-unknown-':
        return -100
    for i in range(len(lans)):
        if lan == lans[i]:
            return i


    
filename = 'test_users.csv'
dataset = loadCsv(filename)
names = find_element(dataset, 8)
print(len(names))

