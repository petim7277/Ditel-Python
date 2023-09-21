

principal : 1000
rate :.07
year1 : 10
year2  :20
year3 : 30
one : 1

amount1=principal  * (one + rate) * year1
amount2=principal * (one + rate) * year2
amount3=principal * (one + rate) * year3

print(f"""
Amount made in ten years is : ",{amount1}
Amount made in twenty years is : ",{amount2}
Amount made in thirty years is : ",{amount3}
     """)

