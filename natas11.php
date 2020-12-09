<?php 

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

// orignal function

// function xor_encrypt($in) {
//     $key = '<censored>';
//     $text = $in;
//     $outText = '';

//     // Iterate through each character
//     for($i=0;$i<strlen($text);$i++) {
//     $outText .= $text[$i] ^ $key[$i % strlen($key)];
//     }

//     return $outText;
// }

// the orignal plain text 

 json_encode($defaultdata);

// the orignal bad cipher text in hex 
$cyphertext = hex2bin('0a554b221e00482b02044f2503131a70531957685d555a2d121854250355026852115e2c17115e680c');
$plaintext = json_encode($defaultdata);
$key = 'qw8J';

$good_data = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");

function xor_encrypt2($in, $key) {
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$key_finder = (xor_encrypt2($cyphertext,$plaintext));
$good_plaintext = json_encode($good_data);
$good_ciphertext = xor_encrypt2($good_plaintext,$key);

echo(base64_encode($good_ciphertext));

// Plaintext ^ key = ciphertext
// cyphertext ^ plaintext = key 
?> 
 
