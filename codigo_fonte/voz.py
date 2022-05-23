import cv2
import pyttsx3
import speech_recognition as sr

recon = sr.Recognizer()
comando = ""
resposta = ""
classificador = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
imagem = cv2.imread(r'fotos\img.jpg')
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
faces = classificador.detectMultiScale(cinza, scaleFactor = 1.50)

def play_audio(message):
    sextaFeira = pyttsx3.init()
    sextaFeira.setProperty('voice',"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0")
    sextaFeira.say(message)
    sextaFeira.setProperty('voice', b'brasil')
    sextaFeira.setProperty('rate', 140)
    sextaFeira.setProperty('volume', 1)
    sextaFeira.runAndWait()

def feedback(nota, restaurant):
    play_audio("Você deu a nota " + nota + " para o restaurante" + restaurant)

for x, y, l, a in faces:
    imagem = cv2.rectangle(imagem, (x, y), (x+l, y+a), (0, 0, 255), 2)

cv2.imshow("Faces detectadas", imagem)
cv2.waitKey()

if len(faces) > 0:
    with sr.Microphone() as source:
        while True:
            print("Começe a falar")
            audio = recon.listen(source)
            comando = recon.recognize_google(audio, language='pt')
            print("Pare de falar")
            print(comando)

            if comando == "Ok restaurante":
                play_audio("Como posso te ajudar?")
                audio = recon.listen(source)
                resposta = recon.recognize_google(audio, language='pt')

                print(resposta)

                if resposta == "listar deficiências":
                    play_audio("Temos suporte para: Auditiva, Visual, Motora, Mental")

                if resposta == "cadastrar cliente":
                    play_audio("Me diga seu nome")
                    insertAudio = recon.listen(source)
                    insertName = recon.recognize_google(insertAudio, language='pt')

                    print(insertName)
                    play_audio("Ok, " + insertName + "você foi cadastrado no sistema")
                    nameAudio = recon.listen(source)
                    clientName = recon.recognize_google(audio, language='pt')

                if resposta == "reservar restaurante":
                    play_audio("Me diga seu nome")
                    pickAudio = recon.listen(source)
                    pickName = recon.recognize_google(pickAudio, language='pt')

                    play_audio("Em qual restaurante você deseja ir? 1- Feijoadinha, 2- Botéquinho, 3- Varandinha")
                    audio = recon.listen(source)
                    resposta = recon.recognize_google(audio, language='pt')

                    print(resposta)

                    if resposta == "feijoadinha":
                        play_audio("Ok, " + pickName + "você resevou um lugar no Feijoadinha")
                    if resposta == "botéquinho":
                        play_audio("Ok, " + pickName + "você resevou um lugar no Botequinho")
                    if resposta == "varandinha":
                        play_audio("Ok, " + pickName + "você resevou um lugar no Varandinha")

                if resposta == "cadastrar avaliação":
                    play_audio("Qual restaurante você deseja avaliar? 1- Feijoadinha, 2- Botéquinho, 3- Varandinha")
                    restaurantAudio = recon.listen(source)
                    restaurantResponse = recon.recognize_google(restaurantAudio, language='pt')

                    if restaurantResponse == "feijoadinha":
                        play_audio("Dê uma nota de 0 a 5")
                        scoreAudio = recon.listen(source)
                        scoreResponse = recon.recognize_google(scoreAudio, language='pt')
                        feedback(scoreResponse, "feijoadinha")

                    if restaurantResponse == "botéquinho":
                        play_audio("Dê uma nota de 0 a 5")
                        scoreAudioTwo = recon.listen(source)
                        scoreResponseTwo = recon.recognize_google(scoreAudioTwo, language='pt')
                        feedback(scoreResponseTwo, "botéquinho")

                    if restaurantResponse == "varandinha":
                        play_audio("Dê uma nota de 0 a 5")
                        scoreAudioTree = recon.listen(source)
                        scoreResponseTree = recon.recognize_google(scoreAudioTree, language='pt')
                        feedback(scoreResponseTree, "varandinha")

            if comando != "Ok restaurante":
                play_audio("Não entendi seu comando")
                break
else:
    print("Não reconhecemos sua face")













