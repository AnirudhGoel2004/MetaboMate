document.addEventListener("DOMContentLoaded", function () {
  // Slider for goal settings
  const goalSlider = document.getElementById("goal-slider");
  const goalLabel = document.getElementById("goal-label");

  goalSlider.addEventListener("input", function () {
    const value = goalSlider.value;
    if (value == 0) {
      goalLabel.textContent = "Lose Weight Aggressively";
    } else if (value == 1) {
      goalLabel.textContent = "Lose Weight Slowly";
    } else if (value == 2) {
      goalLabel.textContent = "Maintain Weight";
    } else if (value == 3) {
      goalLabel.textContent = "Gain Weight Slowly";
    } else {
      goalLabel.textContent = "Gain Weight Aggressively";
    }
  });
});
