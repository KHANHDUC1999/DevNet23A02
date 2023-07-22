from ncclient import manager
import xml.dom.minidom as MD

netconf_net=manager.connect(
    host='10.215.26.229',
    port=830,
    username='vnpro',
    password='vnpro#123',
    hostkey_verify=False
)

# for i in netconf_net.server_capabilities:
#     print(i)


# netconf_reply=netconf_net.get_config(source="running")
# print(netconf_reply)
# print(MD.parseString(netconf_reply.xml).toprettyxml())
# with open('get_config.txt','w') as file:
#     file.write(MD.parseString(netconf_reply.xml).toprettyxml())

netconf_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""

# netconf_reply=netconf_net.get_config(source="running")
# print(netconf_reply)

netconf_reply=netconf_net.get_config(source="running",filter=netconf_filter)
# print(netconf_reply)
with open('interfaces.txt','w') as file:
    file.write(MD.parseString(netconf_reply.xml).toprettyxml())

