<!--
Created using JS Bin
http://jsbin.com

Copyright (c) 2024 by anonymous (http://jsbin.com/letopiqipi/1/edit)

Released under the MIT license: http://jsbin.mit-license.org
-->
<meta name="robots" content="noindex">

<script id="jsbin-javascript">
function isPrimeNumber(num) {
    if (typeof num !== 'number' || num > 1000) {
        console.log("Данные неверны");
        return;
    }
    
    if (num <= 1) {
        console.log("Число не является простым");
        return;
    }

    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) {
            console.log("Число не является простым");
            return;
        }
    }

    console.log("Число является простым");
</script>