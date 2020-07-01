import time
import msvcrt


print("       *****Pulsmessung*****\n\n1. Beginne mit irgendeiner Taste und drücke jedesmal wenn du den Puls spürst nochmal auf diese Taste.\n2. Wenn du das Programm beenden möchtest, drücke \"Leertaste\"\n   Danach wir der Puls für 5 Sekunden angezeigt und das Programm beendet sich von alleine \n")

eingabe = msvcrt.getch().decode('ASCII')

if eingabe != " ":
  
  print("Beginne..")
  start = time.time()
  zaehler = 1

  schlaufe = "an"

  while schlaufe == "an":

    eingabe = msvcrt.getch().decode('ASCII')
    
    if eingabe == " ":
      stop = time.time()
      zaehler += 1
      schlaufe = "aus"
      print("Beende!")

    else:
      zaehler += 1
      print("..Weiter..")

  zeit = stop - start
  puls = zaehler / zeit * 60
  puls = int(puls)
  zeit = int(zeit)

  
  print("\n\nAnzahl Pulsschläge: " + str(zaehler))
  print("Zeit: " + str(zeit) + " Sekunden")
  print("\n-->  Puls: " + str(puls))

  time.sleep(500)
