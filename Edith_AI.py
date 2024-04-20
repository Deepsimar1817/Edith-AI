# Import necessary packages
from body import speak
from time import sleep
import webbrowser
import speech_recognition as sr
from gtts import gTTS
import os
import time

import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pathlib

warnings.simplefilter("ignore")
url = "https://pi.ai/talk"
scriptDirectory = pathlib.Path().absolute()
chrome_driver_path = 'C:\\Users\\dell\\PycharmProjects\\pythonProject\\database\\chromedriver.exe'
chrome_options = Options()
chrome_options.headless = True
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--log-level=3')
chrome_options.add_experimental_option("prefs", {"intl.script_allow_extended_latin_characters": True})
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
service = Service(chrome_driver_path)
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2'
chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(url)
sleep(5)

last_response_time = 0


def cooldown():
    global last_response_time
    last_response_time = time.time()


def is_cooldown():
    global last_response_time
    return time.time() - last_response_time < 7  # Adjust the cooldown time as needed (in seconds)


def error():
    try:
        driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div/div/div[2]/div[2]/div/button').click()
        driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div/div/div[2]/div[2]/div/button').click()
        driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div/div/div[2]/div[2]/div/button').click()

        # button = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[2]/button[2]')
        # button.click()
        # driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[1]/button[5]').click()

    except Exception as e:
        return None


def listen_for_wake_up(trigger_phrase="Hello"):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        # print(f"Listening for wake-up phrase '{trigger_phrase}'...")
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                audio = recognizer.listen(source)
                print("Listening...")

                wake_up_phrase = recognizer.recognize_google(audio)
                # print(f"You said: {wake_up_phrase}")

                if trigger_phrase.lower() in wake_up_phrase.lower():
                    print("Wake-up phrase detected!")
                    return True

            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"Error connecting to Google API: {e}")

            return False


# Example character outside BMP
char = "👋"
# Convert character to Unicode code point
code_point = ord(char)

# Calculate high and low surrogate values
surrogate_high = (code_point - 0x10000) >> 10 + 0xD800
surrogate_low = (code_point - 0x10000) % 0x400 + 0xDC00
# Convert surrogate values to characters and send to ChromeDriver
surrogate_pair = chr(surrogate_high) + chr(surrogate_low)
element_id = "734c6d6a-875d-4b2d-9c69-255a446a3b92"
driver.find_element_by_id(element_id).send_keys(surrogate_pair)


def Introduction():
    try:

        driver.find_element(by=By.XPATH,
                            value='//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/div/textarea').send_keys(
            "Hello")




    except:
        driver.find_element(by=By.XPATH,
                            value='//*[@id="__next"]/main/div/div/div/div[2]/div[3]/div/div/div/div/textarea').send_keys(
            "Deepsimar")
        driver.find_element(by=By.XPATH,
                            value='//*[@id="__next"]/main/div/div/div/div[2]/div[3]/div/div/div/button').click()
        sleep(5)
        driver.find_element(by=By.XPATH,
                            value='//*[@id="__next"]/main/div/div/div/div[2]/div[3]/div/div/div[1]/button[5]').click()
        driver.find_element(by=By.XPATH,
                            value='//*[@id="__next"]/main/div/div/div/div[2]/div[3]/div/div/div[2]/button[1]').click()
        sleep(7)
        driver.find_element(by=By.XPATH,
                            value='//*[@id="__next"]/main/div/div/div/div[2]/div[2]/div[2]/button').click()

    sleep(1)
    # driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/button').click()

    sleep(1)
    # driver.find_element(by=By.XPATH, value='//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/button').click()
    sleep(1)

    try:
        driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[2]/div/div[2]/button[2]").click()

    except:
        pass

        try:
            driver.find_element(by=By.XPATH,
                                value='//*[@id="__next"]/main/div/div/div[3]/div[3]/div/div[2]/button[2]').click()
        except:
            pass

    FileHistory = open("C:\\Users\\dell\\PycharmProjects\\pythonProject\\brain\\chatnumberpi.txt", "w")
    FileHistory.write('1')
    FileHistory.close()
    FileReadNow = open("C:\\Users\\dell\\PycharmProjects\\pythonProject\\brain\\pihistory.txt", "w")
    FileReadNow.write('1')
    FileReadNow.close()


def PopUpRemover():
    try:
        popup = driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[4]/div/div/div[1]").is_enabled()
        if str(popup) == "True":
            driver.refresh()
            sleep(2)

        else:
            pass

    except:
        pass


def QuerySender(Query):
    Query = str(Query)

    try:
        driver.find_element(by=By.XPATH,
                            value='//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/div/textarea').send_keys(
            Query)

    except Exception as e:
        print(e)

    sleep(3)


def ButtonClicker():
    while True:

        SendButton = driver.find_element(by=By.XPATH,
                                         value='//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/button').is_enabled()

        if True == SendButton:
            driver.find_element(by=By.XPATH,
                                value='//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/button').click()
            sleep(5)
            break


def CheckBackSoon(Query):
    Button = driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div").text

    if "Apologies, an unexpected error has occurred. Please check back again soon." == str(Button):
        driver.refresh()
        driver.refresh()
        driver.refresh()
        sleep(2)
        QuerySender(Query=Query)
        ButtonClicker()

    else:
        pass


