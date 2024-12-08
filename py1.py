import requests as r
class Fetcher:
    def __init__(self):
        self.students =[]
        self.l = r.get("https://cdn.ituring.ir/ex/users.json").json()
        for student in self.l:
             moshakhasat = {"esm":student["name"] , "famili":student["last_name"] , "ghad":student["height"] , "wazn":student["weight"] , "nomreh":student["score"] , "pasandaz":student["savings"] , "dast mozd":student["salary"] ,"shahr":student["city"] , "ostan":student["province"] , "arze joghrafiaie":student["latitude"] , "tolejoghrafiaei":student["longitude"]}     
             self.students.append(moshakhasat)
    def nerds(self):
        nerdsnames = set()
        for student in self.students:
            if student["nomreh"] > 18.5:
                nerdsnames.add(student["esm"] + " " + student["famili"])
        print("bache zerangha:", nerdsnames)
    def sultans(self):
        bishtarinnomreh = 0
        sultans = () 
        for student in self.students:
            if student["nomreh"] > bishtarinnomreh:
                bishtarinnomreh = student["nomreh"]
                sultans = (student["esm"] + " " + student["famili"],)  
            elif student["nomreh"] == bishtarinnomreh:
                sultans += (student["esm"] + " " + student["famili"],)  
        print("salatin:", sultans)
    def mean(self):
        tedadenafarat = len(self.students) 
        jamenomreha = 0  
        for student in self.students:
            jamenomreha += float(student["nomreh"])  
        miangin = jamenomreha / tedadenafarat
        print("miangin nomreha:", miangin)
    def get_students(self):
        listedaneshjouha = []
        for student in self.students:
            dictionarydaneshjou = {"esm":student["esm"] , "famili":student["famili"] , "ghad":student["ghad"] , "wazn":student["wazn"] , "nomreh":student["nomreh"] , "pasandaz":student["pasandaz"] , "dast mozd":student["dast mozd"]}    
            listedaneshjouha.append(dictionarydaneshjou)
        print("liste daneshjouha:", listedaneshjouha)
        return listedaneshjouha
iau = Fetcher()
iau.nerds()
iau.sultans()
iau.mean()
iau.get_students()
