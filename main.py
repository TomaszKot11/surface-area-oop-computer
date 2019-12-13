from dispatcher import Dispatcher
from decimal import InvalidOperation

options = ['triangle', 'rectangle', 'square', 'cube', 'shapely pyramind', 'oval', 'exit']

def main():
    dispatcher = Dispatcher()
    print("Welcome to the surface and capacity calculator!")

    while True:
      print_menu()
      option = input("Please chose the option: ")
      try:
          option_int = int(option)
          should_run, result_figure = dispatcher.get_surface_and_capacity(option_int)
          if(not should_run):
            return
          print('The surface area is {}'.format(result_figure.get_surface_area()))
          capacity = result_figure.get_capacity()
          capacity_str = 'The capacity is {}'.format(capacity) if capacity else 'This is 2D figure!'
          print(capacity_str)
      except ValueError:
        print("The option must be an integer")
      except InvalidOperation:
        print("Invalid input")

def print_menu():
  for idx, option in enumerate(options):
    print('{} - {}'.format(idx, option))

if __name__ == '__main__':
    main()