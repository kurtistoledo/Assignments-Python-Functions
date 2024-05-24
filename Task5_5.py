# Lesson 5: Python Functions
# 5. The Fitness Tracker

def log_fitness_activities(activities, duration):
    activity_log = dict(zip(activities, duration))
    return activity_log

def estimate_calories_burned(activity, duration):
    calories_per_minute = 3.5
    total_calories = duration * calories_per_minute
    return total_calories

def generate_summary_report(activity_log):
    total_calories_burned = sum(activity_log.values())
    print("Fitness Summary Report:")
    for activity, duration in activity_log.items():
        print(f"{activity}: {duration} minutes")
    print(f"Total calories burned: {total_calories_burned:.2f} calories")

# Example usage
activities = ["Dancing", "Swimming", "Biking"]
duration = [10, 20, 15]

activity_log = log_fitness_activities(activities, duration)
generate_summary_report(activity_log)
