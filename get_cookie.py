#获取并保存cookie
import requests, UA, json,re

login_url = r"https://forums.e-hentai.org/index.php?act=Login&CODE=01"
hath_perks = "https://e-hentai.org/hathperks.php"
ex = "https://exhentai.org/g/11896/3096eb277b/"
ua = UA.RUA()
header = ua
main = requests.Session()

def Login(User, Pass):
    login_form = {"CookieDate": "1",
                  "b": "d",
                  "bt": "1-1",
                  "UserName": User,
                  "PassWord": Pass,
                  "ipb_login_submit": "Login!"}

    html = main.post(login_url, headers=header, data=login_form)

    if len(re.findall("The following errors were found:", html.text)) != 0:
        with open("login.json","w+") as f:
            f.write("0")
        return 0
    else:
        ck=html.cookies
        cookie_form={}

        ipb_member=ck["ipb_member_id"]
        ipb_pass_hash=ck["ipb_pass_hash"]
        ipb_session_id=ck["ipb_session_id"]
        sk=main.get("https://e-hentai.org/home.php",headers=header)

        cookie_form["ipb_member"]=ipb_member
        cookie_form["ipb_pass_hash"] = ipb_pass_hash
        cookie_form["ipb_session_id"] = ipb_session_id
        cookie_form["sk"] = sk.cookies["sk"]


        try:
            hath_perk = main.get(hath_perks, headers=header).cookies["hath_perks"]
            cookie_form["hath_perks"] = hath_perk
        except:
            pass

        try:
            igneous = main.get(ex, headers=header).cookies["igneous"]
            cookie_form["igneous"] = igneous
        except:
            pass

        with open("login.json","w+") as f:
            f.write(json.dumps(cookie_form))
        return cookie_form

if __name__ == '__main__':
    Login("zk15978053127", "cctv1357910")
