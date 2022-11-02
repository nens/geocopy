import os
import geocopy

OUR_DIR = os.path.dirname(__file__)


def test_grab_geoservers_info():
    example_config_file = os.path.join(OUR_DIR, "example-geoserver.json")
    geoservers_info = geocopy.grab_geoservers_info(example_config_file)
    assert geoservers_info[0]["geoserver_name"] == "geoserver9.lizard.net"


def test_print_info(capsys):
    example_config_file = os.path.join(OUR_DIR, "example-geoserver.json")
    geoservers_info = geocopy.grab_geoservers_info(example_config_file)
    geocopy.print_info(geoservers_info)
    captured = capsys.readouterr()
    assert "workspaces directory" in captured.out
