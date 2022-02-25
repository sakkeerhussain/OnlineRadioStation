import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

tree = ET.parse('config-backup.xml')
root = tree.getroot()

admin_password = os.environ.get('ICECAST_ADMIN_PASSWORD', 'password')
source_password = os.environ.get('ICECAST_SOURCE_PASSWORD', 'password')
relay_password = os.environ.get('ICECAST_RELAY_PASSWORD', 'password')

authentication = tree.find('authentication')
authentication.find('admin-password').text = admin_password
authentication.find('source-password').text = source_password
authentication.find('relay-password').text = relay_password
config_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")

tree.write('config.xml', encoding="utf-8")
