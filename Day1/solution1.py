# part 1
print(max([sum(i) for i in [list(map(int, filter(lambda a:a!='', i))) for i in [i for i in [i.split("\n") for i in open("input.txt","r").read().split('\n\n')]]]]))


# part 2
print(sum(sorted([sum(i) for i in [list(map(int, filter(lambda a:a!='', i))) for i in [i for i in [i.split("\n") for i in open("input.txt","r").read().split('\n\n')]]]])[-1:-4:-1]))