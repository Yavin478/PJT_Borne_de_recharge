<?php

$insertion_consos = "INSERT INTO `consos`(`en_attente_de_livraison`, `users_id`, `consomateur_id`, `produits_id`, `date`, `admins_id`, `montant`, `quantite`) VALUES (0,".$users_id.", NULL, 3222,".$date.", 179,".-1*$montant.", 1);";
mysql_query($insertion_consos);


$selection_consos = "SELECT id FROM consos WHERE users_id=".$users_id." AND date=".$date.";";
$query_selection_consos = mysql_query($selection_consos);
while($row = mysql_fetch_array($query_selection_consos)){
	$id_consos = $row['id'];
}

$update_lydia = "UPDATE consos_lydia SET transaction_identifier='".$transaction_identifier."',id_consos=".$id_consos." WHERE id=".$order_ref.";"; 
$update_credit = "UPDATE users SET credit=credit+".$montant." WHERE id=".$users_id.";";

mysql_query($update_lydia);
mysql_query($update_credit);

?>