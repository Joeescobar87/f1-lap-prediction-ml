import fastf1
import pandas as pd

from pathlib import Path
from features import cleanfpData, cleanqualiData


CACHE_DIR = Path("data/raw/fastf1_cache")
CACHE_DIR.mkdir(parents=True, exist_ok=True)
fastf1.Cache.enable_cache(str(CACHE_DIR))

def freePracticeDF(year: int, race_location: str):

 # ---------- Load sessions ----------
    freePractices = {}
    for fp in ["FP1","FP2","FP3"]:
        try:
            practiceSession = fastf1.get_session(year, race_location, fp)
            practiceSession.load()
            
            freePractices[fp] = practiceSession.laps

        except Exception as e:
            print(f"Could not load {fp} for {race_location} {year} for it does not exist")

     # ---------- Combine FP sessions ----------

    fp_all = pd.concat(freePractices.values(), ignore_index=True)
    fp_all = cleanfpData(fp_all)

    return fp_all



def qualiLapsDF(year: int, race_location: str):

 # ---------- Load sessions ----------

    qualiSession = fastf1.get_session(year, race_location, "Q")
    qualiSession.load()
    qualiLaps = qualiSession.laps
     
# ---------- Clean Quali session ----------
    
    qualiLaps = cleanqualiData(qualiLaps)

    return qualiLaps

if __name__ == "__main__":
    fp_all = freePracticeDF(2025, "Australia")
    quali = qualiLapsDF(2025, "Australia")

    print("FP shape:", fp_all.shape)
    print(fp_all)

    print("\nQuali shape:", quali.shape)
    print(quali)
    
   