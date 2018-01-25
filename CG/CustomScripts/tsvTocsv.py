import csv

txt_file = r"mytxt.txt"
csv_file = r"mycsv.csv"

# use 'with' if the program isn't going to immediately terminate
# so you don't leave files open
# the 'b' is necessary on Windows
# it prevents \x1a, Ctrl-z, from ending the stream prematurely
# and also stops Python converting to / from different line terminators
# On other platforms, it has no effect
txt_file = "../Data/new10.txt"
csv_file = "../Data/featureExtractedDic/feature_dic.csv"
in_txt = csv.reader(open(txt_file, "rb"), delimiter = '\t')
out_csv = csv.writer(open(csv_file, 'a'))

out_csv.writerows(in_txt)