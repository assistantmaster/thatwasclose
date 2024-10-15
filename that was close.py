import pygame
import time
import random
import os


pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

pygame.display.set_caption("That was close!")

font = pygame.font.Font(None,50)
fontklein = pygame.font.Font(None,23)

regeln = True
text = font.render('That was close! V1.0', True, (255,255,255))
text2 = fontklein.render('Regeln: Wenn man das Spiel geschlossen hat, hat man es durchgespielt.', True, (0,0,0))
text3 = fontklein.render('Wenn das Spiel abgestürzt ist, gilt es nicht als durchgespielt.', True, (0,0,0))
text4 = fontklein.render('Die Kommandozeile zu schließen oder das Spiel über den Taskmanager zu beenden, ist nicht erlaubt.', True, (0,0,0))
text_rect = text.get_rect(center=(400,300))
text_rect2 = text2.get_rect(center=(400,400))
text_rect3 = text3.get_rect(center=(400,450))
text_rect4 = text4.get_rect(center=(400,500))
nebenfenster = False
altf4 = True
with open("./gtnn.txt", "w") as file:
    file.write("11")

running = True
while running:
    screen.fill((0, 180, 255))
    screen.blit(text, text_rect)
    if regeln:
        screen.blit(text2, text_rect2)
        screen.blit(text3, text_rect3)
        screen.blit(text4, text_rect4)
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT and altf4:
            regeln = False
            welchertext = random.randint(1, 15)
            if welchertext == 1:
                welchertext = "Das wär der einfache Weg."
            if welchertext == 2:
                welchertext = "So nicht ._."
            if welchertext == 3:
                welchertext = "Haste gedenkt ne xD"
            if welchertext == 4:
                welchertext = "Leider nein"
            if welchertext == 5:
                welchertext = "Immer noch nicht"
            if welchertext == 6:
                welchertext = "Was versuchst du zu versuchen?"
            if welchertext == 7:
                welchertext = "Ein Satz mit x"
            if welchertext == 8:
                welchertext = "Dödum"
            if welchertext == 9 or welchertext == 11 or welchertext == 12 or welchertext == 13 or welchertext == 14 or welchertext == 15:
                welchertext = "Du musst ESCapen"
            if welchertext == 10:
                welchertext = "Gut! Weiter so :o"
            
            text = font.render(f"{welchertext}", True, (0,0,0))
            text_rect = text.get_rect(center=(400,300))

        if keys[pygame.K_ESCAPE]:
            screen = pygame.display.set_mode((width, height), flags=pygame.HIDDEN)
            time.sleep(5)
            screen = pygame.display.set_mode((width, height), flags=pygame.SHOWN)
            pygame.display.set_caption("That was close!      (Drück nicht STRG + Q)")
            text = font.render("SIKE!", True, (255,0,0))
            text_rect = text.get_rect(center=(400,300))
        if keys[pygame.K_a] and keys[pygame.K_l] and keys[pygame.K_t] and keys[pygame.K_f] and keys[pygame.K_4]:
            font = pygame.font.Font(None,50)
            text = font.render("Du hast es geschafft!", True, (0,0,0))
            text_rect = text.get_rect(center=(400,300))
            screen.fill((0, 180, 255))
            screen.blit(text, text_rect)
            pygame.display.update()
            time.sleep(1)
            running = False
            if os.path.exists(".\hinweis.txt"):
                os.remove(".\hinweis.txt")
        if os.path.exists("./gtnn.txt"):
            with open("./gtnn.txt", "r") as gtnfile:
                gtnn = int(gtnfile.read())
        if (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]) and keys[pygame.K_q]:
            os.system('py "./that_was_close_nebenfenster.py"')
            nebenfenster = True



        if event.type == pygame.KEYDOWN and nebenfenster == True:
            if gtnn == 0 and keys[pygame.K_0]:
                nebenfenster = False
                pygame.display.set_caption("Richtig!")
                font = pygame.font.Font(None,20)
                text = font.render("Ratlos? Guck doch mal im Ordner von diesem Spiel nach!", True, (0,0,0))
                text_rect = text.get_rect(center=(400,300))
                with open("./hinweis.txt", "w") as hintfile:
                    hintfile.write("Droppe diese Datei doch mal ins Fenster!")
            elif gtnn == 1 and keys[pygame.K_1]:
                nebenfenster = False
                pygame.display.set_caption("Richtig!")
                font = pygame.font.Font(None,20)
                text = font.render("Ratlos? Guck doch mal im Ordner von diesem Spiel nach!", True, (0,0,0))
                text_rect = text.get_rect(center=(400,300))
                with open("./hinweis.txt", "w") as hintfile:
                    hintfile.write("Droppe diese Datei doch mal ins Fenster!")
            elif gtnn == 2 and keys[pygame.K_2]:
                nebenfenster = False
                pygame.display.set_caption("Richtig!")
                font = pygame.font.Font(None,20)
                text = font.render("Ratlos? Guck doch mal im Ordner von diesem Spiel nach!", True, (0,0,0))
                text_rect = text.get_rect(center=(400,300))
                with open("./hinweis.txt", "w") as hintfile:
                    hintfile.write("Droppe diese Datei doch mal ins Fenster!")
            elif gtnn == 3 and keys[pygame.K_3]:
                nebenfenster = False
                pygame.display.set_caption("Richtig!")
                font = pygame.font.Font(None,20)
                text = font.render("Ratlos? Guck doch mal im Ordner von diesem Spiel nach!", True, (0,0,0))
                text_rect = text.get_rect(center=(400,300))
                with open("./hinweis.txt", "w") as hintfile:
                    hintfile.write("Droppe diese Datei doch mal ins Fenster!")
            elif gtnn == 4 and keys[pygame.K_4]:
                nebenfenster = False
                pygame.display.set_caption("Richtig!")
                font = pygame.font.Font(None,20)
                text = font.render("Ratlos? Guck doch mal im Ordner von diesem Spiel nach!", True, (0,0,0))
                text_rect = text.get_rect(center=(400,300))
                with open("./hinweis.txt", "w") as hintfile:
                    hintfile.write("Droppe diese Datei doch mal ins Fenster!")
            elif gtnn == 5 and keys[pygame.K_5]:
                nebenfenster = False
                pygame.display.set_caption("Richtig!")
                font = pygame.font.Font(None,20)
                text = font.render("Ratlos? Guck doch mal im Ordner von diesem Spiel nach!", True, (0,0,0))
                text_rect = text.get_rect(center=(400,300))
                with open("./hinweis.txt", "w") as hintfile:
                    hintfile.write("Droppe diese Datei doch mal ins Fenster!")
            elif gtnn == 6 and keys[pygame.K_6]:
                nebenfenster = False
                pygame.display.set_caption("Richtig!")
                font = pygame.font.Font(None,20)
                text = font.render("Ratlos? Guck doch mal im Ordner von diesem Spiel nach!", True, (0,0,0))
                text_rect = text.get_rect(center=(400,300))
                with open("./hinweis.txt", "w") as hintfile:
                    hintfile.write("Droppe diese Datei doch mal ins Fenster!")
            elif gtnn == 7 and keys[pygame.K_7]:
                nebenfenster = False
                pygame.display.set_caption("Richtig!")
                font = pygame.font.Font(None,20)
                text = font.render("Ratlos? Guck doch mal im Ordner von diesem Spiel nach!", True, (0,0,0))
                text_rect = text.get_rect(center=(400,300))
                with open("./hinweis.txt", "w") as hintfile:
                    hintfile.write("Droppe diese Datei doch mal ins Fenster!")
            elif gtnn == 8 and keys[pygame.K_8]:
                nebenfenster = False
                pygame.display.set_caption("Richtig!")
                font = pygame.font.Font(None,20)
                text = font.render("Ratlos? Guck doch mal im Ordner von diesem Spiel nach!", True, (0,0,0))
                text_rect = text.get_rect(center=(400,300))
                with open("./hinweis.txt", "w") as hintfile:
                    hintfile.write("Droppe diese Datei doch mal ins Fenster!")
            elif gtnn == 9 and keys[pygame.K_9]:
                nebenfenster = False
                pygame.display.set_caption("Richtig!")
                font = pygame.font.Font(None,20)
                text = font.render("Ratlos? Guck doch mal im Ordner von diesem Spiel nach!", True, (0,0,0))
                text_rect = text.get_rect(center=(400,300))
                with open("./hinweis.txt", "w") as hintfile:
                    hintfile.write("Droppe diese Datei doch mal ins Fenster!")
            else:
                pygame.display.set_caption("Leider Falsch. Versuche es noch einmal.")
        
        if event.type == pygame.DROPFILE:
            dropped_file = event.file
            dateiname = os.path.basename(dropped_file)
            if dateiname == "hinweis.txt":
                altf4 = False
                text = font.render("Hinweis: Hast du es schonmal mit ALT F4 versucht?", True, (0,0,0))
                text_rect = text.get_rect(center=(400,300))

        if event.type == pygame.QUIT and not altf4:
            text = font.render("Ich habe wohl die Trennung zwischen allen Buchstaben vergessen ...", True, (0,0,0))
            text_rect = text.get_rect(center=(400,300))
            

        

    pygame.display.flip()
if os.path.exists(".\hinweis.txt"):
    os.remove(".\hinweis.txt")
if os.path.exists("./gtnn.txt"):
    os.remove("./gtnn.txt")
pygame.quit()