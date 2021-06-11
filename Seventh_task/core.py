from xml.dom import minidom

with open('map1.osm', 'r', encoding='utf-8') as file:
    osm = minidom.parse(file)
police = {}
nodes = osm.getElementsByTagName('node') + osm.getElementsByTagName('way')
for node in nodes:
    tags = node.getElementsByTagName('tag')
    house_number = ''
    street = ''
    for tag in tags:
        k = tag.attributes['k'].value
        v = tag.attributes['v'].value
        if k == 'addr:street':
            street = v
        if k == 'addr:housenumber':
            house_number = str(v)
        if k == 'amenity' and v == 'police':
            node_id = node.attributes['id'].value
            if street and house_number:
                address = '{}, {}'.format(street, house_number)
                police.update({node_id: address})
            else:
                police.update({node_id: ''})
for elem_id, address in police.items():
    print('ID: {} | Адрес: {}'.format(elem_id, address))
