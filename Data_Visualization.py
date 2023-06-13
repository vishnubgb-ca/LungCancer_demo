import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from Data_Preprocessing import data_preprocessing
from matplotlib.backends.backend_pdf import PdfPages

def data_visualization():
    dataset = data_preprocessing()
    for col in dataset.columns:
        if (len(dataset[col].unique()) > 5) and (col != 'Level'):
            fig,ax = plt.subplots(1,1, figsize=(5,4))
            sns.distplot(x=dataset[col][1:])
            plt.show()
        elif col != 'Level':
            dataset[col] != 'Level'
            fig,ax = plt.subplots(1,1, figsize = (5,4))
            sns.countplot(x=dataset[col][1:])
            plt.show()
    sns.pairplot(dataset)
    plt.show()
    cor_mat = dataset.corr()
    fig = plt.figure(figsize=(15,7))
    sns.heatmap(cor_mat,annot=True)
    plt.show()
    return dataset

def save_image(filename):
    p = PdfPages(filename)
    fig_nums = plt.get_fignums()  
    figs = [plt.figure(n) for n in fig_nums]
    # iterating over the numbers in list
    for fig in figs:  
        # and saving the files
        fig.savefig(p, format='pdf')  
    # close the object
    p.close()  
  
# name your Pdf file
filename = "multi_plot_image.pdf"  
data_visualization()  
# call the function
save_image(filename) 


