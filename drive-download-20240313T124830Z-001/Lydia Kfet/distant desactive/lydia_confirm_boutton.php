<?php

require('../config.php');

if(!isset($_POST['request_id']) || !isset($_POST['amount']) 
|| !isset($_POST['signed']) || !isset($_POST['transaction_identifier'])
|| !isset($_POST['vendor_token']) || !isset($_POST['order_ref'])
|| !isset($_POST['sig'])) exit;

$order_ref = (int)$_POST['order_ref'];

require('selection_bdd.php');

$param = array(
        'currency'=>'EUR',
        'request_id'=>$_POST['request_id'],
        'amount'=>number_format(round($montant,2),2,'.',''),
        'signed'=>$_POST['signed'],
        'order_ref'=>$_POST['order_ref'],
	'vendor_token'=>$token_public,
	'transaction_identifier'=>$_POST['transaction_identifier']);

ksort($param);

$sig = array();

foreach ($param as $key => $val) {
    $sig[] .= $key.'='.$val;
}

$callSig = md5(implode("&", $sig)."&".$token_prive);

/* vérification avec la signature envoyée par Lydia */
if($callSig != $_POST['sig'])
{
	exit;
}
$transaction_identifier = $_POST['transaction_identifier'];
require('../finalisation_bdd.php');

?>