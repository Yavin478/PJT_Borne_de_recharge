from main_lydia import *

gala='100J'

type_police="Extra Bold"

h_fleche={"carte":20/38,
          "montant":33/38,
          "QR":12.5/38}


txt_titre= {"carte":"Placez Votre Carte \n de Gala",
            "montant":"Tapez le montant \n à rajouter",
            "Qr":"Scannez votre QR Code LYDIA",
            "terminée":"Opération Effectué",
            "error_QR":"Erreur QR Code LYDIA",
            "error_rezal":"Erreur Réseau",
            "error_carte":"Erreur carte non reconnue",
            "annulée":"Opération Annulée",
            "error_montant":"Erreur montant",}

txt_indic= {"terminée":"Très bon Gala!",
            "montant":"Transaction max de "+str(config.maxTransaction/100)+"€\nArgent sur carte max de "+str(config.maxMontant/100)+" €",
            "QR":"Placez votre QR Code LYDIA proche du scanneur",
            "error_QR":"Recommencez avec un QRcode \n Lydia Valide",
            "error_rezal":"veuillez contacter une caisse",
            "error_carte":"Recommencez avec une carte valide",
            "error_montant":"Le montant doit être < "+str(config.maxTransaction/100)+" € \n vous ne pouvez pas avoir plus de "+str(config.maxMontant/100)+" € sur la carte",
            "no_card":"Vous avez retirez la carte",
            "annulée": "Vous avez annulez l'opération",
            "montant_in":"Vous avez: \n",
            "montant_out":"Vous Rajoutez: \n"}

txt_presentation="Cette borne a pour but \n de recharger votre carte \n de Gala par Lydia"

txt_esc="Retirez la carte pour annuler"


if gala=='baptss':
    path_img_bg = "Static/Bg_Bapt'ss.png"
    path_img_fg = "Static/Cadre_Bapt'ss.png"
    ratio_square = 1.5 #1<      aumgente => diminue taille carré
    taille_police=75
    decalage_label=0.75 #<1      diminue => descend


elif gala=='508':
    path={"bg":"Static/Bg_508.jpg",
          "fg":"Static/Cadre_508.png",
          "fleche":"Static/fleche_wb.png",
          "exclam":"Static/ho_shit.png",
          "smiley":"Static/Smiley_corect.png",
          "cross":"Static/Crossçcorect.png"}

    ratio_square = 1.25
    ratio_img = 5

    decalage= {"top":0.5,
               "bot":0.63,
               "side":0.25,
               "top_montant":0}

    decalage_label = 0.5
    decalage_label_esc=0.63
    decalage_label_montant=0.35
    decalage_info_montant=0.25
    decalage_img=0.1

    ratio_flèche = 7
    décalage_flèche = 30

    taille_police = 47
    taille_police_esc = 30
    taille_police_indic = 35
    taille_police_montant = 35
    taille_police_info = 25

elif gala=='100J':
    path={"bg":"Static/Bg_100J.jpg",
          "fg":"Static/Fg_100J.png",
          "fleche":"Static/fleche_100J.png",
          "exclam":"Static/ho_shit.png",
          "smiley":"Static/Logo_100J.png",
          "cross":"Static/Crossçcorect.png"}

    ratio_square = 1.5
    ratio_img = 5

    decalage= {"top":0.5,
               "bot":0.63,
               "side":0.25,
               "top_montant":0}

    decalage={"titre":0.35,
              "bot":0.3,
              "side":0.4,
              "top":0.65,
              "img":0.1}


    ratio_flèche = 7
    décalage_flèche = 30

    police={"titre":0.057,
            "bot":0.045,
            'top':0.045,
            'side':0.045,
            'center':0.045}

temps_retour=20