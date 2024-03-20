<?php
?>

<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<script src="http://code.jquery.com/jquery-2.2.1.min.js"></script>
		<script type="text/javascript" src="LYDIASDK.js"></script>
		</head>
	<body>
		<div id="lydiaButton">Payer avec Lydia</div>
		<script type="text/javascript">
		$(document).ready(function() {
			$('#lydiaButton').payWithLYDIA({
			amount: "11", // amount in €
			vendor_token: "58ada276ab575970477137", //Business Public Token
			recipient: "0711223344", //cellphone or email of your client. Leave it like this for your test
			message : "Rechargement Kfet", //object of the payment
			env: 'test',
			render : '<img src="https://lydia-app.com/assets/img/paymentbutton.png" />', //button image
			});
		});
		</script>	
		</body>
</html>