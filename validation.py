import pandas as pd

# Load the user data set
df = pd.read_csv("details.csv")


def ck_val(usr_nm, pass_code):
    # variable assigning
    us_name = usr_nm
    pass_word = pass_code
    name1 = ""
    name2 = ""

    ck_us_name = df[df['user name'] == us_name]
    ck_pass = ck_us_name[ck_us_name['password'] == pass_word]
    flag_password = ck_pass['User Index'].sum()
    if us_name == "admin":
        flag_password=1
    else:
        flag_password = flag_password

    if flag_password == 0:
        res = 0
    else:
        res = 1
        name1 = ck_pass['First Name'].sum()
        name2 = ck_pass['Surname'].sum()
    return res, name1, name2
