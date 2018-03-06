import pandas as pd
import pprint
import csv

pp = pprint.PrettyPrinter(indent=4)
def getClassDistributions():

    df = pd.read_csv("/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/featureExtractedDic/conversationparserWithAllFeatures.csv")
    print df.shape
    # result_array = df['result']
    #
    # result_dic = {}
    # for i in result_array:
    #     if i not in result_dic:
    #         result_dic[i] = 1
    #     else:
    #         result_dic[i] +=1
    #
    # print result_dic
    #
    # percent = {}
    # for i,v in result_dic.iteritems():
    #     percent[i] = float(v)/df.shape[0]
    #
    # print percent

    result_dic = {}
    for index, row in df.iterrows():
        if row['result'] in result_dic:
            result_dic[row['result']].append([row['type'], row['source']])
        else:
            result_dic[row['result']] = []
            result_dic[row['result']].append([row['type'], row['source']])

    dic = {}
    for key, value in result_dic.iteritems():

        for val in value:
            if str(val[1] +"_"+ val[0]) not in dic:
                dic[val[1] +"_"+ val[0]] = {'CORRECT':0, 'NO_RESPONSE':0 , 'SKIP':0, 'OUT_OF_TIME':0, 'WRONG':0}
            else:
                dic[val[1] + "_" + val[0]][key] += 1


    for key, value in dic.iteritems():
        try:
            dic[key].update({'TOTAL':value['CORRECT']+value['WRONG']+value['NO_RESPONSE']+value['OUT_OF_TIME']+value['SKIP']})
            dic[key].update({'CORRECT/WRONG':float(value['CORRECT'])/float(value['WRONG'])})
        except:
            dic[key].update({'CORRECT/WRONG': 0})

    pp.pprint(dic)

    out_csv = csv.writer(open("/Users/vaibhavdesai/Documents/Projects/ClueGenerator/CG/Data/chartsExcel/ch1.csv", 'a'))
    header = ['Source_type', 'CORRECT', 'CORRECT/WRONG', 'NO_RESPONSE', 'OUT_OF_TIME', 'SKIP', 'TOTAL', 'WRONG']
    out_csv.writerow(header)
    for key, value in dic.iteritems():
        out_csv.writerow([key,dic[key]['CORRECT'],dic[key]['CORRECT/WRONG'],dic[key]['NO_RESPONSE'],dic[key]['OUT_OF_TIME'],dic[key]['SKIP'],dic[key]['TOTAL'],dic[key]['WRONG']])







getClassDistributions()