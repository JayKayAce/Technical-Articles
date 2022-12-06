# Scientific Notation in Python (A Work in progress)

Have you ever thought about how fast the speed of light is or how long it would take if we could travel to Mars at the speed of light? These questions are really good examples for applying the Scientific Notation since the magnitudes of the numbers are so inconceivable. Scientific notation is supported in Python both for the user input as well as model output. Scientific notation can be used for the representation of both small and large values in your mathematical problem-solving and it embraces representing the speed of light as well as the diameter of a proton.

**In this tutorial, you'll learn:**

* The basics of scientific notation and how to apply this in Python
* Why Python scientific notation is a useful tool for input and presentation
* The difference between float and decimal representation
* The `Decimal` module and why it is important to consider using it
* Understand Pythons usage and caveats of the scientific notation
* Understand how to simplify the conversion of physical properties in Python.
* Identify numerical problems, before combining large and small numbers in mathematical equations in Python

If you already know about the mathematical principles of the Scientific Notation feel free to skip ahead to the section **Using Python Scientific Notation**.

## Getting an overview of Scientific Notation

The Scientific notation is as the name describes used primarily in science and is mainly a specific way of writing numbers to make it easier to read. To improve the readability, any number can be broken down into components. This was historically done to make the mathematical operations easier, such as multiplication, and to speed up writing the calculations with pen and paper.

### Understanding The Basic Principle: Powers of 10

Consider as an example that you had a large number such as 300 million and add this to 2 billion. Try to write out the following math on a piece of paper, like below:

```text
2 000 000 000 + 300 000 000 = 2 300 000 000
```

Now consider how many zeros you had to write the previous addition. This could be reduced by factorization of both numbers into powers of 10. Let's rewrite the equation in powers of 10:

```text
2 * 10 ^ 9 + 3 * 10 ^ 8 = 2.3 * 10 ^ 9
```

Now you can see we have replaced the long numbers with their factorized versions, and significantly reduced the number of zeroes needed to represent the numbers. By convention, the writing of `1*10^6` was replaced by `1e6` or `1E6`, which was faster to write. This would improve writing the same mathematical equation in the following way:

```text
2e9 + 3e8 = 2.3e9
```

Wow, now you have reduced the number of characters to input the math from 35 characters to 17. This is the principle behind the scientific notation, but to make the notation even easier the convention was improved. Now let's consider some more practical examples

### Using Scientific Notation to Convert SI units

