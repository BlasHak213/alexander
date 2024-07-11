<!--
Created using JS Bin
http://jsbin.com

Copyright (c) 2024 by anonymous (http://jsbin.com/letopiqipi/1/edit)

Released under the MIT license: http://jsbin.mit-license.org
-->
<meta name="robots" content="noindex">

<script id="jsbin-javascript">
function countElements(arr) {
    let evenCount = 0;
    let oddCount = 0;
    let zeroCount = 0;

    arr.forEach(element => {
        if (typeof element === 'number') {
            if (element === 0) {
                zeroCount++;
            } else if (element % 2 === 0) {
                evenCount++;
            } else {
                oddCount++;
            }
        }
    });

    console.log(`Количество чётных элементов: ${evenCount}`);
    console.log(`Количество нечётных элементов: ${oddCount}`);
    if (zeroCount > 0) {
        console.log(`Количество нулевых элементов: ${zeroCount}`);
    }
}
</script>