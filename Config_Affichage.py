gala='508'

type_police="Georgia"
ratio_flèche=7
décalage_flèche=30
h_fleche={"carte":1/4,
          "montant":3/4,
          "QR":1/2}


txt_titre= {"carte":"Placez Votre Carte",
            "montant":"Tapez le montant à rajouter",
            "Qr":"Scannez votre QR Code LYDIA",
            "terminée":"Opération Effectué",
            "error_QR":"Erreur QR Code LYDIA",
            "error_rezal":"Erreur rezal",
            "error_carte":"Erreur carte non reconnue",
            "annulée":"Opération Annulée",
            "error_montant":"Erreur montant",}

txt_indic= {"terminée":"Très bon gala!",
            "error_QR":"Recommencez avec un QRcode \n Lydia Valide",
            "error_rezal":"veuillez contacter un membre du Rezal",
            "error_carte":"Recommencez avec une carte valide",
            "error_montant":"Recommencez avec un montant \n valide <90€ ",}

décalage_esc=30
taille_police_esc=30
taille_police_indic=35


if gala=='baptss':
    path_img_bg = "Static/Bg_Bapt'ss.png"
    path_img_fg = "Static/Cadre_Bapt'ss.png"
    ratio_square = 1.5 #1<      aumgente => diminue taille carré
    taille_police=75
    decalage_label=0.75 #<1      diminue => descend


elif gala=='508':
    path_img_bg = "Static/Bg_508.jpg"
    path_img_fg = "Static/Cadre_508.png"
    ratio_square = 1.25
    taille_police = 53
    decalage_label = 0.5
    decalage_label_esc=0.63


box=100




max_transaction=90