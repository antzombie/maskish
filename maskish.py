import os
print('''
 .S_SsS_S.    .S_SSSs      sSSs   .S    S.    .S    sSSs   .S    S.
.SS~S*S~SS.  .SS~SSSSS    d%%SP  .SS    SS.  .SS   d%%SP  .SS    SS.
S%S `Y' S%S  S%S   SSSS  d%S'    S%S    S&S  S%S  d%S'    S%S    S%S
S%S     S%S  S%S    S%S  S%|     S%S    d*S  S%S  S%|     S%S    S%S
S%S     S%S  S%S SSSS%S  S&S     S&S   .S*S  S&S  S&S     S%S SSSS%S
S&S     S&S  S&S  SSS%S  Y&Ss    S&S_sdSSS   S&S  Y&Ss    S&S  SSS&S
S&S     S&S  S&S    S&S  `S&&S   S&S~YSSY%b  S&S  `S&&S   S&S    S&S
S&S     S&S  S&S    S&S    `S*S  S&S    `S%  S&S    `S*S  S&S    S&S
S*S     S*S  S*S    S&S     l*S  S*S     S%  S*S     l*S  S*S    S*S
S*S     S*S  S*S    S*S    .S*P  S*S     S&  S*S    .S*P  S*S    S*S
S*S     S*S  S*S    S*S  sSS*S   S*S     S&  S*S  sSS*S   S*S    S*S
SSS     S*S  SSS    S*S  YSS'    S*S     SS  S*S  YSS'    SSS    S*S
        SP          SP           SP          SP                  SP
        Y           Y            Y           Y                   Y
                          [ Maskish By melentent ]
               [ Please Do not Use For Illigal Activity ]
             [ Any illegal usage is not My Responsibility ]''')
phishing_domain = input("\nEnter Url To Mask: ")
print("\nExamples: https://twitter.com, http://insecure-site.org")
print("Warning: Fake Domain Cannot Have Forward Slash At The End")
mask_domain = input("Enter Fake Domain: ")
print("\nExamples: Free-Followers, Free-Money")
print("Warning: Keywords Must Have Dash Between Each Word")
keywords = input("(Optional) Enter Domain Keywords: ")
command = str(f'curl -s https://is.gd/create.php\?format\=simple\&url\={phishing_domain} > url.txt')
os.system(command)
with open('url.txt') as url:
    tinyurl1 = url.readlines(1)
    tinyurl = tinyurl1[0]
    tinyurl = str(tinyurl.replace("https://", ""))
    tinyurl = str(tinyurl.replace("\n", ""))
os.system("sudo rm -r url.txt")
if keywords == "":
    final_url = str(f"{mask_domain}@{tinyurl}")
if keywords != "":
    final_url = str(f"{mask_domain}-{keywords}@{tinyurl}")
print(f"\nMasked Url: {final_url}")
