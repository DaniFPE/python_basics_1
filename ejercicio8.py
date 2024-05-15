# Convert the argument of generate_report_card to keyword arguments

name = "Alice"
score = 55
subject = "English"
date = "15/05/2022"

def get_result(score=0):
  if score >= 45:
    return "Passed"
  else:
    return "Failed"

def generate_report_card(name, date, subject, score=0):
  print("-------------------------------------------------")
  print(f"| Name: {name} \t\t| Date: {date} \t|")
  print("-------------------------------------------------")
  print(f"| Subject: {subject} \t| Score: {score} \t\t|")
  print("-------------------------------------------------")
  print(f"| Result: \t\t| {get_result(score)} \t\t|")
  print("-------------------------------------------------")


generate_report_card(name=name, date=date, subject=subject, score=score)
