<?php
header('Content-Type: application/json');

$num = $_GET['num'] ?? 'N/A';
$date = $_GET['date'] ?? 'N/A';
$biller = $_GET['biller'] ?? 'N/A';
$time = $_GET['time'] ?? 'N/A';
$volunteer = $_GET['volunteer'] ?? 'N/A';
$amount = $_GET['amount'] ?? 'N/A';

$a = [];

// Details
$lines = [
    "=======================",
    "     RECEIPT #$num",
    "=======================",
    "Date: $date",
    "Time: $time",
    "-----------------------",
    "Biller: $biller",
    "-----------------------",
    "Volunteer: $volunteer",
    "-----------------------",
    "AMOUNT: Rs. $amount",
    "======================="
];

foreach ($lines as $line) {
    $obj = new stdClass();
    $obj->type = 0;
    $obj->content = $line;

    // Header formatting
    if (strpos($line, 'RECEIPT #') !== false) {
        $obj->bold = 1;
        $obj->format = 2; // large font
        $obj->align = 1; // center
    }
    // Amount formatting
    elseif (strpos($line, 'AMOUNT:') === 0) {
        $obj->bold = 1;
        $obj->format = 2; // large font
        $obj->align = 0; // left
    }
    // Separator lines
    elseif (strpos($line, '=') === 0 || strpos($line, '-') === 0) {
        $obj->bold = 0;
        $obj->format = 0; // normal size
        $obj->align = 1; // center
    }
    // Regular content
    else {
        $obj->bold = 0;
        $obj->format = 0; // normal size
        $obj->align = 0; // left
    }

    $a[] = $obj;
}

echo json_encode($a, JSON_FORCE_OBJECT);
?>