<?php
$selection_lydia = "SELECT montant, users_id, date FROM consos_lydia WHERE id=".$order_ref.";";
$query_selection_lydia = mysql_query($selection_lydia);
while($row = mysql_fetch_array($query_selection_lydia)){
    $montant = -1*$row['montant'];
	$users_id = $row['users_id'];
	$date = $row['date'];
}
?>