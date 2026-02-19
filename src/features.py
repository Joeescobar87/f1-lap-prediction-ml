import fastf1
import pandas as pd



def cleanfpData(fp_all: pd.DataFrame):

    fp_all = fp_all[fp_all["IsAccurate"] == True]

    fp_all["LapTimeSeconds"] = fp_all["LapTime"].dt.total_seconds()

    fp_all = fp_all[fp_all["Driver"].notna() & (fp_all["Driver"] != "BAD")]

    fp_all = fp_all[fp_all["LapTimeSeconds"].notna()]

    fp_all = fp_all[fp_all["Deleted"]== False]

    fp_all["Sector1TimeSeconds"] = fp_all["Sector1Time"].dt.total_seconds()
    fp_all["Sector2TimeSeconds"] = fp_all["Sector2Time"].dt.total_seconds()
    fp_all["Sector3TimeSeconds"] = fp_all["Sector3Time"].dt.total_seconds()



    df = fp_all[fp_all.columns.to_list()]

    df.drop(["Time",
             "DriverNumber",
             "LapTime",
             "LapNumber", 
             "Stint",
             "PitOutTime", 
             "PitInTime",
             "Sector1Time",
             "Sector2Time",
             "Sector3Time",
             "Sector1SessionTime",
             "Sector2SessionTime",
             "Sector3SessionTime", 
             "IsPersonalBest",
             "LapStartTime",
             "LapStartDate",
             "Position",
             "Deleted",
             "DeletedReason",
             "LapStartTime",
             "FastF1Generated",
             "IsAccurate"
             ], axis=1, inplace=True)


    return df
    

def cleanqualiData(qualiLaps: pd.DataFrame):

    qualiLaps = qualiLaps[qualiLaps["IsAccurate"] == True]

    qualiLaps["LapTimeSeconds"] = qualiLaps["LapTime"].dt.total_seconds()

    qualiLaps = qualiLaps[qualiLaps["Driver"].notna() & (qualiLaps["Driver"] != "BAD")]
    qualiLaps = qualiLaps[qualiLaps["LapTimeSeconds"].notna()]

    qualiLaps = qualiLaps[qualiLaps["Deleted"]== False]

    qualiLaps["Sector1TimeSeconds"] = qualiLaps["Sector1Time"].dt.total_seconds()
    qualiLaps["Sector2TimeSeconds"] = qualiLaps["Sector2Time"].dt.total_seconds()
    qualiLaps["Sector3TimeSeconds"] = qualiLaps["Sector3Time"].dt.total_seconds()



    df = qualiLaps[qualiLaps.columns.to_list()]

    df.drop(["Time", 
             "DriverNumber",
             "LapTime",
             "LapNumber", 
             "Stint",
             "PitOutTime", 
             "PitInTime",
             "Sector1Time",
             "Sector2Time",
             "Sector3Time",
             "Sector1SessionTime",
             "Sector2SessionTime",
             "Sector3SessionTime", 
             "IsPersonalBest",
             "LapStartTime",
             "LapStartDate",
             "Position",
             "Deleted",
             "DeletedReason",
             "LapStartTime",
             "FastF1Generated",
             "IsAccurate"
             ], axis=1, inplace=True)


    return df