import reader
import utils
import plot
import map

if __name__ == '__main__':
    filepath = "../pneuma_sample_dataset/pneuma_sample_dataset.csv"
    granularity = 25

    BBoxleft = [37.99130, 37.99163, 23.73236, 23.73326]
    BBoxright = [37.99083, 37.99102, 23.73559, 23.73694]
    BBoxdown = [37.99134, 37.99157, 23.72996, 23.73061]

    vehicles = reader.load_rows_in_interval(filepath, 370, 385, granularity)
    ll = utils.pass_through_BBox(vehicles, *BBoxleft)
    rr = utils.pass_through_BBox(ll, *BBoxright)
    dep = utils.pass_through_BBox(rr, *BBoxdown)

    for vehicle in dep:
        print(vehicle)

    map.to_map_plot(dep, "map1.html")
    plot.to_plot(dep)
