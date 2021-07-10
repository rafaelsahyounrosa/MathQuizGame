from models.calculate import Calculate


def main() -> None:
    points: int = 0
    play(points)


def play(points: int) -> None:
    difficulty: int = int(input('Please inform the desired difficulty level [1, 2, 3 or 4]: '))

    calc: Calculate = Calculate(difficulty)

    print('Inform the result of the following operation: ')
    calc.show_operation()

    result: int = int(input())

    if calc.check_result(result):
        points += 1
        print(f'You have {points} point(s)')

    keep_playing: int = int(input('Do you want to keep playing? [1 - Yes, 0 - No ]'))

    if keep_playing:
        play(points)
    else:
        print(f'You ended with {points} point(s)!')
        print('See you again soon.')


if __name__ == '__main__':
    main()
