tech_company = ["Apple", "Microsoft", "Meta", "Alphabet"]
tech_ceos = ["Steve Jobs", "Bill Gates", "Mark Zuckerberg", "Sundar Pichai"]

print(tech_company)

for ceos in tech_ceos:
    print(ceos)

for i in range(len(tech_company)):
    print(tech_company[i],"-", tech_ceos[i])
