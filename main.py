import time
import pyotp
import qrcode


#key = pyotp.random_base32() # law had m3ah da ydkhol 3adi, mmkn thot enta ay string 3adi
key = 'AMTHACKS'
totp = pyotp.TOTP(key)

#======================== 2FA code printing ============================
#print(totp.now())
#input_code = input('enter the 2FA code: ')
#time.sleep(30)
#print(totp.now())
#print(totp.verify(input_code))


#========================= Athentication App =================================
#uri = pyotp.totp.TOTP(key).provisioning_uri(name='AMT', issuer_name='AMT App')

#print(uri)
#qrcode.make(uri).save('totp.png')

print(totp.verify(input('enter code: ')))
