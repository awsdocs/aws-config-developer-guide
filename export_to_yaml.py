import yaml
import os
import re
from os import listdir
from operator import itemgetter

all_rules = []

for f in listdir("doc_source"):
    print(f)

    rule = {}
    rule["File"] = f

    id = f.replace(".md", "")

    rule["Name"] = id
    path = "doc_source/"+f

    # print(path)
    if os.path.isfile(path):
        valid = False
        with open(path, 'r') as infile:
            contents = infile.read()
            rule["FullDocumentation"] = contents.strip()

            if contents.find("**Identifier:**") > 0:
                valid = True
            else:
                print("   - Not a control")
                continue

            # break into lines and ignore first line
            tmp = contents.splitlines(keepends=True)[1:]
            tmp = ''.join(tmp).strip()

            # Grab eventhing before the Identifier row
            rule["Description"] = tmp.split("**Identifier:**")[0].strip()

            m = re.search('\*\*Identifier:\*\*(.+?)\n', contents)
            if m:
                rule["Identifier"] = m.group(1).strip().replace("\\_", "_")
            else:
                rule["Identifier"] = "Unknown"

            m = re.search('\*\*Trigger type:\*\*(.+?)\n', contents)
            if m:
                rule["TriggerType"] = m.group(1).strip()
            else:
                rule["TriggerType"] = "Unknown"

            m = re.search('\*\*AWS Region:\*\*(.+?)\n', contents)
            if m:
                rule["AWSRegion"] = m.group(1).strip()
            else:
                rule["AWSRegion"] = "Unknown"

        if valid:
            all_rules.append(rule)

    else:
        print("NOT FOUND AWS FILE " + path)

all_rules = sorted(all_rules, key=itemgetter('File'))

with open('config-rules.yml', 'w') as outfile:
    yaml.dump(all_rules, outfile, default_flow_style=False)