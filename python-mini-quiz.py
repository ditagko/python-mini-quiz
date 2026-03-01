questions = [
    {'erwtisi': 'Ποιο είναι το χημικό σύμβολο του νερού;', 'apantisi': 'h2o'},
    {'erwtisi': 'Ποιος έγραψε την Οδύσσεια;', 'apantisi': 'όμηρος'},
    {'erwtisi': 'Πόσες ηπείρους έχει η Γη;', 'apantisi': '7'},
    {'erwtisi': 'Σε ποια ήπειρο βρίσκεται η Αίγυπτος;', 'apantisi': 'αφρική'},
    {'erwtisi': 'Ποιο είναι το μεγαλύτερο θηλαστικό στον κόσμο;', 'apantisi': 'γαλάζια φάλαινα'},
    {'erwtisi': 'Ποια χώρα έχει σχήμα μπότας;', 'apantisi': 'ιταλία'},
    {'erwtisi': 'Ποιο όργανο του σώματος αντλεί το αίμα;', 'apantisi': 'καρδιά'},
    {'erwtisi': 'Ποια είναι η πρωτεύουσα της Γαλλίας;', 'apantisi': 'παρίσι'},
    {'erwtisi': 'Πόσο κάνει 5 * 5;', 'apantisi': '25'},
    {'erwtisi': 'Ποιος πλανήτης είναι γνωστός ως ο Κόκκινος Πλανήτης;', 'apantisi': 'άρης'}
]

# Εδώ θα κρατάμε το σκορ
score = 0

# Κάνουμε λούπ για να μας εμφανίζει τις ερωτήσεις
for p in questions:
    print(f" Ερώτηση {questions.index(p) + 1} από {len(questions)}")
    print(p['erwtisi'])
    apanti = input("Γράψε μας την απάντηση: ").strip().lower()
    if apanti == p['apantisi']:
        print("Συγχαρητήρια! ")
        score = score +1
    else:
        print("Λάθος απάντηση!")

print(f"Βρήκες {score} απαντήσεις!")