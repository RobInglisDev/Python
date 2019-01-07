import datetime

def output_header():
    print('---------------------------------------------')
    print('-             BIRTHDAY COUNTDOWN            -')
    print('---------------------------------------------')
    print()

def get_birthday():
    print('When were you born?')
    year = int(input('Year [YYYY] -> '))
    month = int(input('Month [MM] -> '))
    day = int(input('Day [DD] -> '))

    birthday = datetime.date(year, month, day)
    return birthday

def compute_days(orig_date, target_date):
    this_year = datetime.date(target_date.year, orig_date.month, orig_date.day)
    dt = this_year - target_date
    return dt.days

def output_info(days):
    print()
    if days < 0:
        print('You had your birthday {} days ago this year.'.format(-days))
    elif days > 0:
        print('You birthday is in {} days.'.format(days))
    else:
        print('TODAY IS YOUR BIRTHDAY!')


def main():
    output_header()
    bday = get_birthday()
    # print(bday)
    now = datetime.date.today()
    days = compute_days(bday, now)
    # print(days)
    output_info(days)

main()
