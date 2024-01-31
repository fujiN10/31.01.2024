import sys
from geocoder import get_ll_span
from mapapi_PG import show_map

# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом:
toponym_to_find = " ".join(sys.argv[1:])

if toponym_to_find:
    ll, spn = get_ll_span(toponym_to_find)
    add_params = f'pt={ll}'
    ll_spn = f'll={ll}&spn={spn}'
    show_map(ll_spn=ll_spn, map_type="map", add_params=add_params)
else:
    print('No toponym')

