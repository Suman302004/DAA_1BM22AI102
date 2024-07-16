import os

#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringConstruction(s):
    # Use a set to find all unique characters in the string
    unique_characters = set(s)
    # The cost is equal to the number of unique characters
    return len(unique_characters)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input().strip()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
