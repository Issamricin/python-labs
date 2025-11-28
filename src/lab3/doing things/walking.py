"""A program that illustrates the division of functions in walking, albeit with a
rather strange walking or go style ."""

def take_step_first(the_leg):
	"""A function that calls the functions needed to take a step"""
	lift_leg(the_leg)
	lean_body("forward")

def take_step_second(the_leg):
	"""A function that calls the functions to take the complementary step"""
	lift_leg(the_leg)
	lean_body("backward")
	put_leg(the_leg)

def lift_leg(the_leg):
	"""Lifts a leg, the_leg indicates right or left"""
	print(f"lift {the_leg} leg")

def put_leg(the_leg):
	"""Puts down a leg that is in the air"""
	print(f"put {the_leg} leg down")

def lean_body(direction):
	"""Tilts the body, direction indicates direction"""
	print(f"tilt body {direction}")

def walk_1m_fwd():
	"""A function that walks one meter forward"""
	take_step_first("right")
	take_step_second("left")

def walk_fwd(meters):
	"""A function that walks meters number of meters forward"""
	if meters > 0:
		walk_1m_fwd()
		walk_fwd(meters-1)


walk_fwd(2)
