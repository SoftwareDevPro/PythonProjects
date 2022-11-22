

from countryinfo import CountryInfo
from colorama import Fore
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c','--country',help='country to get details on')
args = parser.parse_args()

country = CountryInfo(args.country)

print(Fore.BLUE + "Capital is: ", country.capital())
print(Fore.GREEN + "Area is: ", country.area())
print(Fore.BLUE + "Population is: ", country.population())
print(Fore.GREEN + "Provinces are: ", country.provinces())
print(Fore.BLUE + "Currency is: ", country.currencies())
print(Fore.RED + "Languages are: ", country.languages())
print(Fore.YELLOW + "Borders are: ", country.borders())
print(Fore.CYAN + "Alternative Spellings: ", country.alt_spellings())

