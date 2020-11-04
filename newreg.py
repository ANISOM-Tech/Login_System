import pandas as pd

df = pd.read_csv("details.csv")


def reg_new(f_name, s_name, d_o_b, e_m, ct_n):
    f1_name = f_name
    sr_name = s_name
    dob = d_o_b
    email = e_m
    cont = ct_n
    ui = (df['User Index'].max() + 1)

    re = "."
    fs = sr_name[0]
    re1 = "".join([re, fs])
    urname = f1_name + str(re1)

    pswd = f1_name.lower()+str(dob.year)

    dfn = pd.DataFrame({'User Index': [ui], 'First Name': [f1_name], 'Surname': [sr_name], 'D.O.B': [dob],
                        'Contact Number': [cont],
                        'e-mail address': [email], 'user name': [urname], 'password': [pswd]})

    dfn1 = df.append(dfn, ignore_index=True)
    dfn1.to_csv('details.csv', index=False)
    return urname, pswd
