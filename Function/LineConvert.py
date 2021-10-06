import pandas as pd
from shapely.wkt import dumps, loads
import geopandas as gpd
from shapely.geometry import LineString
 
 
# geoDataFrame对象写入geojson文件
def geoDataframe2geojson(data, geojson_path):
    data.to_file(geojson_path, driver="GeoJSON")
 
 
def list2geojson(write_geojson_path,lst,*others):
    """
    :param write_geojson_path:结果保存成geojson的路径
    :param lst:待转化的列表
    :param others:附加的其它信息
    :return: 空
    """
    #lst与其它附加的info转成dataframe
    pdd = pd.DataFrame()
    pdd["geom"] = lst
    for i in range(len(others)):
        pdd["others_{}".format(i)] = others[i]
    #dataframe转成geodataframe
    gdata = gpd.GeoDataFrame(pdd)
 
    #geom列即lst保存的是geometry类型时：
    gdata["geometry"] = list(gdata["geom"].values)
    #geom列即lst保存的是geometry的str类型时：
    # gdata["geometry"] = list(map(loads, gdata["geom"].values))
 
    gdata.drop(["geom"], axis=1, inplace=True)
    geoDataframe2geojson(gdata, write_geojson_path)
    return
 
list2geojson("tmp.geojson",
[LineString([[1,2],[3,4]]),LineString([[5,6],[7,8]])],        
["linestring1","linestring2"],
["信息1","信息2"])