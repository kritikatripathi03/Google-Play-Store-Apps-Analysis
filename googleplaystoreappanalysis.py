import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
df= pd.read_csv("googleplaystore.csv")
df['Reviews'] = pd.to_numeric(df['Reviews'])
df['Installs'] = pd.to_numeric(df['Installs'])
df['Rating'] = pd.to_numeric(df['Rating'])
#Data analysis:
def csv():
    print(df)
def count():
    #Number of apps in total
    counts = df["App"].count()
    print("There are ", str(counts)," in the analysis.")
def appinfo():
    #Printing Information of any user specified app
    row = input("Please enter the name of any App from the given to analyse it: ")
    print(df[df["App"]==row])
def col():
    field= str(input("Enter the name of the field you want me to display:"))
    field1=df[["App", field]].copy()
    print(field1)
    q=input("Do you want me to sort the values in this field for you? (Yes/No):\n")
    if q== "Yes":
        field2= field1.sort_values(by=field)
        print(field2)
    else:
        print("Okay! Thank you so much!")
def drop():
    print(df.columns)
    delete= eval(input("Enter the field(s) you want me to delete (in square brackets):\n"))
    df.drop(delete, axis=1)
    print(df)
    print(delete," Successfully deleted!")
def max():
    print("These are the columns\n", df.columns)
    field=eval(input("Enter the column names as list in square bracket"))
    print('Print the maximum values of the ',field,' columns')
    print(df[field].max())
    print('Print the minimum values of the ', field, ' columns')
    print(df[field].min())
def catmax():
    #Maximum Rating per Category
    print("The maximum ratings for each Category is:")
    print(pd.pivot_table(df, index=["Category"], values=["Rating"], aggfunc="max"))
    q=input("Do you want me to name the Apps with top Ratings? (Yes/No):\n")
    if q== 'Yes':
        print("Here are the apps with maximum rating per Category:")
        df1=df.drop(['Reviews', 'Size', 'Price', 'Genres', "Current Ver", 'Installs','Type',
                     'Content Rating','Android Ver'], axis=1)
        df2=df1.groupby(["Category"])
        df3=df2.apply(lambda x: x.sort_values(["Rating"], ascending=False)).reset_index(drop=True)
        df4=df3.groupby('Category').head(1)
        print(df4)
        cmap = plt.cm.tab10
        colors = cmap(np.arange(len(df)) % cmap.N)
        df4.plot.barh(x='Category', y='Rating', color=colors)
        plt.show()
    elif q=="No":
        print("Okay! Thank you so much!")
    else:
        print("Sorry! I'm unable to understand what you are trying to say.")
def field():
    #sorting according to a particular row
    field=input("Write any of the given fields to print the number of Apps according to it:\na. Category\n"
                "b. Installs\nc. Content Rating\nd. Type\ne. Android Ver\nf. Current Ver\ng. Genres\n"
                "h. Current Ver\n")
    print("The Field has the following distribution of Apps:")
    unique= df[field].unique()
    print(unique)
    print("There are ", len(unique)," ", field, "in total.")
    q=input("Do you want me to show you the app information for every distribution")
    df.set_index(field)
    if q=="Yes":
        a=str(input("For which Distribution?\n"))
        b= df[df[field] == a]
        print(b)
        num = pd.pivot_table(df, index=[field], values=["App"], aggfunc="count")
        num.plot.pie(y="App", figsize=(10, 5), labeldistance=None)
        plt.legend(prop={'size': 6}, ncol=2, bbox_to_anchor=(0.85, 1.025), loc="upper left")
        plt.show()
    else:
        print("Okay! Thank you so much!")
def maxmin():
    #Minimum/Maximum Rating/Reviews/ Installs
    field=str(input("Select a field from the given list:\n"
                    "a. Reviews\n"
                    "b. Rating\n"
                    "c. Installs"))
    df1=df[["App","Reviews","Rating","Installs"]].copy()
    n=int(input("Enter the number of apps you want to be displayed:"))
    df1.sort_values(by=field, ascending=False)
    print("The app with maximum ", field," is:")
    print(df1.head(n))
    print("The app with minimum ", field, " is:")
    print(df1.tail(n))
def agg():
    field=input("1. Category 2. Genres 3. Type 4. Content Rating\n "
                "Enter the name of the field from the above list:\n")
    perform=input("1. Installs 2. Rating 3. Reviews 4. Price\n"
                  "Enter the name of the field from the above list whose mean you want to find:\n")
    df.groupby(field)
    print(pd.pivot_table(df, index=[field], values=[perform], aggfunc="mean"))
def reviews():
    reviews = df[['Category', 'Reviews']].copy()
    reviews['Reviews'] = pd.to_numeric(reviews['Reviews'])
    num = pd.pivot_table(df, index=["Category"], values=["Reviews"], aggfunc="sum")
    print(num)
    num.boxplot(color='blue', vert=0, notch=True)
    plt.show()
def price():
    price=df[["App","Price"]].copy()
    price["Price"]=pd.to_numeric(price["Price"])
    price.plot(color="blue")
    plt.title("Apps Pricing")
    plt.xlabel("No. Of Apps")
    plt.ylabel("Price")
    plt.show()
def andver():
    print("Play store has these many Android Version ranges:")
    print(df["Android Ver"].unique())
    version= str(input("Type your Android Version Range as per the above ranges:"))
    app=str(input("Enter the name of the app you want to use:"))
    b= df[df["App"] == app]
    if version in b.values:
        print("Yes! Your Android Version is up to date for ", app, '!')
    else:
        print("Sorry! The desired Android Version does not match.")
def hist():
    df.hist()
    plt.show()
#menu
print("_________________________________________________________")
print(" ", "Google Play Store Apps"," ")
print("*********************************************************")
name = input("Please enter you name:")
print("Hello ", name, "! I'm your Analysis Assistant, Anna, here to help you with the analysis!")
print("Please choose and option from the given menu:\n"
      "1. Display the number of Apps in the Data Analysis\n"
      "2. Find any App's information from the dataset\n"
      "3. Display a particular field\n4. Drop field(s) from data set\n"
      "4. Show maximum/ minimum for a particular field\n"
      "5. Show maximum Ratings- Category wise\n"
      "6. Display the number of apps according to a particular field with details\n"
      "7. Display the App with Maximum and minimum Rating/ Reviews/ Installs\n"
      "8. Tell the mean number of Installs/ Ratings/ Reviews/ Price according to "
      "Category/ Genre/ Type/ Content Rating\n"
      "9. Calculate the sum of reviews for each Category\n"
      "10. Show the price distribution of all apps in dataset\n"
      "11. Check if I can run my favourite app on my Android phone"
      "12. Make a histogram for the dataset\n"
      "13. Display th whole CSV File\n"
      "14. Exit")
while True:
    ch=int(input("Enter your choice here(1/2/3/...:"))
    if ch==1:
        count()
    if ch==2:
        appinfo()
    if ch==3:
        col()
    if ch==4:
        drop()
    if ch==5:
        max()
    if ch==6:
        catmax()
    if ch==7:
        field()
    if ch==8:
        maxmin()
    if ch==9:
        agg()
    if ch==10:
        reviews()
    if ch==11:
        price()
    if ch==12:
        andver()
    if ch==13:
        hist()
    if ch==14:
        csv()
    if ch==15:
        print("Thank you so much! Have a great day!")
        sys.exit()
