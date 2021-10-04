import datafilters as df
import matplotlib.pyplot as plt
import geopandas as gpd


def fish():
    labels, values = df.sizeFish()
    fig1, ax1 = plt.subplots(figsize=(10, 4.2))
    ax1.pie(values, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=0)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax1.axis('equal')
    plt.title('Size of Angler Fish in New Zealand waters (millimeters)')
    return plt.gcf()

def line_plot(): 
    labels = []  
    values = []
    data = df.fishAmountYear()
    # sorting
    for key in sorted(data.keys()):
        labels.append(key)
        values.append(data[key])
    fig1, ax1 = plt.subplots(figsize=(10, 4.2))
    plt.plot(labels, values)
    return plt.gcf()


def markLocation():
    data = df.readLocation()
    countries = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

        countries[countries["name"] == "New Zealand"].plot(color="lightgrey", ax=ax)

        # Plot map

        data.plot(x="decimalLongitude", y="decimalLatitude", kind="scatter", colormap="YlOrRd", 

        title=f"New Zealand Location", ax=ax)

        ax.grid(b=True, alpha=0.5)

        ax.set_xlabel('Longtitude')

        ax.set_ylabel('Latitude')
