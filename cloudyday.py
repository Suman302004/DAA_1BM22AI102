import os

def maximumPeople(p, x, y, r):
    # Dictionary to store which clouds cover which towns
    town_clouds = {i: [] for i in range(len(x))}
    cloud_coverage = {i: 0 for i in range(len(y))}

    # Determine which towns are covered by which clouds
    for i in range(len(y)):
        for j in range(len(x)):
            if abs(y[i] - x[j]) <= r[i]:
                town_clouds[j].append(i)
                cloud_coverage[i] += p[j]

    # Total sunny population without removing any cloud
    total_sunny_population = sum(p[j] for j in range(len(x)) if not town_clouds[j])

    # Compute the additional population that would be sunny if each cloud is removed
    max_additional_sunny_population = 0
    for i in range(len(y)):
        additional_sunny_population = 0
        for j in range(len(x)):
            if len(town_clouds[j]) == 1 and town_clouds[j][0] == i:
                additional_sunny_population += p[j]
        max_additional_sunny_population = max(max_additional_sunny_population, additional_sunny_population)

    return total_sunny_population + max_additional_sunny_population

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    x = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    y = list(map(int, input().rstrip().split()))

    r = list(map(int, input().rstrip().split()))

    result = maximumPeople(p, x, y, r)

    fptr.write(str(result) + '\n')

    fptr.close()
