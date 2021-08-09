def Travel_Plan_Restos(city, rating_high):
    df_review = pd.read_excel("Lakbay/Target_Datasets/restaurants_review.xlsx")
    df_element = pd.read_excel("Lakbay/Target_Datasets/restaurants.xls")
    df_element = df_element.dropna()
    cat_list_restos = ["Vegetarian Friendly", "Southeast Asian", "Other Chinese Cuisine"]#, "International", "Fast Food", "Filipino", "American", "Steakhouse", "Cafe", "Italian", "Singaporean", "Mexican","Grill", "Dessert", "Pizza", "European", "Caribbean", "Barbecue", "Seafood", "Fusion", "Japanese", "Bakery", "Contemporary", "Thai", "Diner", "Pub", "Bar", "Chinese", "Asian"] #override

    rating_low = 1 #override

    #step 3
    #code priority to target city not adjacent
    if city in temp_cities:#CAR or city in NCR or city in I or city in II or city in III or city in IV_A or city in IV_B or city in V:
        #os.chdir("Luzon/CAR")
        adjacent = pd.read_excel("Lakbay/Adjacent_Cities_Dataset/Luzon.xlsx")
        adjacent = adjacent.loc[adjacent["Target"] == city]
        adjacent = (adjacent.Adjacent.apply(lambda x: pd.Series(x.split(', '))).transpose().iloc[:,0]).values.tolist()
        adjacent.append(city)
        adjacent.reverse()
        x = df_element[df_element['location'].apply(lambda x: pd.Series(x.split(', ')).isin(adjacent).any())]
    #step 4
    #content filtering
    uid_df0 = x[x['type'].isin(cat_list_restos)]
    uid_df1 = x.loc[(x['ratings'] >= rating_low) & (x['ratings'] <= rating_high)]
    if len(uid_df0) >= len(uid_df1):
        uid_df2 = uid_df0.merge(uid_df1, how = 'inner' ,indicator=False)
        uid_dfF = uid_df2.merge(df_review, on = ['name','ratings'] ,indicator = False)
    elif len(uid_df1) >= len(uid_df0):
        uid_df2 = uid_df1.merge(uid_df0, how = 'inner' ,indicator=False)
        uid_dfF = uid_df2.merge(df_review, on = ['name','ratings'] ,indicator=False)
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
    #fin_items = []
    for i in range(len(dfr)):
        items.append(dfr.iloc[i][0])
    items = list(set(items))
    #step 9
    #new dataframe with element dataset filtered by items on previous step
    df_element = df_element[df_element.name.isin(items)]
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
        d['df:%s' % i]['Estimate_Score'] = d['df:%s' % i]['name'].apply(lambda iid: CoClustering_Model.predict(uid[i], iid, r_ui=None, clip=True, verbose=False).est)
        d['df:%s' % i] = d['df:%s' % i].sort_values('Estimate_Score', ascending = False)
    for i in range(len(d)):
        if (i+1) < len(d):
            d['df:%s' % (i+1)] = d['df:%s' % i].merge(d['df:%s' % (i+1)], how = 'outer', indicator = False)
        else: break
    #step 12
    #average scores and sort descending
    if (len(d)-1) <= 0: bravo = d['df:0']
    else: bravo = d['df:%s' % (len(d)-1)]
    bravo["avg"] = bravo["name"].apply(lambda x: bravo['Estimate_Score'].loc[bravo['name'] == x].mean())
    print (bravo.drop_duplicates(subset = 'name').sort_values(by = 'avg',ascending = False))
    bravo = bravo.drop_duplicates(subset = 'name').sort_values(by = 'avg',ascending = False).drop(columns = ['Estimate_Score', 'avg'])
    #final output sort by location priority
    bravo = bravo[bravo['location'].apply(lambda x: pd.Series(x.split(', ')).isin(adjacent).any())]
    bravo.location = bravo.location.astype("category")
    bravo.location.cat.set_categories(adjacent, inplace=True)
    bravo = bravo.sort_values(["location","ratings"])#.reset_index().drop(columns=['index']).reset_index()
    bravo = bravo.head(1)
    return (bravo)
    #bravo
