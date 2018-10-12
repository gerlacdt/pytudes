def part1(arr, lengths):
    lenghts = map(int, lengths.split(','))
    skipsize = 0  # increase by 1 every iteration
    currentIndex = 0

    for l in lenghts:
        arr = reverse(arr, currentIndex, l)
        currentIndex = (currentIndex + l + skipsize) % len(arr)
        skipsize += 1

    return arr[0] * arr[1]


def reverse(li, currentIndex, reverseLength):
    liLength = len(li)
    newIndex = currentIndex + (reverseLength - 1)
    overshootIndex = newIndex - liLength

    if newIndex < liLength:
        li[currentIndex:newIndex+1] = li[currentIndex:newIndex+1][::-1]
    else:
        tmplist = li[currentIndex:] + li[:overshootIndex+1]
        revlist = tmplist[::-1]

        assert len(li[currentIndex:]) == len(revlist[:reverseLength - overshootIndex - 1])
        li[currentIndex:] = revlist[:reverseLength - overshootIndex - 1]

        assert len(li[:overshootIndex + 1]) == len(revlist[reverseLength - overshootIndex - 1:])
        li[:overshootIndex + 1] = revlist[reverseLength - overshootIndex - 1:]
    return li
