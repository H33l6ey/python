
def get_currentYear():
    import datetime
    now = datetime.datetime.now()
    return now.year

def age_cal(current, birth):
    age = current - birth
    return age




current_year = get_currentYear()
birth_year = int( input("Enter birth year? "))
age = age_cal(current=current_year, birth=birth_year)
print("your age is",age)

