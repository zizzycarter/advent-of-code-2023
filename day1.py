def get_coordinates_p1(data):
    coordinates = []
    for x in data:
        numbers = []
        for a in x:
            if a.isdigit():
                numbers.append(a)
        coordinates.append(int(numbers[0]+numbers[-1]))
    return sum(coordinates)

num_match = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}

def get_coordinates_p2(data,num_match=num_match):
    coordinates = []
    for x in data:
        temp = []
        for i in range(len(x)):
            if (x[i]).isdigit():
                temp.append(x[i])
            else:
                for j in range(1,len(x)+1):
                    for key,value in num_match.items():
                        if key == x[i:j]:
                            temp.append(value)
                            break
                    else:
                        continue
                    break
        coordinates.append(int(str(temp[0])+str(temp[-1])))
    return sum(coordinates)

if __name__ == "__main__":
    with open('d1.txt') as f:
        data = f.read().splitlines()
    part1 = get_coordinates_p1(data)
    part2 = get_coordinates_p2(data)
    print(part1)
    print(part2)