import xml.etree.ElementTree as ET
from pathlib import Path
import logging

xml_file = Path(__file__).parent / "work_with_xml" / "groups.xml"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

tree = ET.parse(xml_file)
root = tree.getroot()


def search_by_group_number(number):
    for group in root.findall("group"):
        number_tag = group.find("number")
        if number_tag is not None and number_tag.text == str(number):
            incoming_tag = group.find("timingExbytes/incoming")
            if incoming_tag is not None:
                incoming = incoming_tag.text
                logging.info(f"Group number {number}: incoming = {incoming}")
                return incoming
            else:
                logging.info(f"Group number {number}: no incoming value")
                return None

    logging.info(f"Group number {number} not found")
    return None


search_by_group_number(0)
search_by_group_number(1)
search_by_group_number(999)