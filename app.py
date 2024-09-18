from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Function to calculate BMI based on weight (kg) and height (cm)
def calculate_bmi(weight, height):
    height_m = height / 100  # convert height to meters
    return weight / (height_m ** 2)

# Function to calculate BMR based on weight, height, age, and gender
def calculate_bmr(weight, height, age, gender):
    if gender == 'male':
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

# Function to calculate caloric needs and daily water intake based on BMR, activity, and goal intensity
def calculate_caloric_needs(bmr, activity_level, goal_value, weight):
    activity_multipliers = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very_active': 1.9
    }

    caloric_needs = bmr * activity_multipliers[activity_level]

    # Adjust caloric intake based on goal intensity from the slider
    if goal_value == '0':
        caloric_needs -= 750  # Aggressive weight loss
    elif goal_value == '1':
        caloric_needs -= 250  # Slow weight loss
    elif goal_value == '3':
        caloric_needs += 250  # Slow weight gain
    elif goal_value == '4':
        caloric_needs += 500  # Aggressive weight gain

    # Calculate daily water intake recommendation (in liters)
    daily_water_intake = weight * 0.033  # 33 ml per kg of body weight

    return round(caloric_needs), round(daily_water_intake, 1)

# Function to split daily calorie intake into meals
def split_calories_by_meal(calories):
    breakfast = round(calories * 0.25)  # 25% of daily intake for breakfast
    lunch = round(calories * 0.35)      # 35% for lunch
    dinner = round(calories * 0.3)      # 30% for dinner
    snacks = round(calories * 0.1)      # 10% for snacks
    return breakfast, lunch, dinner, snacks

# List of fitness tips
fitness_tips = [
    "Stay consistent with your workouts for better results.",
    "Incorporate strength training to build muscle and boost metabolism.",
    "Hydrate regularly, especially before and after exercising.",
    "Focus on whole foods like vegetables, fruits, and lean proteins.",
    "Set realistic, small goals to stay motivated.",
    "Get enough sleep to allow your muscles to recover.",
    "Include a warm-up and cool-down in every workout.",
    "Monitor your progress, but don’t obsess over the scale."
]

@app.route('/')
def index():
    random_tip = random.choice(fitness_tips)
    return render_template('index.html', fitness_tip=random_tip)

@app.route('/result', methods=['POST'])
def result():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    age = int(request.form['age'])
    gender = request.form['gender']
    activity_level = request.form['activity_level']
    goal_value = request.form['goal_value']

    # Calculate BMI, BMR, caloric needs, and daily water intake
    bmi = round(calculate_bmi(weight, height), 2)
    bmr = calculate_bmr(weight, height, age, gender)
    caloric_needs, water_intake = calculate_caloric_needs(bmr, activity_level, goal_value, weight)

    # Split daily calories into meals
    breakfast, lunch, dinner, snacks = split_calories_by_meal(caloric_needs)

    return render_template('result.html', bmi=bmi, caloric_needs=caloric_needs, water_intake=water_intake, breakfast=breakfast, lunch=lunch, dinner=dinner, snacks=snacks)

if __name__ == '__main__':
    app.run(debug=True)
