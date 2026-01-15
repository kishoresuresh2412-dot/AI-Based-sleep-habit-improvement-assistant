print("Smart AI-Based Sleep Habit Improvement Assistant\n")

# -------- Data Storage (Simple Memory) --------
sleep_history = []

days = 3
for day in range(1, days + 1):
    print(f"\nDay {day} Data:")
    sleep_hours = float(input("Hours slept: "))
    phone_use = input("Phone before sleep? (yes/no): ").lower()
    caffeine = input("Tea/Coffee after 6 PM? (yes/no): ").lower()
    feeling = input("Morning feeling (fresh/tired): ").lower()

    sleep_score = 0

    # -------- Sleep Scoring Agent --------
    if sleep_hours < 6:
        sleep_score += 4
    elif sleep_hours < 7:
        sleep_score += 3
    elif sleep_hours < 8:
        sleep_score += 1

    if phone_use == "yes":
        sleep_score += 2

    if caffeine == "yes":
        sleep_score += 1

    if feeling == "tired":
        sleep_score += 2

    sleep_history.append(sleep_score)

# -------- Trend Analysis Agent --------
average_score = sum(sleep_history) / days

print("\n--- AI Sleep Report ---")

if average_score >= 7:
    quality = "Poor"
elif average_score >= 4:
    quality = "Average"
else:
    quality = "Good"

print(f"Overall Sleep Quality: {quality}")
print(f"Average Sleep Score: {average_score:.1f}")

# Trend detection
if sleep_history[-1] < sleep_history[0]:
    trend = "Improving 📈"
elif sleep_history[-1] > sleep_history[0]:
    trend = "Worsening 📉"
else:
    trend = "Stable ➖"

print(f"Sleep Trend: {trend}")

# -------- Recommendation Agent --------
print("\nPersonalized Suggestions:")

if quality == "Poor":
    print("- Increase sleep duration to 7–8 hours")
    print("- Avoid phone usage before bedtime")
    print("- Reduce caffeine intake in evenings")
    print("- Maintain consistent sleep schedule")

elif quality == "Average":
    print("- Improve sleep consistency")
    print("- Reduce screen exposure at night")
    print("- Try relaxation before sleep")

else:
    print("- Maintain your healthy sleep routine")
    print("- Keep up good habits")
print("\nSDG Supported: SDG 3 – Good Health and Well-Being")
print("\nSDG Supported: SDG 3 – Good Health and Well-Being")
