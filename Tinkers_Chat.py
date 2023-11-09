conversion_factors = {
    "length": {
        "meter": {
            "inch": 39.3701,
            "foot": 3.28084,
            "yard": 1.09361,
            "mile": 0.000621371,
            "millimeter": 0.001,
            "centimeter": 0.01,
            "decimeter": 0.1,
            "kilometer": 1000,
        },
        "millimeter": {
            "inch": 0.0393701,
        },
        "centimeter": {
            "inch": 0.393701,
        },
        "decimeter": {
            "inch": 3.93701,
        },
        "kilometer": {
            "mile": 0.621371,
        }
    },
    "weight": {
        "gram": {
            "ounce": 0.03527396,
            "pound": 0.00220462,
        },
        "kilogram": {
            "ounce": 35.27396,
            "pound": 2.20462,
        }
    },
    "volume": {
        "liter": {
            "quart": 1.05668821,
            "cubic foot": 0.035314667,
            "cubic yard": 0.001308,
            "gallon": 0.264172,
        },
        "milliliter": {
            "cubic inch": 0.061023744,
        },
        "centiliter": {
            "cubic inch": 0.61023744,
        },
        "deciliter": {
            "cubic inch": 6.1023744,
        },
        "cubic meter": {
            "cubic foot": 35.314667,
            "cubic yard": 1.30795062,
        }
    },
}


def calculate_answer(string):
    string = string.strip().split()

    amount = float(string[0])
    english_unit = string[1].rstrip("s")
    metric_unit = string[2].rstrip("?")
    metric_unit = metric_unit.rstrip("s")

    conversion_factor = conversion_factors.get(english_unit, {}).get(metric_unit)

    if conversion_factor is None:
        return -1

    answer = amount * conversion_factor
    return answer


def main():
    while True:
        string = input("Enter a conversion: ")
        answer = calculate_answer(string)

        if answer == -1:
            print("Invalid conversion")
        else:
            print(f"{answer:.4f}")


if __name__ == "__main__":
    main()
