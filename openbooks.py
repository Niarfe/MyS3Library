import os


books = [
"9781784397166-JASMINE_COOKBOOK.pdf",
"9781784399085-TESTDRIVEN_MACHINE_LEARNING.pdf",
"9781838559335-MASTERING_GO_SECOND_EDITION.pdf",
"9781786468949-GO_PROGRAMMING_BLUEPRINTS_SECOND_EDITION.pdf",
"9781788830829-MODERN_PYTHON_STANDARD_LIBRARY_COOKBOOK.pdf",
"9781789800982-GO_PROGRAMMING_COOKBOOK_SECOND_EDITION.pdf",
"writing_an_interpreter_in_go_1.6.pdf",
"the-ray-tracer-challenge_p1_0.pdf",
"rediscovering-javascript_p1_0.pdf",
"9781838645359-AI_CRASH_COURSE.pdf",
"Terraform_in_Action_v8_MEAP.pdf",
"Algorithms_and_Data_Structures_in_Action_v11_MEAP.pdf",
"Grokking_Artificial_Intelligence_Algorit_v5.pdf",
"9781838825461-HANDSON_ONESHOT_LEARNING_WITH_PYTHON.pdf",
"9781838984762-LEARN_SQL_DATABASE_PROGRAMMING.pdf",
]

for book in books:
    os.system("do/open {}".format(book))


