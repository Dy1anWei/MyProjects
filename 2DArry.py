
class Two_D_Array():
    def __init__(self):
        self.main = []

    def main1(self):
        num_of_command = int(input("Enter number of lines \n"))
        print("Enter Command Lines")

        while num_of_command != 0:
            user = input()
            command_line = user.split(" ")

            if command_line[0] == "append":
                num = command_line[1].split(",")
                self.main.append(num)
                num_of_command -= 1

            if command_line[0] == "insert":
                num = command_line[1].split(",")
                number = [num[0], num[1]]
                self.main.insert(int(num[2]), number)
                num_of_command -= 1


            if command_line[0] == "print":
                print(self.main)

            if command_line[0] == "remove":
                self.main.remove((self.main[int(command_line[1])]))
                num_of_command -= 1


            if command_line[0] == "change":
                num = command_line[1].split(",")
                num = [int(i) for i in num]
                self.main[num[0]][num[1]] = num[2]
                num_of_command -= 1

            if command_line[0] == "pop":
                self.main.pop()
                num_of_command -= 1

            if command_line[0] == "high":
                num = [list(map(int, i)) for i in self.main]
                max = []
                for j in range(len(num)):
                    if sum(num[j]) > sum(max):
                        max = num[j]
                print(max)
                num_of_command -= 1

            else:
                print("Enter append, high, pop, insert, change, print or remove.\n ")

main_array = Two_D_Array()
main_array.main1()









