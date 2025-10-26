import pandas as pd   # For data storage and CSV export
import numpy as np    # For numerical calculations
import random         # For generating random test data
from datetime import datetime, timedelta

# Set random seeds to make results reproducible (same output each run)
random.seed(42)
np.random.seed(42)

def simulate_driver_data(num_drivers=5, trips_per_driver=5):
    #Generate simulated driving data for multiple drivers and trips.

    all_trips = []

    # Loop through each driver
    for driver_id in range(1, num_drivers + 1):
         # Loop through each trip for that driver
        for trip_id in range(1, trips_per_driver + 1):
            # Random trip start within the past 30 days
            start_time = datetime.now() - timedelta(days=random.randint(0, 30))
            trip_length_min = random.randint(5, 60)      # Trip length (minutes)
            end_time = start_time + timedelta(minutes=trip_length_min)
            
          # Randomized driving metrics
            avg_speed = random.uniform(30, 70)  # Average speed (mph)
            max_speed = avg_speed + random.uniform(5, 25) # Max speed higher than average

            harsh_brakes = random.randint(0, 5)  # Number of hard braking events
            night_drive = random.choice([0, 1])  # 1 if trip occurred at night
            distance = avg_speed * (trip_length_min / 60)
 
             # Store trip details in dictionary
            all_trips.append({
                "driver_id": f"D{driver_id:03}",
                "trip_id": f"T{trip_id:03}_D{driver_id:03}",
                "start_time": start_time,
                "end_time": end_time,
                "avg_speed": avg_speed,
                "max_speed": max_speed,
                "harsh_brakes": harsh_brakes,
                "night_drive": night_drive,
                "distance_miles": round(distance, 2)
            })

     # Convert all trips to DataFrame and save to CSV
    df = pd.DataFrame(all_trips)
    df.to_csv("data/trips.csv", index=False)
    print(f"✅ Simulated {len(df)} trips saved to data/trips.csv")

if __name__ == "__main__":
    simulate_driver_data()