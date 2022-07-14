# A function that adds the duration time to the start time and returns the result.
# day is an optional argument that, when specified as a day of the week, returns the corresponding day of the week of the calculated end time.
def add_time(start, duration, day=None):
    # Split the duration time into a tuple of (hours, ':', minutes).
    # Chose 'partition' instead of the 'split' method because it always returns a tuple of fixed length, making it more predictable.
    duration = duration.partition(":")
    # Convert the hours and minutes strings into integers.
    duration_hours = int(duration[0])
    duration_minutes = int(duration[2])

    # Split the start time into a tuple of (hours, ':', minutes + AM/PM).
    start = start.partition(":")

    # Further split the minutes element into a tuple of (minutes, AM/PM)
    start_minutes_ampm = start[2].split()

    # Convert the hours and minutes strings into integers and store the AM/PM value into its own variable.
    start_hours = int(start[0])
    start_minutes = int(start_minutes_ampm[0])
    am_pm = start_minutes_ampm[1]

    # Calculate the minutes of the end time. If the minutes value is equal to or higher than 60, increase hours by 1 and store the remainder of the minutes of the fractional hour.
    end_minutes = start_minutes + duration_minutes
    while end_minutes >= 60:
        start_hours += 1
        end_minutes = end_minutes - 60
    # Format end minutes for display. If minutes are less than 10, add a '0' before the number.
    if end_minutes < 10:
        end_minutes = "0" + str("end_minutes")

    # Calculate the hours of the end time.
    end_hours = (start_hours + duration_hours) % 12
    # Format end hours for display. If end hours is 0, show 12 instead.
    if end_hours == 0:
        end_hours = 12

    # Calculate how many days passed.
    days_passed = duration_hours // 24
    # If the duration time brings a PM time past midnight, add 1 to the number of days passed.
    if am_pm == "PM" and start_hours + (duration_hours % 12) >= 12:
        days_passed += 1

    # Dictionary with keys assigned to the inverse value to flip values between AM and PM.
    am_pm_flip = {"AM": "PM", "PM": "AM"}
    # Calculate the number of times AM and PM flips.
    am_pm_flip_number = (start_hours + duration_hours) // 12
    # If needed to change the AM/PM indicator if the the am_pm_flip_number is an uneven number, use the am_pm_flip dictionary.
    if am_pm_flip_number % 2 == 1:
        am_pm = am_pm_flip[am_pm]

    # Format the string to be returned.
    new_time = str(end_hours) + ":" + str(end_minutes) + "" + am_pm

    if day is not None:
        # Initialise list of days of the week.
        days_of_the_week_array = [
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        ]
        day = day.strip().lower()
        # Find the position of the starting day of the week on the array and cycle through it to find the end day.
        day_end_index = (days_of_the_week_array.index(day) + days_passed) % 7
        day_end = days_of_the_week_array[day_end_index]

    return new_time
