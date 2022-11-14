import pandas as pd
idf = pd.read_csv("inactives.csv")
cancels = 0
cncamt = 0
collections = 0
clctamt = 0
debtamt = 0
transferouts = 0
toutamt = 0
jandf = idf.query('month == 1')
for index, row in jandf.iterrows():
    if (row["status"]) == "Cancel":
        cancels += 1
        cncamt += (row["Invoice Amount"])
    elif (row["status"]) == "Returned for Collection":
        collections += 1
        clctamt += (row["Invoice Amount"])
        debtamt += (row["amountdue"])
    elif (row["status"]) == "Transferred Account":
        transferouts += 1
        toutamt += (row["Invoice Amount"])
print("Total Cancels:",cancels,"in $:",cncamt)
print("Total Collections:",collections," in $:",clctamt)
print("In Deliquency:",debtamt)
print("Total Transfers:",transferouts," in $:",toutamt)
cancels = 0
cncamt = 0
collections = 0
clctamt = 0
debtamt = 0
transferouts = 0
toutamt = 0
febdf = idf.query('month == 2')
for index, row in febdf.iterrows():
    if (row["status"]) == "Cancel":
        cancels += 1
        cncamt += (row["Invoice Amount"])
    elif (row["status"]) == "Returned for Collection":
        collections += 1
        clctamt += (row["Invoice Amount"])
        debtamt += (row["amountdue"])
    elif (row["status"]) == "Transferred Account":
        transferouts += 1
        toutamt += (row["Invoice Amount"])
print("Total Cancels:",cancels,"in $:",cncamt)
print("Total Collections:",collections," in $:",clctamt)
print("In Deliquency:",debtamt)
print("Total Transfers:",transferouts," in $:",toutamt)
cancels = 0
cncamt = 0
collections = 0
clctamt = 0
debtamt = 0
transferouts = 0
toutamt = 0
mardf = idf.query('month == 3')
for index, row in mardf.iterrows():
    if (row["status"]) == "Cancel":
        cancels += 1
        cncamt += (row["Invoice Amount"])
    elif (row["status"]) == "Returned for Collection":
        collections += 1
        clctamt += (row["Invoice Amount"])
        debtamt += (row["amountdue"])
    elif (row["status"]) == "Transferred Account":
        transferouts += 1
        toutamt += (row["Invoice Amount"])
print("Total Cancels:",cancels,"in $:",cncamt)
print("Total Collections:",collections," in $:",clctamt)
print("In Deliquency:",debtamt)
print("Total Transfers:",transferouts," in $:",toutamt)
cancels = 0
cncamt = 0
collections = 0
clctamt = 0
debtamt = 0
transferouts = 0
toutamt = 0
aprdf = idf.query('month == 4')
for index, row in aprdf.iterrows():
    if (row["status"]) == "Cancel":
        cancels += 1
        cncamt += (row["Invoice Amount"])
    elif (row["status"]) == "Returned for Collection":
        collections += 1
        clctamt += (row["Invoice Amount"])
        debtamt += (row["amountdue"])
    elif (row["status"]) == "Transferred Account":
        transferouts += 1
        toutamt += (row["Invoice Amount"])
print("Total Cancels:",cancels,"in $:",cncamt)
print("Total Collections:",collections," in $:",clctamt)
print("In Deliquency:",debtamt)
print("Total Transfers:",transferouts," in $:",toutamt)
cancels = 0
cncamt = 0
collections = 0
clctamt = 0
debtamt = 0
transferouts = 0
toutamt = 0
maydf = idf.query('month == 5')
for index, row in maydf.iterrows():
    if (row["status"]) == "Cancel":
        cancels += 1
        cncamt += (row["Invoice Amount"])
    elif (row["status"]) == "Returned for Collection":
        collections += 1
        clctamt += (row["Invoice Amount"])
        debtamt += (row["amountdue"])
    elif (row["status"]) == "Transferred Account":
        transferouts += 1
        toutamt += (row["Invoice Amount"])
print("Total Cancels:",cancels,"in $:",cncamt)
print("Total Collections:",collections," in $:",clctamt)
print("In Deliquency:",debtamt)
print("Total Transfers:",transferouts," in $:",toutamt)
cancels = 0
cncamt = 0
collections = 0
clctamt = 0
debtamt = 0
transferouts = 0
toutamt = 0
jundf = idf.query('month == 6')
for index, row in jundf.iterrows():
    if (row["status"]) == "Cancel":
        cancels += 1
        cncamt += (row["Invoice Amount"])
    elif (row["status"]) == "Returned for Collection":
        collections += 1
        clctamt += (row["Invoice Amount"])
        debtamt += (row["amountdue"])
    elif (row["status"]) == "transfer out":
        transferouts += 1
        toutamt += (row["Invoice Amount"])
