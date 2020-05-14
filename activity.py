from dataclasses import dataclass
from category import Categories

@dataclass
class Activity:
	name: str
	category: str = "DEFAULT"
	duration: float = 0
	weight: int = 1

	def __post_init__(self):
		if self.duration == 0:
			self.duration = getattr(Categories, self.category).value

	@property
	def score(self):
		return self.duration*self.weight

if __name__ in ("__main__", "__builtin__"):
	study = Activity(name="Study", category="SELF_DEV")
	print(study.score)