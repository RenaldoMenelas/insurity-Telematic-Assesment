from pydantic import BaseModel # BaseModel checks that the data we send or receive has the right fields and data types.


# Defines and validates the input structure for driver data in the /predict endpoint.
class DriverData(BaseModel):
    avg_speed: float
    harsh_brakes: int
    night_drive: bool
    distance_miles: float

# Defines and validates the output structure for the risk score and premium response.
class PredictionResponse(BaseModel):
    risk_score: float
    premium: float

# This is the raw telemetry item (like from a phone).
# For the POC we accept a list of these to /ingest.
class Telemetry(BaseModel):
    driver_id: str          # which driver this belongs to
    timestamp: float        # when the reading happened (epoch seconds)
    lat: float              # latitude (not used by the formula, kept for realism)
    lon: float              # longitude (not used by the formula, kept for realism)
    speed_mps: float        # speed in meters/second (phones/OBD often use this)
    accel_x: float          # acceleration on X axis (m/s^2)
    accel_y: float          # acceleration on Y axis (m/s^2)
    accel_z: float          # acceleration on Z axis (m/s^2)
