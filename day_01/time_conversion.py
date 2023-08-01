def timeConversion(s):
    if "AM" in s:
        if s[0:2] == "12":
           s = s.replace("12", "00")
    else:
        if "PM" in s:
            if s[0:2] == "12":
                s = s
            else:    
                if 10 <= int(s[0:2]) <= 11:
                    s = s.replace(s[0:2], str(int(s[0:2]) + 12))
                else:
                    s = s.replace(s[0:2], str(int(s[1:2]) + 12))
    return s[:-2]