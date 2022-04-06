#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import sys
import csv
import argparse



# Main logic
def main(args=None):
    # call eosc marketplace with ample number of services per page: default = 1000
    url = "https://marketplace.eosc-portal.eu/services?page=1&per_page={}".format(str(args.items))
    
    print("Retrieving page: marketplace list of services... \nGrabbing url: {0}".format(url))
    page = requests.get(url)
    
    print("Page retrieved!\nGenerating results...")
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find all h2 that contain the data-e2e attribute equal to service-id
    results = soup.findAll("h2", {"data-e2e":"service-id"})
    rows = []
    # populate rows with each row = [service id, service name, service path]
    for item in results:
        a = item.findChildren("a",recursive=False)[0]
        row = [int(item.attrs["data-service-id"]),item.text.strip(),a['href']]
        rows.append(row)
    # sort rows by id 
    rows = sorted(rows, key=lambda x: x[0])
    
    # output to csv
    with open(args.output, "w") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    
    print("File written to {}".format(args.output))


# Parse arguments and call main 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Retrieve service catalog from eosc marketplace")
    parser.add_argument(
        "-n", "--num-of-items", metavar="STRING", help="Number of items per page", required=False, dest="items", default="1000")
    parser.add_argument(
        "-o", "--output", metavar="STRING", help="Output csv file", required=False, dest="output", default="./service_catalog.csv")

    # Parse the arguments
    sys.exit(main(parser.parse_args()))