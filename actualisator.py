import calendar
import datetime
import argparse

def get_businessdays()->int:
    now = datetime.datetime.now()
    holidays = {datetime.date(now.year, 8, 14)} # you can add more here
    businessdays = 0
    for i in range(1, 32):
        try:
            thisdate = datetime.date(now.year, now.month, i)
        except(ValueError):
            break
        if thisdate.weekday() < 5 and thisdate : # Monday == 0, Sunday == 6 
            businessdays += 1
    return businessdays


def calculate (_day_rate:int,_days_off:int)->dict:
    number_of_work_days = get_businessdays() - _days_off
    work_hours = number_of_work_days * 7
    brut = number_of_work_days * _day_rate
    
    return {
        "workhours":work_hours,
        "brut": brut
    }
    
def main():
    print("AdminHelper")
    parser = argparse.ArgumentParser(prog='AdminHelper',description='help calculate work days')
    parser.add_argument('-dr', '--day_rate',required=True)  
    parser.add_argument('-do', '--days_off',required=True)
    args = parser.parse_args()
    print(args)
    result = calculate(int(args.day_rate),int(args.days_off))
    print(f"{result['workhours']}  {result['brut']}")   

    
if __name__=="__main__":
    main()

    '''

py D:/1_TRAVAIL/WIP/CODING/repos/AdminHelp/actualisator.py
'''