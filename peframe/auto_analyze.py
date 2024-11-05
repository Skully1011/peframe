#from pathlib import Path
import os
import glob
import subprocess
import time

def main():
    workdir = "/peframe/peframe/Malware"
    outputdir = "/peframe/peframe/Malware/Analysis"
    # identify PE files; this is a flimsy implementation that should be improved
    # as it relies on a pattern that won't always be true
    pe_files = glob.glob(f"{workdir}/Virusshare.00000/Backdoor.Win32.*")
    # analyze and generate json formatted output for every identified file
    start_time = time.time()
    for filepath in pe_files:
        filename = os.path.basename(filepath)
        print(f"Analyzing {filename}")
        with open(f"{outputdir}/{filename}.json", 'w') as outfile:
            subprocess.run(["peframe", "-j", f"{filepath}"], stdout=outfile)

    stop_time = time.time()
    elapsed_time = stop_time - start_time
    print(f"Finished analysis in {elapsed_time} seconds. Now exiting.")
    return None

if __name__ == "__main__":
    main()
