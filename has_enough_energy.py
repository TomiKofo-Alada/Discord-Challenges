# Do some Pythonic math with the distance_one_way and
# meters_per_energy variables to determine how many points 
# of energy are needed for Tyler to get to the capital city
# AND make it back to the inn. Assign the result to a 
# energy_needed variable. distance_one_way is how many
# meters it is to get from here to there. meters_per_energy
# is how far Tyler's rogue can travel with one energy point.

# Return True if there is at least enough energy based on the 
# energy_needed variable, and False otherwise.

# starting code:

def has_enough_energy(energy_available, distance_one_way, meters_per_energy):
    round_trip = 2 * distance_one_way
    energy_needed = round_trip // meters_per_energy
    return energy_available >= energy_needed

