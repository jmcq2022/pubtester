import pandas as p
x=5
#creates my BS id, this id will be used on all other systems to reference back to a specific report. Imagine it as a key
def bsidchecker(bsid,company,date,report,wordtotal,paragraphtotal,picturetotal):
    #checks if BSid is in total.csv, if not creates it with null values in all columns
    df = p.read_csv('total.csv')
    print(df)
    if bsid in df.bsid.values:
        print('bsid already created')
    else:
        print('bsid not there')
        if x == 5:
           # df = df.row.append(p.DataFrame({bsid,company,date,report,wordtotal,paragraphtotal,picturetotal}))
            df.loc[len(df.index)] = [bsid,company,date,report,wordtotal,paragraphtotal,picturetotal]
            print('added values to df')
            print(df)
            df.to_csv('total.csv',index= False)
            return(df)

bsidchecker(101,'testfirm',20200101,'annual',500,15,20)




