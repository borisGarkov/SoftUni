def loading_bar_visualize(number):
    if number == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        count_percent = 0
        string_visualize = "["
        while number > 0:
            count_percent += 1
            number -= 10

        for _ in range(count_percent):
            string_visualize += "%"

        for _ in range(10 - count_percent):
            string_visualize += "."

        string_visualize += "]"

        print(f"{count_percent}0% {string_visualize}")
        print("Still loading...")


number = int(input())
loading_bar_visualize(number)

