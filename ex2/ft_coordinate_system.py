import math


def get_player_pos() -> None:
    input_user: str = ""
    good_coords: list[float] = []
    if input_user == "" and len(good_coords) == 0:
        input_user = input(
            "Enter new coordinates as \
                           floats in format 'x,y,z':"
        )
    while len(good_coords) == 0:
        try:
            list_input: list[str] = input_user.split(sep=",")
            if input_user == "" or len(list_input) == 0:
                raise SyntaxError("Invalid syntax")
            if len(list_input) != 3:
                raise ValueError("you should have 3 floats")
            for x in list_input:
                try:
                    float(x)
                except ValueError:
                    raise ValueError(
                        f"Error on parameter {x} : "
                        f"could not convert string to float: {x}"
                    )
            good_coords = [float(x) for x in list_input]
        except ValueError as e:
            print(e)
        except SyntaxError as e:
            print(f"Cannot parse the input as a 3d coordinates : {e}")
        finally:
            if len(good_coords) == 0:
                input_user = input("Try again, enter new coodinates 'x,y,z':")
            elif len(good_coords) == 3:
                coords: tuple[float, ...] = tuple(good_coords)
                print("Got a first tuple :", coords)
                print(f"it includes: X={coords[0]}, Y={coords[1]}, Z={coords[2]}")
                distance: float = math.sqrt(
                    coords[0] ** 2 + coords[1] ** 2 + coords[2] ** 2
                )
                print(f"Distance to center: {round(distance, 2)}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    get_player_pos()
