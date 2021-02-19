import random
dice_type = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]

def dices(dice_code):
    """
        Oblicza rzut kostką na podstawie typu kości.
        :param str dice_code: dice pattern ex. `2D10-4`
        :rtype: int, str
        :return: wartość rzutu kośćmi dla prawidłowego typu kostki, lub `Wrong Input` dla nieprawidłowego typu
        """
    for dice in dice_type:
        if dice in dice_code:
            try:
                multiply, modifier = dice_code.split(dice)
            except ValueError:
                return "Wrong Input"
            dice_value = int(dice[1:])
            break
    else:
        return "Wrong Input"

    try:
        multiply = int(multiply) if multiply else 1
    except ValueError:
        return "Wrong Input"
    try:
        modifier = int(modifier) if modifier else 0
    except ValueError:
        return "Wrong Input"

    return sum([random.randint(1, dice_value) for _ in range(multiply)]) + modifier

if __name__ == '__main__':
    print(dices("2D12+10"))
    print(dices("2D10-4"))
    print(dices("D6"))
    print(dices("3D3"))
    print(dices("D12-1"))
    print(dices("DD19"))
    print(dices("23D-6"))

