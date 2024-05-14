from config import *

gala='508'

type_police="Georgia"
ratio_flèche=7
décalage_flèche=30
h_fleche={"carte":20/38,
          "montant":33/38,
          "QR":12.5/38}


txt_titre= {"carte":"Placez Votre Carte de Gala",
            "montant":"Tapez le montant à rajouter",
            "Qr":"Scannez votre QR Code LYDIA",
            "terminée":"Opération Effectué",
            "error_QR":"Erreur QR Code LYDIA",
            "error_rezal":"Erreur rezal",
            "error_carte":"Erreur carte non reconnue",
            "annulée":"Opération Annulée",
            "error_montant":"Erreur montant",}

txt_indic= {"terminée":"Très bon gala!",
            "montant":"Transaction max de "+str(config.maxTransaction/100)+"€\nArgent sur carte max de "+str(config.maxMontant/100)+" €",
            "QR":"Placez votre QR Code LYDIA proche du scanneur",
            "error_QR":"Recommencez avec un QRcode \n Lydia Valide",
            "error_rezal":"veuillez contacter un membre du Rezal",
            "error_carte":"Recommencez avec une carte valide",
            "error_montant":"Recommencez avec un montant \n valide <90€ ",
            "no_card":"Vous avez retirez la carte",
            "annulée": "Vous avez annulez l'opération",
            "montant_in":"Vous avez: \n",
            "montant_out":"Vous Rajoutez: \n"}

txt_presentation="Cette borne a pour but de recharger \n votre carte de Gala par Lydia"

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



    taille_police = 47
    taille_police_esc = 30
    taille_police_indic = 35
    taille_police_montant = 35
    taille_police_info = 25


temps_retour=20