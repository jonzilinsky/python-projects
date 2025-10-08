import sys

halp = """\nUsed as 'python ./converter.py number-value unit'
        'python ./converter.py 32 f' #Converts 32 degrees Fahrenheit
        'python ./converter.py 42 ly' #Converts 42 Light Year

        Distance and Length:
        Millimeters = mm
        Centimeters = cm
        Inches = in
        Feet = ft
        Yards = yd
        Meters = m
        Kilometers = km
        Miles = mi
        Nautical Miles = nmi
        Astronomical Units = au
        Lightyears = ly
        Parsecs = pc

        Mass:
        Milligrams = mg
        Grams = g
        Kilograms = kg
        Ounces = oz
        Pounds = lb
        Short Tons = st
        Long Tons = lt
        Metric Tons = mt

        Temperature:
        Celsius = c
        Fahrenheit = f
        Kelvin = k

        Volume:
        Milliliters = ml
        Teaspoons = tsp
        Tablespoons = tbsp
        Cubicinches = in3
        Fluidounces = floz
        Shots = sh
        Cups = cu
        Pints = pt
        Fifths = fif
        Quarts = qt
        Liters = l
        Gallons = gal
        Cubic Feet = ft3
        Cubic Meters = m3
        """
#Mass
def milligrams(mg):
  conversions = {
    "Grams": (mg / 1000, 4),
    "Kilograms": (mg / 1000000, 6),
    "Ounces": (mg * 0.00003527396, 10),
    "Pounds": (mg * 0.00000220462, 10),
    "Short Tons": (mg * 0.00000000110231, 15),
    "Long Tons": (mg * 0.00000000098421, 15),
    "Metric Tons": (mg / 1000000000, 10)
    }
  mainconvert(mg, "Milligram", conversions)

def grams(g):
  conversions = {
    "Milligrams": (g * 1000, 1),
    "Kilograms": (g /1000, 4),
    "Ounces": (g * 0.03527396195, 4),
    "Pounds": (g * 0.00220462262, 6),
    "Short Tons": (g * 0.00000110231, 10),
    "Long Tons": (g * 0.00000098421, 10),
    "Metric Tons": (g / 1000000, 7)
    }
  mainconvert(g, "Gram", conversions)

def kilograms(kg):
  conversions = {
    "Milligrams": (kg * 1000000, 1),
    "Grams": (kg * 1000, 1),
    "Ounces": (kg * 35.27396195, 2),
    "Pounds": (kg * 2.20462262, 2),
    "Short Tons": (kg * 0.00110231, 6),
    "Long Tons": (kg * 0.00098421, 6),
    "Metric Tons": (kg / 1000, 4)
    }
  mainconvert(kg, "Kilogram", conversions)

def ounces(oz):
  conversions = {
    "Milligrams": (oz * 28349.523125, 1),
    "Grams": (oz * 28.349523125, 1),
    "Kilograms": (oz / 35.27396195, 4),
    "Pounds": (oz / 16, 4),
    "Short Tons": (oz / 32000, 6),
    "Long Tons": (oz / 35840, 7),
    "Metric Tons": (oz / 35273.96195, 7)
    }
  mainconvert(oz, "Ounce", conversions)

def pounds(lb):
  conversions = {
    "Milligrams": (lb * 453592.37, 1),
    "Grams": (lb * 453.59237, 1),
    "Kilograms": (lb * 0.45359237, 4),
    "Ounces": (lb * 16, 4),
    "Short Tons": (lb / 2000, 6),
    "Long Tons": (lb / 2250, 7),
    "Metric Tons": (lb / 2204.62262, 7)
    }
  mainconvert(lb, "Pound", conversions)

