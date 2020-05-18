# M/M/1 tandem network simulation.
# import argparse
import sys

# def simulate():
#     pass


# def parse_arguments():
#     parser = argparse.ArgumentParser(
#         description="Simulate M/M/1 -> ... */M/1 tandem network.")
#     parser.add_argument('')
def x_plus_y(x, y):
    return x + y




if __name__ == '__main__':
    print('Hello, dockerized python app!')
    print('Your args are: ', sys.argv)
    if len(sys.argv) > 1:
        with open(sys.argv[-1]) as f:
            for line in f:
                print(line)