def AnswerReturn(Query):
    Query = str(Query)

    try:
        driver.find_element(by=By.XPATH,
                            value='//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/div/textarea').send_keys(
            Query)

    except Exception as e:
        print(e)

    sleep(5)

    while True:

        SendButton = driver.find_element(by=By.XPATH,
                                         value='//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/button').is_enabled()

        if True == SendButton:

            try:
                Text = driver.find_element(by=By.XPATH,
                                           value='//*[@id="__next"]/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]').text
                print(Text)
                try:
                    with open(r"C:\Users\dell\PycharmProjects\pythonProject\brain\savedtext.txt", "w") as savedfile:
                        while True:
                            savedfile.write(Text + '\n')
                            savedfile.flush()  # Force the buffer to be written immediately
                except:
                    pass

                # speak.speak(Text)

                sleep(3)
                try:
                    driver.find_element(by=By.XPATH,
                                        value='//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/div/textarea').clear()

                except:
                    pass
                # sleep(2)


            except Exception as e:
                print(e)

            FileHistory = open("C:\\Users\\dell\\PycharmProjects\\pythonProject\\brain\\chatnumberpi.txt", "w")
            FileHistory.write('1')
            FileHistory.close()

            break

        else:
            FileRead = open("C:\\Users\\dell\\PycharmProjects\\pythonProject\\brain\\chatnumberpi.txt", "r")
            Data = FileRead.read()
            FileRead.close()

            if str(Data) == '80':
                driver.refresh()
                sleep(2)

                try:
                    Text = driver.find_element(by=By.XPATH,
                                               value='//*[@id="__next"]/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]').text
                    # speak.speak(Text)
                    print("EDITH:", Text)

                    sleep(0.5)

                    try:
                        driver.find_element(by=By.XPATH,
                                            value='//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/div/textarea').clear()

                    except Exception as e:
                        print("no worries")

                    sleep(0.5)

                except Exception as e:
                    print(e)

                break

            else:
                FileRead = open("C:\\Users\\dell\\PycharmProjects\\pythonProject\\brain\\chatnumberpi.txt", "r")
                Data = FileRead.read()
                FileRead.close()
                FileHistory = open("C:\\Users\\dell\\PycharmProjects\\pythonProject\\brain\\chatnumberpi.txt", "w")
                NewData = int(Data) + 1
                NewData = str(NewData)
                FileHistory.write(NewData)
                FileHistory.close()
                sleep(0.5)


def NotNowChecker():
    try:
        driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div/div/div[2]/button").click()
        sleep(1)

    except:
        pass

    try:
        driver.find_element(by=By.XPATH, value="/html/body/div/main/div/div/div[1]/div/div/div/div[2]/button").click()
        sleep(1)

    except:
        pass


error()

sleep(10)
PopUpRemover()

Introduction()


def EdithAI():
    while True:

        try:

            file = open("C:/Users/dell/PycharmProjects/pythonProject/body/speechrecognition.txt", "r")
            Query = file.read()
            file.close()

            filehistory = open("C:\\Users\\dell\\PycharmProjects\\pythonProject\\brain\\historychat.txt", "r")
            datahistory = filehistory.read()
            filehistory.close()

            if str(Query) == str(datahistory):
                sleep(0.5)
                pass





            else:
                if 'open youtube' in Query:
                    # speak.speak("opening youtube now!")
                    webbrowser.open("youtube.com")
                realquestion = str(Query)
                # results = bard.get_answer(realquestion)['content']
                filehistory = open("C:\\Users\\dell\\PycharmProjects\\pythonProject\\brain\\historychat.txt", "w")
                filehistory.write(Query)
                filehistory.close()
                File = open("C:\\Users\\dell\\PycharmProjects\\pythonProject\\brain\\pihistory.txt", "r")
                DataRead = File.read()
                File.close()
                is_cooldown()

                if 'bye' in Query:
                    # speak.speak("until next time.")
                    break
                # elif 'open youtube' in Query:
                #     QuerySender("False")
                #     speak.speak("opening youtube now!")
                #     webbrowser.open("youtube.com")
                elif 'open google' in Query:
                    QuerySender(False)
                    # speak.speak("opening google now!")
                    webbrowser.open("google.com")

                elif 'open stackoverflow' in Query:

                    # speak.speak("opening stactoverflow now!")
                    webbrowser.open("stackoverflow.com")


                elif 'play' in Query:

                    song = Query

                    webbrowser.open(f'https://open.spotify.com/search/{song}')

                    sleep(13)

                    # speak('now playing' + song)
                if str(DataRead) == "49":
                    driver.delete_all_cookies()
                    sleep(2)
                    driver.refresh()
                    driver.refresh()
                    driver.refresh()
                    sleep(2)
                    FileReadNow = open("C:\\Users\\dell\\PycharmProjects\\pythonProject\\brain\\pihistory.txt", "w")
                    FileReadNow.write('1')
                    FileReadNow.close()

                else:
                    try:
                        QuerySender(Query=Query)
                        ButtonClicker()
                        if str(Query) == str(datahistory):
                            sleep(0.5)
                            pass
                        CheckBackSoon(Query=Query)
                        NotNowChecker()
                        AnswerReturn(Query=Query)
                        FileReadNow = open("C:\\Users\\dell\\PycharmProjects\\pythonProject\\brain\\pihistory.txt", "w")
                        NewDataRead = int(DataRead) + 1
                        FileReadNow.write(str(NewDataRead))
                        FileReadNow.close()

                    except Exception as e:
                        print(e)
        except Exception as e:
            print(e)


EdithAI()
