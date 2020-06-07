import os


books = [
"9781784397166-JASMINE_COOKBOOK.pdf",
"9781784399085-TESTDRIVEN_MACHINE_LEARNING.pdf",
"9781838559335-MASTERING_GO_SECOND_EDITION.pdf",
"9781786468949-GO_PROGRAMMING_BLUEPRINTS_SECOND_EDITION.pdf",
"writing_an_interpreter_in_go_1.6.pdf",
"the-ray-tracer-challenge_p1_0.pdf",
"rediscovering-javascript_p1_0.pdf",
"9781838645359-AI_CRASH_COURSE.pdf",
]

for book in books:
    os.system("do/open {}".format(book))


