import utils


def getInput():
    return utils.Integers(utils.Inputstr("01"))


def find2Sum(nums, N=2020):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j]) == N:
                return nums[i] * nums[j]
    return None


def find3Sum(nums, N=2020):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if (nums[i] + nums[j] + nums[k]) == N:
                    return nums[i] * nums[j] * nums[k]
    return None


def test1():
    actual = find2Sum(getInput())
    assert actual == 539851


def test2():
    actual = find3Sum(getInput())
    assert actual == 0
