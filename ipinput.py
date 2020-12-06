"""
Summary:
Example coding excercise result for a route lookup process program (like Cisco process switching)

Instructions:
Develop a Python program which uses a list of 'route' objects as a virtual RIB, and takes input
from the user to determine the best next-hop forwarding path(s). Use the "route_table.json" file
in the same dir to import your route table as a Python dictionary.

Caveats/Notes:
- Individual routes must be Python objects
- Be sure to consider default routes for no specific matches, as well as ECMP in results (ECMP is 'on')
- Match on most-specific routes only (preferring AD/protocol metrics not necessary for this excercise)
"""

from netaddr import IPNetwork, IPAddress
import sys
import json

class Route(object):
    #create route object class
    def __init__(self, protocol, prefix, next_hop):
        self.protocol = protocol
        self.prefix = prefix
        self.next_hop = next_hop

    #bonus points for __str__ and __repr__ class defs:
    def __str__(self):
        return f"-> {self.protocol} route for {self.prefix} points to {self.next_hop}."

    def __repr__(self):
        return f"Route(self.protocol, self.prefix, self.next_hop)"

def openRouteTableFile(filename="route_table.json"):
    #open/load the route table json data
    with open(filename) as routes_file:
        routes = json.load(routes_file)
        items = routes["entries"]
    return [Route(item["protocol"], item["prefix"], item["next_hop"]) for item in items]

def routeLookup(prefix):
    #load synthetic route table
    rib = openRouteTableFile("route_table.json")

    #create list of routes based on match
    #(mega bonus points if able to do this without using the netaddr module)
    matched_route = [route for route in rib if IPAddress(prefix) in IPNetwork(route.prefix)]
    total_routes = len(matched_route)
    total_droutes = len([x for x in matched_route if x.prefix == "0.0.0.0/0"])

    if total_routes != total_droutes:
            #strip default routes from results since we have more specifics
            matched_route = [route for route in matched_route if route.prefix != "0.0.0.0/0"]

    return matched_route

if __name__ == "__main__":
    #take input args from the user
    if len(sys.argv) > 1:
        prefix = str(sys.argv[1])
        result = routeLookup(prefix)
        print(f"\nRoute lookup for prefix {prefix}:")
        for x in result:
            print(f"* {x.prefix} available via {x.next_hop} using protocol {x.protocol}") 
        sys.exit()
    else:
        self_filename = str(sys.argv[0])
        print(f"Please specify route argument (E.g. {self_filename} 10.0.0.1)")
        sys.exit()