def shorttons(st):
  conversions = {
    "Milligrams": (st * 907184740, 1),
    "Grams": (st * 907184.74, 1),
    "Kilograms": (st * 907.18474, 1),
    "Ounces": (st * 32000, 1),
    "Pounds": (st * 2000, 1),
    "Long Tons": (st * 0.892857, 4),
    "Metric Tons": (st / 1.10231, 4)
    }
  mainconvert(st, "Short Ton", conversions)

def longtons(lt):
  conversions = {
    "Milligrams": (lt * 1016046908.8, 1),
    "Grams": (lt * 1016046.9088, 1),
    "Kilograms": (lt * 1016.0469088, 1),
    "Ounces": (lt * 35840, 1),
    "Pounds": (lt * 2240, 1),
    "Short Tons": (lt * 1.12, 4),
    "Metric Tons": (lt / 0.98421, 4)
    }
  mainconvert(lt, "Long Ton", conversions)

def metrictons(mt):
  conversions = {
    "Milligrams": (mt * 1000000000, 1),
    "Grams": (mt * 1000000, 1),
    "Kilograms": (mt * 1000, 1),
    "Ounces": (mt * 35273.96195, 1),
    "Pounds": (mt * 2204.62262, 1),
    "Short Tons": (mt * 1.10231, 4),
    "Long Tons": (mt * 0.98421, 4)
    }
  mainconvert(mt, "Metric Ton", conversions)

#Temperature
def celsius(c):
  print(f"{c} Celsius is:")
  print(f"\t{round(((c * 9/5) + 32),4)} Farenheit")
  print(f"\t{round((c + 273.15),4)} Kelvin")

def fahrenheit(f):
  print(f"{f} Fahrenheit is:")
  print(f"\t{round((((f) - 32) * 5/9), 4)} Celsius")
  print(f"\t{round((((f) - 32) * 5/9 + 273.15), 4)} Kelvin")

def kelvin(k):
  print(f"{k} Kelvin is:")
  print(f"\t{k - 273.15} Celsius")
  print(f"\t{round((((k) - 273.15) * 9/5 + 32), 4)} Fahrenheit")

#Distance
def millimeters(mm):
  conversions = {
    "Centimeters": (mm / 10, 2),
    "Inches": (mm / 25.4, 4),
    "Feet": (mm / 304.8,4),
    "Yards": (mm / 914.4, 4),
    "Meters": (mm / 1000, 4),
    "Kilometers": (mm / 1000000, 6),
    "Miles": (mm / 1609344, 10),
    "Nautical Miles": (mm / 1852000, 10),
    "Astronomical Units": (mm / 149597870700000, 15),
    "Light Years": (mm / 9460730472580800000, 20),
    "Parsecs": (mm / 30856775814913673000, 20)
    }
  mainconvert(mm, "Millimeter", conversions)

def centimeters(cm):
  conversions = {
    "Millimeters": (cm * 10, 4),
    "Inches": (cm / 2.54, 4),
    "Feet": (cm / 30.48,4),
    "Yards": (cm / 91.44, 4),
    "Meters": (cm / 100, 4),
    "Kilometers": (cm / 100000, 6),
    "Miles": (cm / 160900, 10),
    "Nautical Miles": (cm / 185200, 10),
    "Astronomical Units": (cm / 14959787070000, 15),
    "Light Years": (cm / 946073047258080000, 20),
    "Parsecs": (cm / 3085677581491367300, 20)
    }
  mainconvert(cm, "Centimeter", conversions)

def inches(i):
  conversions = {
    "Millimeters": (i * 25.4, 4),
    "Centimeters": (i * 2.54, 4),
    "Feet": (i / 12, 6),
    "Yards": (i / 36, 4),
    "Meters": (i / 39.37007874015748031496, 6),
    "Kilometers": (i / 39370.07874015748031496, 6),
    "Miles": (i / 63360, 4),
    "Nautical Miles": (i / 72913.38582677165354331, 4),
    "Astronomical Units": (i / 5878625373183.61, 15),
    "Light Years":(i / 372461748160000000000, 25),
    "Parsecs": (i / 1215000000000000000, 25)
    }
  mainconvert(i, "Inche", conversions)

