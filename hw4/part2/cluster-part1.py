import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
from operator import itemgetter

def initFunc(k, df, centers, clusters):
    for center_id in range(k):
        centers[center_id] = df[np.random.random_integers(0, df.shape[0])]
        clusters[center_id] = []

    for point in df:
        dist = {}
        for key, val in centers.iteritems():
            dist[key] = distance.euclidean(val, point)

        nearest_center_id = sorted(dist.items(), key=itemgetter(1))[0][0]

        clusters[nearest_center_id].append(list(point))

    return centers, clusters


def clusterCenter(cluster):
    if not cluster:
        return [0] * 784

    return list(np.mean(cluster, axis=0))


def findCenterIdForPointInCluster(point, cluster):
    for center_id in cluster.keys():
        if point in cluster[center_id]:
            return center_id


def recluster(k, df, centers, clusters):
    counter = 0

    addToCluster = []
    removeFromCluster = []

    for point in df:
        dist = {}
        for key, val in centers.iteritems():
            dist[key] = distance.euclidean(val, point)

        nearest_center_id = sorted(dist.items(), key=itemgetter(1))[0][0]

        if list(point) not in clusters[nearest_center_id]:
            addToCluster.append([nearest_center_id, list(point)])
            removeFromCluster.append([findCenterIdForPointInCluster(list(point), clusters), list(point)])
            counter += 1

    for cid, pt in addToCluster:
        clusters[cid].append(pt)

    for cid, pt in removeFromCluster:
        clusters[cid].remove(pt)
        # clusters[nearest_center_id].append(point)

    return centers, clusters, counter


def getError(clusters, centers):
    dist = 0
    for center_id in clusters.keys():
        for point in clusters[center_id]:
            dist += distance.euclidean(centers[center_id], point)

    return dist


def main():
    # k = 2

    df = pd.read_csv('data.txt', index_col=False)
    df = df.as_matrix()

    centers = {}
    clusters = {}

    least_sse = []
    for k in range(2, 10):
        centers, clusters = initFunc(k, df, centers, clusters)

        counter = 1
        iters = []
        sse = []
        ctr = 0
        while counter != 0:
            for center_id in centers.keys():
                centers[center_id] = clusterCenter(clusters[center_id])

            centers, clusters, counter = recluster(k, df, centers, clusters)
            ctr += 1
            print counter, getError(clusters, centers)
            iters.append(ctr)
            sse.append(getError(clusters, centers))

        least_sse.append(sse[-1])

    plt.plot(range(2, 10), least_sse, label='k values')
    plt.xlabel('k')
    plt.ylabel('SSE')
    plt.title('k vs. SSE')

    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
