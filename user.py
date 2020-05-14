import getpass
from activity import Activity

class User:
	def __init__(self):
		self.name = getpass.getuser()
		self.activities = []

	@property
	def score(self):
		return sum([a.score for a in self.activities])


if __name__ in ("__main__", "__builtin__"):

	user = User()
	print("Current activities: ",user.activities)
	print("Current score: ", user.score)
	study =  Activity(name="Study", category="SELF_DEV", weight=7, duration=2)
	user.activities.append(study)
	print("Current activities: ",user.activities)
	print("Current score: ", user.score)
	chore = Activity(name="Chore", category="CHORES", weight=2)
	user.activities.append(chore)
	print("Current activities: ",user.activities)
	print("Current score: ", user.score)