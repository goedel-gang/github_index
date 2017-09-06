"""\
# github\_inventory
A bit of a meta-project on creating a nicer index of my github repositories. Partially motivated because I'm too greedy to do with only 6 pinned repositories.
"""

import sys
import re

sys.stdout.write(__doc__)

for line in sys.stdin:
    if line.strip():
        if line.startswith("#"):
            sys.stdout.write("#{}".format(line))
        else:
            rep_dir, rep_name, rep_url, rep_desc = line.strip().split("\t")
            with open(rep_dir + "README.md", "r") as rep_file:
                for r_line in rep_file:
                    sys.stdout.write(re.sub(r"^# (.*)$", r"### [\1]({})".format(rep_url), r_line))
