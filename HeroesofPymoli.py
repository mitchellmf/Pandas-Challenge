# Import csv dataset.
import pandas as pd
import csv as csv
purchase_df = pd.read_csv(r"C:\Users\mitch\Desktop\Analytical BootCamp\HOMEWORK\HW4 - Pandas\purchase_data.csv")
purchase_df.head()
# ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

# Total number of unique players.
print(f"Player Count")
print(f"--------------------------------------------------")
unique_players = len(purchase_df["SN"].unique())
print(f"Total Number of Players: {unique_players}")

# Total number of unique items.
print(" ")
print(f"Purchasing Analysis (Total)")
print(f"--------------------------------------------------")
unique_items = len(purchase_df["Item Name"].unique())
print(f"Number of Unique Items: {unique_items}")

# Average purchase price.
mean_price = round(purchase_df["Price"].mean(),2)
print(f"Average Purchase Price: {mean_price}")
# Total number of purchases.
sum_ids= purchase_df["Purchase ID"].count()
print(f"Total Number of Purchases: {sum_ids}")
# Total revenue (sum of prices in each order.
sum_price= purchase_df["Price"].sum()
print(f"Total Revenue: {sum_price}")

# ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

# Subsetting datasets by gender.
print(" ")
print(f"Gender Demographics")
print(f"--------------------------------------------------")

purch_df_men = purchase_df.loc[(purchase_df["Gender"] == "Male")]
purch_df_women = purchase_df.loc[(purchase_df["Gender"] == "Female")]
purch_df_other = purchase_df.loc[(purchase_df["Gender"] == " Other / Non-Disclosed")]
unique_men = len(purch_df_men["SN"].unique())
perc_men = round(unique_men * 100 / unique_players,1)
print(f"Total Number / Percentage of Men: {unique_men} / {perc_men}%")
unique_women = len(purch_df_women["SN"].unique())
perc_women = round(unique_women * 100 / unique_players,1)
print(f"Total Number / Percentage of Women: {unique_women} / {perc_women}%")
unique_other = len(purch_df_other["SN"].unique())
perc_other = round(unique_other * 100 / unique_players,1)
print(f"Total Number / Percentage of Other/Non-Disclosed: {unique_other} / {perc_other}%")
print(" ")
print(f"Purchasing Analysis (by Gender)")
print(f"--------------------------------------------------")

# Average purchase price by gender.
mean_price_men = round(purch_df_men["Price"].mean(),2)
print(f"Average Purchase Price for Men: {mean_price_men}")
mean_price_women = round(purch_df_women["Price"].mean(),2)
print(f"Average Purchase Price for Women: {mean_price_women}")


# Total number of purchases by gender.
sum_ids_men = purch_df_men["Purchase ID"].count()
print(f"Total Number of Purchases for Men: {sum_ids_men}")
sum_ids_women = purch_df_women["Purchase ID"].count()
print(f"Total Number of Purchases for Women: {sum_ids_women}")

# Total revenue (sum of prices in each order by gender.
sum_price_men = purch_df_men["Price"].sum()
print(f"Total Revenue for Men: {sum_price_men}")
sum_price_women = purch_df_women["Price"].sum()
print(f"Total Revenue for Women: {sum_price_women}")

# ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

# Obtain the totals and means by SN for men. 
purch_df_men_grpsum = purch_df_men.groupby('SN')['Price'].sum()
purch_df_men_grpsum = purch_df_men_grpsum.drop_duplicates()

merge_df_men_sum = pd.merge(purch_df_men_grpsum, purch_df_men, on='SN', how='left')
merge_df_men_sum = merge_df_men_sum.rename(columns= {'Price_x' : 'Total Price' , 'Price_y' : 'Price'})

purch_df_men_grpmean = purch_df_men.groupby('SN')['Price'].mean()
merge_df_men_mean = pd.merge(purch_df_men_grpmean, purch_df_men, on='SN', how='left')
merge_df_men_mean = merge_df_men_mean.rename(columns= {'Price_x' : 'Total Price' , 'Price_y' : 'Price'})

# Obtain the totals and means by SN for women.
purch_df_women_grpsum = purch_df_women.groupby('SN')['Price'].sum()
purch_df_women_grpsum = purch_df_women_grpsum.drop_duplicates()
merge_df_women_sum = pd.merge(purch_df_women_grpsum, purch_df_women, on='SN', how='left')
merge_df_women_sum = merge_df_women_sum.rename(columns= {'Price_x' : 'Total Price' , 'Price_y' : 'Price'})
purch_df_women_grpmean = purch_df_women.groupby('SN')['Price'].mean()
merge_df_women_mean = pd.merge(purch_df_women_grpmean, purch_df_women, on='SN', how='left')
merge_df_women_mean = merge_df_women_mean.rename(columns= {'Price_x' : 'Total Price' , 'Price_y' : 'Price'})


