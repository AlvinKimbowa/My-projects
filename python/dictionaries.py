monthconversions = {
    "Jan": "January", "Feb": "February", "Mar": "March",
    "Apr": "April", "May": "May", "Jun": "June", "JUl": "July",
    "Aug": "August", "Sep": "September", "Oct": "October",
    "Nov": "November", "Dec": "December"
}

date_conversion = {
    1: "January", 2: "February", 3: "March",
    4: "April", 5: "May", 6: "June", 7: "July",
    8: "August", 9: "September", 10: "October",
    11: "November", 12: "December"
}

print(monthconversions["Mar"] + " " + monthconversions["Oct"])
print(monthconversions.get("Dub", "Invalid Key"))

print(date_conversion[5])
print(date_conversion.get(int(input("Enter the year: ")), "Invalid key"))