def feet(f):
  conversions = {
    "Millimeters": (f * 304.8, 4),
    "Centimeters": (f * 30.48, 4),
    "Inches": (f * 12, 6),
    "Yards": (f / 3, 4),
    "Meters": (f * 0.3048, 4),
    "Kilometers": (f * 0.0003048, 4),
    "Miles": (f / 5280, 4),
    "Nautical Miles": (f / 6076.12, 4),
    "Astronomical Units": ((f * 0.3048)/ 149597870700, 15),
    "Light Years":((f * 0.3048) / 9460730472580800, 20),
    "Parsecs": ((f * 0.3048) / 30856775814913673, 20)
    }
  mainconvert(f, "Feet", conversions)

def yards(y):
  conversions = {
    "Millimeters": (y * 914.4, 1),
    "Centimeters": (y * 91.44, 1),
    "Inches": (y * 36, 1),
    "Feet": (y * 3, 2),
    "Meters": (y * 0.9144, 4),
    "Kilometers": (y * 0.0009144, 4),
    "Miles": (y / 1760, 4),
    "Nautical Miles": (y / 2025.37, 4),
    "Astronomical Units": (y / 163602220839, 20),
    "Light Years":(y / 10346303587051600, 20),
    "Parsecs": (y / 33745380375014952, 20)
    }
  mainconvert(y, "Yard", conversions)

def meters(m):
  conversions = {
    "Millimeters": (m * 1000, 1),
    "Centimeters": (m * 100, 1),
    "Inches": (m / 0.0254, 1),
    "Feet": (m / 0.3048, 2),
    "Yards": (m / 0.9144, 4),
    "Kilometers": (m / 1000, 4),
    "Miles": (m / 1609.344, 4),
    "Nautical Miles": (m / 1852, 4),
    "Astronomical Units": (m / 149597870700, 20),
    "Light Years":(m / 9460730472580800, 20),
    "Parsecs": (m / 30856775814913673, 20)
    }
  mainconvert(m, "Meter", conversions)

def kilometers(k):
  conversions = {
    "Millimeters": (k * 1000000, 1),
    "Centimeters": (k * 100000, 1),
    "Inches": (k * 39370.07874015748, 1),
    "Feet": (k * 3280.839895013123, 1),
    "Yards": (k * 1093.6132983377078, 2),
    "Meters": (k * 1000, 2),
    "Miles": (k / 1.609344, 4),
    "Nautical Miles": (k / 1.852, 4),
    "Astronomical Units": (k / 149597870.7, 20),
    "Light Years":(k / 9460730472580.8, 20),
    "Parsecs": (k / 30856775814913.673, 20)
    }
  mainconvert(k, "Kilometer", conversions)

def miles(m):
  conversions = {
    "Millimeters": (m * 1609344, 1),
    "Centimeters": (m * 160934.4, 1),
    "Inches": (m * 63360, 1),
    "Feet": (m * 5280, 1),
    "Yards": (m * 1760, 2),
    "Meters": (m * 1609.344, 2),
    "Kilometers": (m * 1.609344, 4),
    "Nautical Miles": (m / 1.15078, 4),
    "Astronomical Units": (m / 92955807.26743, 20),
    "Light Years":(m / 5878625373183.6, 20),
    "Parsecs": (m / 19025358738649.6, 20)
    }
  mainconvert(m, "Mile", conversions)

def nautmiles(n):
  conversions = {
    "Millimeters": (n * 1852000, 1),
    "Centimeters": (n * 185200, 1),
    "Inches": (n * 72913.38582677165, 1),
    "Feet": (n * 6076.115485564304, 1),
    "Yards": (n * 2025.3718285214345, 2),
    "Meters": (n * 1852, 2),
    "Kilometers": (n * 1.852, 4),
    "Miles": (n * 1.15078, 4),
    "Astronomical Units": (n / 80655432.552296, 20),
    "Light Years":(n / 5108385789558.6, 20),
    "Parsecs": (n / 16591863067473.8, 20)
    }
  mainconvert(n, "Nautical Mile", conversions)

