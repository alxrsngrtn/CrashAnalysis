from __future__ import print_function

import CrashAnalysis

from sklearn.externals import joblib
import pandas as pd


def main():
   tool = CrashAnalysis.TextAnalysis()

   tool.read_csv('./data/Crashes.csv')
   tool.get_customer_descriptions_by_version('2016040014')
   vocab_frame = tool.create_vocab_frame()
   get_term_frequencies(tool, vocab=vocab_frame)

   #


   # mx, terms = tool.vectorize_corpus()
   #
   #
   #
   # compute = True
   # n_custers = 7
   # if compute:
   #     km = tool.kmeans(mx, n_custers)
   # else:
   #     km = joblib.load('doc_cluster_k{0}.pkl'.format(n_custers))
   #
   # clusters = km.labels_.tolist()
   # cluster_lists = [[x] for x in clusters]
   #
   # print(tool.frequency_count(cluster_lists))
   #
   # new_df = tool.label_dataframe_with_clusters(clusters)
   #
   # print(new_df['Cluster'].value_counts())
   #
   # # tool.label_frame_with_clusters(clusters)
   #
   # top_terms_per_cluster(new_df, km, n_custers, vocab_frame, terms)


def top_terms_per_cluster(frame, km, num_clusters, vocab_frame, terms):
   print("Top terms per cluster:")
   print()

   # sort cluster centers by proximity to centroid
   order_centroids = km.cluster_centers_.argsort()[:, ::-1]

   for i in range(num_clusters):
      print("Cluster %d words:" % i, end='')

      for ind in order_centroids[i, :10]:  # replace 6 with n words per cluster
         print(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'), end=',')
      print()
      print()

      # print("Cluster %d titles:" % i, end='')
      # for err_code in frame.ix[i]['Error_Code'].values.tolist():
      #     print(' %s,' % err_code, end='')
      # print()
      # print()

   print()
   print()


def get_term_frequencies(tool, top_k=30, vocab=None):
   tool.preprocess()
   freq_count = tool.frequency_count()

   sortedFreq = []

   for w in sorted(freq_count, key=freq_count.get, reverse=True):
      sortedFreq.append((w, freq_count[w]))

   for i in range(min(top_k, len(sortedFreq))):
      if type(vocab) is not type(None):
         print(sortedFreq[i], vocab.ix[sortedFreq[i][0]].values.tolist()[:6])
      else:
         print(sortedFreq[i])


if __name__ == '__main__':
   main()
