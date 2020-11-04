import pandas as pd

# Load the user data set
df = pd.read_csv("details.csv")


def ck_pass(name1, name2, email1, ctn):
    # variable assigning
    first_name = name1
    sur_name = name2
    e_mail = email1
    cont = int(ctn)

    df1 = df[df['First Name'] == first_name]
    print(df1)
    df2 = df1[df1['Surname'] == sur_name]
    print(df2)
    df3 = df2[df2['e-mail address'] == e_mail]
    print(df3)
    df4 = df3[df3['Contact Number'] == cont]
    print(df4)

    flag_password = df4['User Index'].sum()
    if flag_password == 0:
        res = 0
    else:
        res = 1
        name1 = df4['user name'].sum()
        name2 = df4['password'].sum()
    return res, name1, name2