def astrounits(au):
  conversions = {
    "Millimeters": (au * 149597870700000, 1),
    "Centimeters": (au * 14959787070000, 1),
    "Inches": (au * 5889026870611.57, 1),
    "Feet": (au * 490752239217.63, 1),
    "Yards": (au * 163584079739.21, 1),
    "Meters": (au * 149597870700, 1),
    "Kilometers": (au * 149597870.7, 1),
    "Miles": (au * 92955807.26743, 1),
    "Nautical Miles": (au * 80776397.17554, 1),
    "Light Years":(au / 63241.077, 5),
    "Parsecs": (au / 206264.806, 5)
    }
  mainconvert(au, "Astronomical Unit", conversions)

def lightyears(ly):
  conversions = {
    "Millimeters": (ly * 9460730472580800000, 1),
    "Centimeters": (ly * 946073047258080000, 1),
    "Inches": (ly * 372469703644528000, 1),
    "Feet": (ly * 31039141970377300, 1),
    "Yards": (ly * 10346380656792400, 1),
    "Meters": (ly * 9460730472580800, 1),
    "Kilometers": (ly * 9460730472580.8, 1),
    "Miles": (ly * 5878625373183.6, 1),
    "Nautical Miles": (ly * 5108385789558.6, 1),
    "Astronomical Units": (ly * 63241.077, 2),
    "Parsecs": (ly / 3.26156, 5)
    }
  mainconvert(ly, "Light Year", conversions)

def parsecs(p):
  conversions = {
    "Millimeters": (p * 30856775814913673000, 1),
    "Centimeters": (p * 3085677581491367300, 1),
    "Inches": (p * 1213610476143818900, 1),
    "Feet": (p * 101134206345318240, 1),
    "Yards": (p * 33711402115106080, 1),
    "Meters": (p * 30856775814913673, 1),
    "Kilometers": (p * 30856775814913.673, 1),
    "Miles": (p * 19173572297532.2, 1),
    "Nautical Miles": (p * 16661310215138.3, 1),
    "Astronomical Units": (p * 206264.806, 1),
    "Light Years": (p * 3.26156, 1)
    }
  mainconvert(p, "Parsec", conversions)

#volume
def milliliters(ml):
  conversions = {
    "Teaspoons": (ml / 4.92892, 4),
    "Tablespoons": (ml / 14.7868, 4),
    "Cubic Inches": (ml / 16.3871, 4),
    "Fluid Ounces": (ml / 29.5735, 4),
    "Shots": (ml / 44.36, 4),
    "Cups": (ml / 236.588, 4),
    "Pints": (ml / 473.176, 4),
    "Fifths": (ml / 757.082, 4),
    "Quarts": (ml / 946.353, 4),
    "Liters": (ml / 1000, 4),
    "Gallons": (ml / 3785.41, 6),
    "Cubic Feet": (ml / 28316.8, 6),
    "Cubic Meters": (ml / 1000000, 8),
    }
  mainconvert(ml, "milliter", conversions)

def teaspoons(tsp):
  conversions = {
    "Milliliters": (tsp / 4.92892, 4),
    "Tablespoons": (tsp / 3, 4),
    "Cubic Inches": (tsp / 0.30078, 4),
    "Fluid Ounces": (tsp / 6, 4),
    "Shots": (tsp / 9.857, 4),
    "Cups": (tsp / 48, 4),
    "Pints": (tsp / 96, 4),
    "Fifths": (tsp / 153.6, 4),
    "Quarts": (tsp / 192, 4),
    "Liters": (tsp / 202.884, 4),
    "Gallons": (tsp / 768, 6),
    "Cubic Feet": (tsp / 5745, 6),
    "Cubic Meters": (tsp / 202884, 8),
    }
  mainconvert(tsp, "Teaspoon", conversions)

