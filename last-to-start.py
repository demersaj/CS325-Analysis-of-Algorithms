# loop through the file, sort the activities, and run the activity selection algorithm
def loop_file():
    with open('act.txt') as f:
        numSets = find_number_of_sets()
        for i in range(numSets):
            print('Set ', i + 1)
            numActivities = int(f.readline())
            selected = []
            activities = [0 for _ in range(numActivities)]
            for j in range(numActivities):
                line = f.readline().split()
                # map activity number, start time, and end time
                activities[j] = int(line[0]), int(line[1]), int(line[2])
            # sort in reverse order using start time
            activities.sort(reverse=True)
            selected.append(activities[0])

            for k in range(1, len(activities)):
                if activities[k][2] <= selected[len(selected) - 1][1]:
                    selected.append(activities[k])

            print('Number of activities selected = ', len(selected))
            selected = [el[0] for el in selected][::-1]
            print('Activities', *selected, '\n')


# read in the file and find the number of times to run the activity selection
def find_number_of_sets():
    lines, i, numSets = [], 0, 0
    with open('act.txt') as f:
        for line in f:
            lines.append(line.strip())

        try:
            while lines:
                linesToSkip = int(lines[i])
                numSets += 1
                i += linesToSkip + 1
        except IndexError:
            _ = 'null'
    return numSets


if __name__ == '__main__':
    loop_file()
