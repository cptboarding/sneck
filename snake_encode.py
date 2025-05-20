

import FileEditor as f
import datetime


e = f.FileEditor("scoreboard")


def assertion():
    if not e.assertfile():
        e.create()


def convert_zero(n):
    if n < 9:
        r = '0' + str(n)
        return r
    else:
        return str(n)

#  value.ddmmyyyy;

def encode(score):
    assertion()
    d = datetime.date.today()
    day = convert_zero(d.day)
    mon = convert_zero(d.month)
    yr = d.year
    s = str(score) + '.' + str(day) + str(mon) + str(yr) + ';'
    e.append(s)

def decode():
    file = e.readfile()
    mode = 0
    val = ''
    dt = ''
    r = []
    for i in file:
        if i == '.':
            mode = 1
        elif i == ';':
            mode = 0
            date = (dt[0]+dt[1], dt[2]+dt[3], dt[4]+dt[5]+dt[6]+dt[7],)
            r.append([val, date])
            val = ''
            dt = ''
        else:
            if mode == 0:
                val += i
            else:
                dt += i
    return r

def score(i):
    return i[0]

def get_top():
    scores = decode()
    scores.sort(reverse=True, key=lambda x: x[0])
    r = []
    i = 0
    while i < 5 and i < len(scores):
        r.append(scores[i])
        i += 1
    return r


if __name__ == "__main__":
    t = get_top()
    print(t)




