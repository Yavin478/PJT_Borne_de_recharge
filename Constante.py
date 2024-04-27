gala='508'

type_police="Old English Text MT"
ratio_flèche=7
décalage_flèche=30
h_fleche=[1/4,1/2,3/4]
txt_titre= {"carte":"Placez la carte",
            "montant":"Rentrez le montant",
            "Qr":"Scannez votre QR Code LYDIA",
            "terminée":"opération Effectué",
            "error":["Erreur", "Recommencez avec", "valide"],
            "error_rezal":"Erreur rezal"}

décalage_esc=30
taille_police_esc=30

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

