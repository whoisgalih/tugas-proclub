def total_kemunculan(some_list):
    x = dict.fromkeys(some_list, 0)

    for i in some_list:
        x[i] += 1

    for k, v in x.items():
        print(f'{k}: {v}')


total_kemunculan(["js", "js", "golang", "ruby", "ruby", "js", "js"])
total_kemunculan(["danu", "danu", "alif", "indra",
                 "indra", "kurniadi", "indra"])
