from pypasser import reCaptchaV3
import requests

class MrX:
    def __init__(self):
        self.reCaptchaV3 = reCaptchaV3("https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LdgMGoeAAAAAECExhXsnXnH8busMCJ3TP4C7wQq&co=aHR0cHM6Ly9hcGlsYXllci5jb206NDQz&hl=tr&v=gWN_U6xTIPevg0vuq7g1hct0&size=invisible&cb=v2173k21xn6g", timeout = 10)

    def getCaptcha(self):

        urll = f"https://apilayer.com/widgets/bincheck?token={self.reCaptchaV3}"

        bin = input("Bin Gir: ")

        x = len(str(bin))

        if x != 6:
            print("Yanlış Bin")
            exit()
        else:
            mrx = requests.post(urll, data={"widget_form_input": "{}".format(bin)})
            if "No such BIN" in mrx.text:
                print("Bin Mevcut Değil")
            else:
                print(mrx.json())

MrX().getCaptcha()
