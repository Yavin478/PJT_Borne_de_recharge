<?php

require('../config.php');

//$url = "https://homologation.lydia-app.com/api/payment/payment.json";
$url = "https://lydia-app.com/api/payment/payment.json";

$PostLydia = array('phone'=>$_POST['phone'],
		   'amount'=>$_POST['amount'],
		   'order_id'=>$_POST['order_id'],
		   'paymentData'=>$_POST['paymentData'],
		   'vendor_token'=>$_POST['vendor_token'],
		   'currency'=>'EUR'); //parameters to be sent

$c = curl_init();
curl_setopt($c, CURLOPT_NOPROGRESS, 0);
curl_setopt($c, CURLOPT_USERAGENT, 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:11.0) Gecko/20100101 Firefox/11.0'); //Inutile mais indispensable
curl_setopt($c, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($c, CURLOPT_FOLLOWLOCATION, 1);
curl_setopt($c, CURLOPT_AUTOREFERER,    1);
curl_setopt($c, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($c, CURLOPT_URL, $url);
curl_setopt($c, CURLOPT_REFERER, $url);
curl_setopt($c, CURLOPT_POST, 1);
curl_setopt($c, CURLOPT_POSTFIELDS, $PostLydia);

$reponse = json_decode(curl_exec($c));
curl_close($c);

//var_dump($reponse);
$error =  $reponse->{'error'};
if($error!="0")
{
	echo("<br/><br/><b>OUPS ERREUR ".$error." ! REESSAYE PLUS TARD ET SI LE PROBLEME PERSISTE VA EN BRASSER AU REZAL 216</b>");
	echo("<br/><br/><b>REDIRECTION IMMINENTE</b>");
?>
<script>
function redirection(){
document.location.href = "qrcode.html";
//location.replace(document.referrer);
}
setTimeout("redirection()",4000);
</script>
<?php
	exit;
}

$transaction_identifier =  $reponse->{'transaction_identifier'};
$order_ref = (int)$_POST['order_id'];

require('../selection_bdd.php');
require('../finalisation_bdd.php');

echo("<br/><br/>PARFAIT TON COMPTE A ETE RECHARGE<br/><br/>");

?>

<!DOCTYPE html>
<html lang="fr">
<head>
<script src = "../javascript/semantic.js" type = "text/javascript"></script>
<link rel = "stylesheet" href = "../css/semantic.css"/>
<link rel = "stylesheet" href = "../css/perso.css"/>
</head>
<body class="ui center aligned basic segment" style="margin:70px;">
	<a href="qrcode.html"></a><input class="fluid ui blue button" type="button" onclick="document.location.href='qrcode.html';" value="RECOMMENCER UN SCAN"></a>
</body>
</html>

