import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import holoviews as hv
from regress import polyfit, regress

plt.style.use('seaborn')


"""
Exploring Ecological data
"""
# Some of this uses holoviews so we have the code in the notebook

def plot_footprint_cap(data, footprints, capacities, gdpColors):
    plt.figure(figsize=(20, 10))
    annotate = 4
    for i,f in enumerate(footprints):
        plt.subplot(2,3,i+1)
        plt.title(f + ' v. Capacity')
        plt.scatter(data[capacities[i]], (data[f]), marker='o', color=gdpColors[i])
        plt.xlabel(capacities[i])
        plt.ylabel('Footprint')
        if (annotate == i+1):
            [txt,p,x,y] = regress(data[capacities[i]],data[f],1)
            plt.text(0,-3,txt)
            plt.plot(x,y)
    plt.show()

"""
Exploring economic data
"""
# Some of this uses holoviews so we have the code in the notebook


def plot_hdi_gdp(data):
    plt.figure(figsize=(20, 10))
    labels = []
    for k, d in data.groupby('Region_x'):
        labels.append(str(k))
        plt.scatter(d.HDI, d['GDP per Capita'])
    plt.legend(labels)
    plt.ylabel("GDP per Capita")
    plt.xlabel("HDI")
    plt.title("GDP per Capita as a function of HDI")
    plt.savefig("Visualizations/GDP per Capita as a function of HDI", dpi=300)
    plt.show()


"""
Exploring Happiness data
"""
def plot_happiness(data):
    data_Happiness_footprint = data[['Country','Happiness Score', 'HDI', 'GDP per Capita','Cropland Footprint', 'Grazing Footprint', 'Forest Footprint',
           'Carbon Footprint', 'Fish Footprint', 'Total Ecological Footprint']].sort_values(by='GDP per Capita')

    l = ['Under 20000', 'Under 60000', 'Above 60000']
    gdpColors = list(reversed(sns.color_palette("viridis",as_cmap=False,n_colors=3)))

    GDP_category_list = []
    for item in data_Happiness_footprint['GDP per Capita']:
        category = ''
        if item < 20000:
            category = 'Under 20000'
        elif item < 60000:
            category = 'Under 60000'
        else:
            category = 'Above 60000'
        GDP_category_list.append(category)
    data_Happiness_footprint['GDP range'] = GDP_category_list
    data['GDP range'] = GDP_category_list

    plt.figure(figsize=(20, 10))
    for i, (k, d) in enumerate(sorted(data_Happiness_footprint.groupby('GDP range'), key=lambda x:l.index(x[0]))):
        plt.bar(d.Country, d['GDP per Capita'], width=.4, align='edge', color=gdpColors[i])
        plt.xticks(rotation=90)
    plt.ylabel("GDP per Capita")
    plt.xlabel("Country")
    plt.title("GDP per Capita by Country, grouped by GDP classification")
    plt.legend(l)
    plt.savefig('Visualizations/GDP vs Country.png')
    plt.show()

"""
Case study
"""
def plot_hist_pop(data):
    data1 = data[data['Population (millions)'] < 400]

    plt.hist(data1['Population (millions)'], bins=30)
    plt.axvline(x=data1['Population (millions)'][data1.Country == 'Bhutan'].values[0], c='r')
    plt.title("Histogram: Population (millions)")
    plt.ylabel('Population (millions)')
    plt.legend(['Bhutan'])

def plot_hist_gdp(data):
    plt.hist(data['GDP per Capita'], bins=30)
    plt.axvline(x=data['GDP per Capita'][data.Country == 'Bhutan'].values[0], c='r')
    plt.title("Histogram: GDP per Capita")
    plt.ylabel("GDP per Capita")
    plt.legend(['Bhutan'])
    plt.savefig("Visualizations/Histogram - GDP per Capita.png", dpi=300, bbox_inches="tight")

def plot_scatter_markbhutan(data, gdpColors):
    offset = 0.08
    style = dict(size=10, color='gray')
    low = data[data['GDP per Capita']<=20000]
    med = data[(data['GDP per Capita']>20000) & (data['GDP per Capita']<=60000)]
    hi = data[(data['GDP per Capita']>60000)]

    bhutanidx = data.index[data['Country']=='Bhutan']
    bhutany = data['Total Ecological Footprint'][bhutanidx].values[0]
    bhutanx = data['Happiness Score'][bhutanidx].values[0]

    plt.figure(figsize=(20, 10))
    style = dict(size=12, color='black')
    for j,datas in enumerate([low,med,hi]):
        plt.scatter(datas['Happiness Score'],(datas['Total Ecological Footprint']), marker='o', color=gdpColors[1+ j*2])
    plt.title('Total Ecological Footprint v. Happiness Score')
    plt.xlabel('Happiness Score')
    plt.ylabel('Footprint')
    plt.text(bhutanx - offset, bhutany + 2*offset,'Bhutan', **style)
    plt.show()