firm_dict = {}
av_dict = {"av_profit": 0}
result = [firm_dict, av_dict]
with open("firms.txt", encoding='utf-8') as my_file:
    firm_count = 0
    lines = my_file.readlines()
    for line in lines:
        if len(line):
            firm_name, firm_type, firm_revenue, firm_costs = line.split()
            firm_profit = float(firm_revenue) - float(firm_costs)
            firm_dict[firm_name] = firm_profit
            if firm_profit > 0:
                av_dict["av_profit"] += firm_profit
                firm_count += 1
    if firm_count:
        av_dict["av_profit"] /= firm_count

with open("firms.json", 'w') as write_file:
    json.dump(result, write_file, ensure_ascii=False, indent=4)
