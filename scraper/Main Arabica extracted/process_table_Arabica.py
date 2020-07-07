import pandas as pd
import numpy as np

df_list = []
files = 757 # the numbers of files you get, for instance: coffee_X_table_0.csv => files = X + 1

n = 0 # factor to don't consider the cell
for i in range(1, files):
	
	# filter the function format i, so only multiples of 8s
	# for instance, 1-1 = 0 or 9 - 1 = 8, so on
	# and do not update the variable n in the first step
	if ((i-1) % 8 == 0 and i != 1):
		n += 1

	# only consider values from column 1 and 4
	include = [1+8*n]
	if i in include:

		print('file # {}'.format(i))
		
		try:
			df1 = pd.read_csv('coffee_{}_table_0.csv'.format(i))
			df2 = pd.read_csv('coffee_{}_table_1.csv'.format(i))
			df3 = pd.read_csv('coffee_{}_table_2.csv'.format(i))
			df4 = pd.read_csv('coffee_{}_table_3.csv'.format(i))
			df5 = pd.read_csv('coffee_{}_table_4.csv'.format(i))

			df6 = pd.read_csv('coffee_{}_table_0.csv'.format(i+3)) #contact detail
			df7 = pd.read_csv('coffee_{}_table_1.csv'.format(i+3)) #contact detail
		except:
			# catch the error if happens
			print('ERROR: failed')
			break

		# df1
		"""
		   Unnamed: 0                                 0          1
		0           0                             90.58        NaN
		1           1        View Q Arabica Certificate        NaN
		2           2       Print Q Arabica Certificate        NaN
		3           3  Cupping Protocol and Descriptors        NaN
		4           4       View Green Analysis Details        NaN
		5           5                  Request a Sample        NaN
		6           6                           Species    Arabica
		7           7                             Owner  metad plc
		"""
		df1.columns = ['one','two']
		column1 = df1['one'].tail(1).tolist()
		data1 = df1['two'].tail(1).tolist()
		column1[0] = "Owner"

		df1_processed = pd.DataFrame([data1],columns=column1)

		# df2
		"""
		   Unnamed: 0                  0                                  1  \
		0           0  Country of Origin                           Ethiopia   
		1           1          Farm Name                          METAD PLC   
		2           2         Lot Number                                NaN   
		3           3               Mill                          METAD PLC   
		4           4         ICO Number                          2014/2015   
		5           5            Company  METAD Agricultural Developmet plc   
		6           6           Altitude                          1950-2200   
		7           7             Region                  GUJI-HAMBELA/GOYO   
		8           8           Producer                          METAD PLC   

		                    2                                   3  
		0      Number of Bags                                 300  
		1          Bag Weight                               60 kg  
		2  In-Country Partner  METAD Agricultural Development plc  
		3        Harvest Year                                2014  
		4        Grading Date                     April 4th, 2015  
		5               Owner                           metad plc  
		6             Variety                                 NaN  
		7              Status                           Completed  
		8   Processing Method                        Washed / Wet  
		"""
		df2.columns = ['one','two','three','four','five']
		colnames1 = df2['two'].tolist()
		colnames2 = df2['four'].tolist()
		data1 = df2['three'].tolist()
		data2 = df2['five'].tolist()

		df2_processed = pd.DataFrame([(data1+data2)],columns=(colnames1+colnames2))

		# df3
		"""
		   Unnamed: 0           0       1                 2              3
		0           0         NaN  Sample               NaN         Sample
		1           1       Aroma    8.67        Uniformity          10.00
		2           2      Flavor    8.83         Clean Cup          10.00
		3           3  Aftertaste    8.67         Sweetness          10.00
		4           4     Acidity    8.75     Cupper Points           8.75
		5           5        Body    8.50  Total Cup Points  Sample  90.58
		6           6     Balance    8.42               NaN            NaN
		"""
		df3.columns = ['one','two','three','four','five']
		colnames1 = df3['two'].tolist()
		colnames2 = df3['four'].tolist()
		data1 = df3['three'].tolist()
		data2 = df3['five'].tolist()

		df3_processed = pd.DataFrame([(data1+data2)],columns=(colnames1+colnames2))

		# df4
		"""
		   Unnamed: 0                     0               1                     2  \
		0           0              Moisture            12 %                 Color   
		1           1  Category One Defects  0 full defects  Category Two Defects   
		2           2               Quakers               0                   NaN   

		                3  
		0           Green  
		1  0 full defects  
		2             NaN  
		"""
		df4.columns = ['one','two','three','four','five']
		colnames1 = df4['two'].tolist()
		colnames2 = df4['four'].tolist()
		data1 = df4['three'].tolist()
		data2 = df4['five'].tolist()

		df4_processed = pd.DataFrame([(data1+data2)],columns=(colnames1+colnames2))

		# df5
		"""
		   Unnamed: 0                      0  \
		0           0             Expiration   
		1           1     Certification Body   
		2           2  Certification Address   
		3           3  Certification Contact   

		                                                   1  
		0                                    April 3rd, 2016  
		1                 METAD Agricultural Development plc  
		2  BAWA Center, 3rd Floor (Gerji), Addis Ababa, E...  
		3  Aman Adinew (Emebet Dinku) - +251-116-292534, ...  
		"""
		df5.columns = ['one','two','three']
		colnames1 = df5['two'].tolist()
		data1 = df5['three'].tolist()

		df5_processed = pd.DataFrame([data1],columns=colnames1)

		# df6
		"""
		,0,1
		0,Phone,(799) 790-1567
		1,City,Vila Velha
		2,State,Espirito Santo
		3,Zip,29122-680
		4,Country,Brazil
		"""
		df6.columns = ['one','two','three']
		colnames1 = df6['two'].tolist()
		data1 = df6['three'].tolist()

		df6_processed = pd.DataFrame([data1],columns=colnames1)

		# df7
		"""
		,0,1
		0,Company,Nestlé Brasil S/A
		1,Title,Gerente Agrícola Cafés
		"""
		df7.columns = ['one','two','three']
		colnames1 = df7['two'].tolist()
		data1 = df7['three'].tolist()

		df7_processed = pd.DataFrame([data1],columns=colnames1)

		# consolidated all data frames
		df = pd.concat([df1_processed,df2_processed,df3_processed,df4_processed,df5_processed, df6_processed, df7_processed], 1)
		df = df.rename(columns = {np.nan : "NA"})
		df_list.append(df)

# Create the data frame final
df_final = pd.concat(df_list, 0)
print(df_final.columns)
print(df_final.shape)
print(df_final.head())
df_final.to_csv('df_Arabica_Detail.csv')