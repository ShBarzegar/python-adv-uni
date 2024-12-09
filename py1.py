import requests as r
class Fetcher:
    def __init__(self):
        
        self.students = r.get("https://cdn.ituring.ir/ex/users.json").json()
        
        
    def nerds(self):
        nerdsnames = set()
        for student in self.students:
            if student["score"] > 18.5:
                nerdsnames.add(student["name"] + " " + student["last_name"])
        print("bache zerangha:", nerdsnames)
    def sultans(self):
        bishtarinnomreh = 0
        sultans = () 
        for student in self.students:
            if student["score"] > bishtarinnomreh:
                bishtarinnomreh = student["score"]
                sultans = (student["name"] + " " + student["last_name"],)  
            elif student["score"] == bishtarinnomreh:
                sultans += (student["name"] + " " + student["last_name"],)  
        print("salatin:", sultans)
    def mean(self):
        tedadenafarat = len(self.students) 
        jamenomreha = 0  
        for student in self.students:
            jamenomreha += float(student["score"])  
        miangin = jamenomreha / tedadenafarat
        print("miangin nomreha:", miangin)
    def get_students(self):
        listedaneshjouha = []
        for student in self.students:
            dictionarydaneshjou = {"name":student["name"] , "last_name":student["last_name"] , "height":student["height"] , "weight":student["weight"] , "score":student["score"] , "savings":student["savings"] , "salary":student["salary"]}    
            listedaneshjouha.append(dictionarydaneshjou)
        print("liste daneshjouha:", listedaneshjouha)
        return listedaneshjouha
iau = Fetcher()
iau.nerds()
iau.sultans()
iau.mean()
iau.get_students()
