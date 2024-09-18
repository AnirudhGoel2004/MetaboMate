# MetaboMate - Calorie & Fitness Tracker

MetaboMate is a user-friendly web application that helps users track their daily caloric needs and BMI based on their body measurements, activity levels, and fitness goals. It also provides meal breakdowns and daily water intake recommendations, making it easier to maintain a healthy lifestyle. 

The app includes a "Fitness Tip of the Day" feature for daily motivation and guidance.

## Features

### 1. **BMI and Caloric Need Calculation**
   - Based on user-provided data such as **weight**, **height**, **age**, **gender**, and **activity level**, the app calculates the **Basal Metabolic Rate (BMR)** and suggests daily caloric intake.
   - The app adjusts calories according to the user’s fitness goal (e.g., losing or gaining weight aggressively or slowly).

### 2. **Caloric Breakdown by Meal**
   - The daily calorie intake is split into breakfast, lunch, dinner, and snack suggestions:
     - **25%** for breakfast
     - **35%** for lunch
     - **30%** for dinner
     - **10%** for snacks

### 3. **Water Intake Recommendation**
   - A personalized daily **water intake suggestion** is calculated based on the user's weight (33 ml per kilogram).

### 4. **Goal Intensity Adjustment via Slider**
   - The app features an interactive slider that allows users to select the intensity of their fitness goal:
     - **Lose Weight Aggressively**
     - **Lose Weight Slowly**
     - **Maintain Weight**
     - **Gain Weight Slowly**
     - **Gain Weight Aggressively**

### 5. **Fitness Tip of the Day**
   - A randomly selected **fitness tip** is displayed on the main page to encourage healthy habits.

## Technologies Used

- **Python**: Core logic for calculating BMI, caloric needs, and water intake.
- **Flask**: Lightweight web framework for the backend.
- **HTML/CSS**: For the user interface and styling.
- **JavaScript**: Adds interactivity (e.g., goal slider functionality).
- **Jinja**: Templating engine for Flask to dynamically render data on HTML pages.

## Installation

To run the MetaboMate application locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/metabomate.git
2. **Install the required dependencies**:
   ```bash
   pip install Flask
3. **Run the application**:
   ```bash
   python3 app.py
4. Open your browser and go to http://localhost:5000 to access the app.
   
## Main Menu
<img width="1470" alt="Screenshot 2024-09-18 at 5 08 33 PM" src="https://github.com/user-attachments/assets/0f9a2510-1008-4fa7-85a5-8a0cc18af7ff">

## Results
<img width="418" alt="Screenshot 2024-09-18 at 5 08 40 PM" src="https://github.com/user-attachments/assets/49200074-114f-405f-8fed-e57eb0afd77d">

