import pickle
import pandas as pd
import numpy as np
import scipy.cluster.hierarchy as hac
import matplotlib.pyplot as plt

from scipy.spatial import distance as ssd
from infodenguepredict.analysis.distance import distance, alocate_data
from infodenguepredict.data.infodengue import get_city_names
from infodenguepredict.predict_settings import *

def hierarchical_clustering(df, t, method='complete'):
    """
    :param method: Clustering method
    :param df: Triangular distances matrix
    :return:
    """
    Z = hac.linkage(ssd.squareform(df.values.T + df.values), method=method)

    ind = hac.fcluster(Z, t * max(Z[:, 2]), 'distance')
    grouped = pd.DataFrame(list(zip(ind, df.index))).groupby(0)
    clusters = [group[1][1].values for group in grouped]
    return Z, clusters


def create_cluster(state, cols, t):
    cities_list = alocate_data(state)
    dists = distance(cities_list, cols)
    Z, clusters = hierarchical_clustering(dists, t=t)

    with open('clusters_{}.pkl'.format(state), 'wb') as fp:
        pickle.dump(clusters, fp)

    print("{} clusters saved".format(state))
    name_ind = get_city_names(list(dists.index))
    return Z, name_ind

def llf(id):
    return name_ind[id][1]


if __name__ == "__main__":
    Z, name_ind = create_cluster(state, cluster_vars, color_treshold)

    plt.figure(figsize=(25, 10))
    # plt.title('Hierarchical Clustering Dendrogram')
    # plt.xlabel('sample index')
    # plt.ylabel('distance')
    # plt.tight_layout()
    hac.dendrogram(
        Z,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels
        leaf_label_func=llf,
        color_threshold=t * max(Z[:, 2])
    )
    plt.show()
    plt.savefig('cluster{}_{}.png'.format(state, t), dpi=300, bbox_inches='tight')

