##inactives analysis
import pandas as pd

mdf = pd.read_csv("inactives.csv")
cancels = 0
cncamt = 0
collections = 0
clctamt = 0
debtamt = 0
transferouts = 0
toutamt = 0
memberslist = mdf.get("membername")
totalmembers = len(memberslist)
for index, row in mdf.iterrows():
    if (row["status"]) == "cancel":
        cancels += 1
        cncamt += (row["invoiceamount"])
    elif (row["status"]) == "collections":
        collections += 1
        clctamt += (row["invoiceamount"])
        debtamt += (row["amountdue"])
    elif (row["status"]) == "transfer out":
        transferouts += 1
        toutamt += (row["invoiceamount"])
print("Total Members:",totalmembers)
print("Total Cancels:",cancels)
print("Total in Cancels $:",cncamt)
print("Total Collections:",collections)
print("Total in Collections $:",clctamt)
print("Total in Lost Dues $:",debtamt)
print("Total Transfers:",transferouts)
print("Total in Transfers $:",toutamt)
