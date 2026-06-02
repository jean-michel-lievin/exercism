"""
Given an age in seconds, calculate how old someone would be on a planet in our Solar System.
"""
class SpaceAge:
    """
    Class to compute orbital period in Earth Years:
    """
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_year = seconds / 31557600

    PLANETS_RATIOS = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1.0,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }

    def __getattr__(self, name):
        if name.startswith("on_"):
            planet = name.split("_")[1]
            if planet in self.PLANETS_RATIOS:
                return lambda: round(self.earth_year / self.PLANETS_RATIOS[planet], 2)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
    # def on_earth(self):
    #     return round(self.earth_year, 2)

    # def on_mercury(self):
    #     return round(self.earth_year / 0.2408467, 2)

    # def on_venus(self):
    #     return round(self.earth_year / 0.61519726, 2)

    # def on_mars(self):
    #     return round(self.earth_year / 1.8808158, 2)

    # def on_jupiter(self):
    #     return round(self.earth_year / 11.8808158, 2)

    # def on_saturn(self):
    #     return round(self.earth_year / 29.447498, 2) 

    # def on_uranus(self):
    #     return round(self.earth_year / 84.016846, 2) 

    # def on_neptune(self):
    #     return round(self.earth_year / 164.79132, 2) 