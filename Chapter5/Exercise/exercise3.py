def turn_camera_on():
    print("Turn camera on!")


light = 0.00
temperature = 32.4

# Check whether the light level is less than 0.01
# and temperature is above freezing.
if (light < 0.01) or (temperature > 0.0):
    turn_camera_on()
