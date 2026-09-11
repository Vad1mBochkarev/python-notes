# robots = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# limit = 10

robots = [1, 1, 1, 1]
limit = 3


def find_two_indexes(data, expected_result):
    left_pointer = 0
    right_pointer = len(data) - 1

    while left_pointer < right_pointer:
        if data[left_pointer] + data[right_pointer] <= expected_result:
            print((left_pointer, right_pointer))
            return (left_pointer, right_pointer)
        else:
            right_pointer -= 1

    return False

def robots_go_calk(rob, lim):
    platforms = 0
    rob = sorted(rob, reverse=True)

    while len(rob) > 0:
        if len(rob) == 1:
            platforms += 1
            break

        x = find_two_indexes(rob, lim)
        if x == False:
            rob.pop(0)
            platforms += 1

        else:
            rob.pop(x[1])
            rob.pop(x[0])
            platforms += 1

    return platforms

if __name__ == '__main__':
    print(f'need {robots_go_calk(robots, limit)} platforms')   