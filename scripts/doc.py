import docx
import os
doc = docx.Document()
user_details={
    "name":"LOKESHWARAN P",
    "regNo":"23BAI1098",
}
doc.add_heading(f"NAME: {user_details['name']}\nREG No.: {user_details['regNo']}\n")
doc.add_page_break() # new page
para = doc.add_paragraph()
run = para.add_run(f"NAME: {user_details['name']}\nREG No.: {user_details['regNo']}\n")
doc.save("test.docx")