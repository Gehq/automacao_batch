import pyautogui ,time
pyautogui.confirm('ajuste a tela\n deixe a tela do batch visivel ')
#variaveis
S_entra =None
S_entra_segundo = None
JOB_vazio =None
filial = "133"
Job_comcluido = None
Job_02 ="sjbdd02"
Job_03 ="sjbdd03"
Job_04 ="sjbdd04"
dd02 = None
dd03 = None
dd04 = None
ddfim = None


while True:#aquarda o fim do processo
    S_entra = pyautogui.locateCenterOnScreen('Screenshot_1_processo.png')
    print('Esperando')
    while S_entra != None:
        S_entra = pyautogui.locateCenterOnScreen('Screenshot_1_processo.png')
    else:
        print('Ok')
        Job_comcluido = pyautogui.locateCenterOnScreen("Screenshot_1_Comcluido.png")
        while Job_comcluido != None:
            print("Job-comcluido")
                #dd02
            dd02 = pyautogui.locateCenterOnScreen("Screenshot_1_dd01_linha.png")
            Job_comcluido = None
            while dd02 != None:
              print("Proximo Job:2")
              pyautogui.press("enter")
              time.sleep(3)
              dd02 =None
            else:
                JOB_vazio = pyautogui.locateCenterOnScreen("Screenshot_1_novoJOB.png")
                print(JOB_vazio)
                while JOB_vazio != None:
                    print("Iniciando a dd02")
                    pyautogui.write(filial,interval=0.25)
                    time.sleep(1)
                    pyautogui.press("enter")
                    time.sleep(1)
                    pyautogui.write(Job_02,interval=0.25)
                    time.sleep(1)
                    pyautogui.press("enter")
                    JOB_vazio = None
                else:
                    #dd03
                    dd03 = pyautogui.locateCenterOnScreen("Screenshot_1_dd02_linha.png")
                    print(dd03)
                    while dd03 != None:
                        print("Proximo Job:3")
                        pyautogui.press("enter")
                        time.sleep(3)
                        dd03 = None
                    else:
                        JOB_vazio = pyautogui.locateCenterOnScreen("Screenshot_1_novoJOB.png")
                        print(JOB_vazio)
                        while JOB_vazio != None:
                            print("Iniciando a dd03")
                            pyautogui.write(filial,interval=0.25)
                            time.sleep(1)
                            pyautogui.press("enter")
                            time.sleep(1)
                            pyautogui.write(Job_03,interval=0.25)
                            time.sleep(1)
                            pyautogui.press("enter")
                            JOB_vazio = None
                        else:
                            #dd04
                            dd04 = pyautogui.locateCenterOnScreen("Screenshot_1_dd03_linha.png")
                            while dd04 != None:
                                print("Proximo Job:4")
                                pyautogui.press("enter")
                                time.sleep(3)
                                dd04 =None
                            else:
                                JOB_vazio = pyautogui.locateCenterOnScreen("Screenshot_1_novoJOB.png")
                                print(JOB_vazio)
                                while JOB_vazio != None:
                                    print("Iniciando a dd04")
                                    pyautogui.write(filial,interval=0.25)
                                    time.sleep(1)
                                    pyautogui.press("enter")
                                    time.sleep(1)
                                    pyautogui.write(Job_04,interval=0.25)
                                    time.sleep(1)
                                    pyautogui.press("enter")
                                    JOB_vazio = None
                                else:
                                    ddfim = pyautogui.locateCenterOnScreen("Screenshot_1_dd04_linha.png")
                                    if ddfim != None:
                                        pyautogui.confirm('Opa Batch Finalizado, Pode me fechar A TELA PRETA no X')
                                        print("Fim dos Job")
                                        exit()
    while S_entra_segundo == None:
        S_entra_segundo = pyautogui.locateCenterOnScreen('Screenshot_5_2.png')
    else:
        pyautogui.press('s')
        pyautogui.press('enter')
        S_entra_segundo=None
        S_entra ='a'
                    
                                        
                   
                                    
                                
                                
                  
             
         
                 
                
            




    
        
   
    
    

