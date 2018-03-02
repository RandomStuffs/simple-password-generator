
def InputFromUser():

    SiteName = input("Please Enter Site Name without spaces: ")

    StringLength = SiteName.__len__()

    # split the title name into half

    AfterSplit = SiteName[0:int(StringLength/2)]

    print(AfterSplit)

    FirstChar = AfterSplit[0]
    RemainingString = AfterSplit.split(AfterSplit[0])

    FinalString = FirstChar.upper().join(RemainingString)

    print(FinalString)

InputFromUser()