Scientific notation is really useful in the conversion of units within the same physical property in the [SI](https://en.wikipedia.org/wiki/International_System_of_Units) units. In the SI system the units have different prefixes for each multiple of 1000, which is easy to represent in the scientific notation as we just learned:

| Name | Scientific notation |
|------| --------------------|
| mega | 1e6                 |
| kilo | 1e3                 |
| mili | 1e-3                |
| micro | 1e-6               |
| nano | 1e-9                |

From the table above a **kilometer** can easily be understood as 1000 **meters** or 1e3 meters in scientific notation. The table is only a small excerpt of [this table](https://en.wikipedia.org/wiki/Metric_prefix#List_of_SI_prefixes) of metric prefixes.

## Using Python Scientific Notation

You can use the scientific notation directly in Python modules as well as the REPL, and it is really easy to use. You can use it for implicit documentation of your mathematic conversions, to show the conversion of units. This makes your code easier to read and understand when sharing or debugging it. The general syntax for the scientific notation can be expressed as follows:

```text
<floating point number>e<sign><power of 10>
```

Above you see that the scientific notation is:

* a [floating-point](https://realpython.com/python-numbers/#floating-point-numbers)
* followed directly by an `e` with no space in-between this and the floating-point number
* followed by the sign, either positive or negative, positive is optional
* followed by the exponent represented as an integer

{% alert %}
**Note:** It is important to note that the exponent MUST be an integer, otherwise a `SyntaxError` will occur.
{% endalert %}

Now that you know the syntax of the scientific notation, let's move on.

### Inputting numbers using Scientific Notation

In the Python REPL you can input numbers directly in scientific notation. Try to input the following into the Python REPL to see the resulting numbers:

```pycon
>>> 1e4
10000.0
>>> 10e-4
0.001
>>> 100e13
1000000000000000.0
>>> 1e16
1e+16
>>> 1e-5
1e-05
```

You should note from the above examples, that even though the large numbers are in general pure integers they are represented in memory as [float values](https://realpython.com/python-numbers/#floating-point-numbers). Another thing you will notice is that value of `1e16` is presented with the sign of the exponent when printing the number. Last but not least there is an upper and lower boundary where the Python REPL will switch to use scientific notation when printing numbers.

You can use either `e` or `E` to denote the exponent of the number, when inputting data:

```pycon
>>> a = 1.3e6
>>> b = 1.3E6
>>> a == b
True
```

Above you can see that you can use either of the notation of the exponent and the variables `a` and `b` are still equal.

### Printing in Scientific Notation using `format`

Now that you know how to input data into Python using scientific notation, it is time to look at printing the values in the scientific notation. Here you need to use the built-in [format](https://realpython.com/python-formatted-output/#the-string-format-method-arguments) function along with the format specifier `'e'` to convert the number into a string in scientific notation. You can easily use the f-strings in combination with the builtin `format` function to convert data:

```pycon
>>> f"{format(1e18,'e')} is a large number"
'1.000000e+18 is a large number'
```

As you can see, the format function reports the value with 6 digits precision on the floating-point. This is the default setting, but can be changed using the [format specification mini language](https://docs.python.org/3.4/library/string.html#format-specification-mini-language). With the same technique, you can print a number as decimal notation using the `'f'` format specifier.

```pycon
>>> format(1e18,'f')
'1000000000000000000.000000'
```

You can combine the f-strings and `format` to convert from meters to kilometers units to make it easier to correlate when debugging:

```python
def km_convert(value:float, unit:str)->str:
    return f"{value} {unit} = {format(value/1e3,'.3e')} k{unit}"
```

You could make your debugging functions for your mathematical models when stepping through your code and inspecting values using the [Python pdb module](https://realpython.com/python-debugging-pdb/)

### Python Floating-Point Representation and IEEE 754

As you may have noted by now all numeric values input using the scientific notation are saved as floating-point numbers. These floating-point numbers, or floats, are following a specific standard [IEEE Standard for Floating-Point Arithmetic](https://en.wikipedia.org/wiki/IEEE_754) or **IEEE 754** for short. This standard is issued from and governed by the Institute of Electrical and Electronics Engineers. The standard describes, how the floating-point numbers are described using a model to represent the number using integers, and going into all the aspects of the model is beyond this tutorial. You can think of the model as an equation to calculate a close approximation of the number, which can be seen below:

TODO: Insert floating-point model here

From the above model you can see that the model consists of:

* **sign**: either positive or negative 1
* **base**: the base number on which the representation is based, this is also referred to as the radix.
* **precision**: number of **digits** that precisely can be represented.
* **e**: the exponent of the base which must be higher than the minimum value and below the max exponent.
* **f**: a non-negative integer less than the base.

You might wonder where the numbers for this model can be found, and in Python this is implemented in the `sys` module. Since the factor f must be non negative and less than the base the value can be either 0 or 1 when having a base of 2. In the Python `sys` module the named tuple `float_info` is included, and this contains the all the information for model and then some:

```pycon
>>> import sys
>>> sys.float_info
sys.float_info(
    max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308,
    min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307,
    dig=15, mant_dig=53, epsilon=2.220446049250313e-16,
    radix=2, rounds=1)
```

In the `sys.float_info` above you can see the following for the model:

* floating-point numbers use a base or radix of 2.
* the maximum exponent **e** is 1024, and the minimum **e** is -1021
* There is a maximum representable number, defined by **max** and a minimum representable number defined by **min**
* The precision is represented by **dig** which is 15
* The mantissa has 53 digits to represent a number, provided by the **mant_dig**
* The epsilon is the smallest difference between two floating-point numbers

This is often referred to as a double-precision floating-point representation and this information is important if you are doing calculations or mathematical operations. It is important because any information above **max** or below **min** will be considered as infinite positive or negative `inf` or infinity. Additionally, you would not be able to calculate differences between two floating-point numbers if the difference is less than the value of **epsilon**. Since the straight floating-point numbers are using base 2 you also have to take the [floating-point representation errors into account](https://realpython.com/python-numbers/#make-python-lie-to-you). But you may wonder that the scientific notation is a base 10 representation and floating-point is base 2, so how would you force the Python to use base 10 for the representation?

### Using the Decimal Module

In the Python standard library, you can find the `decimal` module, which allows you to use the decimal or base 10 representation of your numbers. The module is included to have mathematical operations that work with a decimal-based representation compared to the binary float representation, discussed in the previous section. The model for the decimal representation of the numbers is exactly like the representation of the scientific notation as can be seen below:

```python
x = sign * mantissa * 10 ** exponent
```

Another special thing about `Decimal` is that it is more precise. You can use it to calculate summation with large and small values without having the same problems as the binary **float** implementations. To start using the decimal module you must import the module from the Python standard library and then instantiate the Decimal class with a value you need to use:

```pycon
>>> import decimal
>>> a = decimal.Decimal(100)
>>> a
Decimal('100')
```

You imported the `decimal` module to gain access to all the functions in the `decimal` module, and then you create an instance of the `Decimal` class to represent the value of `100`. This module is particularly useful to make financial calculations, because of the decimal representation in memory. You can see that the `Decimal` class uses a radix of 10, by inspecting the radix of your instance a, by calling the `radix` function:

```pycon
>>> a.radix()
Decimal('10')
```

As you can see this returns the radix of 10, here represented as a decimal object. Decimal objects can be used for calculations, and can be instantiated by either integers, floats or even numeric strings. The thing you need to consider is the consequences of using the various representations:

```pycon
>>> decimal.Decimal(int(10000000))
Decimal('10000000')
>>> decimal.Decimal(1e-5)
Decimal('0.0000010000000000055511151231257827021181583404541015625')
>>> decimal.Decimal("1e-5")
Decimal('1E-5')
```

As you can see from the above examples, you can declare the Decimal objects with integers and floats as well as strings. The `decimal` module works with contexts for the decimal representations, which can be inspected and changed with the `getcontext` function and that will change the context for the calculations globally for the `decimal` module:

```pycon
>>> decimal.getcontext()
Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])
```

You can see that the `getcontext()` function is stored inside the decimal module and the context provides the decimal module with information about precision, **prec**, and the minimum and maximum value of the exponent, **Emin** and **Emax** respectively. The decimal module supports a precision up to 28 digits with a floating position of the decimal point, which makes it possible to add large and small numbers together without loss of data as long as the data is within 28 digits of each other. The subject of the decimal context is only covered briefly here and is a topic of its own.

{% alert %}
**Note:** The important thing to keep in mind is that the precision of the decimal module is only as good as the data used to create the Decimal object.
{% endalert %}

### Caveats when using Floats and Scientific Notation

Some representative errors need to be considered when instantiating decimal objects because the usage of a **float** value for the instantiation includes the data outside the representation of the precision of the floating-point number. This data is not available in the instantiating with a string, because the string only contains the precision of the string and nothing more. Let's consider the differences when comparing the value of `1e25` for the instantiation of the Decimal object:

```pycon
>>> f = decimal.Decimal(1e25)
>>> s = decimal.Decimal("1e25")
>>> s-f
Decimal('-905969664')
```

You have instantiated a `decimal.Decimal` object **f** with the floating value of `1e25` and the object **s** with the string representation of the same value and calculate the difference. This may or may not be a problem for your calculations, but it is something that needs to be taken into account when instantiating the decimal objects. Another thing you may have noticed about the binary floating-point numbers the digits of precision is limited to 15 digits. Consider the following two comparisons:

```pycon
>>> 1e15 == 1e15 + 1
False
>>> 1e16 == 1e16 + 1
True
```

As you can see the second comparison resolves to **True** even though common logic says that if you increment the same number with 1 the new values are no longer the same number. This comes down to the range of the data is truncated. This would also be the problem if adding a small number. The small number would be outside the representation of the floating-point model digits of precision. Consider the same implementation using the decimal module:

```pycon
>>> decimal.Decimal(1e16) == decimal.Decimal(1e16 + 1)
True
>>> decimal.Decimal(1e16) == decimal.Decimal(1e16) + decimal.Decimal(1)
False
```

You might expect that the first comparison would return False, but Python evaluates arguments before instantiating objects and evaluating functions, so the first line compares the decimal object instance where the `1e16 + 1` has already been evaluated to `1e16` before conversion to Decimal. Using the second equation is the better approach because the evaluation is done after the instantiation.

## Simulating Space Travel using Python Scientific Notation

By now you have learned all the components to build a Space travel simulator. To simplify the calculations let's normalize all the distances to one dimension, and ignore the cumbersome calculations of the three-dimensional positions. While you could easily make this in a graphical user interface (GUI) application, let's keep it simple and use a simple command-line application layout in this calculator. Let's start by creating a single Python module named **space_travel.py** and make a simple application structure:

```python
# space_travel.py

def setup():
    print("Welcome to the space simulator. Type Q to quit")

def shutdown():
    print("Closing the space travel simulator")

def main():
    setup()
    while True:
        command = input("?> ")
        if command == "Q":
            break
    shutdown()

if __name__ == "__main__":
    main()
```

What you have created is an application structure with a `main` function, containing:

* a `setup` function, to handle any set up the application
* an infinite loop, to run your simulation code, which takes user input in the form of a string of commands.
* a single command to quit the program loop, when the user inputs a `Q`
* a `shutdown` function to run when the program loop is stopped and clean up after the application

The user scenario for the application is that the user can write commands and each command can have some arguments. The only special command is the `Q` command for quitting the application. Now that you have the application skeleton finished you can start on the implementation of the planets into the simulator.

### Representing Planets and Their Positions: Inputting Planet Positions Using Scientific Notation

In order to make some calculations you need a set of data to work from, and luckily [NASA has you covered](https://www.nasa.gov/audience/foreducators/5-8/features/F_Solar_System_Scale.html). The distances are listed in this table:

| Planet  | Distance From the Sun [km]  |
|---------|---------------------------- |
| Mercury | 35,000,000                  |
| Venus   | 64,000,000                  |
| Earth   | 150,000,000                 |
| Mars    | 228,000,000                 |
| Jupiter | 778,000,000                 |
| Saturn  | 1427,000,000                |
| Uranus  | 2871,000,000                |
| Neptune | 4498,000,000                |
| Pluto   | 5906,000,000                |

As you can see the distances in the table above are large but not too large to fit into Python. Consider this for a moment, What would be the best data structure to implement the data in. You could go with a list of the distances, but then you would have to remember the positions of all the planets. To avoid this you could choose a dictionary since the data is in the form of key-value pairs, so let's try to implement that:

```python
distances =  {"Mercury": 35e6, "Venus": 64e6, "Earth": 150e6, "Mars": 228e6,
 "Jupiter" : 778e6, "Saturn": 1427e6, "Uranus": 2871e6,
 "Neptune": 4498e6, "Pluto": 5906e6}
```

In the above implementation, you have implemented a key-value relational map using a dictionary, with the distances from the sun to the planets of our solar system. Implementing the data in a dictionary serves more than just access to the data via the name of the planet but it also helps to document your code.

Let's implement a command to show to the user the positions of all the planets in order. For that, we need to create a function to display a planet's position, and the name of the planet formatted nicely with the same amount of decimals. Additionally, you should make sure that the function provides the distances in the scientific notation at a variable number of decimals:

```python
def present_planet(planet_name : str, digits) -> str:
    return f"{planet} - {format(distances.get(planet, 0), f'.{digits}e')}"
```

You now have a function taking two arguments the planet_name to present and the number of digits and returns a string formatted uniformly. The function returns an f-string and formats the distance into scientific notation, for an easy overview. One thing to note here is the nested f string within the `format` function to ensure the format specifier string changes, based on the value of digits. The function returns the formatted string instead of printing the string directly to improve the reusability of the function.

Before implementing the `present_planet` function in the main program loop, you should test out your code and make sure this is working correctly. For now, you can use the Python REPL by invoking it in [interactive mode](https://docs.python.org/3/using/cmdline.html#cmdoption-i), which lets you call your functions in the file directly from the Python REPL. To start Python in interactive mode add the command-line option `python -i space_travel.py`, and then press `Q` to quit the main loop for now. After that you can call your function and test it with different planets and representations:

```pycon
c:\>python -i space_travel.py
Welcome to the space simulator. Type Q to quit
?>Q
Closing the space travel simulator
>>> present_planet("Earth", 3)
Earth - 1.500e+08
>>> present_planet("Mercury",5)
Mercury - 3.50000e+07
>>> exit()
```

Now you have access to all the functions within the space_travel.py file and tested that the representation of both **Earth** and **Mercury** functions as you would expect it with both 3 and 5 digits respectively it is time to implement the space shuttle for the traveling between the planets.

### Building a space ship using Scientific Notation: Representing Speed and Units

To travel from planet to planet you would need a spaceship. You could implement a specific shuttle, but for now, let's just make a generic shuttle traveling at the [escape velocity for leaving Earth gravity](https://en.wikipedia.org/wiki/Escape_velocity#List_of_escape_velocities). In the same manner, as the distances for the planets you could implement the ship as a dictionary, with a nested dictionary as well:

```python
SpaceShips = {"Shuttle": {"speed_kms":11.19}}
```

You now have a representation of a space ship in the form of a dictionary with a nested dictionary. This makes it possible to add other properties if needed, and makes it easy to extend with additional ships.

Additionally, you could implement the [speed of light](https://en.wikipedia.org/wiki/Speed_of_light) as a constant in the application, to make sure this cannot be changed from the outside when using your application. In the top of the `space_travel.py` module add your constant `speed_of_light` and set it equal 299792458 meters per second:

```python
speed_of_light = 299792458 # meters per second
```

The speed of the shuttle and the speed of light have different units. The shuttle speed is in kilometers per second and the speed of light is in meters per second, so let's solve that issue next.

### Converting between units in Scientific Notation: Implement unit conversion

To solve the differences in speed units, you'll have to make a conversion function for ensuring the speed units can be compared. To do this let's make a function to implement the conversion to divide the speed of light with `1e3`:

{% alert %}
**Note:** Avoid implementing magic numbers in your calculations and models, since the calculation can be hard to debug if the magic number is not immediately understandable. Use functions for conversions instead.
{% endalert %}

```python
def convert_ms_to_kms(speed: float) -> float:
    "Converts speed from meters/second to kilometers/second"
    return speed / 1e3
```

You now have a specific function to convert the speed to **km/s**, to perform time calculations later on. Keeping the units in the same system may not always be possible so it is really useful to have conversion functions for the debugging and understanding of the code later.

You may have heard that astronomers use the convention of **astronomical units** or **AU**, which relate all distances to the distance between the Sun and Earth. You could implement a function to do this calculation for you. To implement the calculation you could make a function to calculate the relative distance, resulting in the values in AU. Start by creating a function that takes the planet name as an argument. It should look up the distance in the `distances` dictionary and divide this with the distance of **Earth**:

```python
def convert_to_au(planet_name:str, destinations = distances)->float:
    """ Calculate the distances for a given planet in AU"""
    return destinations.get(planet_name, 0) / destinations.get("Earth", 1)
```

The function that you just created looks for the `planet_name` in the dictionary `distances` by using the `get` method of [dictionaries, to avoid key errors](https://realpython.com/python-keyerror/#the-usual-solution-get) and divides it with the value for **Earth**. If the **planet** does not exist in the `distances` dictionary the function will return 0. You could implement the function for the listing of planet positions in both astronomical units and kilometers.

### Traveling to Mars: Calculating distance with Scientific notation

By now you have a dataset of distances in scientific notation and it is time to calculate the distances between the different planets. For this calculation, you could use the Python `decimal` module to accommodate the distances, when they become really large. First, you import the `decimal` module from the Python Standard library and create a function to calculate the distances between two arbitrary planets and return the value as a decimal object:

```python
import decimal

def calculate_distance(start:float, end:float)->decimal.Decimal:
    return decimal.Decimal(end) - decimal.Decimal(start)
```

You imported the `decimal` module to use the Decimal class for the calculations at the top of your `space_travel.py` module. The `calculate_distance` function takes 2 arguments, a starting point, and an endpoint. These are converted to `Decimal` objects to avoid truncation of data and the distance can be calculated by subtracting the `start_position` from the `end_position`. The truncation may happen if combining large and small numbers and as you know by now this can be mitigated by using Pythons **Decimal** modules.

To calculate the travel time for the `Shuttle` you implemented earlier in the `SpaceShips` dictionary, you would calculate the distance traveled and divide it by the speed of the vessel you are flying. This will give the speed in seconds since the speed of the shuttle is in kilometers per second. Let's make a function called `travel` that takes a vessel name a starting planet and a destination planet:

```python
def travel_time(ship_name, starting_planet, destination_planet):
    """ Calculates the travel time in seconds from starting planet to destination planet"""
    speed = decimal.Decimal(SpaceShips[ship_name]["speed_kms"])
    distance = calculate_distance(distances.get(starting_planet, 1),
                                    distances.get(destination_planet, 0))
    return distance / speed
```

You have now implemented a function that calculates the traveling time based on the selected ship and the names of the starting planet and destination planet respectively. The function looks up the speed of the ship from the `SpaceShips` dictionary and converts it to a Decimal object.

### Updating the Tactical Overview: Formatting and presenting the Data to the User

By now it is time to update the space travel simulator with all the functions you have created and to start-up let's implement a function to list all the destinations. We start by implementing a command tuple in the top of the script, called `commands` and instantiate it with the string `"Show Planets"`:

```python
commands = ("Show Planets")
```

To show the planets you would implement the `present_planet` function you created earlier as a command in the `main` function. To implement the command change the `main()` function to have a `try/except` structure to handle user input errors. Additionally you need to check that the program only reacts to the right functions:

```python
def main():
    setup()
    while True:
        command = input("?> ")
        if command == "Q":
            break
        try:
            if command in commands:
                # your command functions goes here
        except Exception as e:
            print(e)
    shutdown()
```

By now you have extended the main program loop with a try/except structure to handle if a user inputs some bad names for planets. To implement the function in the program let's implement a check for the command being equal to the `Show Planets` command, since most of your functions take a planet name, let's check request the planet name from the user as well. As you remember the `present_planet` function presents a planet with its name and the scientific notation of its distance to the Sun. To make it easier for the user, let's implement both an "All" feature presenting all planets and a planet specific implementation only presenting the planet data:

```python
def main():
    # ...
        try:
            if command in commands:
                planet = input("Select Planet> ")
                if command == "Show Planets":
                    if planet == "All":
                        for planet_name in distances.keys():
                            print(present_planet(planet_name, 5))
                    elif planet in distances.keys():
                        print(present_planet(planet, 5))
                    else:
                        print("Faulty planet name, please try again")
```

By now you have implemented the first function into the program's main loop. The main loop requests the user for the planet name after ensuring that the command is in the `commands` tuple. The function checks if the command is matching `Show Planets`. The user has two options now, to input either "All" or a specific planet name. If the user inputs "All" when asked to select a planet, the `for loop` will get all the planets in the `distances` dictionary and print the result of `present_planet` out. If the user inputs a specific planet name the planet will be presented. If the user inputs giberish the program will run the else clause and print an error message. Let's continue to implement the command `Convert AU`. Like before start by adding the command to the commands tuple and implement the check for the command below the check for `Show Planets`:

```python
commands = ("Show Planets", "Convert AU")

def main():
    ...
            if command in commands:
                planet = input("Select Planet> ")
                if command == "Show Planets":
                    ...
                elif command == "Convert AU":
                    if planet in distances.keys():
                        print(convert_to_au(planet))
```

You have now implemented the conversion of distances to astronomical units. The command is checked using the `elif` conditional to check the command is matches the "Convert AU" string, and then the planet name is checked for existence in the `distances` dictionary.

{% alert %}
**Note:** Keep in mind here that you only have one `input` for the `planet` placed before checking the command against the functional implementations.
{% endalert %}

Next, you should implement the distance calculation, using the `calculate_distance` function. In the same manner as before you add the command to **commands** tuple and check the command by name, but now you need to ask the user for the second planet name. This is done with the `input` function, and additionally, you should represent the result in scientific notation:

```python
commands = ("Show Planets", "Convert AU")

def main():
    ...
            if command in commands:
                planet = input("Select Planet> ")
                # ...
            elif command == "Calculate Distance":
                planet_destination = input("Select Second Planet> ")
                print(format(
                    calculate_distance(
                        distances.get(planet, 0), distances.get(planet_destination)
                        )
                    ,".5e")
                )
```

The calculation of the distance requires a second planet and you need to ask the user for the name of the second planet. To show the result in the scientific notation you use the `format` function to wrap the result of the `calculate_distance` function in, with a format specifier of `".5e"` to get 5 digits of precision.

By now it should be trivial for you to implement the `Travel` command using the `travel_time` function. The user inputs the ship name to select if from the SpaceShips dictionary, and you need to know the destination of the voyage. To make it more user friendly you could implement the posibility to list available ships if the user inputs a `?` and of course output the result in scientific notation since the output is in seconds:

```python
                elif command == "Travel":
                    ship_name = input("Ship name > ")
                    planet_destination = input("Select Second planet> ")
                    if ship_name == "?":
                        print(SpaceShips.keys())
                        ship_name = input("Ship ?")
                    print(format(
                            travel_time(ship_name, planet, planet_destination)
                        , ".5e")
                    )
```

You implemented the command in the `commands` tuple and added a comparison clause of the command inside the main loop. The user is requested for the `ship_name` and the destination planet. This implements the basic functionality for traveling space.

### Calling Home from Each Planet: Calculating the time delay to Earth from a planet

Electrical radio transmissions in space travel at the [speed of light](https://www.youtube.com/watch?v=9eyFDBPk4Yw), so you could by now calculate the delay of sending a message from any planet you have in the simulator. The delay can be calculated by the distance divided by the speed. To implement this calculation you need to make a function to divide the distance by the speed of light. You have already created the `calculate_distance` function so use this for the calculation of distance. The speed of the transmission is the speed of light, and this needs to be converted to the same units. To do this you can use the `convert_ms_to_kms` function with the **speed of light** as the input and then divide the distance with the speed of light in km/s:

```python
def calculate_transmission_delay(planet) -> decimal.Decimal:
    """ Calculates the time delay in seconds for a transmission from a planet to Earth"""
    distance = calculate_distance(distances.get("Earth", 1), distances.get(planet, 0))
    speed = convert_ms_to_kms(speed_of_light)
    return distance / speed
```

Now you have implemented the calculation of the transmission delay to the planet you could implement the command `Calculate Delay` to the `commands` tuple and then add the command comparison to `Calculate Delay` under the available main loop. This command is almost the same as the calculation for the travel time but uses the **speed of light** instead of the speed of a vessel, so the only user input is the planet name:

```python
def main():
    #...
                elif command == "Calculate Delay":
                    print(calculate_transmission_delay(planet))
```

By now you have an implementation of an actual shuttle, and the if the speed was using the theoretical possible speed of light. The speed of light is particularly useful for the calculations of the transmission delays as you have shown here.

### Warp 5, Engage: Implementing Warp Speed With Scientific notation

So you may or may not have heard of the different ships in Star Trek, but a particular ship was named the starship **USS Enterprise**, or **Enterprise** for short. This ship was capable of traveling at speeds faster than light, known as warp speed. The speed of warp is divided into different warp factors and Enterprise was capable of sustaining a speed of warp 5. This speed was [213 times](https://en.wikipedia.org/wiki/Warp_drive#Warp_velocities) faster than the speed of light. This would be significantly faster than traveling at the speed of the shuttle you already implemented.

You will implement a second ship in the `SpaceShips` and make it available for the user. The speed of the ship must be implememted in kilometer pr second to match the unit conventions of the calculations already implemented. You already have a function to calculate the speed conversion to kilometer per second available and the **speed of light**. Let's modify the `SpaceShips` dictionary:

```python
SpaceShips = {
    "Shuttle": {"speed_kms":11.19},
    "Enterprise":{
        "speed_kms": 213 * convert_ms_to_kms(speed_of_light),
        "maximum_warp_factor": 5}
    }
```

{% alert %}
**Note:** If your code complains about not being able to find the `convert_ms_to_kms` function move the definition of the function above the definition of the SpaceShips dictionary.
{% endalert %}

To add the **Enterprise** to the `SpaceShips` dictionary you just need to add a key with the name `"Enterprise"` and a dictionary with the key `"speed_kms"` equal to 213 times the speed of light converted to kilometers per second.

## Conclusion

By now you have built a small space simulator to learn how to simulate traveling distances and perform calculations using the scientific notation in Python. You have performed calculations on both large and small numbers in comparison and avoided numerical errors using the built-in `decimal` module from the Python standard library.

Additionally, you have learned the following through this tutorial:

* The basics of scientific notation and how to apply this in Python
* Why Python scientific notation is a useful tool for input and presentation
* The difference between float and decimal representation in memory
* The `Decimal` module and why it is important to consider using it
* Understand Pythons usage and caveats of the scientific notation
* Understand how to simplify the conversion of physical properties in Python
* Identify numerical problems, before combining large and small numbers in mathematical equations in Python

Some of the problems you came across when representing values in floating-point numbers are directly transferable to other calculations using Python. You should always consider how important the representation of the numbers you are working with is, and how numerical value changes will affect your calculations. This concludes the tutorial on scientific notation, but if you have further questions feel free to reach out in the comments section below.
