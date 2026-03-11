def get_season_advice(season):
    season_advice = {
        "summer": "Water your plants regularly and provide some shade.\n",
        "winter": "Protect your plants from frost with covers.\n"
    }
    return season_advice.get(season, "No advice for this season.\n")


def get_plant_advice(plant_type):
    plant_advice = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!"
    }
    return plant_advice.get(plant_type, "No advice for this type of plant.")


def main():
    season = input("Enter the season (summer/winter): ").lower()
    plant_type = input("Enter the plant type (flower/vegetable): ").lower()

    advice = ""
    advice += get_season_advice(season)
    advice += get_plant_advice(plant_type)

    print("\nGardening Advice:")
    print(advice)


main()
