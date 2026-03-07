def get_season_advice(season):
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


def main():
    season = "summer"      # still hardcoded for now (Issue 2 will fix this)
    plant_type = "flower"  # still hardcoded for now

    advice = ""
    advice += get_season_advice(season)
    advice += get_plant_advice(plant_type)

    print(advice)


main()