# Average Purchase Total per Person by Gender
mean_price_men = round(merge_df_men_sum["Total Price"].mean(),2)
print(f"Average Purchase Price for Men: {mean_price_men}")

mean_price_women = round(merge_df_women_sum["Total Price"].mean(),2)
print(f"Average Purchase Price for Women: {mean_price_women}")


print(" ")
print(f"Purchasing Analysis (by Age Groups)")
print(f"--------------------------------------------------")

bins = [ 0 , 10, 20, 30, 40, 100 ]
group_names = [ 'Ages 0-9', 'Ages 10-19', 'Ages 20-29' , 'Ages 30-39' , 'Ages 40+' ]
purchase_df['Age Group'] = pd.cut( purchase_df['Age'], bins, labels = group_names, include_lowest = True )
# Subsetting datasets by age group.
purch_df_agegroup_A = purchase_df.loc[(purchase_df["Age Group"] == "Ages 0-9")]
purch_df_agegroup_B = purchase_df.loc[(purchase_df["Age Group"] == "Ages 10-19")]
purch_df_agegroup_C = purchase_df.loc[(purchase_df["Age Group"] == "Ages 20-29")]
purch_df_agegroup_D = purchase_df.loc[(purchase_df["Age Group"] == "Ages 30-39")]
purch_df_agegroup_E = purchase_df.loc[(purchase_df["Age Group"] == "Ages 40+")]



# Average purchase price by age group.
mean_price_agegroup_A = round(purch_df_agegroup_A["Price"].mean(),2)
print(f"Average Purchase Price for Age Group 0-9: {mean_price_agegroup_A}")
mean_price_agegroup_B = round(purch_df_agegroup_B["Price"].mean(),2)
print(f"Average Purchase Price for Age Group 10-19: {mean_price_agegroup_B}")
mean_price_agegroup_C = round(purch_df_agegroup_C["Price"].mean(),2)
print(f"Average Purchase Price for Age Group 20-29: {mean_price_agegroup_C}")
mean_price_agegroup_D = round(purch_df_agegroup_D["Price"].mean(),2)
print(f"Average Purchase Price for Age Group 30-39: {mean_price_agegroup_D}")
mean_price_agegroup_E = round(purch_df_agegroup_E["Price"].mean(),2)
print(f"Average Purchase Price for Age Group 40+: {mean_price_agegroup_E}")

# Total number of purchases by age group.
sum_ids_agegroup_A = purch_df_agegroup_A["Purchase ID"].count()
print(f"Total Number of Purchases for Age Group 0-9: {sum_ids_agegroup_A}")
sum_ids_agegroup_B = purch_df_agegroup_B["Purchase ID"].count()
print(f"Total Number of Purchases for Age Group 10-19: {sum_ids_agegroup_B}")
sum_ids_agegroup_C = purch_df_agegroup_C["Purchase ID"].count()
print(f"Total Number of Purchases for Age Group 20-29: {sum_ids_agegroup_C}")
sum_ids_agegroup_D = purch_df_agegroup_D["Purchase ID"].count()
print(f"Total Number of Purchases for Age Group 30-39: {sum_ids_agegroup_D}")
sum_ids_agegroup_E = purch_df_agegroup_E["Purchase ID"].count()
print(f"Total Number of Purchases for Age Group 40+: {sum_ids_agegroup_E}")


# Total revenue (sum of prices in each order by age group.
sum_price_agegroup_A = round(purch_df_agegroup_A["Price"].sum(),2)
print(f"Total Revenue for Age Group 0-9: {sum_price_agegroup_A}")
sum_price_agegroup_B = round(purch_df_agegroup_B["Price"].sum(),2)
print(f"Total Revenue for Age Group 10-19: {sum_price_agegroup_B}")
sum_price_agegroup_C = round(purch_df_agegroup_C["Price"].sum(),2)
print(f"Total Revenue for Age Group 20-29: {sum_price_agegroup_C}")
sum_price_agegroup_D = round(purch_df_agegroup_D["Price"].sum(),2)
print(f"Total Revenue for Age Group 30-39: {sum_price_agegroup_D}")
sum_price_agegroup_E = round(purch_df_agegroup_E["Price"].sum(),2)
print(f"Total Revenue for Age Group 40+: {sum_price_agegroup_E}")

