
def search_max_hipo(x):
    for x in range(x, 5, -1):
        for y in range(x-1, 4, -1):
            for z in range(x-1, 3, -1):
                if (x*x==y*y+z*z):
                    return max([x, y, z])

if __name__ == '__main__':
    X = input("What is the maximal length of the triangle side? Enter a number: ")
    print("The longest side possible is " + str(search_max_hipo(int(X))))

