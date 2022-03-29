"""
© https://sudipghimire.com.np

Create 3 different classes Length, Weight, and Time

Add respective attributes to store values.
Add static methods for conversion of different units.

Example:
Length: cm to inches, kilometer to miles, etc
Weight: KG to pounds, gram to Ounces, etc.
Time: seconds to hours, milliseconds to seconds

"""

# answer

class Length:

    @staticmethod
    def meter_to_feet(meter: float):
        return meter * 3.28084

    @staticmethod
    def feet_to_meter(feet: float):
        return feet / 3.28084

class Weight:

    @staticmethod
    def kg_to_pound(kg: float):
        return kg * 2.20462

    @staticmethod
    def pound_to_kg(pound: float):
        return pound / 2.20462

class Time:
    @staticmethod
    def second_to_hour(second: float):
        return second/3600

    @staticmethod
    def hour_to_second(hour: float):
        return hour *3600


# tests
print(Length.feet_to_meter(5.9))
print(Weight.kg_to_pound(5.9))
print(Time.second_to_hour(7200))
