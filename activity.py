from dataclasses import dataclass

@dataclass
class Activity:
	name: str
	weight: float = 1
	time_unit: int

if __name__ in ("__main__", "__builtin__"):
	pass