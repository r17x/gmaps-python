import json, googlemaps as gm
import config

maps = gm.Client(key=config.key)

# open types.txt to view all places type
f = open('types.txt', 'r')
list_type = str(f.read()).replace('\n',' ')
f.close()

# search param
search = {
     'keyword': raw_input('Keyword:'),
     'location': {'lat': -5.147665099999999, 'lng': 119.4327314},
     'type': raw_input(list_type + '\nSelect Type:'),
     'radius': 200
}

result = maps.places_radar(**search)

result = dict(search, **result)

f = open('search_radar.json','w+')
f.write(
    json.dumps(
        result,
        indent=2,
        sort_keys=True
    )
)
f.close()

print("Check search_radar.json to view result")
