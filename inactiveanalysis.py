import pandas as pd
idf = pd.read_csv("inactives.csv")
cancels = 0
cncamt = 0
collections = 0
clctamt = 0
debtamt = 0
transferouts = 0
toutamt = 0
j = 1
while j < 13:
    for index, row in idf.iterrows():
        if (row["month"]) == j:
            if (row["status"]) == "Cancel":
                cancels += 1
                cncamt += (row["Invoice Amount"])
            elif (row["status"]) == "Returned For Collection":
                collections += 1
                clctamt += (row["Invoice Amount"])
                debtamt += (row["amountdue"])
            elif (row["status"]) == "Transferred Account":
                transferouts += 1
                toutamt += (row["Invoice Amount"])
    print("Total Stats for Month #:",j)
    print("Total Cancels:",cancels,"in $:",cncamt)
    print("Total Collections:",collections," in $:",clctamt)
    print("In Deliquency $:",debtamt)
    print("Total Transfers:",transferouts," in $:",toutamt)
    cancels = 0
    cncamt = 0
    collections = 0
    clctamt = 0
    debtamt = 0
    transferouts = 0
    toutamt = 0
    j += 1
