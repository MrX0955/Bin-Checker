from pypasser import reCaptchaV3
import requests, os


class MrX:
    def __init__(self):
        self.reCaptchaV3 = reCaptchaV3(
            "https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LdgMGoeAAAAAECExhXsnXnH8busMCJ3TP4C7wQq&co=aHR0cHM6Ly9hcGlsYXllci5jb206NDQz&hl=tr&v=9pvHvq7kSOTqqZusUzJ6ewaF&size=invisible&cb=mpplbe9iu52o",
            timeout=30,
        )
        self.clear = os.system("cls" if os.name == "nt" else "clear")

    def getCaptcha(self):

        url = f"https://apilayer.com/widgets/bincheck?token={self.reCaptchaV3}"

        self.clear

        bin = str(input("\n Enter Bin (Max Lenght 6): ").strip())

        x = len(bin)

        if x != 6:
            print("\n Bin Lenght must be 6(six) // Bin uzunluğu 6(altı) olmalı.")
            exit()
        else:
            mrx = requests.post(
                url,
                data=f"widget_form_input={bin}",
                timeout=30,
                headers={
                    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
                },
            )
            if "No such BIN" in mrx.text:
                print("\n Bin does not exist or not correct.")
            else:
                print("\n", mrx.json())


MrX().getCaptcha()
