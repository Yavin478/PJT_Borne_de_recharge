<?php

$montant = number_format(abs(round($_POST['montant'],2)),2,'.','');

$date = time();
$selection_user = "SELECT id, bucque FROM users WHERE blairal=".$_POST['tel']." AND deleted=0;";
$query_selection_user = mysql_query($selection_user);
while($row = mysql_fetch_array($query_selection_user)){
	$users_id = $row['id'];
	$user_bucque = $row['bucque'];
}

if (!isset($users_id)) 
{
echo("</br><b>Numero de telephone incorrect - Redirection imminente</b>");
?>
<script>
function redirection(){
//document.location.href = "javascript:history.back(-1)";
location.replace(document.referrer);
}
setTimeout("redirection()",4000);
</script>
<?php
exit();
}


$sql_preparation = "INSERT INTO `consos_lydia`(montant, users_id, date) VALUES (".-1*(float)$montant.",".(int)$users_id.",".$date.");";
mysql_query($sql_preparation);


$sql_order_ref = "SELECT id FROM consos_lydia WHERE users_id=".$users_id." AND `date`=".$date.";";
$query_order_ref = mysql_query($sql_order_ref);
while($row = mysql_fetch_array($query_order_ref)){
	$order_ref = $row['id'];
}

echo '<div class="ui center aligned orange segment">';
echo '<p class="important"><b>'.$user_bucque.'</b></p>';
echo '</div>';
echo '<div class="ui center aligned orange segment">';
echo '<p class="important">Montant de ta recharge : <b>'.$montant.'E</b></p>';
echo '</div>';
//echo "Order ref : ".$order_ref."<br/>";

?>

<!DOCTYPE html>
<html lang="fr">
<head>
<script src = "../javascript/semantic.js" type = "text/javascript"></script>
<link rel = "stylesheet" href = "../css/semantic.css"/>
<link rel = "stylesheet" href = "../css/perso.css"/>
</head>
<body class="ui center aligned basic segment" style="margin:70px;">
</body>
</html>