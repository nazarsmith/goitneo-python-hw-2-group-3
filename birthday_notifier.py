from datetime import datetime
import collections


def get_birthdays_per_week(users: list[dict]):

    bds_seven_days = collections.defaultdict(list)

    current_date = datetime.today().date()

    for user in users:
        user_bd = user["birthday"].date()

        ## calculate user's BD this year
        bd_this_year = user_bd.replace(year=current_date.year)

        if bd_this_year < current_date:
            bd_this_year = bd_this_year.replace(year=current_date.year + 1)

        days_delta = (bd_this_year - current_date).days

        if days_delta < 7:
            day_to_congrats = bd_this_year.strftime("%A")

            day_to_congrats = (
                "Monday"
                if day_to_congrats in ["Saturday", "Sunday"]
                else day_to_congrats
            )

            bds_seven_days[day_to_congrats].append(user["name"])

    ## print out the list of names per day for the next seven days
    for day, names in bds_seven_days.items():
        print("{:<10}{:<5}{}".format(day, ":", ", ".join(names)))

    ## in case the list is needed elsewhere
    return bds_seven_days


## test the function
if __name__ == "__main__":
    test_date = datetime.today()

    users = [
        {
            "name": "Bill Gates",
            "birthday": test_date.replace(
                month=test_date.month - 1
            ),  ## BD this year last month
        },
        {
            "name": "Bill States",
            "birthday": test_date.replace(month=12),  ## BD this year end of year
        },
        {
            "name": "Bill Mates",
            "birthday": test_date.replace(day=test_date.day - 1),  ## BD yesterday
        },
        {
            "name": "Bill Rates",
            "birthday": test_date.replace(day=test_date.day + 1),  ## BD tomorrow
        },
        {"name": "Bill Wates", "birthday": test_date},  ## BD today
        {
            "name": "Bill Spades",
            "birthday": test_date.replace(
                day=test_date.day + 4
            ),  ## BD this weekend; needs adjusting
        },
        {
            "name": "Bill Dates",
            "birthday": test_date.replace(day=test_date.day + 7),  ## BD in a week
        },
    ]

    get_birthdays_per_week(users)

