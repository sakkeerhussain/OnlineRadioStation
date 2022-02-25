import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

tree = ET.parse('config-backup.xml')
root = tree.getroot()

authentication = tree.find('authentication')
authentication.find('admin-password').text = os.environ.get('ICECAST_ADMIN_PASSWORD')
authentication.find('source-password').text = os.environ.get('ICECAST_SOURCE_PASSWORD')
authentication.find('relay-password').text = os.environ.get('ICECAST_SOURCE_PASSWORD')
config_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")

tree.write('config.xml', encoding="utf-8")
