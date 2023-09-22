import spacy
# Load the SpaCy language model
# spacy.cli.download('en_core_web_lg')
nlp = spacy.load('en_core_web_lg')

# Define your set of seed words
seed_words = {
    "Crime": 7,
    "Criminal": 8,
    "Investigation": 6,
    "Suspect": 6,
    "Detective": 7,
    "Evidence": 6,
    "Forensics": 6,
    "Witness": 5,
    "Prosecutor": 8,
    "Defense": 8,
    "Jury": 6,
    "Trial": 7,
    "Verdict": 8,
    "Judge": 8,
    "Lawyer": 8,
    "Alibi": 5,
    "Testimony": 6,
    "Conviction": 9,
    "Acquittal": 4,
    "Sentence": 9,
    "Prison": 9,
    "Bail": 5,
    "Parole": 4,
    "Homicide": 9,
    "Robbery": 7,
    "Burglary": 6,
    "Theft": 5,
    "Assault": 7,
    "Kidnapping": 9,
    "Arson": 8,
    "Forgery": 6,
    "Fraud": 7,
    "Embezzlement": 7,
    "Cybercrime": 8,
    "Identity theft": 8,
    "Drug trafficking": 9,
    "Money laundering": 9,
    "Racketeering": 8,
    "Organized crime": 8,
    "White-collar crime": 7,
    "Domestic violence": 7,
    "Stalking": 6,
    "Harassment": 5,
    "Child abuse": 8,
    "Sexual assault": 9,
    "Cyberbullying": 4,
    "Hate crime": 8,
    "Gang": 6,
    "Drive-by shooting": 7,
    "Carjacking": 7,
    "Terrorism": 10,
    "Extortion": 7,
    "Blackmail": 6,
    "Smuggling": 6,
    "Bribery": 6,
    "Corruption": 7,
    "Perjury": 5,
    "Witness tampering": 6,
    "Interrogation": 6,
    "Search warrant": 6,
    "Surveillance": 6,
    "Wiretap": 7,
    "Crime scene": 6,
    "Autopsy": 5,
    "Missing person": 5,
    "Cold case": 6,
    "Fugitive": 7,
    "Evidence tampering": 7,
    "Crime lab": 6,
    "Polygraph": 5,
    "Miranda rights": 6,
    "Sovereign immunity": 4,
    "Statute of limitations": 4,
    "Legal defense": 7,
    "Plea bargain": 6,
    "Grand jury": 6,
    "Indictment": 6,
    "Felony": 8,
    "Misdemeanor": 5,
    "Probation": 4,
    "Rehabilitation": 5,
    "Juvenile delinquency": 5,
    "Capital punishment": 9,
    "Hate speech": 4,
    "Forensic science": 6,
    "Criminal profiling": 7,
    "Crime prevention": 5,
    "Crime rate": 5,
    "Victim": 5,
    "Vigilante": 4,
    "Crime scene tape": 4,
    "Crime spree": 7,
    "Witness protection": 6,
    "Crime syndicate": 7,
    "Evidence locker": 5,
    "Perp walk": 4,
    "Criminal record": 7,
    "Police brutality": 8,
    "Crime fiction": 3
}


# Input paragraph
paragraph =  "In a high-profile criminal case that captivated the nation, John Smith stood accused of masterminding a complex bank heist. The investigation uncovered a web of evidence, including security camera footage, fingerprints at the scene, and financial transactions linking Smith to the stolen funds. During the trial, the prosecution presented a compelling case, presenting witness testimonies, forensic analysis, and bank records. The defense, however, argued that Smith was wrongly accused and presented an alibi corroborated by family members. After weeks of legal proceedings and intense deliberation, the jury reached a verdict of guilty, and John Smith was sentenced to a lengthy prison term. This criminal case underscored the importance of a thorough investigation and the adversarial nature of the legal system."
common_words = [
    "plaintiff", "defendant", "complaint", "summons", "answer",
    "motion", "judge", "court", "attorney", "evidence",
    "testimony", "jury", "verdict", "appeal", "settlement",
    "counsel", "docket", "pleadings", "discovery", "subpoena",
    "lawsuit", "cause of action", "jurisdiction", "injunction",
    "damages", "cross-examination", "affidavit", "statute",
    "precedent", "hearing"
]
words = paragraph.split()
filtered_words = [word for word in words if word.lower() not in common_words]
filtered_paragraph = " ".join(filtered_words)
paragraph=filtered_paragraph
# print(paragraph)
# Tokenize and process the paragraph
doc = nlp(paragraph)
extracted_words=set()

for token in doc:
    if token.pos_ != "PROPN":
        extracted_words.add(token.text)

# print(extracted_words)

# Initialize a set to store related words
related_words = set()

# Set a similarity threshold
similarity_threshold = 0.75

# Iterate through the tokens and find related words
result=dict()
for word in extracted_words:
    for key in seed_words:
        similarity_score = nlp(word).similarity(nlp(key))
        if similarity_score > similarity_threshold:
            result[key]=seed_words[key]
            #print(key,word)
            #print(similarity_score)

# Print the related words

sorted_dict = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

critical_score=0

max_elements = min(3, len(sorted_dict))

# Iterate through the dictionary up to a maximum of 10 elements
for key, value in list(sorted_dict.items())[:max_elements]:
  critical_score+=value

# print("Related Words:")
# print(sorted_dict)
# print(result)
# for word in related_words:
#     print(word)
print("The critical score is: ")
print(critical_score)