def tablespoons(tbsp):
  conversions = {
    "Milliliters": (tbsp * 14.7868, 1),
    "Teaspoons": (tbsp * 3, 1),
    "Cubic Inches": (tbsp / 0.1026, 2),
    "Fluid Ounces": (tbsp / 2, 2),
    "Shots": (tbsp / 3.286, 4),
    "Cups": (tbsp / 16, 4),
    "Pints": (tbsp / 32, 4),
    "Fifths": (tbsp / 51.2, 4),
    "Quarts": (tbsp / 64, 4),
    "Liters": (tbsp / 67.628, 4),
    "Gallons": (tbsp / 256, 6),
    "Cubic Feet": (tbsp / 1915, 6),
    "Cubic Meters": (tbsp / 67628, 8),
    }
  mainconvert(tbsp, "Tablespoon", conversions)

def cubicinches(in3):
  conversions = {
    "Milliliters": (in3 * 16.3871, 1),
    "Teaspoons": (in3 * 3.32468, 1),
    "Tablespoons": (in3 * 1.10823, 2),
    "Fluid Ounces": (in3 * 0.554113, 2),
    "Shots": (in3 / 1.974, 4),
    "Cups": (in3 / 14.438, 4),
    "Pints": (in3 / 28.875, 4),
    "Fifths": (in3 / 305.6, 4),
    "Quarts": (in3 / 57.75, 4),
    "Liters": (in3 / 61.0237, 4),
    "Gallons": (in3 / 231, 6),
    "Cubic Feet": (in3 / 1728, 6),
    "Cubic Meters": (in3 / 61023.7, 8),
    }
  mainconvert(in3, "Cubic Inch", conversions)

def fluidounces(floz):
  conversions = {
    "Milliliters": (floz * 29.5735, 1),
    "Teaspoons": (floz * 6, 1),
    "Tablespoons": (floz * 2, 2),
    "Cubic Inches": (floz * 1.80469, 2),
    "Shots": (floz / 1.5, 4),
    "Cups": (floz / 8, 4),
    "Pints": (floz / 16, 4),
    "Fifths": (floz / 25.6, 4),
    "Quarts": (floz / 32, 4),
    "Liters": (floz / 33.814, 4),
    "Gallons": (floz / 128, 6),
    "Cubic Feet": (floz / 957.5, 6),
    "Cubic Meters": (floz / 33814, 8),
    }
  mainconvert(floz, "Fluid Ounce", conversions)

def shots(sh):
  conversions = {
    "Milliliters": (sh * 44.36, 1),
    "Teaspoons": (sh * 9.857, 1),
    "Tablespoons": (sh * 3.286, 2),
    "Cubic Inches": (sh * 1.974, 2),
    "Fluid Ounces": (sh * 1.5, 2),
    "Cups": (sh / 1.974, 4),
    "Pints": (sh / 3.943, 4),
    "Fifths": (sh / 25, 4),
    "Quarts": (sh / 7.887, 4),
    "Liters": (sh / 22.5427, 4),
    "Gallons": (sh / 31.507, 6),
    "Cubic Feet": (sh / 64.031, 6),
    "Cubic Meters": (sh / 22542.7, 8),
    }
  mainconvert(sh, "Shot", conversions)

def cups(cu):
  conversions = {
    "Milliliters": (cu * 236.588, 1),
    "Teaspoons": (cu * 48, 1),
    "Tablespoons": (cu * 16, 2),
    "Cubic Inches": (cu * 14.438, 2),
    "Fluid Ounces": (cu * 8, 2),
    "Shots": (cu * 1.971, 4),
    "Pints": (cu / 2, 4),
    "Fifths": (cu * 6.667, 4),
    "Quarts": (cu / 4, 4),
    "Liters": (cu / 4.22675, 4),
    "Gallons": (cu / 16, 6),
    "Cubic Feet": (cu / 117.987, 6),
    "Cubic Meters": (cu / 4226.75, 8),
    }
  mainconvert(cu, "Cup", conversions)

