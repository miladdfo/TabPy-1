import tabpy_client
from time import sleep

sleep(15)

client = tabpy_client.Client('http://localhost:9004/')

def clustering(x, y):
    import numpy as np
    from sklearn.cluster import DBSCAN
    from sklearn.preprocessing import StandardScaler
    X = np.column_stack([x, y])
    X = StandardScaler().fit_transform(X)
    db = DBSCAN(eps=1, min_samples=3).fit(X)
    return db.labels_.tolist()


client.deploy('clustering',
                clustering,
                'Returns cluster Ids for each data point specified by the pairs in x and y')
