from regress import polyfit, regress
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def plot_footprint_gdp(data, footprints, capacities, gdpColors):
    '''
    Description: Plots a scatterplot of the ecological footprints with the corresponding capacities
    Parameters: data is a dataframe of all our ecological data
                footprints is a list of strings of the various footprints
                capacities is a list of strings of the various capacities
                gdpColors is a list of RGB values in our color scheme of choice
    '''
    plt.figure(figsize=(20, 10))
    annotate = 6
    for i,f in enumerate(footprints):
        plt.subplot(2,3,i+1)
        plt.title(f + ' v. GDP Per Capita')
        plt.scatter(data['GDP per Capita'], (data[f]), marker='o', color=gdpColors[i])
        plt.xlabel('GDP per Capita')
        plt.ylabel('Footprint')
        if (annotate == i+1):
            [txt,p,x,y] = regress(data['GDP per Capita'],data[f],3)
            plt.text(0,-3,txt)
            plt.plot(x,y)
    plt.show()

def plot_footprint_hap(data, footprints, capacities, gdpColors):
    '''
    Description: Plots a scatterplot of the ecological footprints with the happiness score
    Parameters: data is a dataframe of all our ecological data and happiness scores
                footprints is a list of strings of the various footprints
                capacities is a list of strings of the various capacities
                gdpColors is a list of RGB values in our color scheme of choice
    '''
	style = dict(size=10, color='gray')
	low = data[data['GDP per Capita']<=20000]
	med = data[(data['GDP per Capita']>20000) & (data['GDP per Capita']<=60000)]
	hi = data[(data['GDP per Capita']>60000)]
	top = 3
	offset = 0.08

	# color_im = np.array([np.array(c) for c in gdpColors]).reshape((1, 6 ,3))
	# plt.imshow(color_im)
	# plt.show()
	fig,axs = plt.subplots(2,3,figsize=(20, 10))
	axs = axs.ravel()
	annotate = 6
	for i,f in enumerate(footprints):
	    max2s = sorted(data[f], reverse=True)[:top]
	    idxs = [data.index[data[f]==ymax] for ymax in max2s]
	    max1s = [data['Happiness Score'][idx].values[0] for idx in idxs]
	    for k in range(len(max1s)):
	        axs[i].text(max1s[k]+offset,max2s[k],data['Country'][idxs[k]].values[0], **style)
	    for j,datas in enumerate([low,med,hi]):
	        axs[i].set_title(f + ' v. Happiness Score')
	        axs[i].scatter(datas['Happiness Score'],(datas[f]), marker='o', color=gdpColors[1+j*2])
	        axs[i].set_xlabel('Happiness Score')
	        axs[i].set_ylabel('Footprint')
	    if annotate == i+1:
	        [txt,p,x,y] = regress(data['Happiness Score'].values,data[f].values,2)
	        axs[i].plot(x,y)
	        axs[i].text(min(data['Happiness Score']),-3,txt)
	fig.legend(['less than 20k','between 20k & 60k','greater than 60k'],bbox_to_anchor=(1.05,.85),title='GDP per Capita ($)',title_fontsize=16,fontsize=16,frameon=True)
	plt.show() 