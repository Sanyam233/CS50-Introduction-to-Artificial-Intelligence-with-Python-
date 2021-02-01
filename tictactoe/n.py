def func(timer):

    if timer == 4:
        return 1

    else:

        for i in range(1,3):
            print(f"function {timer} Loop {i} gets executed")
            func(timer + 1)
            print(f"function {timer} after loop {i} EXECUTED")

func(1)
