from Algorithms_and_structures import parser_numbers

def can_split(arr: list[int]) -> bool:
    total = sum(arr)
    if total % 2 != 0:
        return False
    
    target = total // 2
    possible_sums = [False] * (target + 1)
    possible_sums[0] = True

    for num in arr:
        for i in range(target, num - 1, -1):
            if possible_sums[i - num]:
                possible_sums[i] = True
                if i == target:
                    return True
                
    return possible_sums[target]


def main():
    n = int(input())
    arr = parser_numbers(input())
    if can_split(arr):
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    main()
