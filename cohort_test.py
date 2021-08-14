

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    file = open(filename)
    for line in file:
        print(line)
        data = line.split('|')
        print(data)
        tup = (data[0] + ' ' + data[1], data[2], data[3], data[4])
        print(tup)
        all_data.append(tup)
    
    print(all_data)

    return all_data


def main():
    all_data("cohort_data.txt")


main()