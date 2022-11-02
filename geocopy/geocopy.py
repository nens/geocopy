# Simple utility script for copying/removing workspaces from geoserver.
#
# Keep everything in a single file for easy "deployment". And no dependencies
# for now.
import json
import os
import sys

GEOSERVER_CONFIG_FILE = "/etc/serverscripts/geoserver.json"


def grab_geoservers_info(geoserver_config_file=GEOSERVER_CONFIG_FILE):
    return json.load(open(geoserver_config_file))


def print_info(geoservers_info):
    print("Info on our geoservers")
    for geoserver_info in geoservers_info:
        workspace_dir = os.path.join(geoserver_info["data_dir"], "workspaces")
        print()
        print("Domain: https://%s" % geoserver_info["geoserver_name"])
        print("Nginx logfile: %s" % geoserver_info["logfile"])
        print("To go to the workspaces directory:")
        print("   cd %s" % workspace_dir)


def main():
    geoservers_info = grab_geoservers_info()
    args = sys.argv[1:]
    if not args:
        print_help()
        print_info()


if __name__ == "__main__":
    main()
