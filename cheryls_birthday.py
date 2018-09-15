DATES = ["May 15",    "May 16",    "May 19",
         "June 17",   "June 18",
         "July 14",   "July 16",
         "August 14", "August 15", "August 17"]


def Month(date):
    "Return the month of a given date."
    return date.split()[0]


def Day(date):
    "Return the day of a given date."
    return date.split()[1]


def tell(part, possible_dates=DATES):
    """Cheryl tells a part of her birthdate to someone; return a new list
of possible dates that match the part."""
    return [date for date in possible_dates if part in date]


def know(possible_dates):
    "A person knows the birthdate if they have exactly one possible date."
    return len(possible_dates) == 1


def cheryls_birthday(possible_dates=DATES):
    "Return a list of the possible dates for which statements 3 to 5 are true."
    return filter(statements3to5, possible_dates)


def statements3to5(date):
    return statement3(date) and statement4(date) and statement5(date)


def statement3(date):
    """Albert: I don't know when Cheryl's birthday is, but I know that
Bernard does not know too."""
    possible_dates = tell(Month(date))
    return (not know(possible_dates)
            and all(not know(tell(Day(d)))
                    for d in possible_dates))


def statement4(date):
    "Bernard: At first I don't know when Cheryl's birthday is, but I know now."
    at_first = tell(Day(date))
    return (not know(at_first)
            and know(list(filter(statement3, at_first))))


def statement5(date):
    "Albert: Then I also know when Cheryl's birthday is."
    return know(list(filter(statement4, tell(Month(date)))))


if __name__ == "__main__":
    print(cheryls_birthday())
