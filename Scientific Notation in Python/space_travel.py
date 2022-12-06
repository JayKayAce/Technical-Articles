# space_travel.py

import decimal


distances = {
    "Mercury": decimal.Decimal("35e6"),
    "Venus": decimal.Decimal("64e6"),
    "Earth": decimal.Decimal("150e6"),
    "Mars": decimal.Decimal("228e6"),
    "Jupiter": decimal.Decimal("778e6"),
    "Saturn": decimal.Decimal("1427e6"),
    "Uranus": decimal.Decimal("2871e6"),
    "Neptune": decimal.Decimal("4498e6"),
    "Pluto": decimal.Decimal("5906e6"),
}

commands = ( "Show Planets", "Convert AU", "Calculate Distance", "Travel", "Calculate Delay")

speed_of_light = decimal.Decimal(299792458)  # meters pr second

def convert_ms_to_kms(speed: decimal.Decimal) -> decimal.Decimal:
    "Converts speed from meters/second to kilometers/second"
    return decimal.Decimal(speed / decimal.Decimal(1e3))

SpaceShips = {
    "Shuttle": {"speed_kms":decimal.Decimal("11.19")},
    "Enterprise":{"speed_kms": 213*convert_ms_to_kms(speed_of_light),"maximum_warp_factor": 5}
    }

def calculate_transmission_delay(planet) -> decimal.Decimal:
    """ Calculates the time delay in seconds for a transmission from a planet to Earth"""
    distance = calculate_distance(distances.get("Earth", 1), distances.get(planet, 0))
    speed = convert_ms_to_kms(speed_of_light)
    return distance / speed

def calculate_distance(start: decimal.Decimal, end: decimal.Decimal) -> decimal.Decimal:
    return end - start

def present_planet(planet: str) -> str:
    return f"{planet} - {distances.get(planet, 0).normalize().to_eng_string()}"

def convert_to_au(planet: str, destinations=distances) -> decimal.Decimal:
    """ Calculate the distances for a given planet in AU"""
    return (destinations.get(planet, 0) / destinations.get("Earth", 1))

def travel_time(ship_name, starting_planet, destination_planet) -> decimal.Decimal:
    """ Calculates the traveltime in seconds from starting planet to destination planet"""
    speed = decimal.Decimal(SpaceShips[ship_name]["speed_kms"])
    distance = calculate_distance(distances.get(starting_planet, 1), 
                                    distances.get(destination_planet, 0))
    return distance / speed

def setup():
    print("Welcome to the space simulator. Type Q to quit")
    print("The available commands are: \n")
    for cmd in commands:
        print(cmd)

def shutdown():
    print("Closing the space travel simulator")

def main():
    setup()
    while True:
        command = input("?> ")
        if command == "Q":
            break
        try:
            if command in commands:
                planet = input("Select Planet> ")
                if command == "Show Planets":
                    if planet == "All":
                        for planet_name in distances.keys():
                            print(present_planet(planet_name))
                    elif planet in distances.keys():
                        print(present_planet(planet))
                    else:
                        print("Faulty planet name, please try again")
                elif command == "Convert AU":
                    if planet in distances.keys():
                        print(convert_to_au(planet).to_eng_string())
                elif command == "Calculate Distance":
                    planet_destination = input("Select Second planet> ")
                    print(format(
                        calculate_distance(
                            distances.get(planet, 0), distances.get(planet_destination)
                            ),".5e"
                        )
                    )
                elif command == "Travel":
                    ship_name = input("Ship Name > ")
                    planet_destination = input("Select Second planet > ")
                    if ship_name == "?":
                        print(SpaceShips.keys())
                        ship_name = input("Ship ?")
                    print(format(
                            travel_time(ship_name, planet, planet_destination)
                        , ".5e") 
                    )

                elif command == "Calculate Delay":
                    print(calculate_transmission_delay(planet))

        except Exception as e:
            print(e)

    shutdown()


if __name__ == "__main__":
    main()
