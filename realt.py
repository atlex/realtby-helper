import urllib2

def download(url, fileName):
    print 'Downloading "{}"...'.format(url)

    headers = {'User-Agent':'Mozilla/5.0'}
    req = urllib2.Request(url, None, headers)
    u = urllib2.urlopen(req)

    print 'DONE.'

    print 'Writing file "{}"...'.format(fileName)
    localFile = open(fileName, 'w')
    localFile.write(u.read())
    localFile.close()
    print 'DONE.\n'

FLAT_1_START_YEAR = '2000'
FLAT_1_END_YEAR = '2013'
FLAT_1_FILE = 'realt-flat1.html' 
FLAT_1_ROOMS_MIN = '3'
FLAT_1_ROOMS_MAX = '4'
FLAT_1_LAST_STAGE = '1' #Ne posledni etag

FLAT_2_START_YEAR = '1960'
FLAT_2_END_YEAR = '1975'
FLAT_2_FILE = 'realt-flat2.html'
FLAT_2_ROOMS_MIN = '2'
FLAT_2_ROOMS_MAX = '2'
FLAT_2_LAST_STAGE = '0' #Ne posledni etag

#url = 'http://realt.by/sale/cottages/show/database/?tx_uedbcottage_pi2[DATA][building_year][ge]=' + FLAT_START_YEAR + '&tx_uedbflat_pi2[DATA][building_year][le]=' + FLAT_END_YEAR + '&tx_uedbcottage_pi2[DATA][price][ge]=1&tx_uedbcottage_pi2[DATA][price][le]=130&tx_uedbcottage_pi2[DATA][town_distance][le]=10&tx_uedbcottage_pi2[sort_by][0]=date_revision&tx_uedbcottage_pi2[asc_desc][0]=1&tx_uedbcottage_pi2[sort_by][1]=price&tx_uedbcottage_pi2[DATA][gas][nez]=1&tx_uedbcottage_pi2[DATA][electricity][nez]=1'
#fileName = 'realt-house.html'
#download(url, fileName)

url = 'http://realt.by/sale/flats/show/database/?tx_uedbflat_pi2[cmd]=search&tx_uedbflat_pi2[category]=3&tx_uedbflat_pi2[page_num]=1&tx_uedbflat_pi2[rec_per_page]=30&tx_uedbflat_pi2[sort_by][0]=date_revision&tx_uedbflat_pi2[asc_desc][0]=1&tx_uedbflat_pi2[sort_by][1]=price&tx_uedbflat_pi2[asc_desc][1]=0&tx_uedbflat_pi2[DATA][town_id][e]=5102&tx_uedbflat_pi2[DATA][rooms][e][1]=' + FLAT_1_ROOMS_MIN +'&tx_uedbflat_pi2[DATA][rooms][e][2]=' + FLAT_1_ROOMS_MAX + '&tx_uedbflat_pi2[DATA][building_year][ge]=' + FLAT_1_START_YEAR + '&tx_uedbflat_pi2[DATA][building_year][le]=' + FLAT_1_END_YEAR + '&tx_uedbflat_pi2[DATA][storey][ne]=1&tx_uedbflat_pi2[DATA][storey][fne]=' + FLAT_1_LAST_STAGE + '&tx_uedbflat_pi2[DATA][separate_rooms][fe]=t.rooms&tx_uedbflat_pi2[DATA][town_subdistrict_id][e]=#80'
download(url, FLAT_1_FILE)

url = 'http://realt.by/sale/flats/show/database/?tx_uedbflat_pi2[cmd]=search&tx_uedbflat_pi2[category]=3&tx_uedbflat_pi2[page_num]=1&tx_uedbflat_pi2[rec_per_page]=30&tx_uedbflat_pi2[sort_by][0]=date_revision&tx_uedbflat_pi2[asc_desc][0]=1&tx_uedbflat_pi2[sort_by][1]=price&tx_uedbflat_pi2[asc_desc][1]=0&tx_uedbflat_pi2[DATA][town_id][e]=5102&tx_uedbflat_pi2[DATA][rooms][e][1]=' + FLAT_2_ROOMS_MIN +'&tx_uedbflat_pi2[DATA][rooms][e][2]=' + FLAT_2_ROOMS_MAX + '&tx_uedbflat_pi2[DATA][building_year][ge]=' + FLAT_2_START_YEAR + '&tx_uedbflat_pi2[DATA][building_year][le]=' + FLAT_2_END_YEAR + '&tx_uedbflat_pi2[DATA][storey][ne]=1&tx_uedbflat_pi2[DATA][storey][fne]=' + FLAT_2_LAST_STAGE + '&tx_uedbflat_pi2[DATA][separate_rooms][fe]=t.rooms&tx_uedbflat_pi2[DATA][town_subdistrict_id][e]=#80'
download(url, FLAT_2_FILE)



