with open("match_ids.txt", "r") as f:
    objs = f.read().split("\n")
    objs = list(dict.fromkeys(objs))

with open("match_ids.txt", "w") as f:
    for i in objs:
        f.write(f"{i}\n")  # 1052
