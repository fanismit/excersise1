def sumIntervals(*array): 
 start1=[] #Αρχικοποιώ μία λίστα που μέσα θα εισάγω το πρώτο στοιχείο από κάθε διάστημα
 end1=[]#Αρχικοποιώ μία λίστα που μέσα θα εισάγω το τελευταίο στοιχείο από κάθε διάστημα
 try:
  i=0
  while(array[0][i]):#Για όσα διαστήματα βρεθούν γεμίζουν οι πίνακες που αρχικοποιήθηκαν όπως αναφέρθηκε παραπάνω
    ko=array[0][i]
    end1.append(ko[1])
    start1.append(ko[0])
    i+=1
 except:#Σε κάθε άλλη περ΄πτωση το πρόγραμμα συνεχίζει να εκτελείται
        end1.sort()
        start1.sort()
        max=end1[-1]
        min=start1[0]
        sum=0
        for n in range(0,i):#Υπολογισμός αθροίσματος όλων των διαστημάτων
            sum+=(array[0][n][1]-array[0][n][0])
        for o in range(min,max+1):#Οι μεταβλητές max και min αποτελούν  
            f=0#Η μεταβλητη f αποτελεί τον μετρητή των εμφανίσεων κάθε αριθμού σε διαφορετικά διαστήματα
            for p in range(0,i):                
                for k in range(array[0][p][0],array[0][p][1]):# ΠΡΟΣΟΧΗ ο συγκεκριμένος βρόγχος αποτέλεί το βασικότερο μέρος της άσκησης.Στο loop προσπαθεί να ανιχνευτεί σε όλα τα διαστήματα αν υπάρχει κάποιος όμοιος αριθμός 
                    if(o==k and f!=0):#Αν βρεθει αριθμος όμοιος ενώ έχει βρεθεί ήδη ο εαυτός του τότε μειώνετε το άθροισμα κατα 1
                        sum-=1
                    if(o==k and f==0):
                        f+=1
        print(sum)

