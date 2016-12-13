from __future__ import print_function

import CrashAnalysis


def main():
   tool = CrashAnalysis.TextAnalysis('./data/Crashes1.csv')
   # tool.get_customer_descriptions_by_version('2016040014')
   # vocab_frame = tool.create_vocab_frame()
   # get_term_frequencies(tool, vocab=vocab_frame)
   pro_name = 'ProSeries - 2016'
   basic_name = 'ProSeries Basic Edition - 2016'

   # print(pro_name)
   # tool.frequency('2016040014', product_id=pro_name, top=50)
   # model = tool.lda('2016040014', product_id=pro_name, num_topics=10)
   # tool.print_topics(model, num_words=10)
   #
   # print()
   # print(basic_name)
   # tool.frequency('2016040014', product_id=basic_name, top=50)
   #
   # model = tool.lda('2016040014', product_id=basic_name, num_topics=10)
   # tool.print_topics(model, num_words=10)

   vocab, sortedFreq = tool.frequency('2016040014')

   err_codes = tool.find_error_codes(vocab, sortedFreq, tool.read_csv('./data/Crashes1.csv'))

   print('ERROR CODES')
   for word, count in sortedFreq:
      print(word)
      print(err_codes[word][err_codes[word] > 2])

      if count < 7:
         break

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


if __name__ == '__main__':
   main()
