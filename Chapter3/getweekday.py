def get_weekday(current_weekday, days_ahead):
	""" (int, int) -> int

	Return which day of the week it will be days_ahead days from
	current_weekday.

	current_weekday is the current day of the week and is in the
	range 1-7 indicating whether today is Sunday(1), Monday(2),
	... Saturday(7)
	"""
	return (current_weekday + days_ahead - 1) % 7 + 1


print(get_weekday(3, 1))
print(get_weekday(2, 24))
