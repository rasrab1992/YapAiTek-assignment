import matplotlib.pyplot as plt
from bidi.algorithm import get_display
import arabic_reshaper

plt.rcdefaults();
plt.figure(figsize=(12,12));



def make_farsi_text(x):
    """
    This method takes a Persian(Farsi) text and reshapes it for displaying in figures.
    
    x: Persian string text
    farsi_text: Reshaped Persian text for displaying
    """
    
    reshaped_text = arabic_reshaper.reshape(x)
    farsi_text = get_display(reshaped_text)
    return farsi_text



class PlotFig:
    
    def __init__(self, all_sorted, num_plot):
        """
        Plot: The first num_plot numbers of all_sorted dictionary.
        """
        self.all_sorted = all_sorted
        self.num_plot = num_plot


    def plot_pie(self):
        """
        Ploting pie plot figure for the first num_plot numbers of all_sorted dictionary
        """
        sliced_sorted = [[ i for i, j in self.all_sorted[:self.num_plot]], [ j for i, j in       self.all_sorted[:self.num_plot]]]

        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = [make_farsi_text(x) for x in sliced_sorted[0]]
        sizes = sliced_sorted[1]
        fig, ax = plt.subplots()
        ax.pie(sizes, explode=None, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90, radius=1.4, )
        ax.set_xlabel
        plt.show(make_farsi_text(f"تعداد دفعات تکرار در {self.num_plot} جستجوی اول"))
    
    def plot_barh(self):
        """
        Ploting bar horizontal plot figure for the first num_plot numbers of all_sorted dictionary
        
        """
        sliced_sorted = [[ i for i, j in self.all_sorted[:self.num_plot]], [ j for i, j in self.all_sorted[:self.num_plot]]]
        labels = [make_farsi_text(x) for x in sliced_sorted[0]]
        sizes = sliced_sorted[1]
        fig, ax = plt.subplots()
        ax.barh(labels, sizes, align='center')
        ax.set_yticks(labels)
        ax.set_yticklabels(labels)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel(make_farsi_text(f"تعداد دفعات تکرار در {self.num_plot} جستجوی اول"))
        plt.show()


    def plot_pie_barh(self):
        """
        Ploting pie and bar horizontal plot figure at the same time for the first num_plot numbers of all_sorted dictionary
        
        """
        sliced_sorted = [[ i for i, j in self.all_sorted[:self.num_plot]], [ j for i, j in self.all_sorted[:self.num_plot]]]
        labels = [make_farsi_text(x) for x in sliced_sorted[0]]
        sizes = sliced_sorted[1]

        fig1, (ax1, ax2) = plt.subplots(2)
        ax1.pie(sizes, explode=None, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, radius=1.4, )

        ax2.barh(labels, sizes, align='center')
        ax2.set_yticks(labels)
        ax2.set_yticklabels(labels)
        ax2.invert_yaxis()  # labels read top-to-bottom
        ax2.set_xlabel(make_farsi_text(f"تعداد دفعات تکرار در {self.num_plot} جستجوی اول"))
        plt.show()
