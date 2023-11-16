from cli import *
from pizza_recipes import *


if __name__ == '__main__':
    deliver(Margherita())
    print(Pepperoni('L').__dict__())
    print(Hawaiian('XL').__str__())
