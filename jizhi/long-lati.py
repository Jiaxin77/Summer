def convert_to_dms(dd_lat, dd_lon):

    dd_lat = float(dd_lat)#纬度
    dd_lon = float(dd_lon)#经度


    if int(dd_lat) >= 0:#纬度大于等于0 标N 赤道为N
        dir_lat = "N"
    else:
        dir_lat = "S"
        dd_lat = -dd_lat

    if int(dd_lon) >= 0:
        dir_lon = "E"
    else:
        dir_lon = "W"
        dd_lon = -dd_lon

    def convert60(x):
        return 60 * (float(x) - int(x))

    ddd_lat = '%03d' % int(dd_lat)
    mm_lat = '%02d' % int(convert60(dd_lat))
    ss_lat = ('%.3f' % convert60(convert60(dd_lat))).zfill(6)
    #zfill(width) 右对齐,不够width的在左侧填充0
    dms_lat = ddd_lat + "*" + mm_lat + "'" + ss_lat + '"' + dir_lat


    ddd_lon = '%03d' % int(dd_lon)
    mm_lon = '%02d' % int(60 * (dd_lon - int(dd_lon)))
    ss_lon = ('%.3f' % (60 * (60 * (dd_lon - int(dd_lon))-int(mm_lon)))).zfill(6)

    dms_lon = ddd_lon + "*" + mm_lon + "'" + ss_lon + '"' + dir_lon

    return dms_lat, dms_lon

print(convert_to_dms('35.03299485527936', '33.233755230903625'))
print(convert_to_dms('-37.111415669561595', '-12.284317023586482'))