def pints(pt):
  conversions = {
    "Milliliters": (pt * 473.176, 1),
    "Teaspoons": (pt * 96, 1),
    "Tablespoons": (pt * 32, 1),
    "Cubic Inches": (pt * 28.875, 1),
    "Fluid Ounces": (pt * 16, 1),
    "Shots": (pt * 3.943, 1),
    "Cups": (pt * 2, 1),
    "Fifths": (pt / 3.333, 2),
    "Quarts": (pt / 2, 2),
    "Liters": (pt / 2.11338, 2),
    "Gallons": (pt / 8, 4),
    "Cubic Feet": (pt / 59.844, 6),
    "Cubic Meters": (pt / 2113.38, 8),
    }
  mainconvert(pt, "Pint", conversions)

def fifths(fif):
  conversions = {
    "Milliliters": (fif * 757.082, 1),
    "Teaspoons": (fif * 153.6, 1),
    "Tablespoons": (fif * 51.2, 1),
    "Cubic Inches": (fif * 305.6, 1),
    "Fluid Ounces": (fif * 25.6, 1),
    "Shots": (fif * 25, 1),
    "Cups": (fif * 6.667, 1),
    "Pints": (fif * 3.333, 2),
    "Quarts": (fif * 1.667, 2),
    "Liters": (fif * 0.757082, 2),
    "Gallons": (fif / 5, 2),
    "Cubic Feet": (fif / 10.333, 6),
    "Cubic Meters": (fif / 1320.86, 8),
    }
  mainconvert(fif, "Fifth", conversions)

def quarts(qt):
  conversions = {
    "Milliliters": (qt * 946.353, 1),
    "Teaspoons": (qt * 192, 1),
    "Tablespoons": (qt * 64, 1),
    "Cubic Inches": (qt * 57.75, 1),
    "Fluid Ounces": (qt * 32, 1),
    "Shots": (qt * 7.887, 1),
    "Cups": (qt * 4, 1),
    "Pints": (qt * 2, 2),
    "Fifths": (qt * 1.25, 2),
    "Liters": (qt / 1.05669, 2),
    "Gallons": (qt / 4, 2),
    "Cubic Feet": (qt / 29.922, 4),
    "Cubic Meters": (qt / 1056.69, 6),
    }
  mainconvert(qt, "Quart", conversions)

def liters(l):
  conversions = {
    "Milliliters": (l * 1000, 1),
    "Teaspoons": (l * 202.884, 1),
    "Tablespoons": (l * 67.628, 1),
    "Cubic Inches": (l * 61.0237, 1),
    "Fluid Ounces": (l * 33.814, 1),
    "Shots": (l * 22.5427, 1),
    "Cups": (l * 4.22675, 1),
    "Pints": (l * 2.11338, 2),
    "Fifths": (l / 0.757082, 2),
    "Quarts": (l * 1.05669, 2),
    "Gallons": (l / 3.78541, 2),
    "Cubic Feet": (l / 28.3168, 4),
    "Cubic Meters": (l / 1000, 4),
    }
  mainconvert(l, "Liter", conversions)

def gallons(gal):
  conversions = {
    "Milliliters": (gal * 3785.41, 1),
    "Teaspoons": (gal * 768, 1),
    "Tablespoons": (gal * 256, 1),
    "Cubic Inches": (gal * 231, 1),
    "Fluid Ounces": (gal * 128, 1),
    "Shots": (gal * 31.507, 1),
    "Cups": (gal * 16, 1),
    "Pints": (gal * 8, 2),
    "Fifths": (gal * 5, 2),
    "Quarts": (gal * 4, 2),
    "Liters": (gal * 3.78541, 2),
    "Cubic Feet": (gal / 7.481, 4),
    "Cubic Meters": (gal / 264.172, 4),
    }
  mainconvert(gal, "Gallon", conversions)

