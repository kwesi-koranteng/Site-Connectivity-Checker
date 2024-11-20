#Import URLLIB
#USE URLLIB.REQUEST TO GET DATA FROM THE URL
#A FUNCTION THAT TAKES THE URL AND THEN RETURNS A RESPONSE

import urllib.request as urllib



def main(url):
    print("Checking connectivity...")

    response = urllib.urlopen(url)
    print("Connected to", url, "succesfully!")
    print("The response code was: ", response.getcode())

print("This a site connectivity checker program")
input_url = input("Input the url of the site you want to check: ")

main(input_url)