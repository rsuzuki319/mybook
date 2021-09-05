<?php

$str=mb_convert_kana('PL123', 'R');
$str='abc';
if(preg_match("/^[a-zA-Z0-9ａ-ｚA-Z０-９]+$/", $str)) echo 'すべて 全角英字 でない'; else echo 'すべて 全角英字';
?>