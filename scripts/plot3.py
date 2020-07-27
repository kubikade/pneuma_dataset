import reader
import plot
import map

if __name__ == '__main__':
    filepath = "../pneuma_sample_dataset/pneuma_sample_dataset.csv"
    granularity = 25

    vehicle = reader.load_one_row(filepath, 66, granularity)
    vehicles = [vehicle]
    for vehicle in vehicles:
        print(vehicle)

    map.to_map_plot(vehicles, "map3.html")
    plot.to_plot(vehicles)
