"""
Day 14 - 2026-10-20
Tool: Water Intake Calculator
What it does: Estimates how much water a person should drink per day
from their body weight and activity level, and shows it in litres,
millilitres and glasses - a simple daily health reminder anyone can use.
Who it helps: Anyone trying to stay hydrated, especially people working
outdoors in the heat, students, and athletes. It is a general guide,
not medical advice.
"""

ML_PER_KG = 35          # common rule of thumb per kg of body weight
ML_PER_GLASS = 250      # a standard glass of water
ACTIVITY_EXTRA_ML = {   # extra water for exercise that day
    "none": 0,
    "light": 350,       # about 30 minutes of activity
    "moderate": 700,    # about 1 hour
    "heavy": 1050,      # 90 minutes or more / outdoor labour
}


def daily_water_ml(weight_kg, activity="none"):
    """Recommended daily water in millilitres."""
    if weight_kg <= 0:
        raise ValueError("Weight must be more than zero.")
    if activity not in ACTIVITY_EXTRA_ML:
        raise ValueError("Activity must be one of: " + ", ".join(ACTIVITY_EXTRA_ML))
    return int(weight_kg * ML_PER_KG) + ACTIVITY_EXTRA_ML[activity]


def to_litres(ml):
    return round(ml / 1000, 2)


def to_glasses(ml):
    return round(ml / ML_PER_GLASS, 1)


if __name__ == "__main__":
    # Example 1: a 60 kg office worker with no extra exercise
    ml = daily_water_ml(60, "none")
    print("60 kg, no exercise:", ml, "ml =", to_litres(ml), "litres =",
          to_glasses(ml), "glasses")

    # Example 2: a 75 kg rickshaw puller doing heavy outdoor work
    ml = daily_water_ml(75, "heavy")
    print("75 kg, heavy outdoor work:", ml, "ml =", to_litres(ml),
          "litres =", to_glasses(ml), "glasses")

    # Example 3: a 50 kg student with light evening exercise
    ml = daily_water_ml(50, "light")
    print("50 kg, light exercise:", ml, "ml =", to_litres(ml),
          "litres =", to_glasses(ml), "glasses")