def cubicfeet(ft3):
  conversions = {
    "Milliliters": (ft3 * 28316.8, 1),
    "Teaspoons": (ft3 * 5745.04, 1),
    "Tablespoons": (ft3 * 1915.01, 1),
    "Cubic Inches": (ft3 * 1728, 1),
    "Fluid Ounces": (ft3 * 957.506, 1),
    "Shots": (ft3 * 64.031, 1),
    "Cups": (ft3 * 117.987, 1),
    "Pints": (ft3 * 59.844, 2),
    "Fifths": (ft3 * 10.333, 2),
    "Quarts": (ft3 * 29.922, 2),
    "Liters": (ft3 * 28.3168, 2),
    "Gallons": (ft3 * 7.481, 4),
    "Cubic Meters": (ft3 / 35.3147, 4),
    }
  mainconvert(ft3, "Cubic Feet", conversions)

def cubicmeters(m3):
  conversions = {
    "Milliliters": (m3 * 1000000, 1),
    "Teaspoons": (m3 * 202884, 1),
    "Tablespoons": (m3 * 67628, 1),
    "Cubic Inches": (m3 * 61023.7, 1),
    "Fluid Ounces": (m3 * 33814, 1),
    "Shots": (m3 * 22542.7, 1),
    "Cups": (m3 * 4226.75, 1),
    "Pints": (m3 * 2113.38, 1),
    "Fifths": (m3 * 1320.86, 1),
    "Quarts": (m3 * 1056.69, 1),
    "Liters": (m3 * 1000, 2),
    "Gallons": (m3 * 264.172, 1),
    "Cubic Feet": (m3 * 35.3147, 2),
    }
  mainconvert(m3, "Cubic Meter", conversions)

def mainconvert(uservalue, userunit, conversions):
  if uservalue == 1 and userunit == "Feet":
    print(f"{uservalue} Foot is:")
  elif uservalue == 1:
    print(f"{uservalue} {userunit} is:")
  elif uservalue != 1 and userunit == "Feet":
    print(f"{uservalue} Feet is:")
  else:
    print(f"{uservalue} {userunit}s is:")
  for units, (values, decimals) in conversions.items():
      print(f"\t{values:,.{decimals}f} {units}")

functions = {
  "c":celsius, #temp
  "f":fahrenheit,
  "k":kelvin,
  "mm":millimeters, #distance
  "cm":centimeters,
  "in":inches,
  "ft":feet,
  "yd":yards,
  "m":meters,
  "km":kilometers,
  "mi":miles,
  "nmi":nautmiles,
  "au":astrounits,
  "ly":lightyears,
  "pc":parsecs,
  "mg":milligrams, #mass
  "g":grams,
  "kg":kilograms,
  "oz":ounces,
  "lb":pounds,
  "st":shorttons,
  "lt":longtons,
  "mt":metrictons,
  "ml":milliliters, #volume
  "tsp":teaspoons,
  "tbsp":tablespoons,
  "in3":cubicinches,
  "floz":fluidounces,
  "sh":shots,
  "cu":cups,
  "pt":pints,
  "fif":fifths,
  "qt":quarts,
  "l":liters,
  "gal":gallons,
  "ft3":cubicfeet,
  "m3":cubicmeters,
  }

try:
  if sys.argv[1] == "-h" or sys.argv[1] == "h":
    print(halp)
  else:
    toConvert = float(sys.argv[1])
    oppChoice = str(sys.argv[2].lower())
    functions[oppChoice](toConvert)
except Exception as e:
  print(f"Error: {e} \nUse -h for help")
