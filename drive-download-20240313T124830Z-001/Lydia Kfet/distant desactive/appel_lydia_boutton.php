<?php
require('../config.php');
require('../preparation_bdd.php')
?>

<!DOCTYPE html>
<html lang="fr">
<head>
	<title>Appel_php</title>
	<script src="http://code.jquery.com/jquery-2.2.1.min.js"></script>
	<script type="text/javascript" src="../LYDIASDK.js"></script>
</head>
<body>

<div id="paymentButton">Payer avec Lydia</div>

<script type="text/javascript">
var montant = <?php echo json_encode($montant); ?>;
var tel = <?php echo json_encode($_POST['tel']); ?>;
var ref = <?php echo json_encode($order_ref); ?>;
var token_public = <?php echo json_encode($token_public); ?>;

$(document).ready(function() {
	$('#paymentButton').payWithLYDIA({
	order_ref: ref,
	amount: montant, // amount in €
	vendor_token: token_public, //Business Public Token
	recipient: tel, //cellphone or email of your client. Leave it like this for your test
	message : "Rechargement Kfet", //object of the payment
	//env: 'pro',
	render : '<img src="https://lydia-app.com/assets/img/paymentbutton.png" />',
	browser_success_url: "https://kfet.rezal.fr/",
	confirm_url: "https://lydia.rezal.fr/lydia_confirm_boutton.php",
	});
});
</script>

</body>
</html>
