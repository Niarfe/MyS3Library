import os
files = [
    "Effective_Java,_2nd_Edition.pdf",
    "Head_First_Java,_2nd_Edition.pdf",
    "Mining_the_Social_Web,_Second_Edition_-_Russell,_Matthew_A.pdf",
    "PHP_Cookbook,_3rd_Edition.pdf",
    "Russell_S_Norvig_P_Artificial_intelligence-_a_modern_approach_2ed_PH,2003T1112s.pdf",
    "Violent_Python_-_A_Cookbook_for_Hackers,_Forensic_Analysts,_Penetration_Testers_and_Security_Engineers.pdf",
    "raspberry_pi_home_automation_with_arduino,_2nd_edition.pdf",
]

for fname in files:
    cmd = "aws s3 mv s3://eolibrary/books/{} s3://eolibrary/books/{}".format(
        fname,
        fname.replace(',','_')
        )
    os.system(cmd)
