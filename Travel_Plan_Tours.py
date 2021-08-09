def Travel_Plan_Tours(city, rating_high, cat_list_tours):
	df_review = pd.read_excel("Lakbay/Target_Datasets/tours_and_attractions_review.xlsx")
	df_element = pd.read_excel("Lakbay/Target_Datasets/tours_and_attractions.xlsx")
	#df_element = df_element.dropna()
	rating_low = 1 #override

	#step 3
	#code priority to target city not adjacent
	if city in temp_cities:# or city in NCR or city in I or city in II or city in III or city in IV_A or city in IV_B or city in V:
		adjacent = pd.read_excel("Lakbay/Adjacent_Cities_Dataset/Luzon.xlsx")
		#adjacent = pd.read_excel("Lakbay.ph/Adjacent_Cities_Dataset/%s.xlsx",%Island_Group)
		adjacent = adjacent.loc[adjacent["Target"] == city]
		adjacent = (adjacent.Adjacent.apply(lambda x: pd.Series(x.split(', '))).transpose().iloc[:,0]).values.tolist()
		adjacent.append(city)
		adjacent.reverse()
		x = df_element[df_element['location'].apply(lambda x: pd.Series(x.split(', ')).isin(adjacent).any())]
	tags_type = pd.read_excel("Lakbay/Target_Datasets/tours-tags.xlsx")
	tag_res = tags_type.iloc[:,tags_type.columns.isin(cat_list_tours)]
	dct = {}
	for i in tag_res.columns:
		dct['list:%s' % i] = tag_res[i].dropna().values.tolist()
	tag_merged = []
	for i in dct:
		list(map(lambda x: tag_merged.append(x), dct[i]))
	#step 4
	#content filtering
	uid_df0 = x[x['type'].apply(lambda y: pd.Series(y.split(', ')).isin(tag_merged).any())]
	uid_df1 = x.loc[(x['ratings'] >= rating_low) & (x['ratings'] <= rating_high)]
	if len(uid_df0) >= len(uid_df1):# and len(uid_df1) >= len(uid_df2) and len(uid_df2) >= len(uid_df3):
		uid_df2 = uid_df0.merge(uid_df1, how = 'inner' ,indicator=False)
		uid_dfF = uid_df2.merge(df_review, on = ['name','ratings'] ,indicator = False) #change to index format
	elif len(uid_df1) >= len(uid_df0):# and len(uid_df1) >= len(uid_df3) and len(uid_df3) >= len(uid_df2):
		uid_df2 = uid_df1.merge(uid_df0, how = 'inner' ,indicator=False)
		uid_dfF = uid_df2.merge(df_review, on = ['name','ratings'] ,indicator=False) #change to index format
	#step 5
	#append all items content filtered
	uid_dfF_i = uid_dfF.name.value_counts().to_frame().reset_index()
	items = []
	for i in range(len(uid_dfF_i)):
		items.append(uid_dfF_i.iloc[i][0])
	items = list(set(items))
	#step 6
	#append all matched user ids
	uid_dfF_u = uid_dfF.user_id.value_counts().to_frame().reset_index()
	uid = []
	for i in range(len(uid_dfF_u)):
		uid.append(uid_dfF_u.iloc[i][0])
	uid = list(set(uid))
	#step 7
	#new dataframe reviews dataset filtered by user ids from previous step
	dfr = df_review[df_review.user_id.isin(uid)]
	dfr = dfr[~dfr.name.isin(items)]
	#append all items content filtered
	dfr = dfr.name.value_counts().to_frame().reset_index()
	#step 8
	#append items
	items = []
	for i in range(len(dfr)):
		items.append(dfr.iloc[i][0])
	items = list(set(items))
	#step 9
	#new dataframe with element dataset filtered by items on previous step
	df_element = df_element[df_element.name.isin(items)]
	df_element.head()
	#step 10
	#code priority to target city not adjacent
	if city in temp_cities:#CAR or city in NCR or city in I or city in II or city in III or city in IV_A or city in IV_B or city in V:
		adjacent = pd.read_excel("Lakbay/Adjacent_Cities_Dataset/Luzon.xlsx")
		adjacent = adjacent.loc[adjacent["Target"] == city]
		adjacent = (adjacent.Adjacent.apply(lambda x: pd.Series(x.split(', '))).transpose().iloc[:,0]).values.tolist()
		adjacent.append(city)
		adjacent.reverse()
		x = df_element[df_element['location'].apply(lambda x: pd.Series(x.split(', ')).isin(adjacent).any())]
	#step 11
	#apply model to get estimate scores using uids
	d = {}
	for i in range(len(uid)):
		d['df:%s' % i] = x
		d['df:%s' % i]['Estimate_Score'] = d['df:%s' % i]['name'].apply(lambda iid : SlopeOne_Model.predict(uid[i], iid, r_ui = None, clip = True, verbose = False).est)
		d['df:%s' % i] = d['df:%s' % i].sort_values('Estimate_Score', ascending = False)
	#merge them all
	for i in range(len(d)):
		if (i+1) < len(d):
			d['df:%s' % (i+1)] = d['df:%s' % i].merge(d['df:%s' % (i+1)], how = 'outer', indicator = False)
		else: break
	if (len(d)-1) <= 0: alpha = d['df:0']
	else: alpha = d['df:%s' % (len(d)-1)]
	#step 12
	#average scores and sort descending
	alpha["avg"] = alpha["name"].apply(lambda x: alpha['Estimate_Score'].loc[alpha['name'] == x].mean())
	print (alpha.drop_duplicates(subset = 'name').sort_values(by = 'avg',ascending = False))
	alpha = alpha.drop_duplicates(subset = 'name').sort_values(by = 'avg',ascending = False).drop(columns = ['Estimate_Score', 'avg'])
	#final output sort by location priority
	alpha = alpha[alpha['location'].apply(lambda x: pd.Series(x.split(', ')).isin(adjacent).any())]
	alpha.location = alpha.location.astype("category")
	alpha.location.cat.set_categories(adjacent, inplace=True)
	alpha = alpha.sort_values(["location","ratings"])#.reset_index().drop(columns=['index']).reset_index()
	alpha = alpha.head(3)
	return (alpha)
	#alpha
