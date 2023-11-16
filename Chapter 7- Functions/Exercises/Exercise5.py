def describe_city(city, country='United Kingdom'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('London')
describe_city('Beijing', 'China')
describe_city('Florence' , 'Italy')