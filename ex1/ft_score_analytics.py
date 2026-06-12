import sys


def main() -> None:
    print(f"Program name: {sys.argv[0]}")
    arguments: list[str] = sys.argv[1:]
    scores: list[int] = []
    errors: list[str] = []
    sum: int = 0
    if arguments:
        for param in arguments:
            try:
                param_int: int = int(param)
                scores.append(param_int)
                sum += param_int
            except Exception:
                errors.append(f"Invalid parameter: {param}")
        if len(scores) != 0:
            print(f"Total players : {len(arguments)}")
            print(f"Scores processed: {scores}")
            avg: float = sum / len(arguments)
            print(f"Average score : {avg}")
            print(f"High score : {max(scores)}")
            print(f"Low score : {min(scores)}")
            print(f"Score range : {max(scores) - min(scores)}")
        for err in errors:
            print(err)
        else:
            print(
                (
                    "No score provided. Usage: python3 ft_score_analytics.py "
                    "<score1> <score2> ..."
                )
            )
    else:
        print(
            "No score provided. Usage: python3 ft_score_analytics.py, "
            "<score1> <score2> ..."
        )


if __name__ == "__main__":
    print("=== Player Score Analytics ===\n")
    try:
        main()
    except TypeError as e:
        print(e)