print("Total Cancels:",cancels,"in $:",cncamt)
print("Total Collections:",collections," in $:",clctamt)
print("In Deliquency:",debtamt)
print("Total Transfers:",transferouts," in $:",toutamt)
cancels = 0
cncamt = 0
collections = 0
clctamt = 0
debtamt = 0
transferouts = 0
toutamt = 0
juldf = idf.query('month == 7')
for index, row in juldf.iterrows():
    if (row["status"]) == "Cancel":
        cancels += 1
        cncamt += (row["Invoice Amount"])
    elif (row["status"]) == "Returned for Collection":
        collections += 1
        clctamt += (row["Invoice Amount"])
        debtamt += (row["amountdue"])
    elif (row["status"]) == "Transferred Account":
        transferouts += 1
        toutamt += (row["Invoice Amount"])
print("Total Cancels:",cancels,"in $:",cncamt)
print("Total Collections:",collections," in $:",clctamt)
print("In Deliquency:",debtamt)
print("Total Transfers:",transferouts," in $:",toutamt)
cancels = 0
cncamt = 0
collections = 0
clctamt = 0
debtamt = 0
transferouts = 0
toutamt = 0
augdf = idf.query('month == 8')
for index, row in augdf.iterrows():
    if (row["status"]) == "Cancel":
        cancels += 1
        cncamt += (row["Invoice Amount"])
    elif (row["status"]) == "Returned for Collection":
        collections += 1
        clctamt += (row["Invoice Amount"])
        debtamt += (row["amountdue"])
    elif (row["status"]) == "Transferred Account":
        transferouts += 1
        toutamt += (row["Invoice Amount"])
print("Total Cancels:",cancels,"in $:",cncamt)
print("Total Collections:",collections," in $:",clctamt)
print("In Deliquency:",debtamt)
print("Total Transfers:",transferouts," in $:",toutamt)
cancels = 0
cncamt = 0
collections = 0
clctamt = 0
debtamt = 0
transferouts = 0
toutamt = 0
sepdf = idf.query('month == 9')
for index, row in sepdf.iterrows():
    if (row["status"]) == "Cancel":
        cancels += 1
        cncamt += (row["Invoice Amount"])
    elif (row["status"]) == "Returned for Collection":
        collections += 1
        clctamt += (row["Invoice Amount"])
        debtamt += (row["amountdue"])
    elif (row["status"]) == "Transferred Account":
        transferouts += 1
        toutamt += (row["Invoice Amount"])
print("Total Cancels:",cancels,"in $:",cncamt)
print("Total Collections:",collections," in $:",clctamt)
print("In Deliquency:",debtamt)
print("Total Transfers:",transferouts," in $:",toutamt)
cancels = 0
cncamt = 0
collections = 0
clctamt = 0
debtamt = 0
transferouts = 0
toutamt = 0
octdf = idf.query('month == 10')
for index, row in octdf.iterrows():
    if (row["status"]) == "Cancel":
        cancels += 1
        cncamt += (row["Invoice Amount"])
    elif (row["status"]) == "Returned for Collection":
        collections += 1
        clctamt += (row["Invoice Amount"])
        debtamt += (row["amountdue"])
    elif (row["status"]) == "Transferred Account":
        transferouts += 1
        toutamt += (row["Invoice Amount"])
print("Total Cancels:",cancels,"in $:",cncamt)
print("Total Collections:",collections," in $:",clctamt)
print("In Deliquency:",debtamt)
print("Total Transfers:",transferouts," in $:",toutamt)
cancels = 0
cncamt = 0
collections = 0
clctamt = 0
debtamt = 0
transferouts = 0
toutamt = 0
novdf = idf.query('month == 11')
for index, row in novdf.iterrows():
    if (row["status"]) == "Cancel":
        cancels += 1
        cncamt += (row["Invoice Amount"])
    elif (row["status"]) == "Returned for Collection":
        collections += 1
        clctamt += (row["Invoice Amount"])
        debtamt += (row["amountdue"])
    elif (row["status"]) == "Transferred Account":
        transferouts += 1
        toutamt += (row["Invoice Amount"])
print("Total Cancels:",cancels,"in $:",cncamt)
print("Total Collections:",collections," in $:",clctamt)
print("In Deliquency:",debtamt)
print("Total Transfers:",transferouts," in $:",toutamt)
cancels = 0
cncamt = 0
collections = 0
clctamt = 0
debtamt = 0
transferouts = 0
toutamt = 0
decdf = idf.query('month == 12')
for index, row in decdf.iterrows():
    if (row["status"]) == "Cancel":
        cancels += 1
        cncamt += (row["Invoice Amount"])
    elif (row["status"]) == "Returned for Collection":
        collections += 1
        clctamt += (row["Invoice Amount"])
        debtamt += (row["amountdue"])
    elif (row["status"]) == "Transferred Account":
        transferouts += 1
        toutamt += (row["Invoice Amount"])
print("Total Cancels:",cancels,"in $:",cncamt)
print("Total Collections:",collections," in $:",clctamt)
print("In Deliquency:",debtamt)
print("Total Transfers:",transferouts," in $:",toutamt)
