import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import Preprocessing_for_knn_and_k_means as ps
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix


class k_means():

    def __init__(self,train,test,structure,num_bins,k=None):
        self.preprocessor = ps.Preprocessing_for_knn_and_k_means(train, test, structure, num_bins)
        self.scaled_train = self.scaling(self.preprocessor.train_df)
        if k==None:
            k = self.Silhouette_score(self.scaled_train)
        self.kmeans = KMeans(n_clusters=k, random_state=0).fit(self.scaled_train)
        self.predict = self.kmeans.predict(self.preprocessor.test_df.iloc[:, :-1])
        self.score = 0
        self.matrix = None
        self.cluster_creator()

    # function returns silhouette score for k values from 1 to kmax
    def Silhouette_score(self,df):
        kmax,last_score = 5,0
        # dissimilarity would not be defined for a single cluster, thus,
        # minimum number of clusters should be 2
        for k in range(2, kmax + 1):
            print("testing {} clusters...".format(k))
            kmeans = KMeans(n_clusters=k).fit(df)
            labels = kmeans.labels_
            this_score = silhouette_score(df, labels, metric='euclidean')
            if last_score >= this_score:
                return k-1
            last_score = this_score
        return k

    def scaling(self,data):
        scaler = StandardScaler()
        return scaler.fit_transform(data.iloc[:, :-1])

    def cluster_creator(self):
        clusters = {}
        cluster_class = {}
        for i in pd.unique(self.kmeans.labels_):
            clusters[i] = []

        k = 0
        for points in self.preprocessor.train_df.itertuples():
            clusters[self.kmeans.labels_[k]].append(list(points)[1:])
            k += 1

        for cluster_name in clusters.keys():
            tmp = {'yes': 0, 'no': 0}
            for point in clusters[cluster_name]:
                tmp[point[len(point) - 1]] += 1  # last index of point is a classifier
            if tmp['yes'] > tmp['no']:
                cluster_class[cluster_name] = 'yes'
            else:
                cluster_class[cluster_name] = 'no'
        self.score = self.Score(cluster_class)

    def Score(self,cluster_class):
        new_col = []
        for i in self.predict:
            new_col.append(cluster_class[i])
        counter = 0
        check = list(zip(new_col, self.preprocessor.test_df['class']))
        for i, j in check:
            if i == j:
                counter +=1
        self.matrix = confusion_matrix(self.preprocessor.test_df['class'],new_col)
        return counter/len(new_col)*100


def run(**kwargs ):  # run(files, mode, bins, k=5):
    means = k_means(kwargs['train'], kwargs['test'], kwargs['structure'], kwargs['number_of_bins'],5)
    return {'score': means.score,
            'TP': means.matrix[1][1],
            'TN': means.matrix[0][0],
            'FP': means.matrix[0][1],
            'FN': means.matrix[1][0]
            }

# tmp = open("Structure.txt", "r")
# structure_file = []
#
# for line in tmp:
#     structure_file.append(line)
# tmp.close()
# train = pd.read_csv("train.csv")
# test = pd.read_csv("test.csv")